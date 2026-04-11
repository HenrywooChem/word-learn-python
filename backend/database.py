"""
数据库初始化和操作
"""
import json
from datetime import datetime
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models import Base, User, UserProfile, WordLibrary, LearningSession, DailyRecord

DATABASE_URL = "sqlite:////app/data/wordlearn.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    """初始化数据库并导入系统词库"""
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    try:
        # 检查是否已有数据
        existing = db.query(WordLibrary).filter(WordLibrary.type == "system").first()
        if existing:
            return
        
        # 导入系统词库
        system_libraries = get_system_libraries()
        for lib_data in system_libraries:
            lib = WordLibrary(
                id=lib_data["id"],
                name=lib_data["name"],
                type="system",
                grade=lib_data.get("grade"),
                description=lib_data.get("description"),
                words=json.dumps(lib_data["words"], ensure_ascii=False),
                created_at=lib_data["created_at"]
            )
            db.add(lib)
        
        db.commit()
        print("数据库初始化完成，系统词库已导入")
    finally:
        db.close()


def get_db() -> Session:
    """获取数据库会话"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_system_libraries():
    """系统词库数据"""
    return [
        {
            "id": "sys-shanghai-6",
            "name": "上海版六年级上册",
            "grade": "小学",
            "description": "上海版小学六年级上册英语词汇",
            "created_at": "2024-01-01",
            "words": [
                {"id": "sh6-1", "word": "classroom", "phonetic": "/ˈklɑːsruːm/", "meaning": "教室"},
                {"id": "sh6-2", "word": "blackboard", "phonetic": "/ˈblækbɔːrd/", "meaning": "黑板"},
                {"id": "sh6-3", "word": "window", "phonetic": "/ˈwɪndəʊ/", "meaning": "窗户"},
                {"id": "sh6-4", "word": "door", "phonetic": "/dɔːr/", "meaning": "门"},
                {"id": "sh6-5", "word": "floor", "phonetic": "/flɔːr/", "meaning": "地板"},
                {"id": "sh6-6", "word": "wall", "phonetic": "/wɔːl/", "meaning": "墙"},
                {"id": "sh6-7", "word": "ceiling", "phonetic": "/ˈsiːlɪŋ/", "meaning": "天花板"},
                {"id": "sh6-8", "word": "light", "phonetic": "/laɪt/", "meaning": "灯"},
                {"id": "sh6-9", "word": "fan", "phonetic": "/fæn/", "meaning": "风扇"},
                {"id": "sh6-10", "word": "computer", "phonetic": "/kəmˈpjuːtər/", "meaning": "电脑"},
                {"id": "sh6-11", "word": "keyboard", "phonetic": "/ˈkiːbɔːrd/", "meaning": "键盘"},
                {"id": "sh6-12", "word": "mouse", "phonetic": "/maʊs/", "meaning": "鼠标"},
                {"id": "sh6-13", "word": "screen", "phonetic": "/skriːn/", "meaning": "屏幕"},
                {"id": "sh6-14", "word": "printer", "phonetic": "/ˈprɪntər/", "meaning": "打印机"},
                {"id": "sh6-15", "word": "telephone", "phonetic": "/ˈtelɪfəʊn/", "meaning": "电话"},
                {"id": "sh6-16", "word": "mobile phone", "phonetic": "/ˈməʊbaɪl fəʊn/", "meaning": "手机"},
                {"id": "sh6-17", "word": "camera", "phonetic": "/ˈkæmərə/", "meaning": "照相机"},
                {"id": "sh6-18", "word": "television", "phonetic": "/ˈtelɪvɪʒn/", "meaning": "电视"},
                {"id": "sh6-19", "word": "radio", "phonetic": "/ˈreɪdiəʊ/", "meaning": "收音机"},
                {"id": "sh6-20", "word": "headphones", "phonetic": "/ˈhedfəʊnz/", "meaning": "耳机"},
                {"id": "sh6-21", "word": "speaker", "phonetic": "/ˈspiːkər/", "meaning": "扬声器"},
                {"id": "sh6-22", "word": "microphone", "phonetic": "/ˈmaɪkrəfəʊn/", "meaning": "麦克风"},
                {"id": "sh6-23", "word": "video", "phonetic": "/ˈvɪdiəʊ/", "meaning": "视频"},
                {"id": "sh6-24", "word": "movie", "phonetic": "/ˈmuːvi/", "meaning": "电影"},
                {"id": "sh6-25", "word": "music", "phonetic": "/ˈmjuːzɪk/", "meaning": "音乐"},
                {"id": "sh6-26", "word": "song", "phonetic": "/sɒŋ/", "meaning": "歌曲"},
                {"id": "sh6-27", "word": "dance", "phonetic": "/dɑːns/", "meaning": "舞蹈"},
                {"id": "sh6-28", "word": "game", "phonetic": "/ɡeɪm/", "meaning": "游戏"},
                {"id": "sh6-29", "word": "sport", "phonetic": "/spɔːrt/", "meaning": "运动"},
                {"id": "sh6-30", "word": "football", "phonetic": "/ˈfʊtbɔːl/", "meaning": "足球"},
                {"id": "sh6-31", "word": "basketball", "phonetic": "/ˈbɑːskɪtbɔːl/", "meaning": "篮球"},
                {"id": "sh6-32", "word": "volleyball", "phonetic": "/ˈvɒlibɔːl/", "meaning": "排球"},
                {"id": "sh6-33", "word": "tennis", "phonetic": "/ˈtenɪs/", "meaning": "网球"},
                {"id": "sh6-34", "word": "badminton", "phonetic": "/ˈbædmɪntən/", "meaning": "羽毛球"},
                {"id": "sh6-35", "word": "swimming", "phonetic": "/ˈswɪmɪŋ/", "meaning": "游泳"},
                {"id": "sh6-36", "word": "running", "phonetic": "/ˈrʌnɪŋ/", "meaning": "跑步"},
                {"id": "sh6-37", "word": "walking", "phonetic": "/ˈwɔːkɪŋ/", "meaning": "散步"},
                {"id": "sh6-38", "word": "cycling", "phonetic": "/ˈsaɪklɪŋ/", "meaning": "骑自行车"},
                {"id": "sh6-39", "word": "skating", "phonetic": "/ˈskeɪtɪŋ/", "meaning": "滑冰"},
                {"id": "sh6-40", "word": "skiing", "phonetic": "/ˈskiːɪŋ/", "meaning": "滑雪"},
                {"id": "sh6-41", "word": "climbing", "phonetic": "/ˈklaɪmɪŋ/", "meaning": "爬山"},
                {"id": "sh6-42", "word": "hiking", "phonetic": "/ˈhaɪkɪŋ/", "meaning": "远足"},
                {"id": "sh6-43", "word": "camping", "phonetic": "/ˈkæmpɪŋ/", "meaning": "露营"},
                {"id": "sh6-44", "word": "picnic", "phonetic": "/ˈpɪknɪk/", "meaning": "野餐"},
                {"id": "sh6-45", "word": "travel", "phonetic": "/ˈtrævl/", "meaning": "旅行"},
                {"id": "sh6-46", "word": "holiday", "phonetic": "/ˈhɒlədeɪ/", "meaning": "假日"},
                {"id": "sh6-47", "word": "vacation", "phonetic": "/vəˈkeɪʃn/", "meaning": "假期"},
                {"id": "sh6-48", "word": "weekend", "phonetic": "/ˌwiːkˈend/", "meaning": "周末"},
                {"id": "sh6-49", "word": "morning", "phonetic": "/ˈmɔːrnɪŋ/", "meaning": "早上"},
                {"id": "sh6-50", "word": "afternoon", "phonetic": "/ˌɑːftərˈnuːn/", "meaning": "下午"},
                {"id": "sh6-51", "word": "evening", "phonetic": "/ˈiːvnɪŋ/", "meaning": "晚上"},
                {"id": "sh6-52", "word": "night", "phonetic": "/naɪt/", "meaning": "夜晚"},
                {"id": "sh6-53", "word": "today", "phonetic": "/təˈdeɪ/", "meaning": "今天"},
                {"id": "sh6-54", "word": "tomorrow", "phonetic": "/təˈmɒrəʊ/", "meaning": "明天"},
                {"id": "sh6-55", "word": "yesterday", "phonetic": "/ˈjestərdeɪ/", "meaning": "昨天"},
                {"id": "sh6-56", "word": "week", "phonetic": "/wiːk/", "meaning": "周"},
                {"id": "sh6-57", "word": "month", "phonetic": "/mʌnθ/", "meaning": "月"},
                {"id": "sh6-58", "word": "year", "phonetic": "/jɪər/", "meaning": "年"},
                {"id": "sh6-59", "word": "season", "phonetic": "/ˈsiːzn/", "meaning": "季节"},
                {"id": "sh6-60", "word": "spring", "phonetic": "/sprɪŋ/", "meaning": "春天"},
                {"id": "sh6-61", "word": "summer", "phonetic": "/ˈsʌmər/", "meaning": "夏天"},
                {"id": "sh6-62", "word": "autumn", "phonetic": "/ˈɔːtəm/", "meaning": "秋天"},
                {"id": "sh6-63", "word": "winter", "phonetic": "/ˈwɪntər/", "meaning": "冬天"},
                {"id": "sh6-64", "word": "weather", "phonetic": "/ˈweðər/", "meaning": "天气"},
                {"id": "sh6-65", "word": "sunny", "phonetic": "/ˈsʌni/", "meaning": "晴朗的"},
                {"id": "sh6-66", "word": "rainy", "phonetic": "/ˈreɪni/", "meaning": "下雨的"},
                {"id": "sh6-67", "word": "cloudy", "phonetic": "/ˈklaʊdi/", "meaning": "多云的"},
                {"id": "sh6-68", "word": "snowy", "phonetic": "/ˈsnəʊi/", "meaning": "下雪的"},
                {"id": "sh6-69", "word": "windy", "phonetic": "/ˈwɪndi/", "meaning": "有风的"},
                {"id": "sh6-70", "word": "cold", "phonetic": "/kəʊld/", "meaning": "冷的"},
                {"id": "sh6-71", "word": "warm", "phonetic": "/wɔːrm/", "meaning": "温暖的"},
                {"id": "sh6-72", "word": "hot", "phonetic": "/hɒt/", "meaning": "热的"},
                {"id": "sh6-73", "word": "cool", "phonetic": "/kuːl/", "meaning": "凉爽的"},
                {"id": "sh6-74", "word": "temperature", "phonetic": "/ˈtemprətʃər/", "meaning": "温度"},
                {"id": "sh6-75", "word": "degree", "phonetic": "/dɪˈɡriː/", "meaning": "度"},
                {"id": "sh6-76", "word": "rain", "phonetic": "/reɪn/", "meaning": "雨"},
                {"id": "sh6-77", "word": "snow", "phonetic": "/snəʊ/", "meaning": "雪"},
                {"id": "sh6-78", "word": "wind", "phonetic": "/wɪnd/", "meaning": "风"},
                {"id": "sh6-79", "word": "cloud", "phonetic": "/klaʊd/", "meaning": "云"},
                {"id": "sh6-80", "word": "sky", "phonetic": "/skaɪ/", "meaning": "天空"},
            ],
        },
        {
            "id": "sys-primary-1",
            "name": "小学一年级",
            "grade": "小学",
            "description": "人教版小学一年级英语核心词汇",
            "created_at": "2024-01-01",
            "words": [
                {"id": "p1-1", "word": "apple", "phonetic": "/ˈæpəl/", "meaning": "苹果"},
                {"id": "p1-2", "word": "ball", "phonetic": "/bɔːl/", "meaning": "球"},
                {"id": "p1-3", "word": "cat", "phonetic": "/kæt/", "meaning": "猫"},
                {"id": "p1-4", "word": "dog", "phonetic": "/dɒɡ/", "meaning": "狗"},
                {"id": "p1-5", "word": "egg", "phonetic": "/eɡ/", "meaning": "蛋"},
                {"id": "p1-6", "word": "fish", "phonetic": "/fɪʃ/", "meaning": "鱼"},
                {"id": "p1-7", "word": "girl", "phonetic": "/ɡɜːl/", "meaning": "女孩"},
                {"id": "p1-8", "word": "hat", "phonetic": "/hæt/", "meaning": "帽子"},
                {"id": "p1-9", "word": "ice", "phonetic": "/aɪs/", "meaning": "冰"},
                {"id": "p1-10", "word": "juice", "phonetic": "/dʒuːs/", "meaning": "果汁"},
                {"id": "p1-11", "word": "kite", "phonetic": "/kaɪt/", "meaning": "风筝"},
                {"id": "p1-12", "word": "lion", "phonetic": "/ˈlaɪən/", "meaning": "狮子"},
                {"id": "p1-13", "word": "milk", "phonetic": "/mɪlk/", "meaning": "牛奶"},
                {"id": "p1-14", "word": "nose", "phonetic": "/nəʊz/", "meaning": "鼻子"},
                {"id": "p1-15", "word": "orange", "phonetic": "/ˈɒrɪndʒ/", "meaning": "橙子"},
                {"id": "p1-16", "word": "pen", "phonetic": "/pen/", "meaning": "钢笔"},
                {"id": "p1-17", "word": "queen", "phonetic": "/kwiːn/", "meaning": "女王"},
                {"id": "p1-18", "word": "red", "phonetic": "/red/", "meaning": "红色的"},
                {"id": "p1-19", "word": "sun", "phonetic": "/sʌn/", "meaning": "太阳"},
                {"id": "p1-20", "word": "tree", "phonetic": "/triː/", "meaning": "树"},
            ],
        },
        {
            "id": "sys-primary-3",
            "name": "小学三年级",
            "grade": "小学",
            "description": "人教版小学三年级英语词汇",
            "created_at": "2024-01-01",
            "words": [
                {"id": "p3-1", "word": "book", "phonetic": "/bʊk/", "meaning": "书"},
                {"id": "p3-2", "word": "bag", "phonetic": "/bæɡ/", "meaning": "包；书包"},
                {"id": "p3-3", "word": "ruler", "phonetic": "/ˈruːlər/", "meaning": "尺子"},
                {"id": "p3-4", "word": "pencil", "phonetic": "/ˈpensl/", "meaning": "铅笔"},
                {"id": "p3-5", "word": "eraser", "phonetic": "/ɪˈreɪzər/", "meaning": "橡皮擦"},
                {"id": "p3-6", "word": "school", "phonetic": "/skuːl/", "meaning": "学校"},
                {"id": "p3-7", "word": "teacher", "phonetic": "/ˈtiːtʃər/", "meaning": "教师"},
                {"id": "p3-8", "word": "student", "phonetic": "/ˈstjuːdnt/", "meaning": "学生"},
                {"id": "p3-9", "word": "desk", "phonetic": "/desk/", "meaning": "桌子"},
                {"id": "p3-10", "word": "chair", "phonetic": "/tʃeər/", "meaning": "椅子"},
                {"id": "p3-11", "word": "yellow", "phonetic": "/ˈjeləʊ/", "meaning": "黄色的"},
                {"id": "p3-12", "word": "blue", "phonetic": "/bluː/", "meaning": "蓝色的"},
                {"id": "p3-13", "word": "green", "phonetic": "/ɡriːn/", "meaning": "绿色的"},
                {"id": "p3-14", "word": "white", "phonetic": "/waɪt/", "meaning": "白色的"},
                {"id": "p3-15", "word": "black", "phonetic": "/blæk/", "meaning": "黑色的"},
                {"id": "p3-16", "word": "father", "phonetic": "/ˈfɑːðər/", "meaning": "父亲"},
                {"id": "p3-17", "word": "mother", "phonetic": "/ˈmʌðər/", "meaning": "母亲"},
                {"id": "p3-18", "word": "brother", "phonetic": "/ˈbrʌðər/", "meaning": "兄弟"},
                {"id": "p3-19", "word": "sister", "phonetic": "/ˈsɪstər/", "meaning": "姐妹"},
                {"id": "p3-20", "word": "friend", "phonetic": "/frend/", "meaning": "朋友"},
                {"id": "p3-21", "word": "happy", "phonetic": "/ˈhæpi/", "meaning": "快乐的"},
                {"id": "p3-22", "word": "good", "phonetic": "/ɡʊd/", "meaning": "好的"},
                {"id": "p3-23", "word": "big", "phonetic": "/bɪɡ/", "meaning": "大的"},
                {"id": "p3-24", "word": "small", "phonetic": "/smɔːl/", "meaning": "小的"},
                {"id": "p3-25", "word": "hot", "phonetic": "/hɒt/", "meaning": "热的"},
            ],
        },
        {
            "id": "sys-primary-5",
            "name": "小学五年级",
            "grade": "小学",
            "description": "人教版小学五年级英语词汇",
            "created_at": "2024-01-01",
            "words": [
                {"id": "p5-1", "word": "Monday", "phonetic": "/ˈmʌndeɪ/", "meaning": "星期一"},
                {"id": "p5-2", "word": "Tuesday", "phonetic": "/ˈtjuːzdeɪ/", "meaning": "星期二"},
                {"id": "p5-3", "word": "Wednesday", "phonetic": "/ˈwenzdeɪ/", "meaning": "星期三"},
                {"id": "p5-4", "word": "Thursday", "phonetic": "/ˈθɜːzdeɪ/", "meaning": "星期四"},
                {"id": "p5-5", "word": "Friday", "phonetic": "/ˈfraɪdeɪ/", "meaning": "星期五"},
                {"id": "p5-6", "word": "Saturday", "phonetic": "/ˈsætədeɪ/", "meaning": "星期六"},
                {"id": "p5-7", "word": "Sunday", "phonetic": "/ˈsʌndeɪ/", "meaning": "星期日"},
                {"id": "p5-8", "word": "January", "phonetic": "/ˈdʒænjueri/", "meaning": "一月"},
                {"id": "p5-9", "word": "February", "phonetic": "/ˈfebrueri/", "meaning": "二月"},
                {"id": "p5-10", "word": "March", "phonetic": "/mɑːtʃ/", "meaning": "三月"},
                {"id": "p5-11", "word": "April", "phonetic": "/ˈeɪprəl/", "meaning": "四月"},
                {"id": "p5-12", "word": "sports", "phonetic": "/spɔːts/", "meaning": "运动"},
                {"id": "p5-13", "word": "swimming", "phonetic": "/ˈswɪmɪŋ/", "meaning": "游泳"},
                {"id": "p5-14", "word": "running", "phonetic": "/ˈrʌnɪŋ/", "meaning": "跑步"},
                {"id": "p5-15", "word": "reading", "phonetic": "/ˈriːdɪŋ/", "meaning": "阅读"},
                {"id": "p5-16", "word": "shopping", "phonetic": "/ˈʃɒpɪŋ/", "meaning": "购物"},
                {"id": "p5-17", "word": "cooking", "phonetic": "/ˈkʊkɪŋ/", "meaning": "烹饪"},
                {"id": "p5-18", "word": "hospital", "phonetic": "/ˈhɒspɪtl/", "meaning": "医院"},
                {"id": "p5-19", "word": "library", "phonetic": "/ˈlaɪbrəri/", "meaning": "图书馆"},
                {"id": "p5-20", "word": "supermarket", "phonetic": "/ˈsuːpəmɑːkɪt/", "meaning": "超市"},
                {"id": "p5-21", "word": "turn left", "phonetic": "/tɜːn left/", "meaning": "向左转"},
                {"id": "p5-22", "word": "turn right", "phonetic": "/tɜːn raɪt/", "meaning": "向右转"},
                {"id": "p5-23", "word": "go straight", "phonetic": "/ɡəʊ streɪt/", "meaning": "直走"},
                {"id": "p5-24", "word": "take a bus", "phonetic": "/teɪk ə bʌs/", "meaning": "乘公共汽车"},
                {"id": "p5-25", "word": "by subway", "phonetic": "/baɪ ˈsʌbweɪ/", "meaning": "乘地铁"},
            ],
        },
        {
            "id": "sys-junior-7",
            "name": "初一（七年级）",
            "grade": "初中",
            "description": "人教版初一英语核心词汇",
            "created_at": "2024-01-01",
            "words": [
                {"id": "j7-1", "word": "family", "phonetic": "/ˈfæməli/", "meaning": "家庭；家人"},
                {"id": "j7-2", "word": "subject", "phonetic": "/ˈsʌbdʒɪkt/", "meaning": "学科；科目"},
                {"id": "j7-3", "word": "favorite", "phonetic": "/ˈfeɪvərɪt/", "meaning": "最喜欢的"},
                {"id": "j7-4", "word": "breakfast", "phonetic": "/ˈbrekfəst/", "meaning": "早餐"},
                {"id": "j7-5", "word": "lunch", "phonetic": "/lʌntʃ/", "meaning": "午餐"},
                {"id": "j7-6", "word": "dinner", "phonetic": "/ˈdɪnər/", "meaning": "晚餐"},
                {"id": "j7-7", "word": "bedroom", "phonetic": "/ˈbedrʊm/", "meaning": "卧室"},
                {"id": "j7-8", "word": "living room", "phonetic": "/ˈlɪvɪŋ ruːm/", "meaning": "客厅"},
                {"id": "j7-9", "word": "kitchen", "phonetic": "/ˈkɪtʃɪn/", "meaning": "厨房"},
                {"id": "j7-10", "word": "bathroom", "phonetic": "/ˈbɑːθruːm/", "meaning": "浴室；洗手间"},
                {"id": "j7-11", "word": "telephone", "phonetic": "/ˈtelɪfəʊn/", "meaning": "电话"},
                {"id": "j7-12", "word": "computer", "phonetic": "/kəmˈpjuːtər/", "meaning": "电脑"},
                {"id": "j7-13", "word": "television", "phonetic": "/ˈtelɪvɪʒn/", "meaning": "电视机"},
                {"id": "j7-14", "word": "interesting", "phonetic": "/ˈɪntrəstɪŋ/", "meaning": "有趣的"},
                {"id": "j7-15", "word": "difficult", "phonetic": "/ˈdɪfɪkəlt/", "meaning": "困难的"},
                {"id": "j7-16", "word": "easy", "phonetic": "/ˈiːzi/", "meaning": "容易的"},
                {"id": "j7-17", "word": "boring", "phonetic": "/ˈbɔːrɪŋ/", "meaning": "无聊的"},
                {"id": "j7-18", "word": "exciting", "phonetic": "/ɪkˈsaɪtɪŋ/", "meaning": "令人兴奋的"},
                {"id": "j7-19", "word": "relaxing", "phonetic": "/rɪˈlæksɪŋ/", "meaning": "轻松的"},
                {"id": "j7-20", "word": "dangerous", "phonetic": "/ˈdeɪndʒərəs/", "meaning": "危险的"},
                {"id": "j7-21", "word": "practice", "phonetic": "/ˈpræktɪs/", "meaning": "练习；实践"},
                {"id": "j7-22", "word": "remember", "phonetic": "/rɪˈmembər/", "meaning": "记得；记住"},
                {"id": "j7-23", "word": "forget", "phonetic": "/fəˈɡet/", "meaning": "忘记"},
                {"id": "j7-24", "word": "understand", "phonetic": "/ˌʌndəˈstænd/", "meaning": "理解；明白"},
                {"id": "j7-25", "word": "explain", "phonetic": "/ɪkˈspleɪn/", "meaning": "解释；说明"},
                {"id": "j7-26", "word": "music", "phonetic": "/ˈmjuːzɪk/", "meaning": "音乐"},
                {"id": "j7-27", "word": "science", "phonetic": "/ˈsaɪəns/", "meaning": "科学"},
                {"id": "j7-28", "word": "history", "phonetic": "/ˈhɪstri/", "meaning": "历史"},
                {"id": "j7-29", "word": "geography", "phonetic": "/dʒiˈɒɡrəfi/", "meaning": "地理"},
                {"id": "j7-30", "word": "biology", "phonetic": "/baɪˈɒlədʒi/", "meaning": "生物学"},
            ],
        },
        {
            "id": "sys-junior-9",
            "name": "初三（九年级）",
            "grade": "初中",
            "description": "人教版初三英语重点词汇",
            "created_at": "2024-01-01",
            "words": [
                {"id": "j9-1", "word": "achieve", "phonetic": "/əˈtʃiːv/", "meaning": "实现；取得"},
                {"id": "j9-2", "word": "attitude", "phonetic": "/ˈætɪtjuːd/", "meaning": "态度；看法"},
                {"id": "j9-3", "word": "challenge", "phonetic": "/ˈtʃælɪndʒ/", "meaning": "挑战"},
                {"id": "j9-4", "word": "confidence", "phonetic": "/ˈkɒnfɪdəns/", "meaning": "信心；自信"},
                {"id": "j9-5", "word": "creativity", "phonetic": "/ˌkriːeɪˈtɪvəti/", "meaning": "创造力"},
                {"id": "j9-6", "word": "develop", "phonetic": "/dɪˈveləp/", "meaning": "发展；开发"},
                {"id": "j9-7", "word": "education", "phonetic": "/ˌedʒuˈkeɪʃn/", "meaning": "教育"},
                {"id": "j9-8", "word": "encourage", "phonetic": "/ɪnˈkʌrɪdʒ/", "meaning": "鼓励"},
                {"id": "j9-9", "word": "environment", "phonetic": "/ɪnˈvaɪrənmənt/", "meaning": "环境"},
                {"id": "j9-10", "word": "experience", "phonetic": "/ɪkˈspɪəriəns/", "meaning": "经历；经验"},
                {"id": "j9-11", "word": "government", "phonetic": "/ˈɡʌvənmənt/", "meaning": "政府"},
                {"id": "j9-12", "word": "imagination", "phonetic": "/ɪˌmædʒɪˈneɪʃn/", "meaning": "想象力"},
                {"id": "j9-13", "word": "improve", "phonetic": "/ɪmˈpruːv/", "meaning": "改善；提高"},
                {"id": "j9-14", "word": "influence", "phonetic": "/ˈɪnfluəns/", "meaning": "影响"},
                {"id": "j9-15", "word": "knowledge", "phonetic": "/ˈnɒlɪdʒ/", "meaning": "知识；学问"},
                {"id": "j9-16", "word": "opportunity", "phonetic": "/ˌɒpəˈtjuːnəti/", "meaning": "机会；时机"},
                {"id": "j9-17", "word": "pollution", "phonetic": "/pəˈluːʃn/", "meaning": "污染"},
                {"id": "j9-18", "word": "population", "phonetic": "/ˌpɒpjuˈleɪʃn/", "meaning": "人口"},
                {"id": "j9-19", "word": "protect", "phonetic": "/prəˈtekt/", "meaning": "保护"},
                {"id": "j9-20", "word": "recycling", "phonetic": "/ˌriːˈsaɪklɪŋ/", "meaning": "回收利用"},
                {"id": "j9-21", "word": "responsibility", "phonetic": "/rɪˌspɒnsəˈbɪləti/", "meaning": "责任；职责"},
                {"id": "j9-22", "word": "scientific", "phonetic": "/ˌsaɪənˈtɪfɪk/", "meaning": "科学的"},
                {"id": "j9-23", "word": "succeed", "phonetic": "/səkˈsiːd/", "meaning": "成功"},
                {"id": "j9-24", "word": "technology", "phonetic": "/tekˈnɒlədʒi/", "meaning": "技术；科技"},
                {"id": "j9-25", "word": "volunteer", "phonetic": "/ˌvɒlənˈtɪər/", "meaning": "志愿者；自愿"},
            ],
        },
        {
            "id": "sys-high-10",
            "name": "高中必修词汇",
            "grade": "高中",
            "description": "高中英语课程标准必修词汇",
            "created_at": "2024-01-01",
            "words": [
                {"id": "h10-1", "word": "abandon", "phonetic": "/əˈbændən/", "meaning": "放弃；遗弃"},
                {"id": "h10-2", "word": "absence", "phonetic": "/ˈæbsəns/", "meaning": "缺席；不在场"},
                {"id": "h10-3", "word": "accomplish", "phonetic": "/əˈkɒmplɪʃ/", "meaning": "完成；实现"},
                {"id": "h10-4", "word": "accurate", "phonetic": "/ˈækjərət/", "meaning": "准确的；精确的"},
                {"id": "h10-5", "word": "adequate", "phonetic": "/ˈædɪkwət/", "meaning": "足够的；适当的"},
                {"id": "h10-6", "word": "admire", "phonetic": "/ədˈmaɪər/", "meaning": "钦佩；羡慕"},
                {"id": "h10-7", "word": "adventure", "phonetic": "/ədˈventʃər/", "meaning": "冒险；奇遇"},
                {"id": "h10-8", "word": "afford", "phonetic": "/əˈfɔːd/", "meaning": "负担得起；提供"},
                {"id": "h10-9", "word": "aggressive", "phonetic": "/əˈɡresɪv/", "meaning": "侵略性的；好斗的"},
                {"id": "h10-10", "word": "ambition", "phonetic": "/æmˈbɪʃn/", "meaning": "雄心；野心"},
                {"id": "h10-11", "word": "analyze", "phonetic": "/ˈænəlaɪz/", "meaning": "分析"},
                {"id": "h10-12", "word": "anxiety", "phonetic": "/æŋˈzaɪəti/", "meaning": "焦虑；担心"},
                {"id": "h10-13", "word": "appreciate", "phonetic": "/əˈpriːʃieɪt/", "meaning": "欣赏；感激"},
                {"id": "h10-14", "word": "appropriate", "phonetic": "/əˈprəʊpriət/", "meaning": "合适的；恰当的"},
                {"id": "h10-15", "word": "approximately", "phonetic": "/əˈprɒksɪmətli/", "meaning": "大约；近似地"},
                {"id": "h10-16", "word": "argument", "phonetic": "/ˈɑːɡjumənt/", "meaning": "争论；论点"},
                {"id": "h10-17", "word": "artificial", "phonetic": "/ˌɑːtɪˈfɪʃl/", "meaning": "人工的；人造的"},
                {"id": "h10-18", "word": "authority", "phonetic": "/ɔːˈθɒrəti/", "meaning": "权力；当局"},
                {"id": "h10-19", "word": "average", "phonetic": "/ˈævərɪdʒ/", "meaning": "平均的；普通的"},
                {"id": "h10-20", "word": "barely", "phonetic": "/ˈbeəli/", "meaning": "几乎不；刚刚"},
                {"id": "h10-21", "word": "beneficial", "phonetic": "/ˌbenɪˈfɪʃl/", "meaning": "有益的；有利的"},
                {"id": "h10-22", "word": "capability", "phonetic": "/ˌkeɪpəˈbɪləti/", "meaning": "能力；才能"},
                {"id": "h10-23", "word": "circumstances", "phonetic": "/ˈsɜːkəmstænsɪz/", "meaning": "情况；环境"},
                {"id": "h10-24", "word": "civilization", "phonetic": "/ˌsɪvəlaɪˈzeɪʃn/", "meaning": "文明；文明社会"},
                {"id": "h10-25", "word": "colleague", "phonetic": "/ˈkɒliːɡ/", "meaning": "同事；同僚"},
                {"id": "h10-26", "word": "commit", "phonetic": "/kəˈmɪt/", "meaning": "犯（罪）；承诺"},
                {"id": "h10-27", "word": "communicate", "phonetic": "/kəˈmjuːnɪkeɪt/", "meaning": "沟通；传达"},
                {"id": "h10-28", "word": "consequence", "phonetic": "/ˈkɒnsɪkwəns/", "meaning": "结果；后果"},
                {"id": "h10-29", "word": "considerable", "phonetic": "/kənˈsɪdərəbl/", "meaning": "相当大的；值得注意的"},
                {"id": "h10-30", "word": "contribute", "phonetic": "/kənˈtrɪbjuːt/", "meaning": "贡献；捐献"},
            ],
        },
    ]


if __name__ == "__main__":
    init_db()
