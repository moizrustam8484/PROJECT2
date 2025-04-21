# managers/membership_manager.py

class MembershipManager:
    def __init__(self):
        self.memberships = {
            "SILVER": {"price": 10, "books": 2},
            "GOLD": {"price": 30, "books": 6},
            "PLATINUM": {"price": 50, "books": float('inf')}
        }
        self.user_membership = {}

    def buy_membership(self, email):
        print("\n--- Membership Plans ---")
        for name, info in self.memberships.items():
            books = "Unlimited" if info["books"] == float('inf') else info["books"]
            print(f"{name} - ${info['price']} - {books} books")
        choice = input("Choose plan (SILVER/GOLD/PLATINUM): ").upper()
        if choice in self.memberships:
            self.user_membership[email] = choice
            print(f"Membership purchased: {choice}")
        else:
            print("Invalid plan.")

    def check_membership(self, email):
        return email in self.user_membership
