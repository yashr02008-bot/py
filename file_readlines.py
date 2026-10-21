# Topic: readlines() - list of lines
with open("demo.txt", "w") as f:
    f.write("one\ntwo\nthree\n")
with open("demo.txt") as f:
    lines = f.readlines()
print(lines)
