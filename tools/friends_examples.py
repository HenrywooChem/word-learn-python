# -*- coding: utf-8 -*-
"""
美剧台词例句匹配流水线（含内容安全过滤层）

用途：从美剧台词脚本（纯文本）里，为上海版教材词库（7A/8A，初中）的每个单词
     挑选"生词密度低、句子完整独立、长度适中、内容适合中学生"的地道例句。

用法：
    python tools/friends_examples.py ../data/tv_scripts/2_broke_girls \
        -o data/tv_examples_2bg.json \
        --emit-py backend/word_examples_tv.py \
        --review-dir review --review-count 100

输出：
    JSON: { "word": {"sentence": "...", "score": 88.5, "source": "S01E01.txt",
                     "grade": ["sys-7a"], "flags": []} }
    PY  : backend/word_examples_tv.py（TV_EXAMPLES 字典，供 word_data.enrich_word 使用）
    MD/HTML: 人工复核抽样

过滤层设计（三层）：
  1) 结构层：剔舞台提示、方括号、破折号、过短/过长、疑似两人台词粘连
  2) 安全层：硬黑名单（性/脏话/毒品/暴力/歧视）直接丢弃；软黑名单（轻度冒犯、
     饮酒、恋爱暗示）只扣分，没更好选择时仍可用
  3) 质量层：生词密度、口语缩读、句首句尾规范度打分

注意：目标词本身命中黑名单时豁免该词（否则教材词 die / shot 之类永远选不到），
     但句中其他违规词仍会触发过滤。
"""
import argparse
import html
import json
import os
import random
import re
import sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
BACKEND = os.path.join(os.path.dirname(HERE), "backend")

# ==================== 内容安全：硬黑名单 ====================
# 命中即整句丢弃。词尾 "*" 表示前缀匹配（fuck* 命中 fucking / fucked）
HARD_BANNED = {
    # --- 性 / 身体 ---
    "sex": "sexual", "sexy": "sexual", "sexual": "sexual", "sexually": "sexual",
    "boob": "sexual", "boobs": "sexual", "breast": "sexual", "breasts": "sexual",
    "nipple": "sexual", "nipples": "sexual", "vagina": "sexual", "penis": "sexual",
    "orgasm": "sexual", "orgasms": "sexual", "porn": "sexual", "porno": "sexual",
    "porn*": "sexual", "horny": "sexual", "condom": "sexual", "condoms": "sexual",
    "virgin": "sexual", "virginity": "sexual", "slut": "sexual", "sluts": "sexual",
    "whore": "sexual", "whores": "sexual", "hooker": "sexual", "prostitute": "sexual",
    "blowjob": "sexual", "handjob": "sexual", "threesome": "sexual",
    "masturbat*": "sexual", "erection": "sexual", "aroused": "sexual",
    "foreplay": "sexual", "orgy": "sexual", "kinky": "sexual", "fetish": "sexual",
    "butt": "sexual", "booty": "sexual", "ass": "sexual", "asses": "sexual",
    "gay": "adult", "lesbian": "adult", "lesbians": "adult", "crotch": "sexual", "pubic": "sexual",
    "tampon": "sexual", "tampons": "sexual", "panties": "sexual", "lingerie": "sexual",
    "nude": "sexual", "naked": "sexual", "std": "sexual", "herpes": "sexual",
    "viagra": "sexual", "steroid": "sexual", "steroids": "sexual",
    "stripper": "sexual", "strippers": "sexual", "stripping": "sexual",
    "pimp": "sexual", "pimps": "sexual", "escort": "sexual", "massage": "sexual",
    "pregnancy": "sexual", "pregnant": "sexual", "abortion": "sexual",
    "libido": "sexual", "seduc*": "sexual", "seduct*": "sexual",
    "flirt*": "sexual",
    # --- 脏话 ---
    "fuck*": "profanity", "shit*": "profanity", "bullshit": "profanity",
    "bitch*": "profanity", "bastard": "profanity", "dick": "profanity",
    "dicks": "profanity", "cock": "profanity", "pussy": "profanity",
    "cunt": "profanity", "asshole": "profanity", "assholes": "profanity",
    "arse": "profanity", "douche": "profanity", "douchebag": "profanity",
    "prick": "profanity", "twat": "profanity", "wank*": "profanity",
    "jerkoff": "profanity", "goddamn": "profanity", "goddammit": "profanity",
    # --- 歧视 / 侮辱 ---
    "retard*": "slur", "fag*": "slur", "dyke": "slur", "chink": "slur",
    "nigger": "slur", "nigga": "slur", "spic": "slur", "wetback": "slur",
    "tranny": "slur", "cripple": "slur", "homo": "slur", "racist": "slur",
    # --- 毒品 / 酒精 ---
    "weed": "drugs", "marijuana": "drugs", "cocaine": "drugs", "heroin": "drugs",
    "meth": "drugs", "ecstasy": "drugs", "bong": "drugs", "overdose": "drugs",
    "stoned": "drugs", "drunk": "drugs", "drunkard": "drugs",
    "vodka": "drugs", "whisky": "drugs", "whiskey": "drugs", "tequila": "drugs",
    "beer": "drugs", "booze": "drugs", "hangover": "drugs",
    "cigarette": "drugs", "cigarettes": "drugs", "cigar": "drugs",
    # --- 暴力 / 死亡 ---
    "murder*": "violence", "suicide": "violence", "rape*": "violence",
    "stab*": "violence", "gun": "violence", "guns": "violence",
    "pistol": "violence", "shooting": "violence", "corpse": "violence",
    "vomit*": "violence", "puke": "violence", "diarrhea": "violence",
}

# ==================== 内容安全：软黑名单（扣分不丢弃） ====================
SOFT_BANNED = {
    "damn": "mild", "hell": "mild", "crap": "mild", "piss*": "mild",
    "sucks": "mild", "sucked": "mild", "screw": "mild", "stupid": "mild",
    "idiot": "mild", "moron": "mild", "loser": "mild", "dumb": "mild",
    "shut": "mild", "hate": "mild", "kill": "mild", "killed": "mild",
    "die": "mild", "dead": "mild", "dying": "mild", "death": "mild",
    "drink": "alcohol", "drinks": "alcohol", "drinking": "alcohol",
    "bar": "alcohol", "wine": "alcohol", "dating": "romance",
    "kiss": "romance", "kissed": "romance", "kissing": "romance",
    "boyfriend": "romance", "girlfriend": "romance", "cheat": "romance",
    "cheated": "romance", "cheating": "romance", "sober": "mild",
    "cancer": "mild", "hep": "mild",
}

# 短语级黑名单（不分词，直接正则）
HARD_PHRASES = [
    (r"\bsleep(?:s|ing)?\s+with\b", "sexual"),
    (r"\bslept\s+with\b", "sexual"),
    (r"\bhook(?:ed|ing)?\s+up\b", "sexual"),
    (r"\bmak(?:e|es|ing)\s+out\b", "sexual"),
    (r"\bmade\s+out\b", "sexual"),
    (r"\bone[\s-]night\s+stand\b", "sexual"),
    (r"\bfriends?\s+with\s+benefits\b", "sexual"),
    (r"\bstrip\s+club\b", "sexual"),
    (r"\blap\s+dance\b", "sexual"),
    (r"\bjerk\s+off\b", "profanity"),
    (r"\bscrew\s+you\b", "profanity"),
    (r"\bgo\s+to\s+hell\b", "profanity"),
    (r"\bget\s+high\b", "drugs"),
    (r"\bget\s+drunk\b", "drugs"),
    (r"\bpassed\s+out\b", "drugs"),
    (r"\bkill(?:ed|ing)?\s+(?:you|him|her|me|them)\b", "violence"),
    (r"\bdead\s+body\b", "violence"),
    (r"\bhang(?:ed|ing)?\s+(?:him|her|my)self\b", "violence"),
    (r"\bkill\s+(?:my|him|her)self\b", "violence"),
    (r"\bself[\s-]harm\b", "violence"),
    (r"\btook\s+(?:its|his|her)\s+own\s+life\b", "violence"),
    (r"\bdrug\s+addicts?\b", "drugs"),
    (r"\bpot\s+dealer\b", "drugs"),
    (r"\bbirth\s+control\b", "sexual"),
    (r"\bpaternity\b", "sexual"),
    (r"\bmake\s+it\s+clap\b", "sexual"),
    (r"\blady\s+parts?\b", "sexual"),
    (r"\bput\s+a\s+baby\s+in\b", "sexual"),
    (r"\bhates?\s+women\b", "slur"),
    (r"\bfive\s+silver\s+rings\b", "mild"),
    (r"\bbaby[\s-]making\b", "sexual"),
    (r"\bcleavage\b", "sexual"),
    (r"\burine\b", "sexual"),
    # --- 性暗示短语（2 Broke Girls 高频，必须显式拦）---
    (r"\bspread\s+(?:your|her|his|my)\s+legs?\b", "sexual"),
    (r"\bopen\s+(?:your|her|his|my)\s+legs?\b", "sexual"),
    (r"\blegs?\s+apart\b", "sexual"),
    (r"\btouch\s+(?:your|him)self\b", "sexual"),
    (r"\bback\s*door\b", "sexual"),
    (r"\bturn(?:s|ed|ing)?\s+(?:me|you|him|her)\s+on\b", "sexual"),
    (r"\bin\s+bed\s+with\b", "sexual"),
    (r"\bsleep\s+together\b", "sexual"),
    (r"\bsugar\s+daddy\b", "sexual"),
    (r"\bba\s*d+ies?\b", "sexual"),
    (r"\bnice\s+(?:boobs|butt|ass)\b", "sexual"),
    (r"\bdown\s+there\b", "sexual"),
]

SOFT_PHRASES = [
    (r"\bi\s+hate\b", "mild"),
    (r"\bshut\s+up\b", "mild"),
    (r"\bslept\s+together\b", "romance"),
    (r"\bcame\s+on\s+to\b", "romance"),
    (r"\bhit\s+on\b", "romance"),
]

# 口语缩读/俚语扣分词
SLANG = {
    "gonna", "wanna", "gotta", "kinda", "sorta", "dunno", "ain", "aint", "yeah",
    "yep", "nope", "uh", "um", "oh", "hey", "hi", "okay", "ok", "huh", "wow",
    "y", "know", "em", "ya", "whaddya", "whatcha", "gimme", "lemme", "c_mon",
    "cause", "cos", "cuz", "til", "em", "nah", "hmm", "mmm", "whoa", "yo",
}

# 说话人标签 / 舞台提示
SPEAKER_RE = re.compile(r"^\s*(?:\[[^\]]*\]\s*)?(?:[A-Z][A-Za-z .'\-]{0,20}):\s*")
PAREN_RE = re.compile(r"\([^)]*\)")
STAGE_RE = re.compile(r"\[[^\]]*\]")
LEAD_JUNK_RE = re.compile(r"^[\s\-–—*•\"'`]+")
DIGIT_RE = re.compile(r"\d")

SENT_SPLIT = re.compile(r"(?<=[.!?])\s+")
TOKEN_RE = re.compile(r"[A-Za-z][A-Za-z'\-]*")
APOS = str.maketrans({"\u2019": "'", "\u2018": "'", "\u02bc": "'"})

MIN_CHARS, MAX_CHARS = 22, 150
MIN_TOKENS, MAX_TOKENS = 5, 24
TOP_FREQ = 2000          # 语料高频词门槛
RARE_PENALTY = 22.0      # 每个超纲词的扣分
SLANG_PENALTY = 9.0      # 每个缩读词的扣分
SOFT_PENALTY = 12.0      # 每个软黑名单词的扣分
IDEAL_LO, IDEAL_HI = 35, 110

# 句中突兀出现的大写功能词 = 两人台词被源站粘在一行
MERGED_CAPS = {
    "Is", "Are", "Do", "Does", "Did", "Can", "Could", "Will", "Would", "Should",
    "What", "Why", "How", "Where", "Who", "When", "Hey", "Oh", "No", "Yes",
    "You", "I", "We", "They", "He", "She", "It", "This", "That", "My", "Your",
}


# ==================== 词表加载 ====================
def load_target_words():
    """返回 (目标词 dict[word] -> [lib_id], 教材已知词 set, 词->释义)"""
    sys.path.insert(0, BACKEND)
    from wordbank_shcep import get_shcep_libraries
    words, known, meaning = {}, set(), {}
    for lib in get_shcep_libraries():
        lib_id = lib["id"]
        is_target = lib_id.startswith(("sys-7a-", "sys-8a-"))
        for w in lib["words"]:
            key = w["word"].strip().lower()
            if not key:
                continue
            known.add(key)
            meaning.setdefault(key, w.get("meaning", ""))
            if is_target:
                words.setdefault(key, [])
                if lib_id not in words[key]:
                    words[key].append(lib_id)
    return words, known, meaning


def word_forms(word):
    """目标词的可能词形（轻量词形还原，避免只见原形漏掉 -ed/-ing/-s）"""
    w = word.lower()
    if " " in w or "-" in w:
        return {w}
    forms = {w, w + "s", w + "es", w + "ed", w + "d", w + "ing"}
    if w.endswith("y") and len(w) > 2 and w[-2] not in "aeiou":
        stem = w[:-1]
        forms |= {stem + "ies", stem + "ied"}
    if w.endswith("e"):
        forms |= {w[:-1] + "ing", w[:-1] + "ed"}
    if len(w) > 3 and w[-1] not in "aeiou" and w[-2] in "aeiou" and w[-3] not in "aeiou":
        forms |= {w + w[-1] + "ed", w + w[-1] + "ing"}   # stop -> stopped
    return forms


# ==================== 句子切分 ====================
def iter_sentences(path):
    with open(path, encoding="utf-8", errors="ignore") as f:
        for raw in f:
            line = raw.strip()
            if not line:
                continue
            if any(k in line for k in ("LAUGHTER", "APPLAUSE", "MUSIC", "♪")):
                continue
            line = STAGE_RE.sub(" ", line)
            line = PAREN_RE.sub(" ", line)
            line = SPEAKER_RE.sub("", line)
            for sent in SENT_SPLIT.split(line):
                sent = " ".join(sent.split())
                sent = LEAD_JUNK_RE.sub("", sent).strip()
                sent = sent.strip("\"'` ")
                if sent:
                    yield sent


# ==================== 安全过滤 ====================
def _banned_hit(token, table):
    """精确或前缀命中黑名单，返回类别或 None"""
    if token in table:
        return table[token]
    for pat, cat in table.items():
        if pat.endswith("*") and token.startswith(pat[:-1]):
            return cat
    return None


def safety_check(sent, target=None):
    """返回 (hard_category|None, soft_categories list, matched list)"""
    low = sent.lower().translate(APOS)
    toks = [t.strip("'-") for t in TOKEN_RE.findall(low)]

    hard, soft, matched = None, [], []

    # 短语级（先查，命中即硬丢弃）
    for pat, cat in HARD_PHRASES:
        m = re.search(pat, low)
        if m:
            if target and target in m.group(0).split():
                continue
            hard = hard or cat
            matched.append(m.group(0))
    for pat, cat in SOFT_PHRASES:
        m = re.search(pat, low)
        if m:
            soft.append(cat)
            matched.append(m.group(0))

    for t in toks:
        if target and t in word_forms(target):
            continue          # 目标词自身豁免
        cat = _banned_hit(t, HARD_BANNED)
        if cat:
            hard = hard or cat
            matched.append(t)
            continue
        cat = _banned_hit(t, SOFT_BANNED)
        if cat:
            soft.append(cat)
            matched.append(t)
    return hard, sorted(set(soft)), matched


def looks_merged(sent):
    """检测两人台词被粘连成一句：句中突兀出现大写功能词"""
    words = sent.split()
    for i, w in enumerate(words[1:], 1):
        core = w.strip("\"'`,.!?")
        if core in MERGED_CAPS:
            # 前一个词以句读结尾则属正常
            if words[i - 1].endswith((".", "!", "?", ",", ":", ";")):
                continue
            return True
    return False


# ==================== 质量打分 ====================
def score_sentence(sent, top_set):
    tokens = [t.lower() for t in TOKEN_RE.findall(sent)]
    n = len(tokens)
    if n < MIN_TOKENS or n > MAX_TOKENS:
        return None
    chars = len(sent)
    if chars < MIN_CHARS or chars > MAX_CHARS:
        return None
    if any(ch in sent for ch in "[](){}"):
        return None
    if "--" in sent or "..." in sent or "…" in sent:
        return None
    if sent.count("?") > 1:
        return None
    if not sent[0].isupper():
        return None
    letters = [c for c in sent if c.isalpha()]
    if letters and sum(1 for c in letters if c.isupper()) / len(letters) > 0.7:
        return None      # 全大写 = 喊叫/字幕强调，不做例句
    if sent[-1] not in ".!?":
        return None
    if DIGIT_RE.search(sent):
        return None
    if looks_merged(sent):
        return None
    # 至少一半词是常见词，避免整句都是专有名词
    known = sum(1 for t in tokens if t in top_set)
    if known < n * 0.5:
        return None

    score = 100.0
    if chars < IDEAL_LO:
        score -= (IDEAL_LO - chars) * 0.8
    elif chars > IDEAL_HI:
        score -= (chars - IDEAL_HI) * 0.5
    # 逗号/连词堆叠 = 口语流水句，做例句偏难
    commas = sent.count(",")
    if commas >= 3:
        score -= (commas - 2) * 5
    if sent.count(" and ") >= 2:
        score -= 4
    if sent.lower().startswith(("and ", "but ", "so ", "well ", "now ", "then ",
                                "also ", "okay ", "oh ", "hey ")):
        score -= 5
    for t in tokens:
        if t not in top_set:
            score -= RARE_PENALTY
        if t in SLANG:
            score -= SLANG_PENALTY
    return score


# ==================== 主流程 ====================
def phrase_pattern(phrase):
    """短语整串匹配，前后加字母边界，避免 any time 命中 many times"""
    body = re.escape(phrase.lower()).replace(r"\ ", r"\s+").replace(r"\-", r"[-\s]?")
    return re.compile(r"(?<![A-Za-z])" + body + r"(?![A-Za-z])", re.I)


def build_index(targets):
    """词形 -> 目标词列表；短语单独一组"""
    idx, phrases = defaultdict(list), []
    for w in targets:
        if " " in w or "-" in w:
            phrases.append(w)
        else:
            for f in word_forms(w):
                if w not in idx[f]:
                    idx[f].append(w)
    return idx, phrases


def collect(files):
    corpus, freq = [], Counter()
    for path in files:
        name = os.path.basename(path)
        for sent in iter_sentences(path):
            corpus.append((sent, name))
            for t in TOKEN_RE.findall(sent.lower()):
                freq[t] += 1
    return corpus, freq


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("inputs", nargs="+", help="台词 txt 文件或所在目录")
    ap.add_argument("-o", "--out", default="tv_examples.json")
    ap.add_argument("--report", default="tv_examples_report.txt")
    ap.add_argument("--emit-py", default="", help="输出 backend/word_examples_tv.py")
    ap.add_argument("--review-dir", default="", help="人工复核抽样输出目录")
    ap.add_argument("--review-count", type=int, default=100)
    ap.add_argument("--min-score", type=float, default=40.0)
    ap.add_argument("--seed", type=int, default=20261017)
    ap.add_argument("--deny-file", default="",
                    help='人工复核否决表 JSON: {"word": ["句子片段", ...], "*": [...]}')
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

    deny, deny_all = {}, set()
    if args.deny_file and os.path.exists(args.deny_file):
        with open(args.deny_file, encoding="utf-8") as f:
            deny = json.load(f)
        deny_all = {w for w, frags in deny.items() if "*" in frags}
        print(f"人工否决表：{len(deny)} 个词（整词放弃 {len(deny_all)} 个）")
    else:
        deny_all = set()

    targets, textbook_known, meanings = load_target_words()
    print(f"目标词 {len(targets)} 个（7A/8A），台词文件 {len(files)} 个")

    corpus, freq = collect(files)
    print(f"句子总数 {len(corpus)}，唯一词形 {len(freq)}")

    top_set = {w for w, _ in freq.most_common(TOP_FREQ)}
    top_set |= textbook_known | set(targets)

    idx, phrases = build_index(targets)
    phrase_pats = {p: phrase_pattern(p) for p in phrases}

    best = {}
    seen_sent = set()
    sent_usage = Counter()
    stats = Counter()          # 结构/安全/质量 各阶段淘汰数
    hard_by_cat = Counter()
    survivors = 0

    for sent, name in corpus:
        key_sent = sent.lower()
        sc = score_sentence(sent, top_set)
        if sc is None:
            stats["结构/质量淘汰"] += 1
            continue
        hard, soft, matched = safety_check(sent)
        if hard:
            stats["安全黑名单淘汰"] += 1
            hard_by_cat[hard] += 1
            continue

        low = sent.lower().translate(APOS)
        toks = [t.strip("'-") for t in TOKEN_RE.findall(low)]
        cands = set()
        for t in toks:
            for w in idx.get(t, ()):
                cands.add(w)
        for p, pat in phrase_pats.items():
            if pat.search(low):
                cands.add(p)
        if not cands:
            continue

        # 目标词豁免后重新做一次安全检查（如目标词本身是 die）
        survivors += 1
        for w in cands:
            if w in deny_all:
                continue
            if any(frag.lower() in low for frag in deny.get(w, ())) or \
               any(frag.lower() in low for frag in deny.get("*", ())):
                continue
            h, s, _m = safety_check(sent, target=w)
            if h:
                continue
            if key_sent in seen_sent and sent_usage[key_sent] >= 2:
                continue
            final = sc - SOFT_PENALTY * len(s) - 3.0 * len(s)
            if final < args.min_score:
                continue
            if w not in best or final > best[w]["score"]:
                if w not in best:
                    sent_usage[key_sent] += 1
                best[w] = {
                    "sentence": sent,
                    "score": round(final, 1),
                    "source": name,
                    "grade": sorted({g.split("-")[1] for g in targets[w]}),
                    "flags": s,
                }
                seen_sent.add(key_sent)

    os.makedirs(os.path.dirname(os.path.abspath(args.out)) or ".", exist_ok=True)
    with open(args.out, "w", encoding="utf-8", newline="\n") as f:
        json.dump(dict(sorted(best.items())), f, ensure_ascii=False, indent=2)

    hit = len(best)
    miss_words = sorted(set(targets) - set(best))
    with open(args.report, "w", encoding="utf-8", newline="\n") as f:
        f.write(f"目标词 {len(targets)} | 命中 {hit} | 未命中 {len(miss_words)}\n")
        f.write(f"覆盖率 {hit / len(targets):.1%}\n")
        f.write(f"通过安全过滤的候选句 {survivors}\n\n")
        f.write("=== 淘汰统计 ===\n")
        for k, v in stats.most_common():
            f.write(f"{k}: {v}\n")
        f.write("\n=== 硬黑名单命中分布 ===\n")
        for k, v in hard_by_cat.most_common():
            f.write(f"{k}: {v}\n")
        f.write("\n=== 未命中词表（将回退教学例句）===\n")
        f.write(" ".join(miss_words) + "\n\n")
        f.write("=== 命中样例（分数前 30）===\n")
        for w, v in sorted(best.items(), key=lambda kv: -kv[1]["score"])[:30]:
            f.write(f"{v['score']:5.1f}  {w:<16} {v['sentence']}   [{v['source']}]\n")

    print(f"命中 {hit}/{len(targets)}（{hit / len(targets):.1%}）-> {args.out}")
    print("淘汰统计:", dict(stats))
    print("硬黑名单:", dict(hard_by_cat))
    print(f"报告：{args.report}")

    if args.emit_py:
        write_py(args.emit_py, best, meanings)
        print(f"已生成 {args.emit_py}")

    if args.review_dir:
        write_review(args.review_dir, best, meanings, args.review_count, args.seed)
        print(f"复核抽样 -> {args.review_dir}")

    return 0


def write_py(path, best, meanings):
    lines = [
        '"""',
        "美剧台词例句（自动生成，请勿手工编辑）",
        "生成命令：python tools/friends_examples.py data/tv_scripts/2_broke_girls \\",
        "            -o data/tv_examples_2bg.json --emit-py backend/word_examples_tv.py",
        "",
        "仅覆盖 7A/8A 词库中命中台词的词；未命中的词仍使用教材/教学例句。",
        "所有句子已通过 tools/friends_examples.py 的内容安全黑名单过滤。",
        '"""',
        "",
        "TV_EXAMPLES = {",
    ]
    for w in sorted(best):
        v = best[w]
        sent = v["sentence"].replace("\\", "\\\\").replace('"', '\\"')
        lines.append(
            f'    "{w}": ("{sent}", "{v["source"]}", {v["score"]}),')
    lines.append("}")
    lines.append("")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines))


def write_review(outdir, best, meanings, count, seed):
    os.makedirs(outdir, exist_ok=True)
    items = [(w, v) for w, v in sorted(best.items())]
    random.Random(seed).shuffle(items)
    sample = items[:count]

    rows = []
    for i, (w, v) in enumerate(sorted(sample, key=lambda kv: (-kv[1]["score"])), 1):
        rows.append(
            f"| {i} | {w} | {html.escape(meanings.get(w, ''))} | "
            f"{html.escape(v['sentence'], quote=False)} | {v['score']} | {v['source']} | "
            f"{','.join(v['flags']) or '-'} |"
        )
    md = "\n".join([
        f"# 破产姐妹例句人工复核抽样（{len(sample)} 句）",
        "",
        f"总命中 {len(best)} 词，随机种子 {seed} 抽样 {len(sample)} 句，按分数降序。",
        "",
        "| # | 单词 | 释义 | 例句 | 分数 | 来源 | 软标记 |",
        "|---|---|---|---|---|---|---|",
        *rows,
    ])
    with open(os.path.join(outdir, "tv_examples_review.md"), "w",
              encoding="utf-8", newline="\n") as f:
        f.write(md + "\n")

    trs = []
    for i, (w, v) in enumerate(sorted(sample, key=lambda kv: -kv[1]["score"]), 1):
        trs.append(
            "<tr><td>{}</td><td class='w'>{}</td><td class='m'>{}</td>"
            "<td class='s'>{}</td><td class='sc'>{}</td><td class='src'>{}</td></tr>".format(
                i, html.escape(w), html.escape(meanings.get(w, "")[:14]),
                html.escape(v["sentence"], quote=False), v["score"], html.escape(v["source"])))
    page = """<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8">
<title>破产姐妹例句复核</title><style>
body{font-family:-apple-system,"Segoe UI","Microsoft YaHei",sans-serif;margin:0;padding:28px 36px;background:#f6f7f9;color:#1f2328}
h1{font-size:20px;margin:0 0 6px}.sub{color:#6b7280;font-size:13px;margin-bottom:18px}
table{border-collapse:collapse;width:100%;background:#fff;box-shadow:0 1px 3px rgba(0,0,0,.08);border-radius:8px;overflow:hidden}
th{background:#eef1f5;text-align:left;font-size:12px;color:#4b5563;padding:9px 10px;position:sticky;top:0}
td{padding:9px 10px;border-top:1px solid #eef0f3;font-size:13px;vertical-align:top}
td.w{font-weight:600;color:#0b5cad;white-space:nowrap}td.m{color:#6b7280;white-space:nowrap}
td.s{line-height:1.5}td.sc{font-variant-numeric:tabular-nums;color:#16794b;white-space:nowrap}
td.src{color:#9aa1ab;font-size:11px;white-space:nowrap}
tr:nth-child(even) td{background:#fbfcfd}
</style></head><body>
<h1>破产姐妹台词例句 · 人工复核抽样</h1>
<div class="sub">共 __TOTAL__ 词命中，随机抽 __SAMPLE__ 句（按分数降序）。重点看：句子是否完整、是否像地道口语、有无不适合中学生的内容。</div>
<table><thead><tr><th>#</th><th>单词</th><th>释义</th><th>例句</th><th>分数</th><th>来源</th></tr></thead>
<tbody>__ROWS__</tbody></table></body></html>"""
    page = (page.replace("__TOTAL__", str(len(best)))
                .replace("__SAMPLE__", str(len(sample)))
                .replace("__ROWS__", "\n".join(trs)))
    with open(os.path.join(outdir, "tv_examples_review.html"), "w",
              encoding="utf-8", newline="\n") as f:
        f.write(page)


if __name__ == "__main__":
    sys.exit(main())
