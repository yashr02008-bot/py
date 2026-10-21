# Topic: Split list into even and odd
a = list(range(1, 11))
evens = [x for x in a if x % 2 == 0]
odds = [x for x in a if x % 2 != 0]
print(evens, odds)
