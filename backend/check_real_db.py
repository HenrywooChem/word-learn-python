import database
import sqlite3

# Print actual engine info
print("Engine:", database.engine.url)

# Directly query using sqlite3
db_path = '/app/data/wordlearn.db'
conn = sqlite3.connect(db_path)
cur = conn.cursor()
cur.execute("SELECT id, name FROM word_libraries")
rows = cur.fetchall()
print(f"\nSQLite direct query on {db_path}: {len(rows)} libraries")
for r in rows:
    print(f"  {r[0]}: {r[1]}")
conn.close()

# Also check /app/wordlearn.db
db_path2 = '/app/wordlearn.db'
try:
    conn2 = sqlite3.connect(db_path2)
    cur2 = conn2.cursor()
    cur2.execute("SELECT id, name FROM word_libraries")
    rows2 = cur2.fetchall()
    print(f"\nSQLite direct query on {db_path2}: {len(rows2)} libraries")
    for r in rows2:
        print(f"  {r[0]}: {r[1]}")
    conn2.close()
except Exception as e:
    print(f"\nCannot read {db_path2}: {e}")

# Check via SQLAlchemy (same as FastAPI)
from database import SessionLocal, WordLibrary
db = SessionLocal()
libs = db.query(WordLibrary).all()
print(f"\nSQLAlchemy query: {len(libs)} libraries")
for lib in libs:
    print(f"  {lib.id}: {lib.name}")
db.close()
