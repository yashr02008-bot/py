# Topic: Incorrect indentation = error
code = "if True:\nprint('hi')"  # print is not indented
try:
    exec(code)
except IndentationError as e:
    print("IndentationError caught:", e.msg)
