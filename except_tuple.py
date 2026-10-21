# Topic: One except for several errors
for v in ["5", "x", "0"]:
    try:
        print(10 / int(v))
    except (ValueError, ZeroDivisionError) as e:
        print("Problem:", e)
