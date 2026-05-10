from database import SessionLocal, Word
db = SessionLocal()
# Check unit1 word count and duplicates
words = db.query(Word).filter(Word.library_id == "sys-grade6-down-u1").all()
print(f"Unit1 total words in DB: {len(words)}")
# Check unique word text
unique = set(w.word for w in words)
print(f"Unique words: {len(unique)}")
# Show some duplicates
from collections import Counter
word_counts = Counter(w.word for w in words)
dupes = {w: c for w, c in word_counts.items() if c > 1}
print(f"Duplicated words: {len(dupes)}")
if dupes:
    for w, c in list(dupes.items())[:5]:
        print(f"  '{w}' appears {c} times")
db.close()
