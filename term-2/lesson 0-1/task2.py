class Book:
    def __init__(self, title: str, author: str, year: int) -> None:
        self.title = title
        self.author = author
        self.year = year
    
    def __str__(self) -> str:
        return f"Название {self.title}, Автор: {self.author}, Год {self.year}"

book = Book("Название книги", "автор книги", 2026)
print(book)