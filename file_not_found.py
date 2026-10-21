# Topic: FileNotFoundError
try:
    open("missing_file.txt")
except FileNotFoundError:
    print("File does not exist")
