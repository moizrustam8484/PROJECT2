# models/membership.py

class Membership:
    def __init__(self, plan_name, plan_price, allowed_books):
        self.plan_name = plan_name
        self.plan_price = plan_price
        self.allowed_books = allowed_books

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        return Membership(**data)
