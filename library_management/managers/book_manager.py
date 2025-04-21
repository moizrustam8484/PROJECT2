# managers/book_manager.py

import json
from models.book import Book
from datetime import datetime
import os

class BookManager:
    def __init__(self, filepath='data/books.json'):
        self.filepath = filepath
        self.books = []
        self.load_books()

    def load_books(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, 'r') as f:
                self.books = [Book.from_dict(b) for b in json.load(f)]

    def save_books(self):
        with open(self.filepath, 'w') as f:
            json.dump([b.to_dict() for b in self.books], f, indent=4)

    def add_book(self):
        print("\n--- Add Book ---")
        name = input("Book Name: ")
        author = input("Author: ")
        category = input("Category (comics, horror, sad): ")
        pub_date = input("Published Date (YYYY-MM-DD): ")
        self.books.append(Book(name, author, category, pub_date))
        self.save_books()
        print("Book added.")

    def remove_book(self):
        name = input("Enter book name to remove: ")
        self.books = [b for b in self.books if b.name != name]
        self.save_books()
        print("Book removed.")

    def update_book(self):
        name = input("Enter book name to update: ")
        for b in self.books:
            if b.name == name:
                b.author = input("New Author: ")
                b.category = input("New Category: ")
                b.published_date = input("New Published Date: ")
                self.save_books()
                print("Book updated.")
                return
        print("Book not found.")

    def view_books(self):
        print("\n--- Books ---")
        for b in self.books:
            print(f"{b.name} by {b.author} ({b.published_date}) - Category: {b.category}")

    def display_categories(self):
        print("\nAvailable Categories:")
        print("1. Comics")
        print("2. Horror")
        print("3. Sad")

    def borrow_book(self, user_email):
        self.view_books()
        book_name = input("Enter book to borrow: ")
        for b in self.books:
            if b.name == book_name:
                self.books.remove(b)
                self.save_books()
                print(f"You borrowed: {b.name}")
                return
        print("Book not available.")
