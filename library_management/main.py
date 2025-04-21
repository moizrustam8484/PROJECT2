# main.py

from managers.user_manager import UserManager
from managers.author_manager import AuthorManager
from managers.book_manager import BookManager
from managers.membership_manager import MembershipManager
from datetime import datetime

user_manager = UserManager()
author_manager = AuthorManager()
book_manager = BookManager()
membership_manager = MembershipManager()

def display_menu():
    print("\n==== Welcome to Library Management System ====")
    print("1. Admin Login")
    print("2. User Login")
    print("3. Sign Up as User")
    print("4. Exit")

def admin_menu():
    while True:
        print("\n--- Admin Menu ---")
        print("1. Add Author")
        print("2. Remove Author")
        print("3. Update Author")
        print("4. Add Book")
        print("5. Remove Book")
        print("6. Update Book")
        print("7. Add User")
        print("8. Remove User")
        print("9. View All Users")
        print("10. Logout")
        choice = input("Enter choice: ")
        if choice == '1':
            author_manager.add_author()
        elif choice == '2':
            author_manager.remove_author()
        elif choice == '3':
            author_manager.update_author()
        elif choice == '4':
            book_manager.add_book()
        elif choice == '5':
            book_manager.remove_book()
        elif choice == '6':
            book_manager.update_book()
        elif choice == '7':
            user_manager.add_user_interactive()
        elif choice == '8':
            user_manager.remove_user()
        elif choice == '9':
            user_manager.view_users()
        elif choice == '10':
            break

def user_menu(user_email):
    user = user_manager.get_user_by_email(user_email)
    if not membership_manager.check_membership(user_email):
        print("\nYou need to buy a membership first.")
        membership_manager.buy_membership(user_email)
    else:
        print("\nMembership already active.")
    while True:
        print("\n--- User Menu ---")
        print("1. View Categories")
        print("2. View Authors")
        print("3. View Books")
        print("4. Borrow Book")
        print("5. Logout")
        choice = input("Enter choice: ")
        if choice == '1':
            book_manager.display_categories()
        elif choice == '2':
            author_manager.view_authors()
        elif choice == '3':
            book_manager.view_books()
        elif choice == '4':
            book_manager.borrow_book(user_email)
        elif choice == '5':
            print("\nThanks for your purchase. Have a nice day!")
            break

# Main loop
while True:
    display_menu()
    option = input("Enter option: ")
    if option == '1':
        email = input("Admin Email: ")
        password = input("Admin Password: ")
        result = user_manager.login_admin(email, password)
        if result:
            admin_menu()
        else:
            print("Invalid admin credentials.")
    elif option == '2':
        while True:
            email = input("User Email: ")
            password = input("User Password: ")
            if user_manager.login_user(email, password):
                user_menu(email)
                break
            else:
                print("Invalid credentials. Please try again.")
    elif option == '3':
        user_manager.signup_user()
    elif option == '4':
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid option.")
