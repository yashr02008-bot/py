# Topic: Student marks dictionary
marks = {"Maths": 90, "Science": 85, "English": 78}
print("Total:", sum(marks.values()))
best = max(marks, key=marks.get)
print("Best subject:", best)
