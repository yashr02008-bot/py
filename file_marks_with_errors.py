# Topic: Mini project - read marks safely
with open("bad.txt", "w") as f:
    f.write("80\nabc\n90\n\n70\n")
total = 0
with open("bad.txt") as f:
    for line in f:
        try:
            total += int(line)
        except ValueError:
            print("Skipped bad line:", repr(line.strip()))
print("Total:", total)
