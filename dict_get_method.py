# Topic: get() avoids errors
d = {"apple": 5}
print(d.get("apple"))
print(d.get("mango"))  # None, no error
print(d.get("mango", 0))
