class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def check_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: ₹{self.balance}")


Example usage
def main():
    print("Welcome to Simple Bank!")
    name = input("Enter account holder name: ")
    account = BankAccount(name)

    while True:
        print("\nChoose an option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: ₹"))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: ₹"))
            account.withdraw(amount)
        elif choice == "3":
            account.check_balance()
        elif choice == "4":
            print("Thank you for using Simple Bank!")
            break
        else:
            print("Invalid option. Please try again.")


if name == "__main__":
    main()
