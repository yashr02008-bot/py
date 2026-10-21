# Topic: Mini project - marks report from file
with open("m.csv", "w") as f:
    f.write("Amit,80\nRiya,92\nSam,67\n")
total, count = 0, 0
with open("m.csv") as f:
    for line in f:
        name, marks = line.strip().split(",")
        print(f"{name:<6}{marks}")
        total += int(marks)
        count += 1
print("Class average:", round(total / count, 2))
