# Topic: Change attributes of an object
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
p = Player("Ravi")
p.score += 10
p.score += 5
print(p.name, p.score)
