# managers/user_manager.py

import json
from datetime import datetime
from models.user import User
import os

class UserManager:
    def __init__(self, filepath='data/users.json'):
        self.filepath = filepath
        self.users_list = []
        self.load_users_from_disk()

        if not any(user.role == 'admin' for user in self.users_list):
            admin = User("Admin", "User", "admin@lib.com", "admin123", datetime.now().strftime("%Y-%m-%d"), "admin")
            self.users_list.append(admin)
            self.save_users_to_disk()

    def load_users_from_disk(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, 'r') as f:
                try:
                    data = json.load(f)
                    self.users_list = [User.from_dict(u) for u in data]
                except json.JSONDecodeError:
                    self.users_list = []
        else:
            self.users_list = []

    def save_users_to_disk(self):
        with open(self.filepath, 'w') as f:
            json.dump([user.to_dict() for user in self.users_list], f, indent=4)

    def signup_user(self):
        print("\n--- User Sign Up ---")
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        email = input("Email: ")
        password = input("Password: ")
        joined = datetime.now().strftime("%Y-%m-%d")
        new_user = User(first_name, last_name, email, password, joined)
        self.users_list.append(new_user)
        self.save_users_to_disk()
        print("Signup successful!")

    def login_user(self, email, password):
        for user in self.users_list:
            if user.email == email and user.password == password and user.role == "user":
                return True
        return False

    def login_admin(self, email, password):
        for user in self.users_list:
            if user.email == email and user.password == password and user.role == "admin":
                return True
        return False

    def add_user_interactive(self):
        self.signup_user()

    def remove_user(self):
        email = input("Enter email to remove: ")
        self.users_list = [user for user in self.users_list if user.email != email]
        self.save_users_to_disk()
        print("User removed successfully.")

    def view_users(self):
        print("\n--- All Users ---")
        for user in self.users_list:
            print(f"{user.first_name} {user.last_name} - {user.email} - {user.role}")

    def get_user_by_email(self, email):
        for user in self.users_list:
            if user.email == email:
                return user
        return None
