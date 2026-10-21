# Topic: Linear search in a list
a = [4, 8, 15, 16, 23]
target = 15
for i, v in enumerate(a):
    if v == target:
        print("Found at index", i)
        break
else:
    print("Not found")
