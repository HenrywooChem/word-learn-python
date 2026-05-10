from database import SessionLocal, WordLibrary
db = SessionLocal()
libs = db.query(WordLibrary).all()
for l in libs:
    print(f"{l.id}: {l.name} ({len(l.words)} words)")
db.close()
