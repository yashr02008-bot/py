# Topic: Count lines in a file
with open("t.txt", "w") as f:
    f.write("a\nb\nc\nd\n")
with open("t.txt") as f:
    print("Lines:", len(f.readlines()))
