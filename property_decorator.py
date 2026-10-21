# Topic: Getter and setter with @property
class Temp:
    def __init__(self, c):
        self._c = c
    @property
    def celsius(self):
        return self._c
    @celsius.setter
    def celsius(self, v):
        if v < -273:
            raise ValueError("Too cold!")
        self._c = v
t = Temp(30)
t.celsius = 40
print(t.celsius)
