# Topic: Nested if - login check
user, pwd = "admin", "1234"
if user == "admin":
    if pwd == "1234":  # condition inside another condition
        print("Login success")
    else:
        print("Wrong password")
else:
    print("Unknown user")
