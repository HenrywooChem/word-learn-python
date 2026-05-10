import database
print([x for x in dir(database) if not x.startswith("_")])
