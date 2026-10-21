# Topic: Sum numbers stored in a file
with open("n.txt", "w") as f:
    f.write("10\n20\n30\n")
with open("n.txt") as f:
    total = sum(int(line) for line in f)
print("Total:", total)
