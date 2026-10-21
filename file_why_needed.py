# Topic: Why files - permanent storage
data = "Saved forever"  # variables vanish when program ends
f = open("saved.txt", "w")
f.write(data)
f.close()
print("Saved to file. Check saved.txt")
