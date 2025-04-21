# managers/author_manager.py

import json
from datetime import datetime
from models.author import Author
import os

class AuthorManager:
    def __init__(self, filepath='data/authors.json'):
        self.filepath = filepath
        self.authors_list = []
        self.load_authors()

    def load_authors(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, 'r') as f:
                self.authors_list = [Author.from_dict(a) for a in json.load(f)]

    def save_authors(self):
        with open(self.filepath, 'w') as f:
            json.dump([a.to_dict() for a in self.authors_list], f, indent=4)

    def add_author(self):
        print("\n--- Add Author ---")
        fn = input("First Name: ")
        ln = input("Last Name: ")
        em = input("Email: ")
        jd = datetime.now().strftime("%Y-%m-%d")
        self.authors_list.append(Author(fn, ln, em, jd))
        self.save_authors()
        print("Author added.")

    def remove_author(self):
        email = input("Enter author's email to remove: ")
        self.authors_list = [a for a in self.authors_list if a.email != email]
        self.save_authors()
        print("Author removed.")

    def update_author(self):
        email = input("Enter author's email to update: ")
        for author in self.authors_list:
            if author.email == email:
                author.first_name = input("New First Name: ")
                author.last_name = input("New Last Name: ")
                self.save_authors()
                print("Author updated.")
                return
        print("Author not found.")

    def view_authors(self):
        print("\n--- Authors ---")
        for a in self.authors_list:
            print(f"{a.first_name} {a.last_name} - {a.email}")
