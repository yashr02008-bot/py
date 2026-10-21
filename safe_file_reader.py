# Topic: Safe file reader
def read_file(name):
    try:
        with open(name) as f:
            return f.read()
    except FileNotFoundError:
        return "File not found: " + name
print(read_file("nothing.txt"))
