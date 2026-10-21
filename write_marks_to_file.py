# Topic: Write marks to a file
students = {"Amit": 80, "Riya": 92, "Sam": 67}
with open("marks.txt", "w") as f:
    for name, m in students.items():
        f.write(f"{name},{m}\n")
print(open("marks.txt").read())
