# Importing required modules
from colorama import Fore, Style, init  # colorama is used to make terminal output colorful

init(autoreset=True)  # This will reset the color after every print automatically

# ATM CLASS DEFINITION
class ATM:
    def __init__(self):
        """
        This is the constructor method.
        It initializes the ATM with:
        - A default PIN (used for user authentication)
        - A default balance of Rs. 1000
        - A boolean 'is_authenticated' that keeps track if user has entered the correct PIN
        """
        self.pin = "1234"  # Default PIN
        self.balance = 1000.0  # Initial balance
        self.is_authenticated = False  # User not authenticated until correct PIN is entered

    def authenticate(self, input_pin):
        """
        Compares the entered PIN with the actual PIN.
        If correct, sets 'is_authenticated' to True.
        """
        if input_pin == self.pin:
            self.is_authenticated = True
            print(Fore.GREEN + "✅ PIN verified successfully.\n")
        else:
            print(Fore.RED + "❌ Incorrect PIN. Please try again.\n")

    def check_balance(self):
        """
        Displays the current account balance.
        Only works if the user has successfully entered the correct PIN.
        """
        if self.is_authenticated:
            print(Fore.CYAN + f"💰 Current Balance: Rs. {self.balance:.2f}\n")
        else:
            print(Fore.YELLOW + "🔒 Please enter the correct PIN first.\n")

    def deposit(self, amount):
        """
        Adds the given amount to the balance if:
        - The user is authenticated
        - The amount is positive
        """
        if self.is_authenticated:
            if amount > 0:
                self.balance += amount
                print(Fore.GREEN + f"📥 Rs. {amount:.2f} deposited successfully.\n")
                print(Fore.CYAN + f"💰 New Balance: Rs. {self.balance:.2f}\n")
            else:
                print(Fore.RED + "⚠️ Deposit amount must be positive.\n")
        else:
            print(Fore.YELLOW + "🔒 Please enter the correct PIN first.\n")

    def withdraw(self, amount):
        """
        Deducts the given amount from the balance if:
        - The user is authenticated
        - The amount is positive
        - The amount does not exceed the current balance
        """
        if self.is_authenticated:
            if amount <= 0:
                print(Fore.RED + "⚠️ Withdrawal amount must be positive.\n")
            elif amount > self.balance:
                print(Fore.RED + "🚫 Insufficient balance.\n")
            else:
                self.balance -= amount
                print(Fore.GREEN + f"💸 Rs. {amount:.2f} withdrawn successfully.\n")
                print(Fore.CYAN + f"💰 New Balance: Rs. {self.balance:.2f}\n")
        else:
            print(Fore.YELLOW + "🔒 Please enter the correct PIN first.\n")

    def exit(self):
        """
        Prints a goodbye message and returns False.
        This is used to break the main menu loop.
        """
        print(Fore.MAGENTA + "👋 Thank you for using the ATM. Goodbye!")
        return False

    def menu(self):
        """
        Main method that handles user interaction:
        - Takes PIN input
        - Shows 3 attempts for PIN
        - Displays ATM options after successful authentication
        - Executes user choice using conditionals
        """
        print(Fore.BLUE + "🏧 Welcome to the ATM. Please enter your PIN to continue.")
        attempts = 0  # Counter to track wrong attempts

        # Allow 3 attempts to enter correct PIN
        while attempts < 3:
            input_pin = input(Fore.BLUE + "🔢 Please enter your 4-digit PIN: ")
            if input_pin == self.pin:
                self.is_authenticated = True
                print(Fore.GREEN + "✅ PIN verified successfully.\n")
                break
            else:
                attempts += 1
                print(Fore.RED + f"❌ Incorrect PIN. Attempts left: {3 - attempts}.\n")
        else:
            print(Fore.RED + "🔐 Too many incorrect attempts. Exiting...\n")
            return  # Exit if 3 attempts fail

        # If PIN is correct, show menu options
        while True:
            print(Fore.BLUE + "\n========== 🏧 ATM Menu ==========")
            print("1️⃣  Check Balance")
            print("2️⃣  Deposit")
            print("3️⃣  Withdraw")
            print("4️⃣  Exit")

            choice = input(Fore.BLUE + "👉 Please select an option (1-4): ")

            if choice == "1":
                self.check_balance()  # Show balance
            elif choice == "2":
                try:
                    amount = float(input(Fore.GREEN + "💵 Enter the amount to deposit: "))
                    self.deposit(amount)
                except ValueError:
                    print(Fore.RED + "❌ Invalid input. Please enter a valid number.\n")
            elif choice == "3":
                try:
                    amount = float(input(Fore.YELLOW + "💸 Enter the amount to withdraw: "))
                    self.withdraw(amount)
                except ValueError:
                    print(Fore.RED + "❌ Invalid input. Please enter a valid number.\n")
            elif choice == "4":
                if not self.exit():  # Exit the loop
                    break
            else:
                print(Fore.RED + "⚠️ Invalid selection. Please choose between 1 to 4.\n")

# START THE PROGRAM
# This will run only if this file is executed directly, not if imported elsewhere
if __name__ == "__main__":
    atm = ATM()  # Create a new ATM object
    atm.menu()   # Start the menu interaction
