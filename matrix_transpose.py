# Topic: Matrix transpose
m = [[1, 2, 3], [4, 5, 6]]
t = [[m[i][j] for i in range(len(m))] for j in range(len(m[0]))]
print(t)
