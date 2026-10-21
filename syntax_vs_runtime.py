# Topic: Syntax error vs runtime exception
try:
    eval("print('hi'")  # missing bracket = syntax error
except SyntaxError:
    print("Syntax error: found before running")
try:
    int("abc")  # valid code, fails while running
except ValueError:
    print("Runtime exception: found while running")
