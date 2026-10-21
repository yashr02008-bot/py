# Topic: Remove duplicates from list
a = [1, 2, 2, 3, 3, 3, 4]
unique = []
for x in a:
    if x not in unique:
        unique.append(x)
print(unique)
