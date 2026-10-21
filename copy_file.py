# Topic: Copy one file into another
with open("src.txt", "w") as f:
    f.write("Copy me\nplease\n")
with open("src.txt") as s, open("dst.txt", "w") as d:
    d.write(s.read())
print(open("dst.txt").read())
