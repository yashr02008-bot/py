# Topic: Merge dictionaries
a, b = {"x": 1}, {"y": 2}
print({**a, **b})  # unpack both
print(a | b)  # Python 3.9+
