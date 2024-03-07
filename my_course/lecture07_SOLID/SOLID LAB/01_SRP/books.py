from typing import List


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:
    def __init__(self, name: str):
        self.name = name
        self.books: List[Book] = []

    def add_book(self, book: Book):
        self.books.append(book)
        return f'{book.title} is added to Library {self.name}'

    def remove_book(self, book: Book):
        self.books.remove(book)
        f'{book.title} is removed from Library {self.name}'

    def find_book(self, title: str):
        book = next((b for b in self.books if b.title == title), None)
        if book is None:
            return f'{title} is not in the Library {self.name}.'
        return f'{book.title} is found.'


book = Book('Title1', 'Author1')
book2 = Book('Title2', 'Author2')
book3 = Book('Title3', 'Author3')
library1 = Library('Library1')
library2 = Library('Library2')
print(library1.add_book(book))
print(library1.add_book(book2))
print(library2.add_book(book3))
print(library1.find_book('Title1'))
print(library1.find_book('Semsa '))