# Topic: Library book issue system
class Book:
    def __init__(self, title):
        self.title = title
        self.issued = False
    def issue(self):
        if self.issued:
            print(self.title, "already issued")
        else:
            self.issued = True
            print(self.title, "issued")
    def give_back(self):
        self.issued = False
        print(self.title, "returned")
b = Book("Python Basics")
b.issue(); b.issue(); b.give_back()
