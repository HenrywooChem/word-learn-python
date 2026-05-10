import database
from database import SessionLocal, WordLibrary
import os

# Check which DB the app actually uses
print("DATABASE_URL:", database.DATABASE_URL)

# Check engine
print("Engine URL:", str(database.engine.url))

# Check both DBs
db1 = '/app/wordlearn.db'
db2 = '/app/data/wordlearn.db'

for p in [db1, db2]:
    if os.path.exists(p):
        print(f"\n{p}: {os.path.getsize(p)} bytes")
    else:
        print(f"\n{p}: NOT FOUND")

# The current session should use DATABASE_URL
db = SessionLocal()
libs = db.query(WordLibrary).all()
print(f"\nCurrent DB has {len(libs)} libraries")

# Check if we can read from /app/wordlearn.db too
import sqlite3
try:
    conn = sqlite3.connect(db1)
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM word_libraries")
    count = cur.fetchone()[0]
    print(f"/app/wordlearn.db has {count} libraries in SQLite")
    conn.close()
except Exception as e:
    print(f"Cannot read /app/wordlearn.db: {e}")

try:
    conn = sqlite3.connect(db2)
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM word_libraries")
    count = cur.fetchone()[0]
    print(f"/app/data/wordlearn.db has {count} libraries in SQLite")
    conn.close()
except Exception as e:
    print(f"Cannot read /app/data/wordlearn.db: {e}")
