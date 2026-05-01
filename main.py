# 6-m
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def read(self):
        print(f"{self.title} o'qilmoqda")

class EBook(Book):
    def __init__(self, title, author, pages, file_siza, format):
        super().__init__(title, author, pages)
        self.file_size = file_siza
        self.format = format

    def read(self):
        super().read()
        print(f"Format: {self.format}")
        print(f"Hajmi: {self.file_size}")

e1 = EBook("Python asoslari", "Yoldasheva", 250, 10, "PDF")
e1.read()
