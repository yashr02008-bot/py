# Topic: Pattern - alphabets
for i in range(5):
    for j in range(i + 1):
        print(chr(65 + j), end=" ")  # chr(65) = 'A'
    print()
