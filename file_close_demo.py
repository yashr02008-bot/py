# Topic: close() the file
f = open("c.txt", "w")
f.write("data")
print("Closed?", f.closed)
f.close()  # always close the file
print("Closed?", f.closed)
