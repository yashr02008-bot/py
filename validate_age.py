# Topic: Validate age with exceptions
def check_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be a number")
    if age < 18:
        raise ValueError("Under 18")
    return "Allowed"
for a in [20, 15, "x"]:
    try:
        print(check_age(a))
    except (TypeError, ValueError) as e:
        print("Error:", e)
