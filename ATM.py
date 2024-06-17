import csv
import os

class ATM:
    def __init__(self):
        self.users = self.load_users()
        self.current_user = None
        self.main_menu()

    def load_users(self):
        users = {}
        if os.path.exists("users.csv"):
            with open("users.csv", mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:
                        name, password, balance = row
                        users[name] = {'password': password, 'balance': float(balance)}
        return users

    def save_users(self):
        with open("users.csv", mode='w', newline='') as file:
            writer = csv.writer(file)
            for name, data in self.users.items():
                writer.writerow([name, data['password'], data['balance']])

    def main_menu(self):
        while True:
            print("\nWelcome to the ATM")
            print("1. Open Account")
            print("2. Login")
            print("3. Exit")

            choice = input("Enter your choice: ")
            if choice == '1':
                self.open_account()
            elif choice == '2':
                self.login()
            elif choice == '3':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def open_account(self):
        name = input("Enter your name: ")
        if name in self.users:
            print("Account with this name already exists.")
            return

        password = input("Create a password: ")
        self.users[name] = {'password': password, 'balance': 0.0}
        self.save_users()
        print("Account created successfully!")

    def login(self):
        name = input("Enter your name: ")
        if name not in self.users:
            print("Account not found. Please open an account first.")
            return

        password = input("Enter your password: ")
        if self.users[name]['password'] == password:
            self.current_user = name
            self.user_menu()
        else:
            print("Incorrect password. Please try again.")

    def user_menu(self):
        while True:
            print(f"\nWelcome, {self.current_user}")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Transfer Money")
            print("5. Logout")

            choice = input("Enter your choice: ")
            if choice == '1':
                self.check_balance()
            elif choice == '2':
                self.deposit_money()
            elif choice == '3':
                self.withdraw_money()
            elif choice == '4':
                self.transfer_money()
            elif choice == '5':
                print("Logged out successfully.")
                self.current_user = None
                break
            else:
                print("Invalid choice. Please try again.")

    def check_balance(self):
        balance = self.users[self.current_user]['balance']
        print(f"Your current balance is: ${balance:.2f}")

    def deposit_money(self):
        amount = float(input("Enter the amount to deposit: "))
        if amount > 0:
            self.users[self.current_user]['balance'] += amount
            self.save_users()
            print(f"${amount:.2f} has been deposited. Your new balance is: ${self.users[self.current_user]['balance']:.2f}")
        else:
            print("Invalid amount. Please enter a positive number.")

    def withdraw_money(self):
        amount = float(input("Enter the amount to withdraw: "))
        if 0 < amount <= self.users[self.current_user]['balance']:
            self.users[self.current_user]['balance'] -= amount
            self.save_users()
            print(f"${amount:.2f} has been withdrawn. Your new balance is: ${self.users[self.current_user]['balance']:.2f}")
        else:
            print("Invalid amount or insufficient funds.")

    def transfer_money(self):
        recipient_name = input("Enter the recipient's name: ")
        if recipient_name not in self.users:
            print("Recipient account not found.")
            return

        amount = float(input("Enter the amount to transfer: "))
        if 0 < amount <= self.users[self.current_user]['balance']:
            self.users[self.current_user]['balance'] -= amount
            self.users[recipient_name]['balance'] += amount
            self.save_users()
            print(f"${amount:.2f} has been transferred to {recipient_name}. Your new balance is: ${self.users[self.current_user]['balance']:.2f}")
        else:
            print("Invalid amount or insufficient funds.")

if __name__ == "__main__":
    ATM()
