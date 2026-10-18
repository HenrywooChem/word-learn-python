# -*- coding: utf-8 -*-
"""单词词形变化生成

按词性生成教材需要掌握的变化形式：
  名词 -> 复数
  动词 -> 第三人称单数 / 现在分词 / 过去式 / 过去分词
  形容词、副词 -> 比较级 / 最高级

只输出当前词性适用的项，避免给 "beautiful" 生成 "beautifuls" 这类噪音。
短语（含空格或连字符）不处理。
"""

VOWELS = set("aeiou")

# ==================== 名词 ====================

# 不规则复数
IRREGULAR_PLURALS = {
    "child": "children",
    "person": "people",
    "man": "men",
    "woman": "women",
    "foot": "feet",
    "tooth": "teeth",
    "goose": "geese",
    "mouse": "mice",
    "louse": "lice",
    "ox": "oxen",
    "sheep": "sheep",
    "fish": "fish",
    "deer": "deer",
    "means": "means",
    "series": "series",
    "species": "species",
    "crisis": "crises",
    "analysis": "analyses",
    "basis": "bases",
    "phenomenon": "phenomena",
    "datum": "data",
    "medium": "media",
    "curriculum": "curricula",
}

# 不可数名词（不加复数）
UNCOUNTABLE = {
    "information", "advice", "news", "money", "water", "milk", "bread", "rice",
    "homework", "housework", "music", "weather", "traffic", "luggage", "baggage",
    "furniture", "equipment", "knowledge", "progress", "courage", "health", "fun",
    "work", "food", "electricity", "energy", "air", "salt", "sugar", "butter",
    "cheese", "meat", "research", "evidence", "education", "happiness", "sadness",
    "kindness", "beauty", "pollution", "rubbish", "garbage", "trash", "clothing",
    "jewellery", "jewelry", "software", "hardware", "vocabulary", "grammar",
    "english", "chinese", "math", "mathematics", "physics", "chemistry",
    "biology", "geography", "history", "art", "pe", "cotton", "ink", "paper",
}

# -f / -fe 变 -ves
F_TO_VES = {
    "leaf", "life", "knife", "wife", "half", "shelf", "thief", "wolf", "loaf",
    "calf", "scarf", "self", "elf",
}

# -o 结尾加 -es
O_TO_OES = {
    "potato", "tomato", "hero", "echo", "volcano", "mosquito", "torpedo",
}


def plural_of(w: str) -> str:
    """名词复数"""
    if w in IRREGULAR_PLURALS:
        return IRREGULAR_PLURALS[w]
    if w in UNCOUNTABLE or not w.isalpha():
        return ""
    # policeman / fireman / gentleman 等合成词
    if w.endswith("man") and w not in ("human", "german", "roman", "shaman"):
        return w[:-3] + "men"
    if w.endswith("woman"):
        return w[:-5] + "women"
    if w in F_TO_VES:
        return w[:-2] + "ves" if w.endswith("fe") else w[:-1] + "ves"
    if w.endswith("y") and len(w) > 1 and w[-2] not in VOWELS:
        return w[:-1] + "ies"
    if w.endswith(("s", "x", "z", "ch", "sh")):
        return w + "es"
    if w in O_TO_OES:
        return w + "es"
    if w.endswith("o"):
        return w + "s"
    return w + "s"


# ==================== 动词 ====================

# 需要双写词尾辅音的词（多音节，靠规则判断不准）
DOUBLE_FINAL = {
    "begin", "prefer", "admit", "occur", "refer", "regret", "permit", "commit",
    "control", "upset", "forget", "equip", "compel", "expel", "rebel", "transfer",
    "submit", "travel", "cancel", "label", "quarrel", "signal", "model", "level",
    "pedal", "patrol", "kidnap", "program",
}

# 三单特殊
THIRD_SPECIAL = {"have": "has", "be": "is", "do": "does", "go": "goes"}

# 现在分词：不去 e 的词
KEEP_E_ING = {"see", "agree", "free", "knee", "flee", "dye", "hoe", "toe", "canoe"}


def _syllables(w: str) -> int:
    """粗略音节数（用于判断是否该双写词尾）"""
    n = sum(1 for i, c in enumerate(w) if c in VOWELS and (i == 0 or w[i - 1] not in VOWELS))
    if w.endswith("e") and not w.endswith(("le", "ee", "ye")) and n > 1:
        n -= 1
    return max(1, n)


def _is_cvc(w: str) -> bool:
    """单音节 辅音-元音-辅音 结尾（且结尾不是 w/x/y）"""
    if len(w) < 3:
        return False
    a, b, c = w[-3], w[-2], w[-1]
    return a not in VOWELS and b in VOWELS and c not in VOWELS and c not in "wxy"


def third_person(w: str) -> str:
    """动词第三人称单数"""
    if w in THIRD_SPECIAL:
        return THIRD_SPECIAL[w]
    if w.endswith("y") and len(w) > 1 and w[-2] not in VOWELS:
        return w[:-1] + "ies"
    if w.endswith(("s", "x", "z", "ch", "sh", "o")):
        return w + "es"
    return w + "s"


def present_participle(w: str) -> str:
    """现在分词 -ing"""
    if w in ("be", "see", "flee", "agree", "free", "knee"):
        return w + "ing" if w != "be" else "being"
    if w.endswith("ie"):
        return w[:-2] + "ying"
    if w.endswith("e") and w not in KEEP_E_ING and not w.endswith(("ee", "ye", "oe")):
        return w[:-1] + "ing"
    if w in DOUBLE_FINAL or (_syllables(w) == 1 and _is_cvc(w)):
        return w + w[-1] + "ing"
    return w + "ing"


def past_tense(w: str, irregular: dict = None) -> tuple:
    """过去式/过去分词，返回 (past, pp, 是否不规则)"""
    if irregular and w in irregular:
        return irregular[w]["past"], irregular[w]["pp"], True
    if w.endswith("e"):
        base = w + "d"
    elif w.endswith("y") and len(w) > 1 and w[-2] not in VOWELS:
        base = w[:-1] + "ied"
    elif w in DOUBLE_FINAL or (_syllables(w) == 1 and _is_cvc(w)):
        base = w + w[-1] + "ed"
    else:
        base = w + "ed"
    return base, base, False


# ==================== 形容词 / 副词 ====================

IRREGULAR_COMPARE = {
    "good": ("better", "best"),
    "well": ("better", "best"),
    "bad": ("worse", "worst"),
    "badly": ("worse", "worst"),
    "many": ("more", "most"),
    "much": ("more", "most"),
    "little": ("less", "least"),
    "far": ("farther", "farthest"),
    "old": ("older", "oldest"),
    "early": ("earlier", "earliest"),
}

# 双音节但按 -er/-est 变化的词尾
SHORT_TAILS = ("ow", "le", "y")

# 没有比较级/最高级（或用法固定）的形容词
NO_COMPARE = {
    "other", "outside", "online", "dead", "unique", "perfect", "favourite",
    "favorite", "daily", "weekly", "monthly", "yearly", "main", "only",
    "right", "wrong", "final", "whole", "total", "wooden", "golden",
    "Chinese", "English", "African", "Asian", "European", "American",
}


def compare_forms(w: str, is_adverb: bool = False) -> tuple:
    """比较级/最高级

    副词（尤其 -ly 结尾）一般用 more/most，early/hard/fast 等除外。
    """
    if w in IRREGULAR_COMPARE:
        return IRREGULAR_COMPARE[w]
    if w in NO_COMPARE:
        return ("", "")
    if is_adverb and w.endswith("ly") and w not in IRREGULAR_COMPARE:
        return ("more " + w, "most " + w)
    syllables = _syllables(w)
    short = syllables == 1 or (syllables == 2 and w.endswith(SHORT_TAILS))
    if not short:
        return ("more " + w, "most " + w)
    if w.endswith("y") and len(w) > 1 and w[-2] not in VOWELS:
        return (w[:-1] + "ier", w[:-1] + "iest")
    if w.endswith("e"):
        return (w + "r", w + "st")
    if w in DOUBLE_FINAL or (syllables == 1 and _is_cvc(w)):
        return (w + w[-1] + "er", w + w[-1] + "est")
    return (w + "er", w + "est")


# ==================== 对外接口 ====================

def _pos_tokens(pos: str) -> set:
    """'v./n.'、'n. & v.' -> {'v.', 'n.'}"""
    raw = (pos or "").replace("&", "/").replace(",", "/").replace(" and ", "/")
    return {p.strip() for p in raw.split("/") if p.strip()}


def build_word_forms(word: str, pos: str = "", irregular: dict = None) -> dict:
    """生成词形变化

    返回 {"plural": ..., "third": ..., "ing": ..., "past": ..., "pp": ...,
          "comparative": ..., "superlative": ...}
    仅包含适用的键；无变化时返回空 dict。
    """
    w = (word or "").strip().lower()
    if not w or not w.isalpha() or len(w) < 2:
        return {}
    if w.endswith("ing") and len(w) > 6:      # 词库里有动名词形式，跳过
        pass

    tokens = _pos_tokens(pos)
    forms = {}

    if "n." in tokens:
        pl = plural_of(w)
        if pl and pl != w:
            forms["plural"] = pl

    # 情态动词（can/must/should...）没有人称和分词变化，不生成
    if "v." in tokens and "modal v." not in tokens:
        forms["third"] = third_person(w)
        forms["ing"] = present_participle(w)
        past, pp, _ = past_tense(w, irregular)
        forms["past"] = past
        forms["pp"] = pp

    if "adj." in tokens or "adv." in tokens:
        comp, sup = compare_forms(w, is_adverb=("adv." in tokens and "adj." not in tokens))
        if comp:
            forms["comparative"] = comp
            forms["superlative"] = sup

    return forms
