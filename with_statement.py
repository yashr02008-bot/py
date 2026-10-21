# Topic: with statement - auto close
with open("w.txt", "w") as f:
    f.write("Best practice")
print("File closed automatically:", f.closed)
