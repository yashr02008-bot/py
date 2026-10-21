# Topic: Count words in a file
with open("t.txt", "w") as f:
    f.write("Python is fun\nFiles are easy\n")
with open("t.txt") as f:
    print("Words:", len(f.read().split()))
