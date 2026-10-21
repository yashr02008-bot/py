# Topic: Print file with line numbers
with open("l.txt", "w") as f:
    f.write("first\nsecond\nthird\n")
with open("l.txt") as f:
    for i, line in enumerate(f, start=1):
        print(i, line.strip())
