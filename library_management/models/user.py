# models/user.py

class User:
    def __init__(self, first_name, last_name, email, password, joined_date, role="user"):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.joined_date = joined_date
        self.role = role

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        return User(**data)
