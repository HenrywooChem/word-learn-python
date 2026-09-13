"""
上海教育出版社·五四学制教材词库（上册系列）
数据来源：word_bank_6A/7A/8A.json + irregular_verbs_7A/8A.json（教材 OCR 提取）
由生成脚本自动转换，请勿手工编辑词条
"""

# 教材不规则动词表（7A/8A 附录合并去重）
TEXTBOOK_IRREGULAR = {
    "awake": {
        "past": "awoke",
        "pp": "awoken"
    },
    "be (am, is, are)": {
        "past": "was, were",
        "pp": "been"
    },
    "bear": {
        "past": "bore",
        "pp": "born/borne"
    },
    "beat": {
        "past": "beat",
        "pp": "beaten"
    },
    "become": {
        "past": "became",
        "pp": "become"
    },
    "begin": {
        "past": "began",
        "pp": "begun"
    },
    "bleed": {
        "past": "bled",
        "pp": "bled"
    },
    "blow": {
        "past": "blew",
        "pp": "blown"
    },
    "break": {
        "past": "broke",
        "pp": "broken"
    },
    "bring": {
        "past": "brought",
        "pp": "brought"
    },
    "build": {
        "past": "built",
        "pp": "built"
    },
    "burn": {
        "past": "burnt/burned",
        "pp": "burnt/burned"
    },
    "buy": {
        "past": "bought",
        "pp": "bought"
    },
    "can": {
        "past": "could",
        "pp": "/"
    },
    "catch": {
        "past": "caught",
        "pp": "caught"
    },
    "choose": {
        "past": "chose",
        "pp": "chosen"
    },
    "come": {
        "past": "came",
        "pp": "come"
    },
    "cost": {
        "past": "cost",
        "pp": "cost"
    },
    "cut": {
        "past": "cut",
        "pp": "cut"
    },
    "deal": {
        "past": "dealt",
        "pp": "dealt"
    },
    "dig": {
        "past": "dug",
        "pp": "dug"
    },
    "do": {
        "past": "did",
        "pp": "done"
    },
    "draw": {
        "past": "drew",
        "pp": "drawn"
    },
    "dream": {
        "past": "dreamt/dreamed",
        "pp": "dreamt/dreamed"
    },
    "drink": {
        "past": "drank",
        "pp": "drunk"
    },
    "drive": {
        "past": "drove",
        "pp": "driven"
    },
    "eat": {
        "past": "ate",
        "pp": "eaten"
    },
    "fall": {
        "past": "fell",
        "pp": "fallen"
    },
    "feed": {
        "past": "fed",
        "pp": "fed"
    },
    "feel": {
        "past": "felt",
        "pp": "felt"
    },
    "fight": {
        "past": "fought",
        "pp": "fought"
    },
    "find": {
        "past": "found",
        "pp": "found"
    },
    "fly": {
        "past": "flew",
        "pp": "flown"
    },
    "forget": {
        "past": "forgot",
        "pp": "forgotten"
    },
    "freeze": {
        "past": "froze",
        "pp": "frozen"
    },
    "get": {
        "past": "got",
        "pp": "got/gotten"
    },
    "give": {
        "past": "gave",
        "pp": "given"
    },
    "go": {
        "past": "went",
        "pp": "gone"
    },
    "grow": {
        "past": "grew",
        "pp": "grown"
    },
    "hang（悬挂）": {
        "past": "hung",
        "pp": "hung"
    },
    "have": {
        "past": "had",
        "pp": "had"
    },
    "hear": {
        "past": "heard",
        "pp": "heard"
    },
    "hide": {
        "past": "hid",
        "pp": "hidden"
    },
    "hit": {
        "past": "hit",
        "pp": "hit"
    },
    "hold": {
        "past": "held",
        "pp": "held"
    },
    "hurt": {
        "past": "hurt",
        "pp": "hurt"
    },
    "keep": {
        "past": "kept",
        "pp": "kept"
    },
    "know": {
        "past": "knew",
        "pp": "known"
    },
    "lay": {
        "past": "laid",
        "pp": "laid"
    },
    "lead": {
        "past": "led",
        "pp": "led"
    },
    "learn": {
        "past": "learnt/learned",
        "pp": "learnt/learned"
    },
    "leave": {
        "past": "left",
        "pp": "left"
    },
    "lend": {
        "past": "lent",
        "pp": "lent"
    },
    "let": {
        "past": "let",
        "pp": "let"
    },
    "lie（躺）": {
        "past": "lay",
        "pp": "lain"
    },
    "light": {
        "past": "lit/lighted",
        "pp": "lit/lighted"
    },
    "lose": {
        "past": "lost",
        "pp": "lost"
    },
    "make": {
        "past": "made",
        "pp": "made"
    },
    "may": {
        "past": "might",
        "pp": "/"
    },
    "mean": {
        "past": "meant",
        "pp": "meant"
    },
    "meet": {
        "past": "met",
        "pp": "met"
    },
    "mistake": {
        "past": "mistook",
        "pp": "mistaken"
    },
    "must": {
        "past": "had to / must",
        "pp": "/"
    },
    "pay": {
        "past": "paid",
        "pp": "paid"
    },
    "put": {
        "past": "put",
        "pp": "put"
    },
    "read /ri:d/": {
        "past": "read /red/",
        "pp": "read /red/"
    },
    "ride": {
        "past": "rode",
        "pp": "ridden"
    },
    "ring": {
        "past": "rang",
        "pp": "rung"
    },
    "rise": {
        "past": "rose",
        "pp": "risen"
    },
    "run": {
        "past": "ran",
        "pp": "run"
    },
    "say": {
        "past": "said",
        "pp": "said"
    },
    "see": {
        "past": "saw",
        "pp": "seen"
    },
    "sell": {
        "past": "sold",
        "pp": "sold"
    },
    "send": {
        "past": "sent",
        "pp": "sent"
    },
    "set": {
        "past": "set",
        "pp": "set"
    },
    "shake": {
        "past": "shook",
        "pp": "shaken"
    },
    "shall": {
        "past": "should",
        "pp": "/"
    },
    "shine": {
        "past": "shone",
        "pp": "shone"
    },
    "shoot": {
        "past": "shot",
        "pp": "shot"
    },
    "show": {
        "past": "showed",
        "pp": "shown"
    },
    "shut": {
        "past": "shut",
        "pp": "shut"
    },
    "sing": {
        "past": "sang",
        "pp": "sung"
    },
    "sit": {
        "past": "sat",
        "pp": "sat"
    },
    "sleep": {
        "past": "slept",
        "pp": "slept"
    },
    "smell": {
        "past": "smelt/smelled",
        "pp": "smelt/smelled"
    },
    "speak": {
        "past": "spoke",
        "pp": "spoken"
    },
    "speed": {
        "past": "sped/speeded",
        "pp": "sped/speeded"
    },
    "spell": {
        "past": "spelt/spelled",
        "pp": "spelt/spelled"
    },
    "spend": {
        "past": "spent",
        "pp": "spent"
    },
    "spread": {
        "past": "spread",
        "pp": "spread"
    },
    "stand": {
        "past": "stood",
        "pp": "stood"
    },
    "steal": {
        "past": "stole",
        "pp": "stolen"
    },
    "stick": {
        "past": "stuck",
        "pp": "stuck"
    },
    "sweep": {
        "past": "swept",
        "pp": "swept"
    },
    "swim": {
        "past": "swam",
        "pp": "swum"
    },
    "take": {
        "past": "took",
        "pp": "taken"
    },
    "teach": {
        "past": "taught",
        "pp": "taught"
    },
    "tell": {
        "past": "told",
        "pp": "told"
    },
    "think": {
        "past": "thought",
        "pp": "thought"
    },
    "throw": {
        "past": "threw",
        "pp": "thrown"
    },
    "understand": {
        "past": "understood",
        "pp": "understood"
    },
    "wake": {
        "past": "woke",
        "pp": "woken"
    },
    "wear": {
        "past": "wore",
        "pp": "worn"
    },
    "will": {
        "past": "would",
        "pp": "/"
    },
    "win": {
        "past": "won",
        "pp": "won"
    },
    "write": {
        "past": "wrote",
        "pp": "written"
    },
    "understand understood understood wake": {
        "past": "woke",
        "pp": "woken"
    }
}


def get_shcep_libraries():
    """返回上海教育出版社上册系列系统词库"""
    return [
    {
        "id": "sys-6a-u1",
        "name": "六年级上册 Unit 1",
        "grade": "小学",
        "description": "上海版六年级上册 Unit 1 英语词汇（上海教育出版社·五四学制）",
        "created_at": "2024-01-01",
        "words": [
            {
                "id": "g6a1-1",
                "word": "life",
                "phonetic": "/laɪf/",
                "meaning": "(pl. lives) 生活；生命",
                "pos": "n.",
                "unit": "Unit 1"
            },
            {
                "id": "g6a1-2",
                "word": "break",
                "phonetic": "/breɪk/",
                "meaning": "课间休息；间歇；休息",
                "pos": "n.",
                "unit": "Unit 1",
                "irregular_forms": {
                    "past": "broke",
                    "pp": "broken"
                }
            },
            {
                "id": "g6a1-3",
                "word": "ICT",
                "phonetic": "",
                "meaning": "(= information and communications technology) 信息通信技术（课程）",
                "pos": "n.",
                "unit": "Unit 1"
            },
            {
                "id": "g6a1-4",
                "word": "geography",
                "phonetic": "/dʒiˈɒɡrəfi/",
                "meaning": "地理",
                "pos": "n.",
                "unit": "Unit 1"
            },
            {
                "id": "g6a1-5",
                "word": "history",
                "phonetic": "/ˈhɪstri/",
                "meaning": "历史",
                "pos": "n.",
                "unit": "Unit 1"
            },
            {
                "id": "g6a1-6",
                "word": "more",
                "phonetic": "/mɔː(r)/",
                "meaning": "更多的",
                "pos": "det. & pron.",
                "unit": "Unit 1"
            },
            {
                "id": "g6a1-7",
                "word": "instruction",
                "phonetic": "/ɪnˈstrʌkʃn/",
                "meaning": "指示；命令",
                "pos": "n.",
                "unit": "Unit 1"
            },
            {
                "id": "g6a1-8",
                "word": "experiment",
                "phonetic": "/ɪkˈsperɪmənt/",
                "meaning": "实验；试验",
                "pos": "n.",
                "unit": "Unit 1"
            },
            {
                "id": "g6a1-9",
                "word": "activity",
                "phonetic": "/ækˈtɪvəti/",
                "meaning": "活动",
                "pos": "n.",
                "unit": "Unit 1"
            },
            {
                "id": "g6a1-10",
                "word": "club",
                "phonetic": "/klʌb/",
                "meaning": "社团",
                "pos": "n.",
                "unit": "Unit 1"
            },
            {
                "id": "g6a1-11",
                "word": "calligraphy",
                "phonetic": "/kəˈlɪɡrəfi/",
                "meaning": "书法",
                "pos": "n.",
                "unit": "Unit 1"
            },
            {
                "id": "g6a1-12",
                "word": "join",
                "phonetic": "/dʒɔɪn/",
                "meaning": "加入",
                "pos": "v.",
                "unit": "Unit 1"
            },
            {
                "id": "g6a1-13",
                "word": "technology",
                "phonetic": "/tekˈnɒlədʒi/",
                "meaning": "科技",
                "pos": "n.",
                "unit": "Unit 1"
            },
            {
                "id": "g6a1-14",
                "word": "everyone",
                "phonetic": "/ˈevriwʌn/",
                "meaning": "(= everybody) 每个人",
                "pos": "pron.",
                "unit": "Unit 1"
            },
            {
                "id": "g6a1-15",
                "word": "lab",
                "phonetic": "/læb/",
                "meaning": "(= laboratory) 实验室",
                "pos": "n.",
                "unit": "Unit 1"
            },
            {
                "id": "g6a1-16",
                "word": "field",
                "phonetic": "/fiːld/",
                "meaning": "场地",
                "pos": "n.",
                "unit": "Unit 1"
            },
            {
                "id": "g6a1-17",
                "word": "grade",
                "phonetic": "/ɡreɪd/",
                "meaning": "年级",
                "pos": "n.",
                "unit": "Unit 1"
            },
            {
                "id": "g6a1-18",
                "word": "excuse",
                "phonetic": "/ɪkˈskjuːz/",
                "meaning": "原谅；宽恕",
                "pos": "v.",
                "unit": "Unit 1"
            },
            {
                "id": "g6a1-19",
                "word": "excuse me",
                "phonetic": "",
                "meaning": "（因打扰别人或失礼表示歉意）对不起；劳驾",
                "pos": "phr.",
                "unit": "Unit 1"
            },
            {
                "id": "g6a1-20",
                "word": "of course",
                "phonetic": "",
                "meaning": "当然",
                "pos": "phr.",
                "unit": "Unit 1"
            },
            {
                "id": "g6a1-21",
                "word": "project",
                "phonetic": "/ˈprɒdʒekt/",
                "meaning": "项目",
                "pos": "n.",
                "unit": "Unit 1"
            },
            {
                "id": "g6a1-22",
                "word": "start",
                "phonetic": "/stɑːt/",
                "meaning": "开始（做某事）",
                "pos": "v.",
                "unit": "Unit 1"
            },
            {
                "id": "g6a1-23",
                "word": "topic",
                "phonetic": "/ˈtɒpɪk/",
                "meaning": "话题；主题",
                "pos": "n.",
                "unit": "Unit 1"
            },
            {
                "id": "g6a1-24",
                "word": "online",
                "phonetic": "/ˌɒnˈlaɪn/",
                "meaning": "adv. 在线 / adj. 在线的；联网的",
                "pos": "adv. & adj.",
                "unit": "Unit 1"
            },
            {
                "id": "g6a1-25",
                "word": "receive",
                "phonetic": "/rɪˈsiːv/",
                "meaning": "接到；收到",
                "pos": "v.",
                "unit": "Unit 1"
            },
            {
                "id": "g6a1-26",
                "word": "reply",
                "phonetic": "/rɪˈplaɪ/",
                "meaning": "回答；答复",
                "pos": "n.",
                "unit": "Unit 1"
            },
            {
                "id": "g6a1-27",
                "word": "group",
                "phonetic": "/ɡruːp/",
                "meaning": "组；群；批；类",
                "pos": "n.",
                "unit": "Unit 1"
            },
            {
                "id": "g6a1-28",
                "word": "most",
                "phonetic": "/məʊst/",
                "meaning": "最",
                "pos": "adv.",
                "unit": "Unit 1"
            },
            {
                "id": "g6a1-29",
                "word": "a.m.",
                "phonetic": "",
                "meaning": "(AmE A.M.) 上午",
                "pos": "abbr.",
                "unit": "Unit 1"
            },
            {
                "id": "g6a1-30",
                "word": "end",
                "phonetic": "/end/",
                "meaning": "结束",
                "pos": "v.",
                "unit": "Unit 1"
            },
            {
                "id": "g6a1-31",
                "word": "p.m.",
                "phonetic": "",
                "meaning": "(AmE P.M.) 下午",
                "pos": "abbr.",
                "unit": "Unit 1"
            },
            {
                "id": "g6a1-32",
                "word": "difference",
                "phonetic": "/ˈdɪfrəns/",
                "meaning": "差别；不同之处",
                "pos": "n.",
                "unit": "Unit 1"
            },
            {
                "id": "g6a1-33",
                "word": "same",
                "phonetic": "/seɪm/",
                "meaning": "一样的",
                "pos": "adj.",
                "unit": "Unit 1"
            },
            {
                "id": "g6a1-34",
                "word": "during",
                "phonetic": "/ˈdjʊərɪŋ/",
                "meaning": "在……期间",
                "pos": "prep.",
                "unit": "Unit 1"
            },
            {
                "id": "g6a1-35",
                "word": "outside",
                "phonetic": "/ˌaʊtˈsaɪd/",
                "meaning": "adv. 在外面 / prep. 在……外面",
                "pos": "adv. & prep.",
                "unit": "Unit 1"
            },
            {
                "id": "g6a1-36",
                "word": "noon",
                "phonetic": "/nuːn/",
                "meaning": "正午；中午",
                "pos": "n.",
                "unit": "Unit 1"
            },
            {
                "id": "g6a1-37",
                "word": "connect",
                "phonetic": "/kəˈnekt/",
                "meaning": "连接",
                "pos": "v.",
                "unit": "Unit 1"
            },
            {
                "id": "g6a1-38",
                "word": "comment",
                "phonetic": "/ˈkɒment/",
                "meaning": "n. 议论；评论；解释 / v. 表达意见",
                "pos": "n. & v.",
                "unit": "Unit 1"
            }
        ]
    },
    {
        "id": "sys-6a-u2",
        "name": "六年级上册 Unit 2",
        "grade": "小学",
        "description": "上海版六年级上册 Unit 2 英语词汇（上海教育出版社·五四学制）",
        "created_at": "2024-01-01",
        "words": [
            {
                "id": "g6a2-1",
                "word": "tie",
                "phonetic": "/taɪ/",
                "meaning": "联系；关系；纽带",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g6a2-2",
                "word": "relation",
                "phonetic": "/rɪˈleɪʃn/",
                "meaning": "关系；联系",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g6a2-3",
                "word": "introduce",
                "phonetic": "/ˌɪntrəˈdjuːs/",
                "meaning": "介绍",
                "pos": "v.",
                "unit": "Unit 2"
            },
            {
                "id": "g6a2-4",
                "word": "classmate",
                "phonetic": "/ˈklɑːsmeɪt/",
                "meaning": "同班同学",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g6a2-5",
                "word": "relative",
                "phonetic": "/ˈrelətɪv/",
                "meaning": "亲戚；亲属",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g6a2-6",
                "word": "only",
                "phonetic": "/ˈəʊnli/",
                "meaning": "仅有的；唯一的",
                "pos": "adj.",
                "unit": "Unit 2"
            },
            {
                "id": "g6a2-7",
                "word": "only child",
                "phonetic": "",
                "meaning": "独生子（或女）",
                "pos": "phr.",
                "unit": "Unit 2"
            },
            {
                "id": "g6a2-8",
                "word": "twin",
                "phonetic": "/twɪn/",
                "meaning": "双胞胎之一",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g6a2-9",
                "word": "husband",
                "phonetic": "/ˈhʌzbənd/",
                "meaning": "丈夫",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g6a2-10",
                "word": "wife",
                "phonetic": "/waɪf/",
                "meaning": "(pl. wives) 妻子",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g6a2-11",
                "word": "son",
                "phonetic": "/sʌn/",
                "meaning": "儿子",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g6a2-12",
                "word": "daughter",
                "phonetic": "/ˈdɔːtə(r)/",
                "meaning": "女儿",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g6a2-13",
                "word": "other",
                "phonetic": "/ˈʌðə(r)/",
                "meaning": "adj. 另外；其他 / pron. 另外的人（或物）",
                "pos": "adj. & pron.",
                "unit": "Unit 2"
            },
            {
                "id": "g6a2-14",
                "word": "member",
                "phonetic": "/ˈmembə(r)/",
                "meaning": "成员；分子",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g6a2-15",
                "word": "add",
                "phonetic": "/æd/",
                "meaning": "添加；增加",
                "pos": "v.",
                "unit": "Unit 2"
            },
            {
                "id": "g6a2-16",
                "word": "note",
                "phonetic": "/nəʊt/",
                "meaning": "笔记；记录；音符",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g6a2-17",
                "word": "album",
                "phonetic": "/ˈælbəm/",
                "meaning": "相册；影集",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g6a2-18",
                "word": "teach",
                "phonetic": "/tiːtʃ/",
                "meaning": "教（某人）；使（某人）明白或会做某事",
                "pos": "v.",
                "unit": "Unit 2",
                "irregular_forms": {
                    "past": "taught",
                    "pp": "taught"
                }
            },
            {
                "id": "g6a2-19",
                "word": "homework",
                "phonetic": "/ˈhəʊmwɜːk/",
                "meaning": "（学生的）家庭作业",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g6a2-20",
                "word": "guitar",
                "phonetic": "/ɡɪˈtɑː(r)/",
                "meaning": "吉他",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g6a2-21",
                "word": "elder",
                "phonetic": "/ˈeldə(r)/",
                "meaning": "年长的；年龄较大的",
                "pos": "adj.",
                "unit": "Unit 2"
            },
            {
                "id": "g6a2-22",
                "word": "sofa",
                "phonetic": "/ˈsəʊfə/",
                "meaning": "长沙发",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g6a2-23",
                "word": "round",
                "phonetic": "/raʊnd/",
                "meaning": "圆形的",
                "pos": "adj.",
                "unit": "Unit 2"
            },
            {
                "id": "g6a2-24",
                "word": "dark",
                "phonetic": "/dɑːk/",
                "meaning": "乌黑的；深色的；黑暗的",
                "pos": "adj.",
                "unit": "Unit 2"
            },
            {
                "id": "g6a2-25",
                "word": "chess",
                "phonetic": "/tʃes/",
                "meaning": "国际象棋",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g6a2-26",
                "word": "duty",
                "phonetic": "/ˈdjuːti/",
                "meaning": "责任；义务；本分",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g6a2-27",
                "word": "born",
                "phonetic": "/bɔːn/",
                "meaning": "（仅用于被动语态 be born）出生；出世",
                "pos": "v.",
                "unit": "Unit 2"
            },
            {
                "id": "g6a2-28",
                "word": "weekend",
                "phonetic": "/ˌwiːkˈend/",
                "meaning": "星期六和星期日；周末",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g6a2-29",
                "word": "thing",
                "phonetic": "/θɪŋ/",
                "meaning": "事情；事件",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g6a2-30",
                "word": "enough",
                "phonetic": "/ɪˈnʌf/",
                "meaning": "足够地；充分地",
                "pos": "adv.",
                "unit": "Unit 2"
            },
            {
                "id": "g6a2-31",
                "word": "Well done!",
                "phonetic": "",
                "meaning": "做得好！干得好！",
                "pos": "phr.",
                "unit": "Unit 2"
            },
            {
                "id": "g6a2-32",
                "word": "dish",
                "phonetic": "/dɪʃ/",
                "meaning": "碟子；盘子；一道菜；菜肴",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g6a2-33",
                "word": "usually",
                "phonetic": "/ˈjuːʒuəli/",
                "meaning": "通常地；经常地",
                "pos": "adv.",
                "unit": "Unit 2"
            },
            {
                "id": "g6a2-34",
                "word": "quick",
                "phonetic": "/kwɪk/",
                "meaning": "快的；迅速的",
                "pos": "adj.",
                "unit": "Unit 2"
            },
            {
                "id": "g6a2-35",
                "word": "together",
                "phonetic": "/təˈɡeðə(r)/",
                "meaning": "在一起；共同",
                "pos": "adv.",
                "unit": "Unit 2"
            },
            {
                "id": "g6a2-36",
                "word": "flat",
                "phonetic": "/flæt/",
                "meaning": "公寓；一套房间",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g6a2-37",
                "word": "fun",
                "phonetic": "/fʌn/",
                "meaning": "乐趣；快乐",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g6a2-38",
                "word": "celebration",
                "phonetic": "/ˌselɪˈbreɪʃn/",
                "meaning": "庆典；庆祝活动",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g6a2-39",
                "word": "prepare",
                "phonetic": "/prɪˈpeə(r)/",
                "meaning": "使做好准备；把……预备好",
                "pos": "v.",
                "unit": "Unit 2"
            },
            {
                "id": "g6a2-40",
                "word": "decorate",
                "phonetic": "/ˈdekəreɪt/",
                "meaning": "装饰",
                "pos": "v.",
                "unit": "Unit 2"
            },
            {
                "id": "g6a2-41",
                "word": "living room",
                "phonetic": "/ˈlɪvɪŋ ruːm/",
                "meaning": "(= sitting room) 客厅；起居室",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g6a2-42",
                "word": "balloon",
                "phonetic": "/bəˈluːn/",
                "meaning": "气球",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g6a2-43",
                "word": "set",
                "phonetic": "/set/",
                "meaning": "放置；摆放",
                "pos": "v.",
                "unit": "Unit 2",
                "irregular_forms": {
                    "past": "set",
                    "pp": "set"
                }
            },
            {
                "id": "g6a2-44",
                "word": "surprised",
                "phonetic": "/səˈpraɪzd/",
                "meaning": "惊奇的；惊讶的；感觉意外的",
                "pos": "adj.",
                "unit": "Unit 2"
            },
            {
                "id": "g6a2-45",
                "word": "super-excited",
                "phonetic": "/ˌsuːpə(r) ɪkˈsaɪtɪd/",
                "meaning": "超级激动的；格外兴奋的",
                "pos": "adj.",
                "unit": "Unit 2"
            },
            {
                "id": "g6a2-46",
                "word": "joy",
                "phonetic": "/dʒɔɪ/",
                "meaning": "高兴；愉快；喜悦",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g6a2-47",
                "word": "jump for joy",
                "phonetic": "",
                "meaning": "欢呼雀跃",
                "pos": "phr.",
                "unit": "Unit 2"
            }
        ]
    },
    {
        "id": "sys-6a-u3",
        "name": "六年级上册 Unit 3",
        "grade": "小学",
        "description": "上海版六年级上册 Unit 3 英语词汇（上海教育出版社·五四学制）",
        "created_at": "2024-01-01",
        "words": [
            {
                "id": "g6a3-1",
                "word": "something",
                "phonetic": "/ˈsʌmθɪŋ/",
                "meaning": "某事；某物",
                "pos": "pron.",
                "unit": "Unit 3"
            },
            {
                "id": "g6a3-2",
                "word": "beef",
                "phonetic": "/biːf/",
                "meaning": "牛肉",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g6a3-3",
                "word": "tofu",
                "phonetic": "/ˈtəʊfuː/",
                "meaning": "豆腐",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g6a3-4",
                "word": "pepper",
                "phonetic": "/ˈpepə(r)/",
                "meaning": "甜椒",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g6a3-5",
                "word": "cabbage",
                "phonetic": "/ˈkæbɪdʒ/",
                "meaning": "卷心菜",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g6a3-6",
                "word": "onion",
                "phonetic": "/ˈʌnjən/",
                "meaning": "洋葱",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g6a3-7",
                "word": "carrot",
                "phonetic": "/ˈkærət/",
                "meaning": "胡萝卜",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g6a3-8",
                "word": "watermelon",
                "phonetic": "/ˈwɔːtəmelən/",
                "meaning": "西瓜",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g6a3-9",
                "word": "cucumber",
                "phonetic": "/ˈkjuːkʌmbə(r)/",
                "meaning": "黄瓜",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g6a3-10",
                "word": "strawberry",
                "phonetic": "/ˈstrɔːbəri/",
                "meaning": "草莓",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g6a3-11",
                "word": "pear",
                "phonetic": "/peə(r)/",
                "meaning": "梨",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g6a3-12",
                "word": "yogurt",
                "phonetic": "/ˈjɒɡət/",
                "meaning": "酸奶；一份酸奶",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g6a3-13",
                "word": "cheese",
                "phonetic": "/tʃiːz/",
                "meaning": "干酪；奶酪",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g6a3-14",
                "word": "corn",
                "phonetic": "/kɔːn/",
                "meaning": "（小麦等）谷物；玉米",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g6a3-15",
                "word": "butter",
                "phonetic": "/ˈbʌtə(r)/",
                "meaning": "黄油",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g6a3-16",
                "word": "oil",
                "phonetic": "/ɔɪl/",
                "meaning": "食用油",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g6a3-17",
                "word": "salt",
                "phonetic": "/sɔːlt/",
                "meaning": "盐；食盐",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g6a3-18",
                "word": "bean",
                "phonetic": "/biːn/",
                "meaning": "豆；豆科植物",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g6a3-19",
                "word": "product",
                "phonetic": "/ˈprɒdʌkt/",
                "meaning": "产品；制品",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g6a3-20",
                "word": "grain",
                "phonetic": "/ɡreɪn/",
                "meaning": "谷物；谷粒",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g6a3-21",
                "word": "rainbow",
                "phonetic": "/ˈreɪnbəʊ/",
                "meaning": "虹；彩虹",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g6a3-22",
                "word": "balanced",
                "phonetic": "/ˈbælənst/",
                "meaning": "保持（或显示）平衡的",
                "pos": "adj.",
                "unit": "Unit 3"
            },
            {
                "id": "g6a3-23",
                "word": "diet",
                "phonetic": "/ˈdaɪət/",
                "meaning": "日常饮食；日常食物",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g6a3-24",
                "word": "each",
                "phonetic": "/iːtʃ/",
                "meaning": "（两个或以上的人或物中）各自，各个，每个",
                "pos": "det. & pron.",
                "unit": "Unit 3"
            },
            {
                "id": "g6a3-25",
                "word": "plenty",
                "phonetic": "/ˈplenti/",
                "meaning": "大量",
                "pos": "pron.",
                "unit": "Unit 3"
            },
            {
                "id": "g6a3-26",
                "word": "plenty of",
                "phonetic": "",
                "meaning": "大量；很多的",
                "pos": "phr.",
                "unit": "Unit 3"
            },
            {
                "id": "g6a3-27",
                "word": "choice",
                "phonetic": "/tʃɔɪs/",
                "meaning": "选择；挑选；抉择",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g6a3-28",
                "word": "list",
                "phonetic": "/lɪst/",
                "meaning": "一览表；清单",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g6a3-29",
                "word": "few",
                "phonetic": "/fjuː/",
                "meaning": "不多；很少",
                "pos": "det. & adj.",
                "unit": "Unit 3"
            },
            {
                "id": "g6a3-30",
                "word": "a few",
                "phonetic": "",
                "meaning": "有些；几个（用于可数名词之前）",
                "pos": "phr.",
                "unit": "Unit 3"
            },
            {
                "id": "g6a3-31",
                "word": "pleasure",
                "phonetic": "/ˈpleʒə(r)/",
                "meaning": "高兴；快乐；愉快",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g6a3-32",
                "word": "ingredient",
                "phonetic": "/ɪnˈɡriːdiənt/",
                "meaning": "（尤指烹饪）材料；成分",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g6a3-33",
                "word": "tasty",
                "phonetic": "/ˈteɪsti/",
                "meaning": "美味的；可口的",
                "pos": "adj.",
                "unit": "Unit 3"
            },
            {
                "id": "g6a3-34",
                "word": "need",
                "phonetic": "/niːd/",
                "meaning": "需要",
                "pos": "v.",
                "unit": "Unit 3"
            },
            {
                "id": "g6a3-35",
                "word": "fridge",
                "phonetic": "/frɪdʒ/",
                "meaning": "(= refrigerator) 冰箱",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g6a3-36",
                "word": "surprise",
                "phonetic": "/səˈpraɪz/",
                "meaning": "n. 意想不到（或突然）的事 / v. 使惊奇；使诧异；使感到意外",
                "pos": "n. & v.",
                "unit": "Unit 3"
            },
            {
                "id": "g6a3-37",
                "word": "blog",
                "phonetic": "/blɒɡ/",
                "meaning": "(= weblog) 博客；网志",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g6a3-38",
                "word": "as",
                "phonetic": "/æz; əz/",
                "meaning": "作为；当作",
                "pos": "prep.",
                "unit": "Unit 3"
            },
            {
                "id": "g6a3-39",
                "word": "soy sauce",
                "phonetic": "/ˌsɔɪ ˈsɔːs/",
                "meaning": "(= soya sauce) 酱油",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g6a3-40",
                "word": "into",
                "phonetic": "/ˈɪntuː; ˈɪntə/",
                "meaning": "（表示状态的变化）；进入",
                "pos": "prep.",
                "unit": "Unit 3"
            },
            {
                "id": "g6a3-41",
                "word": "piece",
                "phonetic": "/piːs/",
                "meaning": "碎片；碎块",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g6a3-42",
                "word": "fry",
                "phonetic": "/fraɪ/",
                "meaning": "油炒；油煎",
                "pos": "v.",
                "unit": "Unit 3"
            },
            {
                "id": "g6a3-43",
                "word": "finally",
                "phonetic": "/ˈfaɪnəli/",
                "meaning": "最后",
                "pos": "adv.",
                "unit": "Unit 3"
            },
            {
                "id": "g6a3-44",
                "word": "boil",
                "phonetic": "/bɔɪl/",
                "meaning": "煮沸；烧开",
                "pos": "v.",
                "unit": "Unit 3"
            },
            {
                "id": "g6a3-45",
                "word": "side",
                "phonetic": "/saɪd/",
                "meaning": "一边；侧面",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g6a3-46",
                "word": "side dish",
                "phonetic": "",
                "meaning": "（随同主菜一起上的）配菜",
                "pos": "phr.",
                "unit": "Unit 3"
            },
            {
                "id": "g6a3-47",
                "word": "mutton",
                "phonetic": "/ˈmʌtn/",
                "meaning": "羊肉",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g6a3-48",
                "word": "recipe",
                "phonetic": "/ˈresəpi/",
                "meaning": "食谱；烹饪法",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g6a3-49",
                "word": "beat",
                "phonetic": "/biːt/",
                "meaning": "（用叉等）快速搅拌；打",
                "pos": "v.",
                "unit": "Unit 3",
                "irregular_forms": {
                    "past": "beat",
                    "pp": "beaten"
                }
            },
            {
                "id": "g6a3-50",
                "word": "chopsticks",
                "phonetic": "/ˈtʃɒpstɪks/",
                "meaning": "(pl.) 筷子",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g6a3-51",
                "word": "bowl",
                "phonetic": "/bəʊl/",
                "meaning": "碗",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g6a3-52",
                "word": "menu",
                "phonetic": "/ˈmenjuː/",
                "meaning": "菜单",
                "pos": "n.",
                "unit": "Unit 3"
            }
        ]
    },
    {
        "id": "sys-6a-u4",
        "name": "六年级上册 Unit 4",
        "grade": "小学",
        "description": "上海版六年级上册 Unit 4 英语词汇（上海教育出版社·五四学制）",
        "created_at": "2024-01-01",
        "words": [
            {
                "id": "g6a4-1",
                "word": "date",
                "phonetic": "/deɪt/",
                "meaning": "日期；日子",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g6a4-2",
                "word": "ground",
                "phonetic": "/ɡraʊnd/",
                "meaning": "（特定用途的）场地；地面",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g6a4-3",
                "word": "sports ground",
                "phonetic": "",
                "meaning": "运动场；操场",
                "pos": "phr.",
                "unit": "Unit 4"
            },
            {
                "id": "g6a4-4",
                "word": "gym",
                "phonetic": "/dʒɪm/",
                "meaning": "(= gymnasium) 健身房；体育馆",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g6a4-5",
                "word": "team",
                "phonetic": "/tiːm/",
                "meaning": "（游戏或运动的）队",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g6a4-6",
                "word": "high",
                "phonetic": "/haɪ/",
                "meaning": "高的",
                "pos": "adj.",
                "unit": "Unit 4"
            },
            {
                "id": "g6a4-7",
                "word": "rope",
                "phonetic": "/rəʊp/",
                "meaning": "绳",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g6a4-8",
                "word": "kick",
                "phonetic": "/kɪk/",
                "meaning": "踢",
                "pos": "v.",
                "unit": "Unit 4"
            },
            {
                "id": "g6a4-9",
                "word": "rock",
                "phonetic": "/rɒk/",
                "meaning": "岩石",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g6a4-10",
                "word": "climb",
                "phonetic": "/klaɪm/",
                "meaning": "攀登；爬",
                "pos": "v.",
                "unit": "Unit 4"
            },
            {
                "id": "g6a4-11",
                "word": "rock climbing",
                "phonetic": "",
                "meaning": "攀岩",
                "pos": "phr.",
                "unit": "Unit 4"
            },
            {
                "id": "g6a4-12",
                "word": "kung fu",
                "phonetic": "/ˌkʌŋ ˈfuː/",
                "meaning": "功夫（中国拳术）",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g6a4-13",
                "word": "active",
                "phonetic": "/ˈæktɪv/",
                "meaning": "活跃的；充满活力的；积极的",
                "pos": "adj.",
                "unit": "Unit 4"
            },
            {
                "id": "g6a4-14",
                "word": "part",
                "phonetic": "/pɑːt/",
                "meaning": "部分",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g6a4-15",
                "word": "take part in",
                "phonetic": "",
                "meaning": "参加",
                "pos": "phr.",
                "unit": "Unit 4"
            },
            {
                "id": "g6a4-16",
                "word": "baseball",
                "phonetic": "/ˈbeɪsbɔːl/",
                "meaning": "棒球运动",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g6a4-17",
                "word": "volleyball",
                "phonetic": "/ˈvɒlibɔːl/",
                "meaning": "排球；排球运动",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g6a4-18",
                "word": "badminton",
                "phonetic": "/ˈbædmɪntən/",
                "meaning": "羽毛球运动",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g6a4-19",
                "word": "tennis",
                "phonetic": "/ˈtenɪs/",
                "meaning": "网球",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g6a4-20",
                "word": "pull",
                "phonetic": "/pʊl/",
                "meaning": "拉；拔出",
                "pos": "v.",
                "unit": "Unit 4"
            },
            {
                "id": "g6a4-21",
                "word": "jog",
                "phonetic": "/dʒɒɡ/",
                "meaning": "慢跑",
                "pos": "v.",
                "unit": "Unit 4"
            },
            {
                "id": "g6a4-22",
                "word": "safety",
                "phonetic": "/ˈseɪfti/",
                "meaning": "安全；平安",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g6a4-23",
                "word": "ankle",
                "phonetic": "/ˈæŋkl/",
                "meaning": "踝；踝关节",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g6a4-24",
                "word": "match",
                "phonetic": "/mætʃ/",
                "meaning": "比赛",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g6a4-25",
                "word": "gear",
                "phonetic": "/ɡɪə(r)/",
                "meaning": "(某种活动的）设备，用具，衣服",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g6a4-26",
                "word": "example",
                "phonetic": "/ɪɡˈzɑːmpl/",
                "meaning": "例子；实例",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g6a4-27",
                "word": "for example",
                "phonetic": "",
                "meaning": "例如",
                "pos": "phr.",
                "unit": "Unit 4"
            },
            {
                "id": "g6a4-28",
                "word": "warm up",
                "phonetic": "",
                "meaning": "（为体育活动或表演）做适应性练习，做准备活动；热身",
                "pos": "phr.",
                "unit": "Unit 4"
            },
            {
                "id": "g6a4-29",
                "word": "watch out",
                "phonetic": "",
                "meaning": "小心；留神；注意",
                "pos": "phr.",
                "unit": "Unit 4"
            },
            {
                "id": "g6a4-30",
                "word": "matter",
                "phonetic": "/ˈmætə(r)/",
                "meaning": "问题；事情",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g6a4-31",
                "word": "What’s the matter?",
                "phonetic": "",
                "meaning": "怎么了？",
                "pos": "phr.",
                "unit": "Unit 4"
            },
            {
                "id": "g6a4-32",
                "word": "happen",
                "phonetic": "/ˈhæpən/",
                "meaning": "发生",
                "pos": "v.",
                "unit": "Unit 4"
            },
            {
                "id": "g6a4-33",
                "word": "just",
                "phonetic": "/dʒʌst/",
                "meaning": "仅仅是；只是",
                "pos": "adv.",
                "unit": "Unit 4"
            },
            {
                "id": "g6a4-34",
                "word": "fall",
                "phonetic": "/fɔːl/",
                "meaning": "突然倒下；跌倒",
                "pos": "v.",
                "unit": "Unit 4",
                "irregular_forms": {
                    "past": "fell",
                    "pp": "fallen"
                }
            },
            {
                "id": "g6a4-35",
                "word": "guess",
                "phonetic": "/ɡes/",
                "meaning": "猜测；估计",
                "pos": "v.",
                "unit": "Unit 4"
            },
            {
                "id": "g6a4-36",
                "word": "knee",
                "phonetic": "/niː/",
                "meaning": "膝盖",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g6a4-37",
                "word": "How come?",
                "phonetic": "",
                "meaning": "怎么回事？怎么发生的？",
                "pos": "phr.",
                "unit": "Unit 4"
            },
            {
                "id": "g6a4-38",
                "word": "seem",
                "phonetic": "/siːm/",
                "meaning": "好像；似乎；看来",
                "pos": "v.",
                "unit": "Unit 4"
            },
            {
                "id": "g6a4-39",
                "word": "problem",
                "phonetic": "/ˈprɒbləm/",
                "meaning": "棘手的问题；难题；困难",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g6a4-40",
                "word": "score",
                "phonetic": "/skɔː(r)/",
                "meaning": "得（分）；进（球）",
                "pos": "v.",
                "unit": "Unit 4"
            },
            {
                "id": "g6a4-41",
                "word": "goal",
                "phonetic": "/ɡəʊl/",
                "meaning": "进球得的分；球门；目标",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g6a4-42",
                "word": "goalkeeper",
                "phonetic": "/ˈɡəʊlkiːpə(r)/",
                "meaning": "守门员",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g6a4-43",
                "word": "hold",
                "phonetic": "/həʊld/",
                "meaning": "使……保持在某位置；拿着；抓住",
                "pos": "v.",
                "unit": "Unit 4",
                "irregular_forms": {
                    "past": "held",
                    "pp": "held"
                }
            },
            {
                "id": "g6a4-44",
                "word": "throw",
                "phonetic": "/θrəʊ/",
                "meaning": "投；抛；掷",
                "pos": "v.",
                "unit": "Unit 4",
                "irregular_forms": {
                    "past": "threw",
                    "pp": "thrown"
                }
            },
            {
                "id": "g6a4-45",
                "word": "point",
                "phonetic": "/pɔɪnt/",
                "meaning": "得分；点",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g6a4-46",
                "word": "control",
                "phonetic": "/kənˈtrəʊl/",
                "meaning": "控制；管理",
                "pos": "v. & n.",
                "unit": "Unit 4"
            },
            {
                "id": "g6a4-47",
                "word": "mind",
                "phonetic": "/maɪnd/",
                "meaning": "n. 头脑；心智 / v. 当心；注意",
                "pos": "n. & v.",
                "unit": "Unit 4"
            },
            {
                "id": "g6a4-48",
                "word": "powerful",
                "phonetic": "/ˈpaʊəfl/",
                "meaning": "强有力的",
                "pos": "adj.",
                "unit": "Unit 4"
            },
            {
                "id": "g6a4-49",
                "word": "style",
                "phonetic": "/staɪl/",
                "meaning": "风格；样式",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g6a4-50",
                "word": "moment",
                "phonetic": "/ˈməʊmənt/",
                "meaning": "片刻；瞬间",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g6a4-51",
                "word": "report",
                "phonetic": "/rɪˈpɔːt/",
                "meaning": "汇报；报告；报道",
                "pos": "v. & n.",
                "unit": "Unit 4"
            },
            {
                "id": "g6a4-52",
                "word": "newspaper",
                "phonetic": "/ˈnjuːzpeɪpə(r)/",
                "meaning": "报纸",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g6a4-53",
                "word": "court",
                "phonetic": "/kɔːt/",
                "meaning": "球场",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g6a4-54",
                "word": "against",
                "phonetic": "/əˈɡenst/",
                "meaning": "与……对阵；与……相反；反对",
                "pos": "prep.",
                "unit": "Unit 4"
            },
            {
                "id": "g6a4-55",
                "word": "shoot",
                "phonetic": "/ʃuːt/",
                "meaning": "射门；投篮",
                "pos": "v.",
                "unit": "Unit 4",
                "irregular_forms": {
                    "past": "shot",
                    "pp": "shot"
                }
            },
            {
                "id": "g6a4-56",
                "word": "basket",
                "phonetic": "/ˈbɑːskɪt/",
                "meaning": "（篮球运动的）篮；筐",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g6a4-57",
                "word": "tie",
                "phonetic": "/taɪ/",
                "meaning": "(比赛或竞争中）得分相同",
                "pos": "v.",
                "unit": "Unit 4"
            },
            {
                "id": "g6a4-58",
                "word": "track",
                "phonetic": "/træk/",
                "meaning": "（赛跑、赛车等的）跑道",
                "pos": "n.",
                "unit": "Unit 4"
            }
        ]
    },
    {
        "id": "sys-6a-u5",
        "name": "六年级上册 Unit 5",
        "grade": "小学",
        "description": "上海版六年级上册 Unit 5 英语词汇（上海教育出版社·五四学制）",
        "created_at": "2024-01-01",
        "words": [
            {
                "id": "g6a5-1",
                "word": "amazing",
                "phonetic": "/əˈmeɪzɪŋ/",
                "meaning": "令人大为惊奇的；令人惊喜或惊叹的",
                "pos": "adj.",
                "unit": "Unit 5"
            },
            {
                "id": "g6a5-2",
                "word": "website",
                "phonetic": "/ˈwebsaɪt/",
                "meaning": "网站",
                "pos": "n.",
                "unit": "Unit 5"
            },
            {
                "id": "g6a5-3",
                "word": "feed",
                "phonetic": "/fiːd/",
                "meaning": "给（人或动物）食物；喂养",
                "pos": "v.",
                "unit": "Unit 5",
                "irregular_forms": {
                    "past": "fed",
                    "pp": "fed"
                }
            },
            {
                "id": "g6a5-4",
                "word": "herd",
                "phonetic": "/hɜːd/",
                "meaning": "牧放（牲畜、兽群）",
                "pos": "v.",
                "unit": "Unit 5"
            },
            {
                "id": "g6a5-5",
                "word": "goat",
                "phonetic": "/ɡəʊt/",
                "meaning": "山羊",
                "pos": "n.",
                "unit": "Unit 5"
            },
            {
                "id": "g6a5-6",
                "word": "remember",
                "phonetic": "/rɪˈmembə(r)/",
                "meaning": "记得；记起",
                "pos": "v.",
                "unit": "Unit 5"
            },
            {
                "id": "g6a5-7",
                "word": "collect",
                "phonetic": "/kəˈlekt/",
                "meaning": "收集；采集",
                "pos": "v.",
                "unit": "Unit 5"
            },
            {
                "id": "g6a5-8",
                "word": "recognise (AmE recognize)",
                "phonetic": "/ˈrekəɡnaɪz/",
                "meaning": "识别；认出",
                "pos": "v.",
                "unit": "Unit 5"
            },
            {
                "id": "g6a5-9",
                "word": "care",
                "phonetic": "/keə(r)/",
                "meaning": "照顾；照看",
                "pos": "n.",
                "unit": "Unit 5"
            },
            {
                "id": "g6a5-10",
                "word": "take care of",
                "phonetic": "",
                "meaning": "照顾；照料",
                "pos": "phr.",
                "unit": "Unit 5"
            },
            {
                "id": "g6a5-11",
                "word": "prefer",
                "phonetic": "/prɪˈfɜː(r)/",
                "meaning": "较喜欢；喜欢……多于……",
                "pos": "v.",
                "unit": "Unit 5"
            },
            {
                "id": "g6a5-12",
                "word": "get along with",
                "phonetic": "",
                "meaning": "和睦相处；关系良好",
                "pos": "phr.",
                "unit": "Unit 5"
            },
            {
                "id": "g6a5-13",
                "word": "sign",
                "phonetic": "/saɪn/",
                "meaning": "标牌；指示牌",
                "pos": "n.",
                "unit": "Unit 5"
            },
            {
                "id": "g6a5-14",
                "word": "bite",
                "phonetic": "/baɪt/",
                "meaning": "v. 咬 / n. 咬；咬下的一口",
                "pos": "v. & n.",
                "unit": "Unit 5"
            },
            {
                "id": "g6a5-15",
                "word": "warning",
                "phonetic": "/ˈwɔːnɪŋ/",
                "meaning": "警告；警示",
                "pos": "n.",
                "unit": "Unit 5"
            },
            {
                "id": "g6a5-16",
                "word": "peck",
                "phonetic": "/pek/",
                "meaning": "啄",
                "pos": "v.",
                "unit": "Unit 5"
            },
            {
                "id": "g6a5-17",
                "word": "sweet",
                "phonetic": "/swiːt/",
                "meaning": "adj. 含糖的；甜的 / n. 糖果",
                "pos": "adj. & n.",
                "unit": "Unit 5"
            },
            {
                "id": "g6a5-18",
                "word": "calf",
                "phonetic": "/kɑːf/",
                "meaning": "小牛；牛犊",
                "pos": "n.",
                "unit": "Unit 5"
            },
            {
                "id": "g6a5-19",
                "word": "loud",
                "phonetic": "/laʊd/",
                "meaning": "大声的；喧闹的",
                "pos": "adj.",
                "unit": "Unit 5"
            },
            {
                "id": "g6a5-20",
                "word": "noise",
                "phonetic": "/nɔɪz/",
                "meaning": "噪音；响声",
                "pos": "n.",
                "unit": "Unit 5"
            },
            {
                "id": "g6a5-21",
                "word": "meaning",
                "phonetic": "/ˈmiːnɪŋ/",
                "meaning": "意义；意思",
                "pos": "n.",
                "unit": "Unit 5"
            },
            {
                "id": "g6a5-22",
                "word": "shout",
                "phonetic": "/ʃaʊt/",
                "meaning": "大声说；叫",
                "pos": "v.",
                "unit": "Unit 5"
            },
            {
                "id": "g6a5-23",
                "word": "jacket",
                "phonetic": "/ˈdʒækɪt/",
                "meaning": "夹克衫；短上衣",
                "pos": "n.",
                "unit": "Unit 5"
            },
            {
                "id": "g6a5-24",
                "word": "if",
                "phonetic": "/ɪf/",
                "meaning": "如果；假若",
                "pos": "conj.",
                "unit": "Unit 5"
            },
            {
                "id": "g6a5-25",
                "word": "snack",
                "phonetic": "/snæk/",
                "meaning": "点心；小吃",
                "pos": "n.",
                "unit": "Unit 5"
            },
            {
                "id": "g6a5-26",
                "word": "could",
                "phonetic": "/kʊd; kəd/",
                "meaning": "modal v. （询问是否可以做某事）能；可以",
                "pos": "",
                "unit": "Unit 5"
            },
            {
                "id": "g6a5-27",
                "word": "hen",
                "phonetic": "/hen/",
                "meaning": "母鸡",
                "pos": "n.",
                "unit": "Unit 5"
            },
            {
                "id": "g6a5-28",
                "word": "diary",
                "phonetic": "/ˈdaɪəri/",
                "meaning": "日记；日记簿",
                "pos": "n.",
                "unit": "Unit 5"
            },
            {
                "id": "g6a5-29",
                "word": "cookie",
                "phonetic": "/ˈkʊki/",
                "meaning": "曲奇饼",
                "pos": "n.",
                "unit": "Unit 5"
            },
            {
                "id": "g6a5-30",
                "word": "direct",
                "phonetic": "/dəˈrekt; daɪˈrekt/",
                "meaning": "指路；领路；指导",
                "pos": "v.",
                "unit": "Unit 5"
            },
            {
                "id": "g6a5-31",
                "word": "yard",
                "phonetic": "/jɑːd/",
                "meaning": "（某种用途的）区域，场地",
                "pos": "n.",
                "unit": "Unit 5"
            },
            {
                "id": "g6a5-32",
                "word": "glad",
                "phonetic": "/ɡlæd/",
                "meaning": "高兴；愉快",
                "pos": "adj.",
                "unit": "Unit 5"
            },
            {
                "id": "g6a5-33",
                "word": "believe",
                "phonetic": "/bɪˈliːv/",
                "meaning": "相信",
                "pos": "v.",
                "unit": "Unit 5"
            },
            {
                "id": "g6a5-34",
                "word": "unforgettable",
                "phonetic": "/ˌʌnfəˈɡetəbl/",
                "meaning": "令人难忘的",
                "pos": "adj.",
                "unit": "Unit 5"
            },
            {
                "id": "g6a5-35",
                "word": "smooth",
                "phonetic": "/smuːð/",
                "meaning": "光滑的；平坦的；平整的",
                "pos": "adj.",
                "unit": "Unit 5"
            },
            {
                "id": "g6a5-36",
                "word": "neck",
                "phonetic": "/nek/",
                "meaning": "颈；脖子",
                "pos": "n.",
                "unit": "Unit 5"
            },
            {
                "id": "g6a5-37",
                "word": "friendly",
                "phonetic": "/ˈfrendli/",
                "meaning": "友爱的；友好的",
                "pos": "adj.",
                "unit": "Unit 5"
            },
            {
                "id": "g6a5-38",
                "word": "ride",
                "phonetic": "/raɪd/",
                "meaning": "v. 骑马；驾驶 / n. （乘车或骑车的）短途旅程",
                "pos": "v. & n.",
                "unit": "Unit 5",
                "irregular_forms": {
                    "past": "rode",
                    "pp": "ridden"
                }
            }
        ]
    },
    {
        "id": "sys-6a-u6",
        "name": "六年级上册 Unit 6",
        "grade": "小学",
        "description": "上海版六年级上册 Unit 6 英语词汇（上海教育出版社·五四学制）",
        "created_at": "2024-01-01",
        "words": [
            {
                "id": "g6a6-1",
                "word": "around",
                "phonetic": "/əˈraʊnd/",
                "meaning": "prep. 在……周围 / adv. 在周围；大约",
                "pos": "prep. & adv.",
                "unit": "Unit 6"
            },
            {
                "id": "g6a6-2",
                "word": "vacation",
                "phonetic": "/vəˈkeɪʃn/",
                "meaning": "假期",
                "pos": "n.",
                "unit": "Unit 6"
            },
            {
                "id": "g6a6-3",
                "word": "trip",
                "phonetic": "/trɪp/",
                "meaning": "（尤指短程往返的）旅行；旅游；出行",
                "pos": "n.",
                "unit": "Unit 6"
            },
            {
                "id": "g6a6-4",
                "word": "popular",
                "phonetic": "/ˈpɒpjələ(r)/",
                "meaning": "大众喜爱的；广受欢迎的；当红的",
                "pos": "adj.",
                "unit": "Unit 6"
            },
            {
                "id": "g6a6-5",
                "word": "tour",
                "phonetic": "/tʊə(r)/",
                "meaning": "旅行；旅游",
                "pos": "n.",
                "unit": "Unit 6"
            },
            {
                "id": "g6a6-6",
                "word": "tip",
                "phonetic": "/tɪp/",
                "meaning": "指点；实用的提示",
                "pos": "n.",
                "unit": "Unit 6"
            },
            {
                "id": "g6a6-7",
                "word": "footprint",
                "phonetic": "/ˈfʊtprɪnt/",
                "meaning": "脚印；足迹",
                "pos": "n.",
                "unit": "Unit 6"
            },
            {
                "id": "g6a6-8",
                "word": "hike",
                "phonetic": "/haɪk/",
                "meaning": "徒步旅行",
                "pos": "v.",
                "unit": "Unit 6"
            },
            {
                "id": "g6a6-9",
                "word": "nature",
                "phonetic": "/ˈneɪtʃə(r)/",
                "meaning": "大自然",
                "pos": "n.",
                "unit": "Unit 6"
            },
            {
                "id": "g6a6-10",
                "word": "enjoy",
                "phonetic": "/ɪnˈdʒɔɪ/",
                "meaning": "享受；欣赏",
                "pos": "v.",
                "unit": "Unit 6"
            },
            {
                "id": "g6a6-11",
                "word": "local",
                "phonetic": "/ˈləʊkl/",
                "meaning": "当地的",
                "pos": "adj.",
                "unit": "Unit 6"
            },
            {
                "id": "g6a6-12",
                "word": "lazy",
                "phonetic": "/ˈleɪzi/",
                "meaning": "懒散的；悠闲的",
                "pos": "adj.",
                "unit": "Unit 6"
            },
            {
                "id": "g6a6-13",
                "word": "roof",
                "phonetic": "/ruːf/",
                "meaning": "屋顶；顶部",
                "pos": "n.",
                "unit": "Unit 6"
            },
            {
                "id": "g6a6-14",
                "word": "ski",
                "phonetic": "/skiː/",
                "meaning": "滑雪",
                "pos": "v.",
                "unit": "Unit 6"
            },
            {
                "id": "g6a6-15",
                "word": "reason",
                "phonetic": "/ˈriːzn/",
                "meaning": "原因；理由",
                "pos": "n.",
                "unit": "Unit 6"
            },
            {
                "id": "g6a6-16",
                "word": "drive",
                "phonetic": "/draɪv/",
                "meaning": "驾驶；开车",
                "pos": "v.",
                "unit": "Unit 6",
                "irregular_forms": {
                    "past": "drove",
                    "pp": "driven"
                }
            },
            {
                "id": "g6a6-17",
                "word": "shall",
                "phonetic": "/ʃæl; ʃəl/",
                "meaning": "modal v. （同I 和we 连用，表示将来）将要；将会",
                "pos": "",
                "unit": "Unit 6",
                "irregular_forms": {
                    "past": "should",
                    "pp": "/"
                }
            },
            {
                "id": "g6a6-18",
                "word": "afraid",
                "phonetic": "/əˈfreɪd/",
                "meaning": "害怕；畏惧",
                "pos": "adj.",
                "unit": "Unit 6"
            },
            {
                "id": "g6a6-19",
                "word": "I’m afraid",
                "phonetic": "",
                "meaning": "我怕；恐怕；很遗憾；对不起",
                "pos": "phr.",
                "unit": "Unit 6"
            },
            {
                "id": "g6a6-20",
                "word": "expensive",
                "phonetic": "/ɪkˈspensɪv/",
                "meaning": "昂贵的；价格高的",
                "pos": "adj.",
                "unit": "Unit 6"
            },
            {
                "id": "g6a6-21",
                "word": "price",
                "phonetic": "/praɪs/",
                "meaning": "价格；价钱",
                "pos": "n.",
                "unit": "Unit 6"
            },
            {
                "id": "g6a6-22",
                "word": "ticket",
                "phonetic": "/ˈtɪkɪt/",
                "meaning": "票；入场券",
                "pos": "n.",
                "unit": "Unit 6"
            },
            {
                "id": "g6a6-23",
                "word": "better",
                "phonetic": "/ˈbetə(r)/",
                "meaning": "adj. （good 的比较级）较好的；更好的 / adv. （well 的比较级）更好",
                "pos": "adj. & adv.",
                "unit": "Unit 6"
            },
            {
                "id": "g6a6-24",
                "word": "convenient",
                "phonetic": "/kənˈviːniənt/",
                "meaning": "方便的；便利的；省事的",
                "pos": "adj.",
                "unit": "Unit 6"
            },
            {
                "id": "g6a6-25",
                "word": "speed",
                "phonetic": "/spiːd/",
                "meaning": "速度",
                "pos": "n.",
                "unit": "Unit 6",
                "irregular_forms": {
                    "past": "sped/speeded",
                    "pp": "sped/speeded"
                }
            },
            {
                "id": "g6a6-26",
                "word": "high-speed",
                "phonetic": "/ˌhaɪ ˈspiːd/",
                "meaning": "高速的",
                "pos": "adj.",
                "unit": "Unit 6"
            },
            {
                "id": "g6a6-27",
                "word": "comfortable",
                "phonetic": "/ˈkʌmftəbl/",
                "meaning": "使人舒服的；舒适的",
                "pos": "adj.",
                "unit": "Unit 6"
            },
            {
                "id": "g6a6-28",
                "word": "view",
                "phonetic": "/vjuː/",
                "meaning": "景色；（尤指）乡间美景；视野；（个人的）看法",
                "pos": "n.",
                "unit": "Unit 6"
            },
            {
                "id": "g6a6-29",
                "word": "carry",
                "phonetic": "/ˈkæri/",
                "meaning": "拿；提；运送；输送",
                "pos": "v.",
                "unit": "Unit 6"
            },
            {
                "id": "g6a6-30",
                "word": "plan",
                "phonetic": "/plæn/",
                "meaning": "计划；打算",
                "pos": "n. & v.",
                "unit": "Unit 6"
            },
            {
                "id": "g6a6-31",
                "word": "own",
                "phonetic": "/əʊn/",
                "meaning": "（用于强调）自己的，本人的",
                "pos": "adj. & pron.",
                "unit": "Unit 6"
            },
            {
                "id": "g6a6-32",
                "word": "historical",
                "phonetic": "/hɪˈstɒrɪkl/",
                "meaning": "（有关）历史的",
                "pos": "adj.",
                "unit": "Unit 6"
            },
            {
                "id": "g6a6-33",
                "word": "such",
                "phonetic": "/sʌtʃ/",
                "meaning": "这样的；那样的；类似的",
                "pos": "det. & pron.",
                "unit": "Unit 6"
            },
            {
                "id": "g6a6-34",
                "word": "such as",
                "phonetic": "",
                "meaning": "例如；诸如",
                "pos": "phr.",
                "unit": "Unit 6"
            },
            {
                "id": "g6a6-35",
                "word": "palace",
                "phonetic": "/ˈpæləs/",
                "meaning": "宫殿",
                "pos": "n.",
                "unit": "Unit 6"
            },
            {
                "id": "g6a6-36",
                "word": "museum",
                "phonetic": "/mjuˈziːəm/",
                "meaning": "博物馆",
                "pos": "n.",
                "unit": "Unit 6"
            },
            {
                "id": "g6a6-37",
                "word": "national",
                "phonetic": "/ˈnæʃnəl/",
                "meaning": "国家的；全国的",
                "pos": "adj.",
                "unit": "Unit 6"
            },
            {
                "id": "g6a6-38",
                "word": "forest",
                "phonetic": "/ˈfɒrɪst/",
                "meaning": "森林；林区",
                "pos": "n.",
                "unit": "Unit 6"
            },
            {
                "id": "g6a6-39",
                "word": "mountain",
                "phonetic": "/ˈmaʊntən/",
                "meaning": "山；高山",
                "pos": "n.",
                "unit": "Unit 6"
            },
            {
                "id": "g6a6-40",
                "word": "postcard",
                "phonetic": "/ˈpəʊstkɑːd/",
                "meaning": "明信片",
                "pos": "n.",
                "unit": "Unit 6"
            },
            {
                "id": "g6a6-41",
                "word": "volunteer",
                "phonetic": "/ˌvɒlənˈtɪə(r)/",
                "meaning": "志愿者；义务工作者",
                "pos": "n.",
                "unit": "Unit 6"
            },
            {
                "id": "g6a6-42",
                "word": "opera",
                "phonetic": "/ˈɒprə/",
                "meaning": "歌剧",
                "pos": "n.",
                "unit": "Unit 6"
            },
            {
                "id": "g6a6-43",
                "word": "myself",
                "phonetic": "/maɪˈself/",
                "meaning": "（用于动作影响说话人或作者时）我自己",
                "pos": "pron.",
                "unit": "Unit 6"
            },
            {
                "id": "g6a6-44",
                "word": "enjoy oneself",
                "phonetic": "",
                "meaning": "过得快乐；玩得高兴",
                "pos": "phr.",
                "unit": "Unit 6"
            }
        ]
    },
    {
        "id": "sys-7a-u1",
        "name": "七年级上册 Unit 1",
        "grade": "初中",
        "description": "上海版七年级上册 Unit 1 英语词汇（上海教育出版社·五四学制）",
        "created_at": "2024-01-01",
        "words": [
            {
                "id": "g7a1-1",
                "word": "curious",
                "phonetic": "/ˈkjʊəriəs/",
                "meaning": "好奇的",
                "pos": "adj.",
                "unit": "Unit 1"
            },
            {
                "id": "g7a1-2",
                "word": "magazine",
                "phonetic": "/ˌmæɡəˈziːn/",
                "meaning": "杂志",
                "pos": "n.",
                "unit": "Unit 1"
            },
            {
                "id": "g7a1-3",
                "word": "test",
                "phonetic": "/test/",
                "meaning": "测试；检测",
                "pos": "v.",
                "unit": "Unit 1"
            },
            {
                "id": "g7a1-4",
                "word": "windsurf",
                "phonetic": "/ˈwɪndsɜːf/",
                "meaning": "做帆板运动",
                "pos": "v.",
                "unit": "Unit 1"
            },
            {
                "id": "g7a1-5",
                "word": "feeling",
                "phonetic": "/ˈfiːlɪŋ/",
                "meaning": "感受",
                "pos": "n.",
                "unit": "Unit 1"
            },
            {
                "id": "g7a1-6",
                "word": "brave",
                "phonetic": "/breɪv/",
                "meaning": "勇敢的",
                "pos": "adj.",
                "unit": "Unit 1"
            },
            {
                "id": "g7a1-7",
                "word": "challenge",
                "phonetic": "/ˈtʃælɪndʒ/",
                "meaning": "挑战",
                "pos": "n.",
                "unit": "Unit 1"
            },
            {
                "id": "g7a1-8",
                "word": "machine",
                "phonetic": "/məˈʃiːn/",
                "meaning": "机器",
                "pos": "n.",
                "unit": "Unit 1"
            },
            {
                "id": "g7a1-9",
                "word": "traffic",
                "phonetic": "/ˈtræfɪk/",
                "meaning": "交通",
                "pos": "n.",
                "unit": "Unit 1"
            },
            {
                "id": "g7a1-10",
                "word": "board",
                "phonetic": "/bɔːd/",
                "meaning": "板",
                "pos": "n.",
                "unit": "Unit 1"
            },
            {
                "id": "g7a1-11",
                "word": "print",
                "phonetic": "/prɪnt/",
                "meaning": "打印",
                "pos": "v.",
                "unit": "Unit 1"
            },
            {
                "id": "g7a1-12",
                "word": "printing",
                "phonetic": "/ˈprɪntɪŋ/",
                "meaning": "印刷；打印",
                "pos": "n.",
                "unit": "Unit 1"
            },
            {
                "id": "g7a1-13",
                "word": "grow",
                "phonetic": "/ɡrəʊ/",
                "meaning": "生长；栽种",
                "pos": "v.",
                "unit": "Unit 1",
                "irregular_forms": {
                    "past": "grew",
                    "pp": "grown"
                }
            },
            {
                "id": "g7a1-14",
                "word": "improve",
                "phonetic": "/ɪmˈpruːv/",
                "meaning": "改善；改进",
                "pos": "v.",
                "unit": "Unit 1"
            },
            {
                "id": "g7a1-15",
                "word": "camp",
                "phonetic": "/kæmp/",
                "meaning": "v. 露营 / n. 营地",
                "pos": "v. & n.",
                "unit": "Unit 1"
            },
            {
                "id": "g7a1-16",
                "word": "sticker",
                "phonetic": "/ˈstɪkə(r)/",
                "meaning": "贴纸",
                "pos": "n.",
                "unit": "Unit 1"
            },
            {
                "id": "g7a1-17",
                "word": "power",
                "phonetic": "/ˈpaʊə(r)/",
                "meaning": "驱动（机器）",
                "pos": "v.",
                "unit": "Unit 1"
            },
            {
                "id": "g7a1-18",
                "word": "discuss",
                "phonetic": "/dɪˈskʌs/",
                "meaning": "讨论",
                "pos": "v.",
                "unit": "Unit 1"
            },
            {
                "id": "g7a1-19",
                "word": "everywhere",
                "phonetic": "/ˈevriweə(r)/",
                "meaning": "到处",
                "pos": "adv.",
                "unit": "Unit 1"
            },
            {
                "id": "g7a1-20",
                "word": "impossible",
                "phonetic": "/ɪmˈpɒsəbl/",
                "meaning": "不可能的",
                "pos": "adj.",
                "unit": "Unit 1"
            },
            {
                "id": "g7a1-21",
                "word": "solar panel",
                "phonetic": "/ˌsəʊlə ˈpænl/",
                "meaning": "太阳能电池板",
                "pos": "n.",
                "unit": "Unit 1"
            },
            {
                "id": "g7a1-22",
                "word": "solar cell",
                "phonetic": "/ˌsəʊlə ˈsel/",
                "meaning": "太阳能电池",
                "pos": "n.",
                "unit": "Unit 1"
            },
            {
                "id": "g7a1-23",
                "word": "holder",
                "phonetic": "/ˈhəʊldə(r)/",
                "meaning": "支托物",
                "pos": "n.",
                "unit": "Unit 1"
            },
            {
                "id": "g7a1-24",
                "word": "fail",
                "phonetic": "/feɪl/",
                "meaning": "失败",
                "pos": "v.",
                "unit": "Unit 1"
            },
            {
                "id": "g7a1-25",
                "word": "pizza",
                "phonetic": "/ˈpiːtsə/",
                "meaning": "比萨饼",
                "pos": "n.",
                "unit": "Unit 1"
            },
            {
                "id": "g7a1-26",
                "word": "burn",
                "phonetic": "/bɜːn/",
                "meaning": "烫伤",
                "pos": "v.",
                "unit": "Unit 1",
                "irregular_forms": {
                    "past": "burnt/burned",
                    "pp": "burnt/burned"
                }
            },
            {
                "id": "g7a1-27",
                "word": "pan",
                "phonetic": "/pæn/",
                "meaning": "平底锅",
                "pos": "n.",
                "unit": "Unit 1"
            },
            {
                "id": "g7a1-28",
                "word": "troublesome",
                "phonetic": "/ˈtrʌblsəm/",
                "meaning": "令人烦恼的",
                "pos": "adj.",
                "unit": "Unit 1"
            },
            {
                "id": "g7a1-29",
                "word": "luckily",
                "phonetic": "/ˈlʌkɪli/",
                "meaning": "幸好",
                "pos": "adv.",
                "unit": "Unit 1"
            },
            {
                "id": "g7a1-30",
                "word": "layer",
                "phonetic": "/ˈleɪə(r)/",
                "meaning": "层；层次",
                "pos": "n.",
                "unit": "Unit 1"
            },
            {
                "id": "g7a1-31",
                "word": "separate",
                "phonetic": "/ˈsepəreɪt/",
                "meaning": "隔开；分离",
                "pos": "v.",
                "unit": "Unit 1"
            },
            {
                "id": "g7a1-32",
                "word": "away",
                "phonetic": "/əˈweɪ/",
                "meaning": "离开",
                "pos": "adv.",
                "unit": "Unit 1"
            },
            {
                "id": "g7a1-33",
                "word": "take away",
                "phonetic": "",
                "meaning": "拿走",
                "pos": "phr.",
                "unit": "Unit 1"
            },
            {
                "id": "g7a1-34",
                "word": "stick",
                "phonetic": "/stɪk/",
                "meaning": "v. 粘贴 / n. 拐杖；枝条；棍子",
                "pos": "v. & n.",
                "unit": "Unit 1",
                "irregular_forms": {
                    "past": "stuck",
                    "pp": "stuck"
                }
            },
            {
                "id": "g7a1-35",
                "word": "device",
                "phonetic": "/dɪˈvaɪs/",
                "meaning": "仪器",
                "pos": "n.",
                "unit": "Unit 1"
            },
            {
                "id": "g7a1-36",
                "word": "countless",
                "phonetic": "/ˈkaʊntləs/",
                "meaning": "无数的；数不尽的",
                "pos": "adj.",
                "unit": "Unit 1"
            },
            {
                "id": "g7a1-37",
                "word": "succeed",
                "phonetic": "/səkˈsiːd/",
                "meaning": "成功",
                "pos": "v.",
                "unit": "Unit 1"
            },
            {
                "id": "g7a1-38",
                "word": "hopefully",
                "phonetic": "/ˈhəʊpfəli/",
                "meaning": "有希望地",
                "pos": "adv.",
                "unit": "Unit 1"
            },
            {
                "id": "g7a1-39",
                "word": "creative",
                "phonetic": "/kriˈeɪtɪv/",
                "meaning": "有创造力的",
                "pos": "adj.",
                "unit": "Unit 1"
            },
            {
                "id": "g7a1-40",
                "word": "handle",
                "phonetic": "/ˈhændl/",
                "meaning": "把手",
                "pos": "n.",
                "unit": "Unit 1"
            },
            {
                "id": "g7a1-41",
                "word": "proud",
                "phonetic": "/praʊd/",
                "meaning": "骄傲的；自豪的",
                "pos": "adj.",
                "unit": "Unit 1"
            }
        ]
    },
    {
        "id": "sys-7a-u2",
        "name": "七年级上册 Unit 2",
        "grade": "初中",
        "description": "上海版七年级上册 Unit 2 英语词汇（上海教育出版社·五四学制）",
        "created_at": "2024-01-01",
        "words": [
            {
                "id": "g7a2-1",
                "word": "radio",
                "phonetic": "/ˈreɪdiəʊ/",
                "meaning": "无线电广播；收音机",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g7a2-2",
                "word": "deal",
                "phonetic": "/diːl/",
                "meaning": "处理",
                "pos": "v.",
                "unit": "Unit 2",
                "irregular_forms": {
                    "past": "dealt",
                    "pp": "dealt"
                }
            },
            {
                "id": "g7a2-3",
                "word": "deal with",
                "phonetic": "",
                "meaning": "处理",
                "pos": "phr.",
                "unit": "Unit 2"
            },
            {
                "id": "g7a2-4",
                "word": "fear",
                "phonetic": "/fɪə(r)/",
                "meaning": "害怕；担忧",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g7a2-5",
                "word": "deep",
                "phonetic": "/diːp/",
                "meaning": "低沉的；深的",
                "pos": "adj.",
                "unit": "Unit 2"
            },
            {
                "id": "g7a2-6",
                "word": "rough",
                "phonetic": "/rʌf/",
                "meaning": "令人不舒服的；粗糙的",
                "pos": "adj.",
                "unit": "Unit 2"
            },
            {
                "id": "g7a2-7",
                "word": "belief",
                "phonetic": "/bɪˈliːf/",
                "meaning": "信念；相信",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g7a2-8",
                "word": "ourselves",
                "phonetic": "/ɑːˈselvz/ /ˌaʊəˈselvz/",
                "meaning": "（we 的反身形式）我们自己",
                "pos": "pron.",
                "unit": "Unit 2"
            },
            {
                "id": "g7a2-9",
                "word": "weak",
                "phonetic": "/wiːk/",
                "meaning": "虚弱的；无力的",
                "pos": "adj.",
                "unit": "Unit 2"
            },
            {
                "id": "g7a2-10",
                "word": "heart",
                "phonetic": "/hɑːt/",
                "meaning": "心脏；内心",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g7a2-11",
                "word": "paper cutting",
                "phonetic": "",
                "meaning": "剪纸",
                "pos": "phr.",
                "unit": "Unit 2"
            },
            {
                "id": "g7a2-12",
                "word": "teenager",
                "phonetic": "/ˈtiːneɪdʒə(r)/",
                "meaning": "青少年",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g7a2-13",
                "word": "honest",
                "phonetic": "/ˈɒnɪst/",
                "meaning": "坦率的；诚实的",
                "pos": "adj.",
                "unit": "Unit 2"
            },
            {
                "id": "g7a2-14",
                "word": "alive",
                "phonetic": "/əˈlaɪv/",
                "meaning": "继续存在的；活着的",
                "pos": "adj.",
                "unit": "Unit 2"
            },
            {
                "id": "g7a2-15",
                "word": "dream",
                "phonetic": "/driːm/",
                "meaning": "梦想；做梦",
                "pos": "v.",
                "unit": "Unit 2",
                "irregular_forms": {
                    "past": "dreamt/dreamed",
                    "pp": "dreamt/dreamed"
                }
            },
            {
                "id": "g7a2-16",
                "word": "final",
                "phonetic": "/ˈfaɪnl/",
                "meaning": "最终的",
                "pos": "adj.",
                "unit": "Unit 2"
            },
            {
                "id": "g7a2-17",
                "word": "sink",
                "phonetic": "/sɪŋk/",
                "meaning": "下沉；沉没",
                "pos": "v.",
                "unit": "Unit 2"
            },
            {
                "id": "g7a2-18",
                "word": "later",
                "phonetic": "/ˈleɪtə(r)/",
                "meaning": "随后；后来",
                "pos": "adv.",
                "unit": "Unit 2"
            },
            {
                "id": "g7a2-19",
                "word": "news",
                "phonetic": "/njuːz/",
                "meaning": "消息；新闻",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g7a2-20",
                "word": "funny",
                "phonetic": "/ˈfʌni/",
                "meaning": "滑稽的；好笑的",
                "pos": "adj.",
                "unit": "Unit 2"
            },
            {
                "id": "g7a2-21",
                "word": "costume",
                "phonetic": "/ˈkɒstjuːm/",
                "meaning": "服装；演出服",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g7a2-22",
                "word": "instead",
                "phonetic": "/ɪnˈsted/",
                "meaning": "代替",
                "pos": "adv.",
                "unit": "Unit 2"
            },
            {
                "id": "g7a2-23",
                "word": "instead of",
                "phonetic": "",
                "meaning": "代替",
                "pos": "phr.",
                "unit": "Unit 2"
            },
            {
                "id": "g7a2-24",
                "word": "had better",
                "phonetic": "",
                "meaning": "最好",
                "pos": "phr.",
                "unit": "Unit 2"
            },
            {
                "id": "g7a2-25",
                "word": "disappointment",
                "phonetic": "/ˌdɪsəˈpɔɪntmənt/",
                "meaning": "失望",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g7a2-26",
                "word": "respond",
                "phonetic": "/rɪˈspɒnd/",
                "meaning": "作出反应；回应",
                "pos": "v.",
                "unit": "Unit 2"
            },
            {
                "id": "g7a2-27",
                "word": "ring",
                "phonetic": "/rɪŋ/",
                "meaning": "回响",
                "pos": "v.",
                "unit": "Unit 2",
                "irregular_forms": {
                    "past": "rang",
                    "pp": "rung"
                }
            },
            {
                "id": "g7a2-28",
                "word": "after all",
                "phonetic": "",
                "meaning": "毕竟",
                "pos": "phr.",
                "unit": "Unit 2"
            },
            {
                "id": "g7a2-29",
                "word": "decide",
                "phonetic": "/dɪˈsaɪd/",
                "meaning": "决定",
                "pos": "v.",
                "unit": "Unit 2"
            },
            {
                "id": "g7a2-30",
                "word": "become",
                "phonetic": "/bɪˈkʌm/",
                "meaning": "变成",
                "pos": "v.",
                "unit": "Unit 2",
                "irregular_forms": {
                    "past": "became",
                    "pp": "become"
                }
            },
            {
                "id": "g7a2-31",
                "word": "through",
                "phonetic": "/θruː/",
                "meaning": "凭借；穿过",
                "pos": "prep.",
                "unit": "Unit 2"
            },
            {
                "id": "g7a2-32",
                "word": "preparation",
                "phonetic": "/ˌprepəˈreɪʃn/",
                "meaning": "准备",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g7a2-33",
                "word": "breath",
                "phonetic": "/breθ/",
                "meaning": "呼吸；呼气",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g7a2-34",
                "word": "crowd",
                "phonetic": "/kraʊd/",
                "meaning": "观众；人群",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g7a2-35",
                "word": "chant",
                "phonetic": "/tʃɑːnt/",
                "meaning": "反复呼喊；反复唱",
                "pos": "v.",
                "unit": "Unit 2"
            },
            {
                "id": "g7a2-36",
                "word": "bright",
                "phonetic": "/braɪt/",
                "meaning": "快活而生气勃勃的；明亮的",
                "pos": "adj.",
                "unit": "Unit 2"
            },
            {
                "id": "g7a2-37",
                "word": "coach",
                "phonetic": "/kəʊtʃ/",
                "meaning": "教练",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g7a2-38",
                "word": "enter",
                "phonetic": "/ˈentə(r)/",
                "meaning": "进来",
                "pos": "v.",
                "unit": "Unit 2"
            },
            {
                "id": "g7a2-39",
                "word": "enter for",
                "phonetic": "",
                "meaning": "报名参加",
                "pos": "phr.",
                "unit": "Unit 2"
            },
            {
                "id": "g7a2-40",
                "word": "design",
                "phonetic": "/dɪˈzaɪn/",
                "meaning": "设计",
                "pos": "v.",
                "unit": "Unit 2"
            },
            {
                "id": "g7a2-41",
                "word": "competition",
                "phonetic": "/ˌkɒmpəˈtɪʃn/",
                "meaning": "竞争；比赛",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g7a2-42",
                "word": "chance",
                "phonetic": "/tʃɑːns/",
                "meaning": "机会",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g7a2-43",
                "word": "past",
                "phonetic": "/pɑːst/",
                "meaning": "adj. 过去的；以往的 / prep. 经过",
                "pos": "adj. & prep.",
                "unit": "Unit 2"
            },
            {
                "id": "g7a2-44",
                "word": "deskmate",
                "phonetic": "/ˈdeskmeɪt/",
                "meaning": "同桌",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g7a2-45",
                "word": "while",
                "phonetic": "/waɪl/",
                "meaning": "n. 一会儿；一段时间 / conj. （对比两件事物）然而",
                "pos": "n. & conj.",
                "unit": "Unit 2"
            },
            {
                "id": "g7a2-46",
                "word": "firmly",
                "phonetic": "/ˈfɜːmli/",
                "meaning": "坚定地；坚固地",
                "pos": "adv.",
                "unit": "Unit 2"
            }
        ]
    },
    {
        "id": "sys-7a-u3",
        "name": "七年级上册 Unit 3",
        "grade": "初中",
        "description": "上海版七年级上册 Unit 3 英语词汇（上海教育出版社·五四学制）",
        "created_at": "2024-01-01",
        "words": [
            {
                "id": "g7a3-1",
                "word": "career",
                "phonetic": "/kəˈrɪə(r)/",
                "meaning": "职业；事业",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g7a3-2",
                "word": "guidance",
                "phonetic": "/ˈɡaɪdns/",
                "meaning": "指导；引导",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g7a3-3",
                "word": "practical",
                "phonetic": "/ˈpræktɪkl/",
                "meaning": "实际的",
                "pos": "adj.",
                "unit": "Unit 3"
            },
            {
                "id": "g7a3-4",
                "word": "hairdresser",
                "phonetic": "/ˈheədresə(r)/",
                "meaning": "理发师",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g7a3-5",
                "word": "tailor",
                "phonetic": "/ˈteɪlə(r)/",
                "meaning": "裁缝",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g7a3-6",
                "word": "service",
                "phonetic": "/ˈsɜːvɪs/",
                "meaning": "服务",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g7a3-7",
                "word": "officer",
                "phonetic": "/ˈɒfɪsə(r)/",
                "meaning": "长官",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g7a3-8",
                "word": "fireman",
                "phonetic": "/ˈfaɪəmən/",
                "meaning": "(pl. firemen) 消防员",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g7a3-9",
                "word": "artistic",
                "phonetic": "/ɑːˈtɪstɪk/",
                "meaning": "艺术的",
                "pos": "adj.",
                "unit": "Unit 3"
            },
            {
                "id": "g7a3-10",
                "word": "photographer",
                "phonetic": "/fəˈtɒɡrəfə(r)/",
                "meaning": "摄影师",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g7a3-11",
                "word": "artist",
                "phonetic": "/ˈɑːtɪst/",
                "meaning": "艺术家",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g7a3-12",
                "word": "actor / actress",
                "phonetic": "/ˈæktə(r)//ˈæktrəs/",
                "meaning": "（男/女）演员",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g7a3-13",
                "word": "engineer",
                "phonetic": "/ˌendʒɪˈnɪə(r)/",
                "meaning": "工程师",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g7a3-14",
                "word": "architect",
                "phonetic": "/ˈɑːkɪtekt/",
                "meaning": "建筑师",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g7a3-15",
                "word": "designer",
                "phonetic": "/dɪˈzaɪnə(r)/",
                "meaning": "设计师",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g7a3-16",
                "word": "entertain",
                "phonetic": "/ˌentəˈteɪn/",
                "meaning": "使快乐；娱乐",
                "pos": "v.",
                "unit": "Unit 3"
            },
            {
                "id": "g7a3-17",
                "word": "audience",
                "phonetic": "/ˈɔːdiəns/",
                "meaning": "观众",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g7a3-18",
                "word": "set",
                "phonetic": "/set/",
                "meaning": "n. 摄影场 / adj. 指定的",
                "pos": "n. & adj.",
                "unit": "Unit 3",
                "irregular_forms": {
                    "past": "set",
                    "pp": "set"
                }
            },
            {
                "id": "g7a3-19",
                "word": "role",
                "phonetic": "/rəʊl/",
                "meaning": "角色",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g7a3-20",
                "word": "scene",
                "phonetic": "/siːn/",
                "meaning": "现场；场景",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g7a3-21",
                "word": "arrive",
                "phonetic": "/əˈraɪv/",
                "meaning": "到达",
                "pos": "v.",
                "unit": "Unit 3"
            },
            {
                "id": "g7a3-22",
                "word": "page",
                "phonetic": "/peɪdʒ/",
                "meaning": "（书刊或纸张的）页",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g7a3-23",
                "word": "knowledge",
                "phonetic": "/ˈnɒlɪdʒ/",
                "meaning": "知识；学问",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g7a3-24",
                "word": "biology",
                "phonetic": "/baɪˈɒlədʒi/",
                "meaning": "生物学",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g7a3-25",
                "word": "education",
                "phonetic": "/ˌedʒuˈkeɪʃn/",
                "meaning": "教育",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g7a3-26",
                "word": "above",
                "phonetic": "/əˈbʌv/",
                "meaning": "（水平）超过，更多，更大",
                "pos": "adv.",
                "unit": "Unit 3"
            },
            {
                "id": "g7a3-27",
                "word": "readiness",
                "phonetic": "/ˈredinəs/",
                "meaning": "乐意",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g7a3-28",
                "word": "communication",
                "phonetic": "/kəˌmjuːnɪˈkeɪʃn/",
                "meaning": "交流；交际",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g7a3-29",
                "word": "training",
                "phonetic": "/ˈtreɪnɪŋ/",
                "meaning": "训练；培训",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g7a3-30",
                "word": "taste",
                "phonetic": "/teɪst/",
                "meaning": "品尝",
                "pos": "v.",
                "unit": "Unit 3"
            },
            {
                "id": "g7a3-31",
                "word": "maybe",
                "phonetic": "/ˈmeɪbi/",
                "meaning": "有可能",
                "pos": "adv.",
                "unit": "Unit 3"
            },
            {
                "id": "g7a3-32",
                "word": "yours",
                "phonetic": "/jɔːz/",
                "meaning": "您的；你的；你们的",
                "pos": "pron.",
                "unit": "Unit 3"
            },
            {
                "id": "g7a3-33",
                "word": "customer",
                "phonetic": "/ˈkʌstəmə(r)/",
                "meaning": "顾客；客户",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g7a3-34",
                "word": "market",
                "phonetic": "/ˈmɑːkɪt/",
                "meaning": "市场；集市",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g7a3-35",
                "word": "everything",
                "phonetic": "/ˈevriθɪŋ/",
                "meaning": "每样事物",
                "pos": "pron.",
                "unit": "Unit 3"
            },
            {
                "id": "g7a3-36",
                "word": "fresh",
                "phonetic": "/freʃ/",
                "meaning": "新鲜的",
                "pos": "adj.",
                "unit": "Unit 3"
            },
            {
                "id": "g7a3-37",
                "word": "restaurant",
                "phonetic": "/ˈrestrɒnt/",
                "meaning": "餐厅",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g7a3-38",
                "word": "pride",
                "phonetic": "/praɪd/",
                "meaning": "骄傲；自豪",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g7a3-39",
                "word": "kilometre (AmE kilometer)",
                "phonetic": "/ˈkɪləmiːtə(r)/",
                "meaning": "公里；千米",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g7a3-40",
                "word": "exactly",
                "phonetic": "/ɪɡˈzæktli/",
                "meaning": "确切地",
                "pos": "adv.",
                "unit": "Unit 3"
            },
            {
                "id": "g7a3-41",
                "word": "ever",
                "phonetic": "/ˈevə(r)/",
                "meaning": "在任何时候；从来",
                "pos": "adv.",
                "unit": "Unit 3"
            },
            {
                "id": "g7a3-42",
                "word": "centre (AmE center)",
                "phonetic": "/ˈsentə(r)/",
                "meaning": "中心；中央",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g7a3-43",
                "word": "greet",
                "phonetic": "/ɡriːt/",
                "meaning": "打招呼；欢迎",
                "pos": "v.",
                "unit": "Unit 3"
            },
            {
                "id": "g7a3-44",
                "word": "distance",
                "phonetic": "/ˈdɪstəns/",
                "meaning": "距离",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g7a3-45",
                "word": "method",
                "phonetic": "/ˈmeθəd/",
                "meaning": "方法；措施",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g7a3-46",
                "word": "simple",
                "phonetic": "/ˈsɪmpl/",
                "meaning": "简单的",
                "pos": "adj.",
                "unit": "Unit 3"
            },
            {
                "id": "g7a3-47",
                "word": "railway",
                "phonetic": "/ˈreɪlweɪ/",
                "meaning": "铁路；铁道",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g7a3-48",
                "word": "each other",
                "phonetic": "",
                "meaning": "相互；彼此",
                "pos": "phr.",
                "unit": "Unit 3"
            },
            {
                "id": "g7a3-49",
                "word": "address",
                "phonetic": "/əˈdres/",
                "meaning": "地址",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g7a3-50",
                "word": "deliver",
                "phonetic": "/dɪˈlɪvə(r)/",
                "meaning": "递送",
                "pos": "v.",
                "unit": "Unit 3"
            },
            {
                "id": "g7a3-51",
                "word": "serve",
                "phonetic": "/sɜːv/",
                "meaning": "服务",
                "pos": "v.",
                "unit": "Unit 3"
            },
            {
                "id": "g7a3-52",
                "word": "trust",
                "phonetic": "/trʌst/",
                "meaning": "信任",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g7a3-53",
                "word": "respect",
                "phonetic": "/rɪˈspekt/",
                "meaning": "n. 尊重；尊敬 / v. 尊重；尊敬",
                "pos": "n. & v.",
                "unit": "Unit 3"
            },
            {
                "id": "g7a3-54",
                "word": "lively",
                "phonetic": "/ˈlaɪvli/",
                "meaning": "有活力的；活泼的",
                "pos": "adj.",
                "unit": "Unit 3"
            },
            {
                "id": "g7a3-55",
                "word": "dictionary",
                "phonetic": "/ˈdɪkʃənri/",
                "meaning": "词典；字典",
                "pos": "n.",
                "unit": "Unit 3"
            }
        ]
    },
    {
        "id": "sys-7a-u4",
        "name": "七年级上册 Unit 4",
        "grade": "初中",
        "description": "上海版七年级上册 Unit 4 英语词汇（上海教育出版社·五四学制）",
        "created_at": "2024-01-01",
        "words": [
            {
                "id": "g7a4-1",
                "word": "camera",
                "phonetic": "/ˈkæmərə/",
                "meaning": "照相机；摄影机",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g7a4-2",
                "word": "itself",
                "phonetic": "/ɪtˈself/",
                "meaning": "它自己（it 的反身形式）",
                "pos": "pron.",
                "unit": "Unit 4"
            },
            {
                "id": "g7a4-3",
                "word": "alarm",
                "phonetic": "/əˈlɑːm/",
                "meaning": "警报器",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g7a4-4",
                "word": "stranger",
                "phonetic": "/ˈstreɪndʒə(r)/",
                "meaning": "陌生人",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g7a4-5",
                "word": "lock",
                "phonetic": "/lɒk/",
                "meaning": "锁",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g7a4-6",
                "word": "explore",
                "phonetic": "/ɪkˈsplɔː(r)/",
                "meaning": "探索；探究",
                "pos": "v.",
                "unit": "Unit 4"
            },
            {
                "id": "g7a4-7",
                "word": "rock",
                "phonetic": "/rɒk/",
                "meaning": "（使）轻轻摇晃",
                "pos": "v.",
                "unit": "Unit 4"
            },
            {
                "id": "g7a4-8",
                "word": "shower",
                "phonetic": "/ˈʃaʊə(r)/",
                "meaning": "淋浴",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g7a4-9",
                "word": "mode",
                "phonetic": "/məʊd/",
                "meaning": "模式；方式",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g7a4-10",
                "word": "text message",
                "phonetic": "",
                "meaning": "（手机）短信息",
                "pos": "phr.",
                "unit": "Unit 4"
            },
            {
                "id": "g7a4-11",
                "word": "bedroom",
                "phonetic": "/ˈbedruːm/",
                "meaning": "卧室",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g7a4-12",
                "word": "bathroom",
                "phonetic": "/ˈbɑːθruːm/",
                "meaning": "浴室；盥洗室",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g7a4-13",
                "word": "suggest",
                "phonetic": "/səˈdʒest/",
                "meaning": "建议",
                "pos": "v.",
                "unit": "Unit 4"
            },
            {
                "id": "g7a4-14",
                "word": "protect",
                "phonetic": "/prəˈtekt/",
                "meaning": "保护",
                "pos": "v.",
                "unit": "Unit 4"
            },
            {
                "id": "g7a4-15",
                "word": "review",
                "phonetic": "/rɪˈvjuː/",
                "meaning": "n. 评论 / v. 复习",
                "pos": "n. & v.",
                "unit": "Unit 4"
            },
            {
                "id": "g7a4-16",
                "word": "heating",
                "phonetic": "/ˈhiːtɪŋ/",
                "meaning": "供暖；暖气设备",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g7a4-17",
                "word": "guide",
                "phonetic": "/ɡaɪd/",
                "meaning": "指导；指引",
                "pos": "v.",
                "unit": "Unit 4"
            },
            {
                "id": "g7a4-18",
                "word": "personal",
                "phonetic": "/ˈpɜːsənl/",
                "meaning": "个人的；私人的",
                "pos": "adj.",
                "unit": "Unit 4"
            },
            {
                "id": "g7a4-19",
                "word": "owner",
                "phonetic": "/ˈəʊnə(r)/",
                "meaning": "物主；主人",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g7a4-20",
                "word": "alarm clock",
                "phonetic": "",
                "meaning": "闹钟",
                "pos": "phr.",
                "unit": "Unit 4"
            },
            {
                "id": "g7a4-21",
                "word": "keep track of",
                "phonetic": "",
                "meaning": "追踪",
                "pos": "phr.",
                "unit": "Unit 4"
            },
            {
                "id": "g7a4-22",
                "word": "schedule",
                "phonetic": "/ˈʃedjuːl/",
                "meaning": "日程安排",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g7a4-23",
                "word": "health care",
                "phonetic": "",
                "meaning": "医疗（服务）",
                "pos": "phr.",
                "unit": "Unit 4"
            },
            {
                "id": "g7a4-24",
                "word": "order",
                "phonetic": "/ˈɔːdə(r)/",
                "meaning": "订购",
                "pos": "v.",
                "unit": "Unit 4"
            },
            {
                "id": "g7a4-25",
                "word": "signal",
                "phonetic": "/ˈsɪɡnəl/",
                "meaning": "发信号；示意",
                "pos": "v.",
                "unit": "Unit 4"
            },
            {
                "id": "g7a4-26",
                "word": "sense",
                "phonetic": "/sens/",
                "meaning": "感觉到；意识到",
                "pos": "v.",
                "unit": "Unit 4"
            },
            {
                "id": "g7a4-27",
                "word": "manage",
                "phonetic": "/ˈmænɪdʒ/",
                "meaning": "明智地使用；管理；完成（困难的事）",
                "pos": "v.",
                "unit": "Unit 4"
            },
            {
                "id": "g7a4-28",
                "word": "remind",
                "phonetic": "/rɪˈmaɪnd/",
                "meaning": "提醒；使……想起",
                "pos": "v.",
                "unit": "Unit 4"
            },
            {
                "id": "g7a4-29",
                "word": "produce",
                "phonetic": "/prəˈdjuːs/",
                "meaning": "生产",
                "pos": "v.",
                "unit": "Unit 4"
            },
            {
                "id": "g7a4-30",
                "word": "store",
                "phonetic": "/stɔː(r)/",
                "meaning": "保存",
                "pos": "v.",
                "unit": "Unit 4"
            },
            {
                "id": "g7a4-31",
                "word": "sore",
                "phonetic": "/sɔː(r)/",
                "meaning": "疼痛的；酸痛的",
                "pos": "adj.",
                "unit": "Unit 4"
            },
            {
                "id": "g7a4-32",
                "word": "throat",
                "phonetic": "/θrəʊt/",
                "meaning": "嗓子",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g7a4-33",
                "word": "understand",
                "phonetic": "/ˌʌndəˈstænd/",
                "meaning": "懂；理解",
                "pos": "v.",
                "unit": "Unit 4",
                "irregular_forms": {
                    "past": "understood",
                    "pp": "understood"
                }
            },
            {
                "id": "g7a4-34",
                "word": "already",
                "phonetic": "/ɔːlˈredi/",
                "meaning": "已经",
                "pos": "adv.",
                "unit": "Unit 4"
            },
            {
                "id": "g7a4-35",
                "word": "depend",
                "phonetic": "/dɪˈpend/",
                "meaning": "依靠；根据……而定",
                "pos": "v.",
                "unit": "Unit 4"
            },
            {
                "id": "g7a4-36",
                "word": "depend on",
                "phonetic": "",
                "meaning": "依赖",
                "pos": "phr.",
                "unit": "Unit 4"
            },
            {
                "id": "g7a4-37",
                "word": "oven",
                "phonetic": "/ˈʌvn/",
                "meaning": "烤箱；烤炉",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g7a4-38",
                "word": "truly",
                "phonetic": "/ˈtruːli/",
                "meaning": "确实地；真诚地",
                "pos": "adv.",
                "unit": "Unit 4"
            }
        ]
    },
    {
        "id": "sys-7a-u5",
        "name": "七年级上册 Unit 5",
        "grade": "初中",
        "description": "上海版七年级上册 Unit 5 英语词汇（上海教育出版社·五四学制）",
        "created_at": "2024-01-01",
        "words": [
            {
                "id": "g7a5-1",
                "word": "expect",
                "phonetic": "/ɪkˈspekt/",
                "meaning": "期望；期待",
                "pos": "v.",
                "unit": "Unit 5"
            },
            {
                "id": "g7a5-2",
                "word": "pleasant",
                "phonetic": "/ˈpleznt/",
                "meaning": "令人愉快的",
                "pos": "adj.",
                "unit": "Unit 5"
            },
            {
                "id": "g7a5-3",
                "word": "element",
                "phonetic": "/ˈelɪmənt/",
                "meaning": "要素",
                "pos": "n.",
                "unit": "Unit 5"
            },
            {
                "id": "g7a5-4",
                "word": "plot",
                "phonetic": "/plɒt/",
                "meaning": "故事情节",
                "pos": "n.",
                "unit": "Unit 5"
            },
            {
                "id": "g7a5-5",
                "word": "main",
                "phonetic": "/meɪn/",
                "meaning": "主要的",
                "pos": "adj.",
                "unit": "Unit 5"
            },
            {
                "id": "g7a5-6",
                "word": "director",
                "phonetic": "/dəˈrektə(r)/",
                "meaning": "导演；（某一活动的）负责人",
                "pos": "n.",
                "unit": "Unit 5"
            },
            {
                "id": "g7a5-7",
                "word": "polite",
                "phonetic": "/pəˈlaɪt/",
                "meaning": "有礼貌的",
                "pos": "adj.",
                "unit": "Unit 5"
            },
            {
                "id": "g7a5-8",
                "word": "impolite",
                "phonetic": "/ˌɪmpəˈlaɪt/",
                "meaning": "不礼貌的",
                "pos": "adj.",
                "unit": "Unit 5"
            },
            {
                "id": "g7a5-9",
                "word": "correct",
                "phonetic": "/kəˈrekt/",
                "meaning": "准确无误的",
                "pos": "adj.",
                "unit": "Unit 5"
            },
            {
                "id": "g7a5-10",
                "word": "incorrect",
                "phonetic": "/ˌɪnkəˈrekt/",
                "meaning": "不准确的",
                "pos": "adj.",
                "unit": "Unit 5"
            },
            {
                "id": "g7a5-11",
                "word": "screen",
                "phonetic": "/skriːn/",
                "meaning": "银幕；屏幕",
                "pos": "n.",
                "unit": "Unit 5"
            },
            {
                "id": "g7a5-12",
                "word": "web",
                "phonetic": "/web/",
                "meaning": "网",
                "pos": "n.",
                "unit": "Unit 5"
            },
            {
                "id": "g7a5-13",
                "word": "spider",
                "phonetic": "/ˈspaɪdə(r)/",
                "meaning": "蜘蛛",
                "pos": "n.",
                "unit": "Unit 5"
            },
            {
                "id": "g7a5-14",
                "word": "friendship",
                "phonetic": "/ˈfrendʃɪp/",
                "meaning": "友谊；朋友关系",
                "pos": "n.",
                "unit": "Unit 5"
            },
            {
                "id": "g7a5-15",
                "word": "subtitle",
                "phonetic": "/ˈsʌbtaɪtl/",
                "meaning": "字幕",
                "pos": "n.",
                "unit": "Unit 5"
            },
            {
                "id": "g7a5-16",
                "word": "true",
                "phonetic": "/truː/",
                "meaning": "真实的",
                "pos": "adj.",
                "unit": "Unit 5"
            },
            {
                "id": "g7a5-17",
                "word": "wrestle",
                "phonetic": "/ˈresl/",
                "meaning": "摔跤",
                "pos": "v.",
                "unit": "Unit 5"
            },
            {
                "id": "g7a5-18",
                "word": "weekday",
                "phonetic": "/ˈwiːkdeɪ/",
                "meaning": "工作日（星期一到星期五的任何一天）",
                "pos": "n.",
                "unit": "Unit 5"
            },
            {
                "id": "g7a5-19",
                "word": "ocean",
                "phonetic": "/ˈəʊʃn/",
                "meaning": "海洋",
                "pos": "n.",
                "unit": "Unit 5"
            },
            {
                "id": "g7a5-20",
                "word": "classic",
                "phonetic": "/ˈklæsɪk/",
                "meaning": "adj. 经典的 / n. （书、电影或歌曲的）经典作品",
                "pos": "adj. & n.",
                "unit": "Unit 5"
            },
            {
                "id": "g7a5-21",
                "word": "return",
                "phonetic": "/rɪˈtɜːn/",
                "meaning": "回来",
                "pos": "v.",
                "unit": "Unit 5"
            },
            {
                "id": "g7a5-22",
                "word": "common",
                "phonetic": "/ˈkɒmən/",
                "meaning": "共同的；常见的",
                "pos": "adj.",
                "unit": "Unit 5"
            },
            {
                "id": "g7a5-23",
                "word": "generation",
                "phonetic": "/ˌdʒenəˈreɪʃn/",
                "meaning": "代；一代人",
                "pos": "n.",
                "unit": "Unit 5"
            },
            {
                "id": "g7a5-24",
                "word": "hero",
                "phonetic": "/ˈhɪərəʊ/",
                "meaning": "男主人公；英雄",
                "pos": "n.",
                "unit": "Unit 5"
            },
            {
                "id": "g7a5-25",
                "word": "fight",
                "phonetic": "/faɪt/",
                "meaning": "打斗；战斗",
                "pos": "v.",
                "unit": "Unit 5",
                "irregular_forms": {
                    "past": "fought",
                    "pp": "fought"
                }
            },
            {
                "id": "g7a5-26",
                "word": "silly",
                "phonetic": "/ˈsɪli/",
                "meaning": "愚蠢的；不明事理的",
                "pos": "adj.",
                "unit": "Unit 5"
            },
            {
                "id": "g7a5-27",
                "word": "fox",
                "phonetic": "/fɒks/",
                "meaning": "狐狸",
                "pos": "n.",
                "unit": "Unit 5"
            },
            {
                "id": "g7a5-28",
                "word": "imagination",
                "phonetic": "/ɪˌmædʒɪˈneɪʃn/",
                "meaning": "想象；想象力",
                "pos": "n.",
                "unit": "Unit 5"
            },
            {
                "id": "g7a5-29",
                "word": "meaningful",
                "phonetic": "/ˈmiːnɪŋfl/",
                "meaning": "有意义的",
                "pos": "adj.",
                "unit": "Unit 5"
            },
            {
                "id": "g7a5-30",
                "word": "form",
                "phonetic": "/fɔːm/",
                "meaning": "形式；类型",
                "pos": "n.",
                "unit": "Unit 5"
            },
            {
                "id": "g7a5-31",
                "word": "ink",
                "phonetic": "/ɪŋk/",
                "meaning": "墨水",
                "pos": "n.",
                "unit": "Unit 5"
            },
            {
                "id": "g7a5-32",
                "word": "painting",
                "phonetic": "/ˈpeɪntɪŋ/",
                "meaning": "绘画",
                "pos": "n.",
                "unit": "Unit 5"
            },
            {
                "id": "g7a5-33",
                "word": "make-up",
                "phonetic": "/ˈmeɪkʌp/",
                "meaning": "化妆品",
                "pos": "n.",
                "unit": "Unit 5"
            },
            {
                "id": "g7a5-34",
                "word": "pretty",
                "phonetic": "/ˈprɪti/",
                "meaning": "漂亮的",
                "pos": "adj.",
                "unit": "Unit 5"
            },
            {
                "id": "g7a5-35",
                "word": "custom",
                "phonetic": "/ˈkʌstəm/",
                "meaning": "习俗",
                "pos": "n.",
                "unit": "Unit 5"
            },
            {
                "id": "g7a5-36",
                "word": "rich",
                "phonetic": "/rɪtʃ/",
                "meaning": "丰富的",
                "pos": "adj.",
                "unit": "Unit 5"
            },
            {
                "id": "g7a5-37",
                "word": "whole",
                "phonetic": "/həʊl/",
                "meaning": "完全的",
                "pos": "adj.",
                "unit": "Unit 5"
            },
            {
                "id": "g7a5-38",
                "word": "magic",
                "phonetic": "/ˈmædʒɪk/",
                "meaning": "魔法",
                "pos": "n.",
                "unit": "Unit 5"
            },
            {
                "id": "g7a5-39",
                "word": "special effects",
                "phonetic": "",
                "meaning": "（电影或电视节目的）特技效果",
                "pos": "phr.",
                "unit": "Unit 5"
            },
            {
                "id": "g7a5-40",
                "word": "recommend",
                "phonetic": "/ˌrekəˈmend/",
                "meaning": "推荐；建议",
                "pos": "v.",
                "unit": "Unit 5"
            }
        ]
    },
    {
        "id": "sys-7a-u6",
        "name": "七年级上册 Unit 6",
        "grade": "初中",
        "description": "上海版七年级上册 Unit 6 英语词汇（上海教育出版社·五四学制）",
        "created_at": "2024-01-01",
        "words": [
            {
                "id": "g7a6-1",
                "word": "metre (AmE meter)",
                "phonetic": "/ˈmiːtə(r)/",
                "meaning": "米",
                "pos": "n.",
                "unit": "Unit 6"
            },
            {
                "id": "g7a6-2",
                "word": "locate",
                "phonetic": "/ləʊˈkeɪt/",
                "meaning": "确定……的准确地点",
                "pos": "v.",
                "unit": "Unit 6"
            },
            {
                "id": "g7a6-3",
                "word": "total",
                "phonetic": "/ˈtəʊtl/",
                "meaning": "总的",
                "pos": "adj.",
                "unit": "Unit 6"
            },
            {
                "id": "g7a6-4",
                "word": "length",
                "phonetic": "/leŋθ/",
                "meaning": "长度",
                "pos": "n.",
                "unit": "Unit 6"
            },
            {
                "id": "g7a6-5",
                "word": "height",
                "phonetic": "/haɪt/",
                "meaning": "高度",
                "pos": "n.",
                "unit": "Unit 6"
            },
            {
                "id": "g7a6-6",
                "word": "influence",
                "phonetic": "/ˈɪnfluəns/",
                "meaning": "影响",
                "pos": "n.",
                "unit": "Unit 6"
            },
            {
                "id": "g7a6-7",
                "word": "poster",
                "phonetic": "/ˈpəʊstə(r)/",
                "meaning": "海报",
                "pos": "n.",
                "unit": "Unit 6"
            },
            {
                "id": "g7a6-8",
                "word": "breathe",
                "phonetic": "/briːð/",
                "meaning": "呼吸",
                "pos": "v.",
                "unit": "Unit 6"
            },
            {
                "id": "g7a6-9",
                "word": "frozen",
                "phonetic": "/ˈfrəʊzn/",
                "meaning": "冰冻的",
                "pos": "adj.",
                "unit": "Unit 6"
            },
            {
                "id": "g7a6-10",
                "word": "adventure",
                "phonetic": "/ədˈventʃə(r)/",
                "meaning": "冒险",
                "pos": "n.",
                "unit": "Unit 6"
            },
            {
                "id": "g7a6-11",
                "word": "woods",
                "phonetic": "/wʊdz/",
                "meaning": "树林",
                "pos": "n.",
                "unit": "Unit 6"
            },
            {
                "id": "g7a6-12",
                "word": "promise",
                "phonetic": "/ˈprɒmɪs/",
                "meaning": "v. 承诺 / n. 诺言",
                "pos": "v. & n.",
                "unit": "Unit 6"
            },
            {
                "id": "g7a6-13",
                "word": "blood",
                "phonetic": "/blʌd/",
                "meaning": "血；血液",
                "pos": "n.",
                "unit": "Unit 6"
            },
            {
                "id": "g7a6-14",
                "word": "lifeblood",
                "phonetic": "/ˈlaɪfblʌd/",
                "meaning": "生命线",
                "pos": "n.",
                "unit": "Unit 6"
            },
            {
                "id": "g7a6-15",
                "word": "have ... in common",
                "phonetic": "",
                "meaning": "有相同的特征",
                "pos": "phr.",
                "unit": "Unit 6"
            },
            {
                "id": "g7a6-16",
                "word": "interest",
                "phonetic": "/ˈɪntrəst/",
                "meaning": "趣味；兴趣",
                "pos": "n.",
                "unit": "Unit 6"
            },
            {
                "id": "g7a6-17",
                "word": "tower",
                "phonetic": "/ˈtaʊə(r)/",
                "meaning": "塔",
                "pos": "n.",
                "unit": "Unit 6"
            },
            {
                "id": "g7a6-18",
                "word": "tourist",
                "phonetic": "/ˈtʊərɪst/",
                "meaning": "旅行者",
                "pos": "n.",
                "unit": "Unit 6"
            },
            {
                "id": "g7a6-19",
                "word": "attraction",
                "phonetic": "/əˈtrækʃən/",
                "meaning": "向往的地方",
                "pos": "n.",
                "unit": "Unit 6"
            },
            {
                "id": "g7a6-20",
                "word": "both",
                "phonetic": "/bəʊθ/",
                "meaning": "（与复数名词连用）两个，两个都",
                "pos": "det. & pron.",
                "unit": "Unit 6"
            },
            {
                "id": "g7a6-21",
                "word": "flow",
                "phonetic": "/fləʊ/",
                "meaning": "流；流动",
                "pos": "v.",
                "unit": "Unit 6"
            },
            {
                "id": "g7a6-22",
                "word": "leading",
                "phonetic": "/ˈliːdɪŋ/",
                "meaning": "最重要的",
                "pos": "adj.",
                "unit": "Unit 6"
            },
            {
                "id": "g7a6-23",
                "word": "port",
                "phonetic": "/pɔːt/",
                "meaning": "港口",
                "pos": "n.",
                "unit": "Unit 6"
            },
            {
                "id": "g7a6-24",
                "word": "environment",
                "phonetic": "/ɪnˈvaɪrənmənt/",
                "meaning": "环境",
                "pos": "n.",
                "unit": "Unit 6"
            },
            {
                "id": "g7a6-25",
                "word": "provide",
                "phonetic": "/prəˈvaɪd/",
                "meaning": "提供；供应",
                "pos": "v.",
                "unit": "Unit 6"
            },
            {
                "id": "g7a6-26",
                "word": "riverside",
                "phonetic": "/ˈrɪvəsaɪd/",
                "meaning": "河畔；河岸",
                "pos": "n.",
                "unit": "Unit 6"
            },
            {
                "id": "g7a6-27",
                "word": "almost",
                "phonetic": "/ˈɔːlməʊst/",
                "meaning": "几乎",
                "pos": "adv.",
                "unit": "Unit 6"
            },
            {
                "id": "g7a6-28",
                "word": "along",
                "phonetic": "/əˈlɒŋ/",
                "meaning": "沿着；顺着",
                "pos": "prep.",
                "unit": "Unit 6"
            },
            {
                "id": "g7a6-29",
                "word": "bank",
                "phonetic": "/bæŋk/",
                "meaning": "岸",
                "pos": "n.",
                "unit": "Unit 6"
            },
            {
                "id": "g7a6-30",
                "word": "waterfall",
                "phonetic": "/ˈwɔːtəfɔːl/",
                "meaning": "瀑布",
                "pos": "n.",
                "unit": "Unit 6"
            },
            {
                "id": "g7a6-31",
                "word": "silver",
                "phonetic": "/ˈsɪlvə(r)/",
                "meaning": "银色的",
                "pos": "adj.",
                "unit": "Unit 6"
            },
            {
                "id": "g7a6-32",
                "word": "belt",
                "phonetic": "/belt/",
                "meaning": "皮带；腰带",
                "pos": "n.",
                "unit": "Unit 6"
            },
            {
                "id": "g7a6-33",
                "word": "glow",
                "phonetic": "/ɡləʊ/",
                "meaning": "发光",
                "pos": "v.",
                "unit": "Unit 6"
            }
        ]
    },
    {
        "id": "sys-8a-u1",
        "name": "八年级上册 Unit 1",
        "grade": "初中",
        "description": "上海版八年级上册 Unit 1 英语词汇（上海教育出版社·五四学制）",
        "created_at": "2024-01-01",
        "words": [
            {
                "id": "g8a1-1",
                "word": "litre (AmE liter)",
                "phonetic": "/ˈliːtə(r)/",
                "meaning": "升",
                "pos": "n.",
                "unit": "Unit 1"
            },
            {
                "id": "g8a1-2",
                "word": "factory",
                "phonetic": "/ˈfæktri/",
                "meaning": "工厂",
                "pos": "n.",
                "unit": "Unit 1"
            },
            {
                "id": "g8a1-3",
                "word": "billion",
                "phonetic": "/ˈbɪljən/",
                "meaning": "十亿",
                "pos": "n.",
                "unit": "Unit 1"
            },
            {
                "id": "g8a1-4",
                "word": "salty",
                "phonetic": "/ˈsɔːlti/",
                "meaning": "含盐的；咸的",
                "pos": "adj.",
                "unit": "Unit 1"
            },
            {
                "id": "g8a1-5",
                "word": "rest",
                "phonetic": "/rest/",
                "meaning": "剩余部分；休息时间",
                "pos": "n.",
                "unit": "Unit 1"
            },
            {
                "id": "g8a1-6",
                "word": "rare",
                "phonetic": "/reə(r)/",
                "meaning": "稀少的；珍贵的",
                "pos": "adj.",
                "unit": "Unit 1"
            },
            {
                "id": "g8a1-7",
                "word": "presentation",
                "phonetic": "/ˌpreznˈteɪʃn/",
                "meaning": "展示会；介绍会",
                "pos": "n.",
                "unit": "Unit 1"
            },
            {
                "id": "g8a1-8",
                "word": "boring",
                "phonetic": "/ˈbɔːrɪŋ/",
                "meaning": "没趣的",
                "pos": "adj.",
                "unit": "Unit 1"
            },
            {
                "id": "g8a1-9",
                "word": "chemical",
                "phonetic": "/ˈkemɪkl/",
                "meaning": "化学品",
                "pos": "n.",
                "unit": "Unit 1"
            },
            {
                "id": "g8a1-10",
                "word": "wastewater",
                "phonetic": "/ˈweɪstwɔːtə(r)/",
                "meaning": "废水",
                "pos": "n.",
                "unit": "Unit 1"
            },
            {
                "id": "g8a1-11",
                "word": "treatment",
                "phonetic": "/ˈtriːtmənt/",
                "meaning": "（净化或防治）处理；加工",
                "pos": "n.",
                "unit": "Unit 1"
            },
            {
                "id": "g8a1-12",
                "word": "include",
                "phonetic": "/ɪnˈkluːd/",
                "meaning": "把……列为…… 的一部分；包括",
                "pos": "v.",
                "unit": "Unit 1"
            },
            {
                "id": "g8a1-13",
                "word": "research",
                "phonetic": "/rɪˈsɜːtʃ/",
                "meaning": "v. 研究；探讨；调查 / n. 研究；调查；探索",
                "pos": "v. & n.",
                "unit": "Unit 1"
            },
            {
                "id": "g8a1-14",
                "word": "agree",
                "phonetic": "/əˈɡriː/",
                "meaning": "同意；赞成",
                "pos": "v.",
                "unit": "Unit 1"
            },
            {
                "id": "g8a1-15",
                "word": "beyond",
                "phonetic": "/bɪˈjɒnd/",
                "meaning": "除……之外",
                "pos": "prep.",
                "unit": "Unit 1"
            },
            {
                "id": "g8a1-16",
                "word": "energy-saving",
                "phonetic": "/ˈenədʒi ˌseɪvɪŋ/",
                "meaning": "节能的",
                "pos": "adj.",
                "unit": "Unit 1"
            },
            {
                "id": "g8a1-17",
                "word": "dishwasher",
                "phonetic": "/ˈdɪʃwɒʃə(r)/",
                "meaning": "洗碗碟机",
                "pos": "n.",
                "unit": "Unit 1"
            },
            {
                "id": "g8a1-18",
                "word": "indirect",
                "phonetic": "/ˌɪndəˈrekt; ˌɪndaɪˈrekt/",
                "meaning": "间接的",
                "pos": "adj.",
                "unit": "Unit 1"
            },
            {
                "id": "g8a1-19",
                "word": "kilo",
                "phonetic": "/ˈkiːləʊ/",
                "meaning": "(= kilogram) 千克；公斤",
                "pos": "n.",
                "unit": "Unit 1"
            },
            {
                "id": "g8a1-20",
                "word": "hamburger",
                "phonetic": "/ˈhæmbɜːɡə(r)/",
                "meaning": "汉堡包",
                "pos": "n.",
                "unit": "Unit 1"
            },
            {
                "id": "g8a1-21",
                "word": "cotton",
                "phonetic": "/ˈkɒtn/",
                "meaning": "棉织物；棉布",
                "pos": "n.",
                "unit": "Unit 1"
            },
            {
                "id": "g8a1-22",
                "word": "touching",
                "phonetic": "/ˈtʌtʃɪŋ/",
                "meaning": "令人同情的；感人的",
                "pos": "adj.",
                "unit": "Unit 1"
            },
            {
                "id": "g8a1-23",
                "word": "desert",
                "phonetic": "/ˈdezət/",
                "meaning": "沙漠",
                "pos": "n.",
                "unit": "Unit 1"
            },
            {
                "id": "g8a1-24",
                "word": "soap",
                "phonetic": "/səʊp/",
                "meaning": "n. 肥皂 / v. 抹肥皂；用肥皂擦洗",
                "pos": "n. & v.",
                "unit": "Unit 1"
            },
            {
                "id": "g8a1-25",
                "word": "corner",
                "phonetic": "/ˈkɔːnə(r)/",
                "meaning": "角",
                "pos": "n.",
                "unit": "Unit 1"
            },
            {
                "id": "g8a1-26",
                "word": "pot",
                "phonetic": "/pɒt/",
                "meaning": "罐；瓶；壶；锅",
                "pos": "n.",
                "unit": "Unit 1"
            },
            {
                "id": "g8a1-27",
                "word": "set off",
                "phonetic": "",
                "meaning": "出发；动身；启程",
                "pos": "phr.",
                "unit": "Unit 1"
            },
            {
                "id": "g8a1-28",
                "word": "hole",
                "phonetic": "/həʊl/",
                "meaning": "洞；坑",
                "pos": "n.",
                "unit": "Unit 1"
            },
            {
                "id": "g8a1-29",
                "word": "step",
                "phonetic": "/step/",
                "meaning": "迈步；踩",
                "pos": "v.",
                "unit": "Unit 1"
            },
            {
                "id": "g8a1-30",
                "word": "mud",
                "phonetic": "/mʌd/",
                "meaning": "泥；淤泥",
                "pos": "n.",
                "unit": "Unit 1"
            },
            {
                "id": "g8a1-31",
                "word": "bathe",
                "phonetic": "/beɪð/",
                "meaning": "用水清洗（尤指身体部位）",
                "pos": "v.",
                "unit": "Unit 1"
            },
            {
                "id": "g8a1-32",
                "word": "shine",
                "phonetic": "/ʃaɪn/",
                "meaning": "照耀",
                "pos": "v.",
                "unit": "Unit 1",
                "irregular_forms": {
                    "past": "shone",
                    "pp": "shone"
                }
            },
            {
                "id": "g8a1-33",
                "word": "forward",
                "phonetic": "/ˈfɔːwəd/",
                "meaning": "向前",
                "pos": "adv.",
                "unit": "Unit 1"
            },
            {
                "id": "g8a1-34",
                "word": "pour",
                "phonetic": "/pɔː(r)/",
                "meaning": "使（液体）连续流出；倒出",
                "pos": "v.",
                "unit": "Unit 1"
            },
            {
                "id": "g8a1-35",
                "word": "shut",
                "phonetic": "/ʃʌt/",
                "meaning": "关闭；合上",
                "pos": "adj. & v.",
                "unit": "Unit 1",
                "irregular_forms": {
                    "past": "shut",
                    "pp": "shut"
                }
            },
            {
                "id": "g8a1-36",
                "word": "drop",
                "phonetic": "/drɒp/",
                "meaning": "滴；水珠",
                "pos": "n.",
                "unit": "Unit 1"
            },
            {
                "id": "g8a1-37",
                "word": "fully",
                "phonetic": "/ˈfʊli/",
                "meaning": "完全地；充分地",
                "pos": "adv.",
                "unit": "Unit 1"
            },
            {
                "id": "g8a1-38",
                "word": "precious",
                "phonetic": "/ˈpreʃəs/",
                "meaning": "宝贵的；珍贵的",
                "pos": "adj.",
                "unit": "Unit 1"
            },
            {
                "id": "g8a1-39",
                "word": "shoulder",
                "phonetic": "/ˈʃəʊldə(r)/",
                "meaning": "n. 肩膀 / v. 背；扛；挑",
                "pos": "n. & v.",
                "unit": "Unit 1"
            },
            {
                "id": "g8a1-40",
                "word": "snake",
                "phonetic": "/sneɪk/",
                "meaning": "n. 蛇 / v. 曲折前行；蛇行；蜿蜒伸展",
                "pos": "n. & v.",
                "unit": "Unit 1"
            },
            {
                "id": "g8a1-41",
                "word": "thirsty",
                "phonetic": "/ˈθɜːsti/",
                "meaning": "口渴的",
                "pos": "adj.",
                "unit": "Unit 1"
            },
            {
                "id": "g8a1-42",
                "word": "nor",
                "phonetic": "/nɔː(r)/",
                "meaning": "也不",
                "pos": "conj.",
                "unit": "Unit 1"
            },
            {
                "id": "g8a1-43",
                "word": "limited",
                "phonetic": "/ˈlɪmɪtɪd/",
                "meaning": "有限的",
                "pos": "adj.",
                "unit": "Unit 1"
            },
            {
                "id": "g8a1-44",
                "word": "spread",
                "phonetic": "/spred/",
                "meaning": "传播",
                "pos": "v.",
                "unit": "Unit 1",
                "irregular_forms": {
                    "past": "spread",
                    "pp": "spread"
                }
            },
            {
                "id": "g8a1-45",
                "word": "awareness",
                "phonetic": "/əˈweənəs/",
                "meaning": "意识",
                "pos": "n.",
                "unit": "Unit 1"
            }
        ]
    },
    {
        "id": "sys-8a-u2",
        "name": "八年级上册 Unit 2",
        "grade": "初中",
        "description": "上海版八年级上册 Unit 2 英语词汇（上海教育出版社·五四学制）",
        "created_at": "2024-01-01",
        "words": [
            {
                "id": "g8a2-1",
                "word": "digital",
                "phonetic": "/ˈdɪdʒɪtl/",
                "meaning": "数码的；数字式的",
                "pos": "adj.",
                "unit": "Unit 2"
            },
            {
                "id": "g8a2-2",
                "word": "support",
                "phonetic": "/səˈpɔːt/",
                "meaning": "技术支持；支持；帮助",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g8a2-3",
                "word": "laptop",
                "phonetic": "/ˈlæptɒp/",
                "meaning": "便携式电脑；笔记本电脑",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g8a2-4",
                "word": "keyboard",
                "phonetic": "/ˈkiːbɔːd/",
                "meaning": "（计算机或打字机的）键盘",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g8a2-5",
                "word": "bluetooth",
                "phonetic": "/ˈbluːtuːθ/",
                "meaning": "蓝牙（用于手机、计算机等电子设备的短距离无线连接技术）",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g8a2-6",
                "word": "smartphone",
                "phonetic": "/ˈsmɑːtfəʊn/",
                "meaning": "智能手机",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g8a2-7",
                "word": "headset",
                "phonetic": "/ˈhedset/",
                "meaning": "（尤指带麦克风的）头戴式受话器，耳机",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g8a2-8",
                "word": "large",
                "phonetic": "/lɑːdʒ/",
                "meaning": "大的；大规模的；大量的",
                "pos": "adj.",
                "unit": "Unit 2"
            },
            {
                "id": "g8a2-9",
                "word": "clear",
                "phonetic": "/klɪə(r)/",
                "meaning": "adj. 听得清的；清楚的；明白的 / v. 移走，清除（不需要的东西）",
                "pos": "adj. & v.",
                "unit": "Unit 2"
            },
            {
                "id": "g8a2-10",
                "word": "private",
                "phonetic": "/ˈpraɪvət/",
                "meaning": "私人的；个人的",
                "pos": "adj.",
                "unit": "Unit 2"
            },
            {
                "id": "g8a2-11",
                "word": "touch",
                "phonetic": "/tʌtʃ/",
                "meaning": "n. 触摸；触觉 / v. 触摸；碰",
                "pos": "n. & v.",
                "unit": "Unit 2"
            },
            {
                "id": "g8a2-12",
                "word": "touch screen",
                "phonetic": "/ˈtʌtʃ skriːn/",
                "meaning": "（计算机）触摸屏",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g8a2-13",
                "word": "advantage",
                "phonetic": "/ədˈvɑːntɪdʒ/",
                "meaning": "优点；优势",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g8a2-14",
                "word": "chip",
                "phonetic": "/tʃɪp/",
                "meaning": "芯片",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g8a2-15",
                "word": "lightning",
                "phonetic": "/ˈlaɪtnɪŋ/",
                "meaning": "adj. 闪电般的；飞快的 / n. 闪电",
                "pos": "adj. & n.",
                "unit": "Unit 2"
            },
            {
                "id": "g8a2-16",
                "word": "purple",
                "phonetic": "/ˈpɜːpl/",
                "meaning": "紫色的",
                "pos": "adj.",
                "unit": "Unit 2"
            },
            {
                "id": "g8a2-17",
                "word": "AI",
                "phonetic": "",
                "meaning": "(= artificial intelligence) 人工智能",
                "pos": "abbr.",
                "unit": "Unit 2"
            },
            {
                "id": "g8a2-18",
                "word": "keep an eye on",
                "phonetic": "",
                "meaning": "照看；留神；留意",
                "pos": "phr.",
                "unit": "Unit 2"
            },
            {
                "id": "g8a2-19",
                "word": "health",
                "phonetic": "/helθ/",
                "meaning": "人的身体（或精神）状况；健康",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g8a2-20",
                "word": "complaint",
                "phonetic": "/kəmˈpleɪnt/",
                "meaning": "投诉；抱怨",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g8a2-21",
                "word": "press",
                "phonetic": "/pres/",
                "meaning": "按，压（使启动）",
                "pos": "v.",
                "unit": "Unit 2"
            },
            {
                "id": "g8a2-22",
                "word": "inconvenience",
                "phonetic": "/ˌɪnkənˈviːniəns/",
                "meaning": "不便；麻烦；困难",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g8a2-23",
                "word": "repeat",
                "phonetic": "/rɪˈpiːt/",
                "meaning": "重复；重做；重说",
                "pos": "v.",
                "unit": "Unit 2"
            },
            {
                "id": "g8a2-24",
                "word": "couple",
                "phonetic": "/ˈkʌpl/",
                "meaning": "几个人；几件事物",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g8a2-25",
                "word": "freeze",
                "phonetic": "/friːz/",
                "meaning": "（屏幕）冻结",
                "pos": "v.",
                "unit": "Unit 2",
                "irregular_forms": {
                    "past": "froze",
                    "pp": "frozen"
                }
            },
            {
                "id": "g8a2-26",
                "word": "software",
                "phonetic": "/ˈsɒftweə(r)/",
                "meaning": "软件",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g8a2-27",
                "word": "app",
                "phonetic": "/æp/",
                "meaning": "(= application) 应用程序；应用软件",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g8a2-28",
                "word": "network",
                "phonetic": "/ˈnetwɜːk/",
                "meaning": "（互联）网络",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g8a2-29",
                "word": "disabled",
                "phonetic": "/dɪsˈeɪbld/",
                "meaning": "有残疾的",
                "pos": "adj.",
                "unit": "Unit 2"
            },
            {
                "id": "g8a2-30",
                "word": "type",
                "phonetic": "/taɪp/",
                "meaning": "类型；种类",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g8a2-31",
                "word": "blind",
                "phonetic": "/blaɪnd/",
                "meaning": "瞎的；失明的",
                "pos": "adj.",
                "unit": "Unit 2"
            },
            {
                "id": "g8a2-32",
                "word": "detect",
                "phonetic": "/dɪˈtekt/",
                "meaning": "发现；查明；侦察出",
                "pos": "v.",
                "unit": "Unit 2"
            },
            {
                "id": "g8a2-33",
                "word": "object",
                "phonetic": "/ˈɒbdʒɪkt/",
                "meaning": "物体；东西",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g8a2-34",
                "word": "as soon as",
                "phonetic": "",
                "meaning": "一……就……",
                "pos": "phr.",
                "unit": "Unit 2"
            },
            {
                "id": "g8a2-35",
                "word": "warn",
                "phonetic": "/wɔːn/",
                "meaning": "提醒注意（可能发生的事）；使警惕",
                "pos": "v.",
                "unit": "Unit 2"
            },
            {
                "id": "g8a2-36",
                "word": "direction",
                "phonetic": "/dəˈrekʃn; daɪˈrekʃn/",
                "meaning": "方向；用法说明（常为复数）",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g8a2-37",
                "word": "inform",
                "phonetic": "/ɪnˈfɔːm/",
                "meaning": "知会；通知",
                "pos": "v.",
                "unit": "Unit 2"
            },
            {
                "id": "g8a2-38",
                "word": "report",
                "phonetic": "/rɪˈpɔːt/",
                "meaning": "调查报告；报告",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g8a2-39",
                "word": "population",
                "phonetic": "/ˌpɒpjuˈleɪʃn/",
                "meaning": "（地区、国家等的）人口，人口数量",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g8a2-40",
                "word": "rural",
                "phonetic": "/ˈrʊərəl/",
                "meaning": "乡村的；农村的",
                "pos": "adj.",
                "unit": "Unit 2"
            },
            {
                "id": "g8a2-41",
                "word": "connection",
                "phonetic": "/kəˈnekʃn/",
                "meaning": "连接",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g8a2-42",
                "word": "firefighting",
                "phonetic": "/ˈfaɪəfaɪtɪŋ/",
                "meaning": "灭火；消防",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g8a2-43",
                "word": "send",
                "phonetic": "/send/",
                "meaning": "发送",
                "pos": "v.",
                "unit": "Unit 2",
                "irregular_forms": {
                    "past": "sent",
                    "pp": "sent"
                }
            },
            {
                "id": "g8a2-44",
                "word": "unit",
                "phonetic": "/ˈjuːnɪt/",
                "meaning": "装置；机件",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g8a2-45",
                "word": "opinion",
                "phonetic": "/əˈpɪnjən/",
                "meaning": "意见；看法",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g8a2-46",
                "word": "in my opinion",
                "phonetic": "",
                "meaning": "依我看",
                "pos": "phr.",
                "unit": "Unit 2"
            },
            {
                "id": "g8a2-47",
                "word": "aware",
                "phonetic": "/əˈweə(r)/",
                "meaning": "意识到；明白",
                "pos": "adj.",
                "unit": "Unit 2"
            },
            {
                "id": "g8a2-48",
                "word": "be aware of",
                "phonetic": "",
                "meaning": "知道；意识到；明白",
                "pos": "phr.",
                "unit": "Unit 2"
            },
            {
                "id": "g8a2-49",
                "word": "disadvantage",
                "phonetic": "/ˌdɪsədˈvɑːntɪdʒ/",
                "meaning": "不利因素",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g8a2-50",
                "word": "hide",
                "phonetic": "/haɪd/",
                "meaning": "藏；隐蔽",
                "pos": "v.",
                "unit": "Unit 2",
                "irregular_forms": {
                    "past": "hid",
                    "pp": "hidden"
                }
            },
            {
                "id": "g8a2-51",
                "word": "hidden",
                "phonetic": "/ˈhɪdn/",
                "meaning": "隐藏的",
                "pos": "adj.",
                "unit": "Unit 2"
            },
            {
                "id": "g8a2-52",
                "word": "virus",
                "phonetic": "/ˈvaɪrəs/",
                "meaning": "病毒",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g8a2-53",
                "word": "conclusion",
                "phonetic": "/kənˈkluːʒn/",
                "meaning": "结束；结尾；结论",
                "pos": "n.",
                "unit": "Unit 2"
            },
            {
                "id": "g8a2-54",
                "word": "in conclusion",
                "phonetic": "",
                "meaning": "最后",
                "pos": "phr.",
                "unit": "Unit 2"
            },
            {
                "id": "g8a2-55",
                "word": "benefit",
                "phonetic": "/ˈbenɪfɪt/",
                "meaning": "优势；益处；成效",
                "pos": "n.",
                "unit": "Unit 2"
            }
        ]
    },
    {
        "id": "sys-8a-u3",
        "name": "八年级上册 Unit 3",
        "grade": "初中",
        "description": "上海版八年级上册 Unit 3 英语词汇（上海教育出版社·五四学制）",
        "created_at": "2024-01-01",
        "words": [
            {
                "id": "g8a3-1",
                "word": "inborn",
                "phonetic": "/ˌɪnˈbɔːn/",
                "meaning": "天生的",
                "pos": "adj.",
                "unit": "Unit 3"
            },
            {
                "id": "g8a3-2",
                "word": "unfamiliar",
                "phonetic": "/ˌʌnfəˈmɪliə(r)/",
                "meaning": "陌生的；不熟悉的",
                "pos": "adj.",
                "unit": "Unit 3"
            },
            {
                "id": "g8a3-3",
                "word": "grown-up",
                "phonetic": "/ˌɡrəʊn ˈʌp/",
                "meaning": "（尤指用于对儿童说话时）大人",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g8a3-4",
                "word": "continuous",
                "phonetic": "/kənˈtɪnjuəs/",
                "meaning": "不断的；持续的；连续的",
                "pos": "adj.",
                "unit": "Unit 3"
            },
            {
                "id": "g8a3-5",
                "word": "either",
                "phonetic": "/ˈaɪðə(r)/",
                "meaning": "（用于否定词组后）也",
                "pos": "adv.",
                "unit": "Unit 3"
            },
            {
                "id": "g8a3-6",
                "word": "ruin",
                "phonetic": "/ˈruːɪn/",
                "meaning": "毁坏；破坏",
                "pos": "v.",
                "unit": "Unit 3"
            },
            {
                "id": "g8a3-7",
                "word": "eyesight",
                "phonetic": "/ˈaɪsaɪt/",
                "meaning": "视力",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g8a3-8",
                "word": "fantastic",
                "phonetic": "/fænˈtæstɪk/",
                "meaning": "极好的；了不起的",
                "pos": "adj.",
                "unit": "Unit 3"
            },
            {
                "id": "g8a3-9",
                "word": "ant",
                "phonetic": "/ænt/",
                "meaning": "蚂蚁",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g8a3-10",
                "word": "surprising",
                "phonetic": "/səˈpraɪzɪŋ/",
                "meaning": "令人吃惊的",
                "pos": "adj.",
                "unit": "Unit 3"
            },
            {
                "id": "g8a3-11",
                "word": "awake",
                "phonetic": "/əˈweɪk/",
                "meaning": "醒着（尤指入睡前或刚醒时）",
                "pos": "adj.",
                "unit": "Unit 3",
                "irregular_forms": {
                    "past": "awoke",
                    "pp": "awoken"
                }
            },
            {
                "id": "g8a3-12",
                "word": "eagle",
                "phonetic": "/ˈiːɡl/",
                "meaning": "雕",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g8a3-13",
                "word": "cartoon",
                "phonetic": "/kɑːˈtuːn/",
                "meaning": "动画片；卡通片",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g8a3-14",
                "word": "movie",
                "phonetic": "/ˈmuːvi/",
                "meaning": "（美）电影",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g8a3-15",
                "word": "never-ending",
                "phonetic": "/ˌnevər ˈendɪŋ/",
                "meaning": "永无止境的；没完没了的",
                "pos": "adj.",
                "unit": "Unit 3"
            },
            {
                "id": "g8a3-16",
                "word": "annoying",
                "phonetic": "/əˈnɔɪɪŋ/",
                "meaning": "恼人的；讨厌的",
                "pos": "adj.",
                "unit": "Unit 3"
            },
            {
                "id": "g8a3-17",
                "word": "brain",
                "phonetic": "/breɪn/",
                "meaning": "脑；脑力",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g8a3-18",
                "word": "researcher",
                "phonetic": "/rɪˈsɜːtʃə(r)/",
                "meaning": "研究者",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g8a3-19",
                "word": "rate",
                "phonetic": "/reɪt/",
                "meaning": "划分等级；评估",
                "pos": "v.",
                "unit": "Unit 3"
            },
            {
                "id": "g8a3-20",
                "word": "result",
                "phonetic": "/rɪˈzʌlt/",
                "meaning": "结果",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g8a3-21",
                "word": "magician",
                "phonetic": "/məˈdʒɪʃn/",
                "meaning": "魔术师；变戏法的人",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g8a3-22",
                "word": "recent",
                "phonetic": "/ˈriːsnt/",
                "meaning": "近来的；新近的",
                "pos": "adj.",
                "unit": "Unit 3"
            },
            {
                "id": "g8a3-23",
                "word": "trick",
                "phonetic": "/trɪk/",
                "meaning": "戏法；把戏",
                "pos": "n.",
                "unit": "Unit 3"
            },
            {
                "id": "g8a3-24",
                "word": "voluntary",
                "phonetic": "/ˈvɒləntri/",
                "meaning": "自愿的；主动的；志愿的",
                "pos": "adj.",
                "unit": "Unit 3"
            },
            {
                "id": "g8a3-25",
                "word": "crazy",
                "phonetic": "/ˈkreɪzi/",
                "meaning": "热衷的；狂热的",
                "pos": "adj.",
                "unit": "Unit 3"
            },
            {
                "id": "g8a3-26",
                "word": "therefore",
                "phonetic": "/ˈðeəfɔː(r)/",
                "meaning": "因此",
                "pos": "adv.",
                "unit": "Unit 3"
            },
            {
                "id": "g8a3-27",
                "word": "wonder",
                "phonetic": "/ˈwʌndə(r)/",
                "meaning": "想知道；想弄明白；琢磨",
                "pos": "v.",
                "unit": "Unit 3"
            },
            {
                "id": "g8a3-28",
                "word": "shake",
                "phonetic": "/ʃeɪk/",
                "meaning": "摇动；抖动",
                "pos": "v.",
                "unit": "Unit 3",
                "irregular_forms": {
                    "past": "shook",
                    "pp": "shaken"
                }
            },
            {
                "id": "g8a3-29",
                "word": "bark",
                "phonetic": "/bɑːk/",
                "meaning": "（狗）吠叫",
                "pos": "v.",
                "unit": "Unit 3"
            }
        ]
    },
    {
        "id": "sys-8a-u4",
        "name": "八年级上册 Unit 4",
        "grade": "初中",
        "description": "上海版八年级上册 Unit 4 英语词汇（上海教育出版社·五四学制）",
        "created_at": "2024-01-01",
        "words": [
            {
                "id": "g8a4-1",
                "word": "memory",
                "phonetic": "/ˈmeməri/",
                "meaning": "记忆",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g8a4-2",
                "word": "seldom",
                "phonetic": "/ˈseldəm/",
                "meaning": "不常；很少；难得",
                "pos": "adv.",
                "unit": "Unit 4"
            },
            {
                "id": "g8a4-3",
                "word": "journey",
                "phonetic": "/ˈdʒɜːni/",
                "meaning": "旅行",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g8a4-4",
                "word": "nowadays",
                "phonetic": "/ˈnaʊədeɪz/",
                "meaning": "现今；现在；目前",
                "pos": "adv.",
                "unit": "Unit 4"
            },
            {
                "id": "g8a4-5",
                "word": "truck",
                "phonetic": "/trʌk/",
                "meaning": "卡车；货运汽车",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g8a4-6",
                "word": "wide",
                "phonetic": "/waɪd/",
                "meaning": "宽的；宽阔的",
                "pos": "adj.",
                "unit": "Unit 4"
            },
            {
                "id": "g8a4-7",
                "word": "modern",
                "phonetic": "/ˈmɒdn/",
                "meaning": "现代的；近代的",
                "pos": "adj.",
                "unit": "Unit 4"
            },
            {
                "id": "g8a4-8",
                "word": "stay",
                "phonetic": "/steɪ/",
                "meaning": "停留；逗留（时间）",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g8a4-9",
                "word": "tape",
                "phonetic": "/teɪp/",
                "meaning": "磁带；录像带",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g8a4-10",
                "word": "inside",
                "phonetic": "/ˌɪnˈsaɪd/",
                "meaning": "在（或向）…… 内；在（或向）……里",
                "pos": "prep.",
                "unit": "Unit 4"
            },
            {
                "id": "g8a4-11",
                "word": "any more",
                "phonetic": "",
                "meaning": "（常用于否定句和疑问句句末）再也（不），（不）再",
                "pos": "adv.",
                "unit": "Unit 4"
            },
            {
                "id": "g8a4-12",
                "word": "borrow",
                "phonetic": "/ˈbɒrəʊ/",
                "meaning": "借；借用",
                "pos": "v.",
                "unit": "Unit 4"
            },
            {
                "id": "g8a4-13",
                "word": "imagine",
                "phonetic": "/ɪˈmædʒɪn/",
                "meaning": "想象；设想",
                "pos": "v.",
                "unit": "Unit 4"
            },
            {
                "id": "g8a4-14",
                "word": "roll",
                "phonetic": "/rəʊl/",
                "meaning": "卷；卷轴",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g8a4-15",
                "word": "record",
                "phonetic": "/ˈrekɔːd/",
                "meaning": "唱片",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g8a4-16",
                "word": "business",
                "phonetic": "/ˈbɪznəs/",
                "meaning": "公司；商业",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g8a4-17",
                "word": "except",
                "phonetic": "/ɪkˈsept/",
                "meaning": "除……之外",
                "pos": "prep.",
                "unit": "Unit 4"
            },
            {
                "id": "g8a4-18",
                "word": "belong",
                "phonetic": "/bɪˈlɒŋ/",
                "meaning": "应在（某处）",
                "pos": "v.",
                "unit": "Unit 4"
            },
            {
                "id": "g8a4-19",
                "word": "belong to sb",
                "phonetic": "",
                "meaning": "属于某人；归某人所有",
                "pos": "phr.",
                "unit": "Unit 4"
            },
            {
                "id": "g8a4-20",
                "word": "century",
                "phonetic": "/ˈsentʃəri/",
                "meaning": "世纪；百年",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g8a4-21",
                "word": "worst",
                "phonetic": "/wɜːst/",
                "meaning": "最差的；最坏的；最糟的",
                "pos": "adj.",
                "unit": "Unit 4"
            },
            {
                "id": "g8a4-22",
                "word": "industry",
                "phonetic": "/ˈɪndəstri/",
                "meaning": "工业",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g8a4-23",
                "word": "progress",
                "phonetic": "/ˈprəʊɡres/",
                "meaning": "进步；进展",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g8a4-24",
                "word": "ordinary",
                "phonetic": "/ˈɔːdnri/",
                "meaning": "普通的；平凡的",
                "pos": "adj.",
                "unit": "Unit 4"
            },
            {
                "id": "g8a4-25",
                "word": "dramatically",
                "phonetic": "/drəˈmætɪkli/",
                "meaning": "突然地；巨大地；令人吃惊地",
                "pos": "adv.",
                "unit": "Unit 4"
            },
            {
                "id": "g8a4-26",
                "word": "rarely",
                "phonetic": "/ˈreəli/",
                "meaning": "罕有；很少；不常",
                "pos": "adv.",
                "unit": "Unit 4"
            },
            {
                "id": "g8a4-27",
                "word": "decade",
                "phonetic": "/ˈdekeɪd/",
                "meaning": "十年",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g8a4-28",
                "word": "development",
                "phonetic": "/dɪˈveləpmənt/",
                "meaning": "发展；成长；壮大",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g8a4-29",
                "word": "develop",
                "phonetic": "/dɪˈveləp/",
                "meaning": "（使）成长，发展，壮大",
                "pos": "v.",
                "unit": "Unit 4"
            },
            {
                "id": "g8a4-30",
                "word": "condition",
                "phonetic": "/kənˈdɪʃn/",
                "meaning": "状况；状态",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g8a4-31",
                "word": "living conditions",
                "phonetic": "",
                "meaning": "生活条件",
                "pos": "phr.",
                "unit": "Unit 4"
            },
            {
                "id": "g8a4-32",
                "word": "major",
                "phonetic": "/ˈmeɪdʒə(r)/",
                "meaning": "主要的；重要的",
                "pos": "adj.",
                "unit": "Unit 4"
            },
            {
                "id": "g8a4-33",
                "word": "growth",
                "phonetic": "/ɡrəʊθ/",
                "meaning": "增长",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g8a4-34",
                "word": "countryside",
                "phonetic": "/ˈkʌntrisaɪd/",
                "meaning": "乡村；农村",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g8a4-35",
                "word": "although",
                "phonetic": "/ɔːlˈðəʊ/",
                "meaning": "虽然；尽管",
                "pos": "conj.",
                "unit": "Unit 4"
            },
            {
                "id": "g8a4-36",
                "word": "unpleasant",
                "phonetic": "/ʌnˈpleznt/",
                "meaning": "令人不快的；不舒服的",
                "pos": "adj.",
                "unit": "Unit 4"
            },
            {
                "id": "g8a4-37",
                "word": "bath",
                "phonetic": "/bɑːθ/",
                "meaning": "浴缸；洗澡",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g8a4-38",
                "word": "extremely",
                "phonetic": "/ɪkˈstriːmli/",
                "meaning": "极其；非常",
                "pos": "adv.",
                "unit": "Unit 4"
            },
            {
                "id": "g8a4-39",
                "word": "smelly",
                "phonetic": "/ˈsmeli/",
                "meaning": "有难闻气味的；有臭味的",
                "pos": "adj.",
                "unit": "Unit 4"
            },
            {
                "id": "g8a4-40",
                "word": "wealthy",
                "phonetic": "/ˈwelθi/",
                "meaning": "富有的；富裕的",
                "pos": "adj.",
                "unit": "Unit 4"
            },
            {
                "id": "g8a4-41",
                "word": "education",
                "phonetic": "/ˌedʒuˈkeɪʃn/",
                "meaning": "教育",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g8a4-42",
                "word": "foreign",
                "phonetic": "/ˈfɒrən/",
                "meaning": "外国的",
                "pos": "adj.",
                "unit": "Unit 4"
            },
            {
                "id": "g8a4-43",
                "word": "mine",
                "phonetic": "/maɪn/",
                "meaning": "矿井；矿",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g8a4-44",
                "word": "result in",
                "phonetic": "",
                "meaning": "造成；导致",
                "pos": "phr.",
                "unit": "Unit 4"
            },
            {
                "id": "g8a4-45",
                "word": "severe",
                "phonetic": "/sɪˈvɪə(r)/",
                "meaning": "极为恶劣的；十分严重的",
                "pos": "adj.",
                "unit": "Unit 4"
            },
            {
                "id": "g8a4-46",
                "word": "punish",
                "phonetic": "/ˈpʌnɪʃ/",
                "meaning": "处罚；惩罚",
                "pos": "v.",
                "unit": "Unit 4"
            },
            {
                "id": "g8a4-47",
                "word": "punishment",
                "phonetic": "/ˈpʌnɪʃmənt/",
                "meaning": "惩罚；处罚",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g8a4-48",
                "word": "burn",
                "phonetic": "/bɜːn/",
                "meaning": "燃烧；烧",
                "pos": "v.",
                "unit": "Unit 4",
                "irregular_forms": {
                    "past": "burnt/burned",
                    "pp": "burnt/burned"
                }
            },
            {
                "id": "g8a4-49",
                "word": "heater",
                "phonetic": "/ˈhiːtə(r)/",
                "meaning": "加热器；炉子；热水器",
                "pos": "n.",
                "unit": "Unit 4"
            },
            {
                "id": "g8a4-50",
                "word": "housework",
                "phonetic": "/ˈhaʊswɜːk/",
                "meaning": "家务劳动；家务事",
                "pos": "n.",
                "unit": "Unit 4"
            }
        ]
    },
    {
        "id": "sys-8a-u5",
        "name": "八年级上册 Unit 5",
        "grade": "初中",
        "description": "上海版八年级上册 Unit 5 英语词汇（上海教育出版社·五四学制）",
        "created_at": "2024-01-01",
        "words": [
            {
                "id": "g8a5-1",
                "word": "teamwork",
                "phonetic": "/ˈtiːmwɜːk/",
                "meaning": "协同工作；配合",
                "pos": "n.",
                "unit": "Unit 5"
            },
            {
                "id": "g8a5-2",
                "word": "band",
                "phonetic": "/bænd/",
                "meaning": "流行音乐乐队",
                "pos": "n.",
                "unit": "Unit 5"
            },
            {
                "id": "g8a5-3",
                "word": "DJ",
                "phonetic": "",
                "meaning": "(= disc jockey) （电台、电视台、俱乐部）唱片节目主持人",
                "pos": "n.",
                "unit": "Unit 5"
            },
            {
                "id": "g8a5-4",
                "word": "lead",
                "phonetic": "/liːd/",
                "meaning": "（戏剧、电影等中的）主角；（竞赛中的）领先地位",
                "pos": "n.",
                "unit": "Unit 5",
                "irregular_forms": {
                    "past": "led",
                    "pp": "led"
                }
            },
            {
                "id": "g8a5-5",
                "word": "conversation",
                "phonetic": "/ˌkɒnvəˈseɪʃn/",
                "meaning": "（非正式）交谈，谈话",
                "pos": "n.",
                "unit": "Unit 5"
            },
            {
                "id": "g8a5-6",
                "word": "secret",
                "phonetic": "/ˈsiːkrət/",
                "meaning": "秘密；机密",
                "pos": "n.",
                "unit": "Unit 5"
            },
            {
                "id": "g8a5-7",
                "word": "passion",
                "phonetic": "/ˈpæʃn/",
                "meaning": "酷爱；热衷的爱好（或活动等）",
                "pos": "n.",
                "unit": "Unit 5"
            },
            {
                "id": "g8a5-8",
                "word": "off-stage",
                "phonetic": "/ˌɒf ˈsteɪdʒ/",
                "meaning": "adj. 舞台外的；幕后的 / adv. 在舞台外；在幕后",
                "pos": "adj. & adv.",
                "unit": "Unit 5"
            },
            {
                "id": "g8a5-9",
                "word": "guest",
                "phonetic": "/ɡest/",
                "meaning": "客人；宾客",
                "pos": "n.",
                "unit": "Unit 5"
            },
            {
                "id": "g8a5-10",
                "word": "hold",
                "phonetic": "/həʊld/",
                "meaning": "使保持（在某位置）",
                "pos": "v.",
                "unit": "Unit 5",
                "irregular_forms": {
                    "past": "held",
                    "pp": "held"
                }
            },
            {
                "id": "g8a5-11",
                "word": "nation",
                "phonetic": "/ˈneɪʃn/",
                "meaning": "国家；民族",
                "pos": "n.",
                "unit": "Unit 5"
            },
            {
                "id": "g8a5-12",
                "word": "IT",
                "phonetic": "",
                "meaning": "(= information technology) 信息技术",
                "pos": "n.",
                "unit": "Unit 5"
            },
            {
                "id": "g8a5-13",
                "word": "VIP",
                "phonetic": "",
                "meaning": "(= Very Important Person) 要人；贵宾",
                "pos": "n.",
                "unit": "Unit 5"
            },
            {
                "id": "g8a5-14",
                "word": "ASAP",
                "phonetic": "",
                "meaning": "(= as soon as possible) 尽快",
                "pos": "abbr.",
                "unit": "Unit 5"
            },
            {
                "id": "g8a5-15",
                "word": "meeting",
                "phonetic": "/ˈmiːtɪŋ/",
                "meaning": "会议",
                "pos": "n.",
                "unit": "Unit 5"
            },
            {
                "id": "g8a5-16",
                "word": "complain",
                "phonetic": "/kəmˈpleɪn/",
                "meaning": "抱怨；投诉",
                "pos": "v.",
                "unit": "Unit 5"
            },
            {
                "id": "g8a5-17",
                "word": "task",
                "phonetic": "/tɑːsk/",
                "meaning": "任务；工作",
                "pos": "n.",
                "unit": "Unit 5"
            },
            {
                "id": "g8a5-18",
                "word": "pity",
                "phonetic": "/ˈpɪti/",
                "meaning": "（用于表示失望）遗憾，可惜",
                "pos": "n.",
                "unit": "Unit 5"
            },
            {
                "id": "g8a5-19",
                "word": "shame",
                "phonetic": "/ʃeɪm/",
                "meaning": "令人惋惜的事；让人遗憾的事",
                "pos": "n.",
                "unit": "Unit 5"
            },
            {
                "id": "g8a5-20",
                "word": "discussion",
                "phonetic": "/dɪˈskʌʃn/",
                "meaning": "讨论；商讨",
                "pos": "n.",
                "unit": "Unit 5"
            },
            {
                "id": "g8a5-21",
                "word": "cooperate",
                "phonetic": "/kəʊˈɒpəreɪt/",
                "meaning": "合作；协作",
                "pos": "v.",
                "unit": "Unit 5"
            },
            {
                "id": "g8a5-22",
                "word": "success",
                "phonetic": "/səkˈses/",
                "meaning": "成功；胜利",
                "pos": "n.",
                "unit": "Unit 5"
            },
            {
                "id": "g8a5-23",
                "word": "wonderland",
                "phonetic": "/ˈwʌndəlænd/",
                "meaning": "（童话中的）仙境，奇境",
                "pos": "n.",
                "unit": "Unit 5"
            },
            {
                "id": "g8a5-24",
                "word": "eagerly",
                "phonetic": "/ˈiːɡəli/",
                "meaning": "渴望地；热切地",
                "pos": "adv.",
                "unit": "Unit 5"
            },
            {
                "id": "g8a5-25",
                "word": "disappoint",
                "phonetic": "/ˌdɪsəˈpɔɪnt/",
                "meaning": "使失望",
                "pos": "v.",
                "unit": "Unit 5"
            },
            {
                "id": "g8a5-26",
                "word": "disappointed",
                "phonetic": "/ˌdɪsəˈpɔɪntɪd/",
                "meaning": "失望的；沮丧的",
                "pos": "adj.",
                "unit": "Unit 5"
            },
            {
                "id": "g8a5-27",
                "word": "backstage",
                "phonetic": "/ˌbækˈsteɪdʒ/",
                "meaning": "adv. 在后台 / adj. 后台的",
                "pos": "adv. & adj.",
                "unit": "Unit 5"
            },
            {
                "id": "g8a5-28",
                "word": "enjoyable",
                "phonetic": "/ɪnˈdʒɔɪəbl/",
                "meaning": "有乐趣的；令人愉快的",
                "pos": "adj.",
                "unit": "Unit 5"
            },
            {
                "id": "g8a5-29",
                "word": "satisfying",
                "phonetic": "/ˈsætɪsfaɪɪŋ/",
                "meaning": "令人满意（或满足）的",
                "pos": "adj.",
                "unit": "Unit 5"
            },
            {
                "id": "g8a5-30",
                "word": "curtain",
                "phonetic": "/ˈkɜːtn/",
                "meaning": "（舞台上的）幕，幕布",
                "pos": "n.",
                "unit": "Unit 5"
            },
            {
                "id": "g8a5-31",
                "word": "pleased",
                "phonetic": "/pliːzd/",
                "meaning": "高兴；满意；愉快",
                "pos": "adj.",
                "unit": "Unit 5"
            },
            {
                "id": "g8a5-32",
                "word": "self-important",
                "phonetic": "/ˌself ɪmˈpɔːtnt/",
                "meaning": "自大的；自负的",
                "pos": "adj.",
                "unit": "Unit 5"
            },
            {
                "id": "g8a5-33",
                "word": "natural",
                "phonetic": "/ˈnætʃrəl/",
                "meaning": "自然的",
                "pos": "adj.",
                "unit": "Unit 5"
            },
            {
                "id": "g8a5-34",
                "word": "perfect",
                "phonetic": "/ˈpɜːfɪkt/",
                "meaning": "完美的",
                "pos": "adj.",
                "unit": "Unit 5"
            },
            {
                "id": "g8a5-35",
                "word": "clap",
                "phonetic": "/klæp/",
                "meaning": "鼓掌，拍手（表示赞许或欣赏）",
                "pos": "v.",
                "unit": "Unit 5"
            },
            {
                "id": "g8a5-36",
                "word": "talented",
                "phonetic": "/ˈtæləntɪd/",
                "meaning": "有才能的；天才的；有才干的",
                "pos": "adj.",
                "unit": "Unit 5"
            },
            {
                "id": "g8a5-37",
                "word": "flag",
                "phonetic": "/flæɡ/",
                "meaning": "（体育运动的）信号旗；标志旗",
                "pos": "n.",
                "unit": "Unit 5"
            },
            {
                "id": "g8a5-38",
                "word": "captain",
                "phonetic": "/ˈkæptɪn/",
                "meaning": "（尤指运动队的）队长",
                "pos": "n.",
                "unit": "Unit 5"
            },
            {
                "id": "g8a5-39",
                "word": "miss",
                "phonetic": "/mɪs/",
                "meaning": "未击中；未得到；错过",
                "pos": "v.",
                "unit": "Unit 5"
            },
            {
                "id": "g8a5-40",
                "word": "row",
                "phonetic": "/rəʊ/",
                "meaning": "一排；一列；一行",
                "pos": "n.",
                "unit": "Unit 5"
            },
            {
                "id": "g8a5-41",
                "word": "in a row",
                "phonetic": "",
                "meaning": "连续几次地",
                "pos": "phr.",
                "unit": "Unit 5"
            },
            {
                "id": "g8a5-42",
                "word": "victory",
                "phonetic": "/ˈvɪktəri/",
                "meaning": "胜利；成功",
                "pos": "n.",
                "unit": "Unit 5"
            }
        ]
    },
    {
        "id": "sys-8a-u6",
        "name": "八年级上册 Unit 6",
        "grade": "初中",
        "description": "上海版八年级上册 Unit 6 英语词汇（上海教育出版社·五四学制）",
        "created_at": "2024-01-01",
        "words": [
            {
                "id": "g8a6-1",
                "word": "VR",
                "phonetic": "",
                "meaning": "(= virtual reality) 虚拟现实",
                "pos": "abbr.",
                "unit": "Unit 6"
            },
            {
                "id": "g8a6-2",
                "word": "hat",
                "phonetic": "/hæt/",
                "meaning": "（常指带檐的）帽子",
                "pos": "n.",
                "unit": "Unit 6"
            },
            {
                "id": "g8a6-3",
                "word": "able",
                "phonetic": "/ˈeɪbl/",
                "meaning": "能；能够",
                "pos": "adj.",
                "unit": "Unit 6"
            },
            {
                "id": "g8a6-4",
                "word": "be able to",
                "phonetic": "",
                "meaning": "能；能够",
                "pos": "phr.",
                "unit": "Unit 6"
            },
            {
                "id": "g8a6-5",
                "word": "attend",
                "phonetic": "/əˈtend/",
                "meaning": "出席；参加",
                "pos": "v.",
                "unit": "Unit 6"
            },
            {
                "id": "g8a6-6",
                "word": "absent",
                "phonetic": "/ˈæbsənt/",
                "meaning": "缺席；不在",
                "pos": "adj.",
                "unit": "Unit 6"
            },
            {
                "id": "g8a6-7",
                "word": "attitude",
                "phonetic": "/ˈætɪtjuːd/",
                "meaning": "态度；看法",
                "pos": "n.",
                "unit": "Unit 6"
            },
            {
                "id": "g8a6-8",
                "word": "disturbing",
                "phonetic": "/dɪˈstɜːbɪŋ/",
                "meaning": "令人不安的",
                "pos": "adj.",
                "unit": "Unit 6"
            },
            {
                "id": "g8a6-9",
                "word": "possible",
                "phonetic": "/ˈpɒsəbl/",
                "meaning": "可能",
                "pos": "adj.",
                "unit": "Unit 6"
            },
            {
                "id": "g8a6-10",
                "word": "unless",
                "phonetic": "/ənˈles/",
                "meaning": "除非；如果不",
                "pos": "conj.",
                "unit": "Unit 6"
            },
            {
                "id": "g8a6-11",
                "word": "any time",
                "phonetic": "/ˈenɪ taɪm/",
                "meaning": "(= anytime) 在任何时候",
                "pos": "adv.",
                "unit": "Unit 6"
            },
            {
                "id": "g8a6-12",
                "word": "probably",
                "phonetic": "/ˈprɒbəbli/",
                "meaning": "很可能；大概",
                "pos": "adv.",
                "unit": "Unit 6"
            },
            {
                "id": "g8a6-13",
                "word": "circle",
                "phonetic": "/ˈsɜːkl/",
                "meaning": "v. （尤指在空中）盘旋，环行 / n. 圆形",
                "pos": "v. & n.",
                "unit": "Unit 6"
            },
            {
                "id": "g8a6-14",
                "word": "rocket",
                "phonetic": "/ˈrɒkɪt/",
                "meaning": "火箭",
                "pos": "n.",
                "unit": "Unit 6"
            },
            {
                "id": "g8a6-15",
                "word": "unlikely",
                "phonetic": "/ʌnˈlaɪkli/",
                "meaning": "不大可能发生的",
                "pos": "adj.",
                "unit": "Unit 6"
            },
            {
                "id": "g8a6-16",
                "word": "super-speed",
                "phonetic": "/ˈsjuːpə spiːd/",
                "meaning": "超高速的",
                "pos": "adj.",
                "unit": "Unit 6"
            },
            {
                "id": "g8a6-17",
                "word": "flight",
                "phonetic": "/flaɪt/",
                "meaning": "航班飞机；飞行",
                "pos": "n.",
                "unit": "Unit 6"
            },
            {
                "id": "g8a6-18",
                "word": "elevator",
                "phonetic": "/ˈelɪveɪtə(r)/",
                "meaning": "电梯；升降机",
                "pos": "n.",
                "unit": "Unit 6"
            },
            {
                "id": "g8a6-19",
                "word": "alien",
                "phonetic": "/ˈeɪliən/",
                "meaning": "外星人；外星生物",
                "pos": "n.",
                "unit": "Unit 6"
            },
            {
                "id": "g8a6-20",
                "word": "within",
                "phonetic": "/wɪˈðɪn/",
                "meaning": "在（某段时间）之内",
                "pos": "prep.",
                "unit": "Unit 6"
            },
            {
                "id": "g8a6-21",
                "word": "kiss",
                "phonetic": "/kɪs/",
                "meaning": "亲吻",
                "pos": "v.",
                "unit": "Unit 6"
            },
            {
                "id": "g8a6-22",
                "word": "scarf",
                "phonetic": "/skɑːf/",
                "meaning": "围巾；头巾",
                "pos": "n.",
                "unit": "Unit 6"
            },
            {
                "id": "g8a6-23",
                "word": "risk",
                "phonetic": "/rɪsk/",
                "meaning": "冒……的风险（或危险）",
                "pos": "v.",
                "unit": "Unit 6"
            },
            {
                "id": "g8a6-24",
                "word": "town",
                "phonetic": "/taʊn/",
                "meaning": "镇；市镇",
                "pos": "n.",
                "unit": "Unit 6"
            },
            {
                "id": "g8a6-25",
                "word": "primary",
                "phonetic": "/ˈpraɪməri/",
                "meaning": "主要的；最重要的；基本的",
                "pos": "adj.",
                "unit": "Unit 6"
            },
            {
                "id": "g8a6-26",
                "word": "security",
                "phonetic": "/sɪˈkjʊərəti/",
                "meaning": "安全工作；保安部门",
                "pos": "n.",
                "unit": "Unit 6"
            },
            {
                "id": "g8a6-27",
                "word": "float",
                "phonetic": "/fləʊt/",
                "meaning": "飘动；漂移",
                "pos": "v.",
                "unit": "Unit 6"
            },
            {
                "id": "g8a6-28",
                "word": "tower",
                "phonetic": "/ˈtaʊə(r)/",
                "meaning": "高于，超过（附近的人或物）",
                "pos": "v.",
                "unit": "Unit 6"
            },
            {
                "id": "g8a6-29",
                "word": "figure",
                "phonetic": "/ˈfɪɡə(r) /",
                "meaning": "计算",
                "pos": "v.",
                "unit": "Unit 6"
            },
            {
                "id": "g8a6-30",
                "word": "figure out",
                "phonetic": "",
                "meaning": "弄懂；弄明白",
                "pos": "phr.",
                "unit": "Unit 6"
            },
            {
                "id": "g8a6-31",
                "word": "familiar",
                "phonetic": "/fəˈmɪliə(r)/",
                "meaning": "熟悉的",
                "pos": "adj.",
                "unit": "Unit 6"
            },
            {
                "id": "g8a6-32",
                "word": "handprint",
                "phonetic": "/ˈhændprɪnt/",
                "meaning": "手印",
                "pos": "n.",
                "unit": "Unit 6"
            },
            {
                "id": "g8a6-33",
                "word": "mile",
                "phonetic": "/maɪl/",
                "meaning": "英里（= 1 609 米或 1 760 码）",
                "pos": "n.",
                "unit": "Unit 6"
            },
            {
                "id": "g8a6-34",
                "word": "unbelievable",
                "phonetic": "/ˌʌnbɪˈliːvəbl/",
                "meaning": "难以置信的；惊人的",
                "pos": "adj.",
                "unit": "Unit 6"
            },
            {
                "id": "g8a6-35",
                "word": "cut in",
                "phonetic": "",
                "meaning": "插嘴",
                "pos": "phr.",
                "unit": "Unit 6"
            },
            {
                "id": "g8a6-36",
                "word": "blow",
                "phonetic": "/bləʊ/",
                "meaning": "炸开；吹",
                "pos": "v.",
                "unit": "Unit 6",
                "irregular_forms": {
                    "past": "blew",
                    "pp": "blown"
                }
            },
            {
                "id": "g8a6-37",
                "word": "blow up",
                "phonetic": "",
                "meaning": "爆炸",
                "pos": "phr.",
                "unit": "Unit 6"
            },
            {
                "id": "g8a6-38",
                "word": "positive",
                "phonetic": "/ˈpɒzətɪv/",
                "meaning": "积极乐观的",
                "pos": "adj.",
                "unit": "Unit 6"
            },
            {
                "id": "g8a6-39",
                "word": "cure",
                "phonetic": "/kjʊə(r)/",
                "meaning": "药物；疗法",
                "pos": "n.",
                "unit": "Unit 6"
            },
            {
                "id": "g8a6-40",
                "word": "cancer",
                "phonetic": "/ˈkænsə(r)/",
                "meaning": "癌；癌症",
                "pos": "n.",
                "unit": "Unit 6"
            }
        ]
    }
]
