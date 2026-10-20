# Topic: input() always returns a string
x = input("Enter a number: ")
print(type(x))  # it is str, even if you typed digits
print(x + x)  # strings join: "55"
