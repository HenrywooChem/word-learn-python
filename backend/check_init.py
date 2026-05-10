import database
# Check WordLibrary structure
lib = database.WordLibrary
cols = [c.name for c in lib.__table__.columns]
print("WordLibrary columns:", cols)
print()

# Check if there's a relationship to words
print("WordLibrary relationships:", [r.key for r in lib.__mapper__.relationships])
print()

# Check init_db logic - is it deduplicating?
import inspect
src = inspect.getsource(database.init_db)
print("init_db source:")
print(src)
