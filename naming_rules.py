# Topic: Variable naming rules
my_name = "ok"  # letters and underscore are fine
name2 = "ok"  # digits allowed, but not at the start
_hidden = "ok"  # can start with underscore
print(my_name, name2, _hidden)
# 2name = 1   -> wrong: starts with digit
# my-name = 1 -> wrong: dash not allowed
# class = 1   -> wrong: keyword
