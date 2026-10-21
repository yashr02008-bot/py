# Topic: Phonebook with dictionary
book = {"Amit": "9876500001", "Riya": "9876500002"}
book["Sam"] = "9876500003"
name = "Riya"
print(name, "->", book.get(name, "Not found"))
