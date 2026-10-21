# Topic: Mini project - grade book (list + dict + tuple)
book = {"Amit": (80, 90), "Riya": (95, 88)}
for name, (m1, m2) in book.items():
    print(name, "average:", (m1 + m2) / 2)
