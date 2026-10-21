# Topic: See the error message using "as e"
try:
    [1, 2][5]
except IndexError as e:
    print("Message:", e)
    print("Type:", type(e).__name__)
