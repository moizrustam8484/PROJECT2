# models/author.py

class Author:
    def __init__(self, first_name, last_name, email, joined_date):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.joined_date = joined_date

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        return Author(**data)
