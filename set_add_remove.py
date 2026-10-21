# Topic: Set add() and remove()
s = {1, 2, 3}
s.add(4)
s.remove(2)
s.discard(99)  # no error if missing
print(s)
