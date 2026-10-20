# Topic: Nested if - shopping discount
amount = 3500
member = True
if amount >= 3000:
    if member:
        print("Discount 20%")
    else:
        print("Discount 10%")
else:
    print("No discount")
