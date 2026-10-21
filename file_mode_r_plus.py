# Topic: r+ mode (read and write)
with open("rp.txt", "w") as f:
    f.write("Hello")
with open("rp.txt", "r+") as f:
    print(f.read())
    f.write(" World")  # added after reading
    f.seek(0)  # go back to start
    print(f.read())
