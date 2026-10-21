# Topic: Search a word in a file
with open("s.txt", "w") as f:
    f.write("apple pie\nmango shake\napple juice\n")
with open("s.txt") as f:
    for no, line in enumerate(f, 1):
        if "apple" in line:
            print("Line", no, ":", line.strip())
