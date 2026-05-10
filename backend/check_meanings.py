import json
from database import SessionLocal, WordLibrary

db = SessionLocal()

# Check grade6 unit1 meanings for any issues
lib = db.query(WordLibrary).filter(WordLibrary.id == "sys-grade6-down-u1").first()
if lib:
    words = json.loads(lib.words)
    print(f"Unit 1: {len(words)} words")
    for w in words:
        m = w["meaning"]
        # Check for unusual characters
        has_semicolon = "；" in m
        has_slash = "/" in m
        has_newline = "\n" in m or "\r" in m
        has_extra_space = "  " in m
        has_english_in_meaning = any(c.isalpha() for c in m)
        
        issues = []
        if has_semicolon: issues.append("chinese_semicolon")
        if has_slash: issues.append("slash")
        if has_newline: issues.append("newline")
        if has_extra_space: issues.append("double_space")
        
        if issues:
            print(f"  [{w['id']}] {w['word']}: issues={issues}")
            print(f"    meaning repr: {repr(m)}")

# Also check if any two words have same meaning (which could cause confusion)
lib2 = db.query(WordLibrary).filter(WordLibrary.id == "sys-grade6-down-u2").first()
if lib2:
    words2 = json.loads(lib2.words)
    print(f"\nUnit 2: {len(words2)} words")
    for w in words2:
        m = w["meaning"]
        has_semicolon = "；" in m
        if has_semicolon:
            print(f"  [{w['id']}] {w['word']}: has semicolon")
            print(f"    meaning repr: {repr(m)}")

db.close()
