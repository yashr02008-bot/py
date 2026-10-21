# Topic: Tuple vs list
l = [1, 2, 3]
t = (1, 2, 3)
l.append(4)  # works
print(l, t)
print(l.__sizeof__() > t.__sizeof__())  # tuple uses less memory
