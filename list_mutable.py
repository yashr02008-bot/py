# Topic: Lists are mutable
a = [1, 2, 3]
a[0] = 99  # change an item
print(a)
s = "abc"
# s[0] = "x" -> error: strings are immutable
