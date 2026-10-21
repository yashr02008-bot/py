# Topic: Matrix addition
a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8]]
c = [[a[i][j] + b[i][j] for j in range(2)] for i in range(2)]
print(c)
