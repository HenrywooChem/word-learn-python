# -*- coding: utf-8 -*-
"""
老友记台词例句匹配流水线

用途：从《老友记》台词脚本（纯文本）里，为上海版教材词库（7A/8A，初中）的每个单词
     挑选"生词密度低、句子完整独立、长度适中"的地道例句。

用法：
    python tools/friends_examples.py <台词目录或txt文件...> [-o friends_examples.json]

输出：
    JSON: { "word": {"sentence": "...", "score": 88.5, "source": "S01E01.txt"} }

设计要点（对应筛选规则）：
  - 只取含目标词的句子，单词做词边界匹配，短语做整串匹配
  - 剔除含舞台提示/方括号/破折号的句子，剔除过短或过长的
  - 用"语料内词频"给生词密度打分：句子中越少低频词，分数越高
  - 口语缩读（gonna / wanna / ain_t / y_know 等）按个数扣分，初中词库尽量选书面度高的
"""
import argparse
import json
import os
import re
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
BACKEND = os.path.join(os.path.dirname(HERE), "backend")

# ---------- 口语缩读/俚语扣分词 ----------
SLANG = {
    "gonna", "wanna", "gotta", "kinda", "sorta", "dunno", "ain", "aint", "yeah",
    "yep", "nope", "uh", "um", "oh", "hey", "hi", "okay", "ok", "huh", "wow",
    "damn", "hell", "god", "gosh", "jeez", "crap", "screw", "stupid", "idiot",
    "y", "know", "em", "ya", "whaddya", "whatcha", "gimme", "lemme", "c_mon",
}

# 句子中的"说话人标签"和舞台提示
SPEAKER_RE = re.compile(r"^\s*(?:\[[^\]]*\]\s*)?(?:[A-Z][A-Za-z .'\-]{0,20}):\s*")
PAREN_RE = re.compile(r"\([^)]*\)")
STAGE_RE = re.compile(r"\[[^\]]*\]")

SENT_SPLIT = re.compile(r"(?<=[.!?])\s+")
TOKEN_RE = re.compile(r"[A-Za-z][A-Za-z'\-]*")

MIN_CHARS, MAX_CHARS = 22, 150
MIN_TOKENS, MAX_TOKENS = 5, 24
TOP_FREQ = 2000          # 语料高频词门槛
RARE_PENALTY = 22.0      # 每个超纲词的扣分
SLANG_PENALTY = 9.0      # 每个缩读词的扣分
IDEAL_LO, IDEAL_HI = 35, 110


def load_target_words():
    """返回 (目标词 dict, 教材已知词 set)

    目标词 = 7A/8A（初中）；已知词 = 6A/7A/8A 全部词汇（用于生词密度判定的兜底）
    """
    sys.path.insert(0, BACKEND)
    from wordbank_shcep import get_shcep_libraries
    words, known = {}, set()
    for lib in get_shcep_libraries():
        is_target = lib["id"].startswith(("sys-7a-", "sys-8a-"))
        for w in lib["words"]:
            key = w["word"].strip().lower()
            if not key:
                continue
            known.add(key)
            if is_target:
                words.setdefault(key, []).append(lib["id"])
    return words, known


def iter_sentences(path):
    with open(path, encoding="utf-8", errors="ignore") as f:
        for raw in f:
            line = raw.strip()
            if not line:
                continue
            line = STAGE_RE.sub(" ", line)
            line = SPEAKER_RE.sub("", line)
            for sent in SENT_SPLIT.split(line):
                sent = " ".join(sent.split())
                if sent:
                    yield sent


def build_frequency(sentences):
    cnt = Counter()
    for s in sentences:
        for t in TOKEN_RE.findall(s.lower()):
            cnt[t] += 1
    return cnt


def word_pattern(word):
    """单词用词边界；短语/含连字符用宽松匹配"""
    if " " in word or "-" in word:
        return re.compile(re.escape(word).replace(r"\ ", r"\s+"), re.I)
    return re.compile(r"\b" + re.escape(word) + r"\b", re.I)


def score_sentence(sent, freq, top_set):
    tokens = [t.lower() for t in TOKEN_RE.findall(sent)]
    n = len(tokens)
    if n < MIN_TOKENS or n > MAX_TOKENS:
        return None
    chars = len(sent)
    if chars < MIN_CHARS or chars > MAX_CHARS:
        return None
    if any(ch in sent for ch in "[]()"):
        return None
    if "--" in sent or "..." in sent:
        return None
    if sent.count("?") > 1:
        return None

    score = 100.0
    # 长度：偏离理想区间扣分
    if chars < IDEAL_LO:
        score -= (IDEAL_LO - chars) * 0.8
    elif chars > IDEAL_HI:
        score -= (chars - IDEAL_HI) * 0.5
    # 生词密度
    for t in tokens:
        if t not in top_set:
            score -= RARE_PENALTY
        if t in SLANG:
            score -= SLANG_PENALTY
    # 首个单词是目标词（大写开头）更像典型例句，略加分
    return score


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("inputs", nargs="+", help="台词 txt 文件或所在目录")
    ap.add_argument("-o", "--out", default="friends_examples.json")
    ap.add_argument("--report", default="friends_examples_report.txt")
    args = ap.parse_args()

    files = []
    skip = {os.path.abspath(args.out), os.path.abspath(args.report)}
    for p in args.inputs:
        if os.path.isdir(p):
            files += [os.path.join(p, f) for f in sorted(os.listdir(p))
                      if f.lower().endswith((".txt", ".md"))]
        else:
            files.append(p)
    files = [f for f in files if os.path.abspath(f) not in skip]
    if not files:
        print("没有找到台词文本文件")
        return 1

    targets, textbook_known = load_target_words()
    print(f"目标词 {len(targets)} 个（7A/8A），台词文件 {len(files)} 个")

    # 第一遍：收集句子 + 统计词频
    corpus = []  # (sentence, filename)
    freq = Counter()
    for path in files:
        name = os.path.basename(path)
        for sent in iter_sentences(path):
            corpus.append((sent, name))
            for t in TOKEN_RE.findall(sent.lower()):
                freq[t] += 1
    print(f"句子总数 {len(corpus)}，唯一词形 {len(freq)}")

    top_set = {w for w, _ in freq.most_common(TOP_FREQ)}
    # 目标词与教材词汇永远不算生词
    top_set |= textbook_known
    top_set |= set(targets)

    # 第二遍：为每个目标词挑最优句
    best = {}
    patterns = {w: word_pattern(w) for w in targets}
    for sent, name in corpus:
        low = sent.lower()
        for w, pat in patterns.items():
            if w in best and best[w]["score"] >= 96:
                continue
            if pat.search(low) is None:
                continue
            sc = score_sentence(sent, freq, top_set)
            if sc is None:
                continue
            if w not in best or sc > best[w]["score"]:
                best[w] = {"sentence": sent, "score": round(sc, 1), "source": name}

    with open(args.out, "w", encoding="utf-8", newline="\n") as f:
        json.dump(best, f, ensure_ascii=False, indent=2)

    hit, miss = len(best), len(targets) - len(best)
    with open(args.report, "w", encoding="utf-8", newline="\n") as f:
        f.write(f"目标词 {len(targets)} | 命中 {hit} | 未命中 {miss}\n")
        f.write(f"覆盖率 {hit / len(targets):.1%}\n\n")
        f.write("=== 未命中词表 ===\n")
        f.write(" ".join(sorted(set(targets) - set(best))) + "\n\n")
        f.write("=== 命中样例（分数前 30）===\n")
        for w, v in sorted(best.items(), key=lambda kv: -kv[1]["score"])[:30]:
            f.write(f"{v['score']:5.1f}  {w:<16} {v['sentence']}   [{v['source']}]\n")
    print(f"命中 {hit}/{len(targets)}（{hit / len(targets):.1%}）-> {args.out}")
    print(f"报告：{args.report}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
