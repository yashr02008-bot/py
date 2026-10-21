# Topic: Keep asking until valid number
while True:
    try:
        n = int(input("Enter a number: "))
        break  # valid, leave the loop
    except ValueError:
        print("Invalid! Try again.")
print("You entered", n)
