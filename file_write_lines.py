# Topic: writelines()
items = ["apple\n", "banana\n", "mango\n"]  # need \n yourself
with open("fruits.txt", "w") as f:
    f.writelines(items)
print(open("fruits.txt").read())
