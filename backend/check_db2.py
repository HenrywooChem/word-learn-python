import database
print('Database URL:', database.DATABASE_URL)

import os
db_path = '/app/data/wordlearn.db'
if os.path.exists(db_path):
    print(f'DB exists: {db_path}')
    print(f'DB size: {os.path.getsize(db_path)} bytes')
else:
    print(f'DB NOT found at {db_path}')
    for root, dirs, files in os.walk('/app'):
        for f in files:
            if f.endswith('.db'):
                full = os.path.join(root, f)
                print(f'Found DB: {full} ({os.path.getsize(full)} bytes)')

# Also check init_db output
from database import init_db
print('\nCalling init_db()...')
init_db()

# Now check again
from database import SessionLocal, WordLibrary
db = SessionLocal()
libs = db.query(WordLibrary).all()
print(f'\nAfter init_db, total libraries: {len(libs)}')
for lib in libs:
    import json
    words = json.loads(lib.words) if lib.words else []
    print(f"  {lib.id}: {lib.name} ({len(words)} words)")
db.close()
