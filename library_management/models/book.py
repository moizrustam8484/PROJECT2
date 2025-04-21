# models/book.py

class Book:
    def __init__(self, name, author, category, published_date):
        self.name = name
        self.author = author
        self.category = category
        self.published_date = published_date

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        return Book(**data)
