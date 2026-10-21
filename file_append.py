# Topic: Append mode "a"
with open("log.txt", "w") as f:
    f.write("First\n")
with open("log.txt", "a") as f:  # a = add to the end
    f.write("Second\n")
print(open("log.txt").read())
