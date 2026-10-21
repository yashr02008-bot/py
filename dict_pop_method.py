# Topic: pop()
d = {"a": 1, "b": 2}
print(d.pop("a"))  # removes and returns the value
print(d)
print(d.pop("zzz", "not found"))
