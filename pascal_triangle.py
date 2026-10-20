# Topic: Pattern - Pascal's triangle
n = 6
for i in range(n):
    val = 1
    print(" " * (n - i), end="")
    for j in range(i + 1):
        print(val, end=" ")
        val = val * (i - j) // (j + 1)
    print()
