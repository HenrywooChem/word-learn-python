from database import SessionLocal, WordLibrary
import json

db = SessionLocal()
lib = db.query(WordLibrary).filter(WordLibrary.id == "sys-grade6-down-u1").first()
if lib:
    words = json.loads(lib.words)
    print(f"Unit1 words JSON length: {len(words)}")
    # Show first 3 and last 3
    for w in words[:3]:
        print(f"  {w}")
    print("  ...")
    for w in words[-3:]:
        print(f"  {w}")
    
    # Check for duplicate word IDs
    word_ids = [w["id"] for w in words]
    from collections import Counter
    dupes = {k: v for k, v in Counter(word_ids).items() if v > 1}
    print(f"\nDuplicate word IDs: {len(dupes)}")
    if dupes:
        for wid, c in list(dupes.items())[:5]:
            print(f"  '{wid}' appears {c} times")
db.close()
