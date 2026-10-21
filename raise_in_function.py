# Topic: raise inside a function
def set_marks(m):
    if m < 0 or m > 100:
        raise ValueError("Marks must be 0 to 100")
    return m
for m in [85, 150]:
    try:
        print("OK:", set_marks(m))
    except ValueError as e:
        print("Error:", e)
