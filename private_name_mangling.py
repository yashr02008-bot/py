# Topic: How private attributes are really stored
class Secret:
    def __init__(self):
        self.__code = 1234
s = Secret()
print(s._Secret__code)  # Python renames __code
