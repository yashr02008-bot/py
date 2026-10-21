# Topic: Mini project - notes app
notes = ["Buy milk", "Study Python", "Call mom"]
with open("notes.txt", "w") as f:
    for n in notes:
        f.write(n + "\n")
print("Your notes:")
with open("notes.txt") as f:
    for i, line in enumerate(f, 1):
        print(f"{i}. {line.strip()}")
