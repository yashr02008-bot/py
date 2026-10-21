# Topic: Nested dictionary
students = {
    "s1": {"name": "Amit", "marks": 80},
    "s2": {"name": "Riya", "marks": 92},
}
for sid, info in students.items():
    print(sid, info["name"], info["marks"])
