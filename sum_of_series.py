# Topic: Sum of series 1+2+3+...+N and squares
n = 5
s1 = sum_sq = 0
for i in range(1, n + 1):
    s1 += i
    sum_sq += i * i
print("Sum:", s1, "Sum of squares:", sum_sq)
