# do everything you learned this week

from __future__ import annotations
import copy
from dataclasses import dataclass, field
from typing import Iterator


@dataclass
class Book:
    title: str
    author: str
    pages: int
    
    def __repr__(self) -> str:
        return f"Book({self.title!r}, {self.author!r}, {self.pages}pp)"

#iterate through books
# get first few books
# print books
# check if book is in bookshelf
# combine bookshelfs
# get next item in bookshelf lazily

class Bookshelf():
    def __init__(self, name, books = None):
        
        if books == None:
            self.books = []
        self.name = name
        self.idx = 0
    def __iter__(self):
        self._idx = 0
        return self
    
    def __repr__(self):
        return f"Shelf {self.name}, {len(shelf)} books"
    def __next__(self):
        if self._idx >= len(self.books):
            raise StopIteration
        book = self.books[self._idx]
        self._idx += 1
        return book

    def add_book(self, book : Book):
        self.books.append(book)
        print(f"Successfully added {book}")
    
    def __len__(self):
        return len(self.books)
    
    def __getitem__(self, key):
        return self.books[key]
    
    def __contains__(self, title: str) -> bool:
        return any(b.title == title for b in self.books)

b1 = Book("Book1", "Kelvin", 56)
b2 = Book("Book2", "Kelvin", 56)
b3 = Book("Book3", "Kelvin", 56)
print(b1) # print book

shelf = Bookshelf("example")
print(shelf)
shelf.add_book(b1)
shelf.add_book(b2)
shelf.add_book(b3)
print(shelf)

print(shelf.books) # print the books 
print("Book1" in shelf) # find a book
for i in shelf: # iterate through the shelf
    print(i)
