# Topic: readline() - one line at a time
with open("demo.txt", "w") as f:
    f.write("one\ntwo\nthree\n")
with open("demo.txt") as f:
    print(f.readline().strip())
    print(f.readline().strip())
