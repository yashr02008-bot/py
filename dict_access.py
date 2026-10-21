# Topic: Access values by key
d = {"name": "Riya", "age": 20}
print(d["name"])  # key in []
print(d.get("age"))
print(d.get("city", "unknown"))  # default if missing
