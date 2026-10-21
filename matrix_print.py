# Topic: Print a matrix neatly
m = [[1, 2, 3], [4, 5, 6]]
for row in m:
    for val in row:
        print(val, end="\t")
    print()
