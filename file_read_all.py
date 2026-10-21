# Topic: read() - whole file
with open("demo.txt", "w") as f:
    f.write("Line A\nLine B\nLine C\n")
with open("demo.txt", "r") as f:
    print(f.read())
