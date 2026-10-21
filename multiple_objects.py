# Topic: Many objects from one class
class Book:
    def __init__(self, title, pages):
        self.title, self.pages = title, pages
books = [Book("Python", 300), Book("Java", 450), Book("C", 250)]
for b in books:
    print(b.title, "-", b.pages, "pages")
