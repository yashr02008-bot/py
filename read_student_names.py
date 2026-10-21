# Topic: Read student names from file
with open("students.txt", "w") as f:
    f.write("Amit\nRiya\nSam\nNeha\n")
with open("students.txt") as f:
    for line in f:
        print("Student:", line.strip())
