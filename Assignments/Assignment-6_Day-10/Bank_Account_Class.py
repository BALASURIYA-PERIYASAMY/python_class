class BankAccount:
    def __init__(self, owner, account_number, balance=0):
        self.owner =owner
        self.act_no = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Deposited {amount}. Balance{self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            print(f"Withdrawn {amount}. Balance: {self.amount}")
        else:
            print("Insufficient balance!")

    def show_balance(self):
        print(f"Balance: {self.balance}")

acc1 = BankAccount('Rahul', 'ACC001', 1000)
acc1.show_balance()       # Balance: 1000
acc1.deposit(500)         # Deposited 500. Balance: 1500
acc1.withdraw(200)        # Withdrawn 200. Balance: 1300
acc1.withdraw(2000)       # Insufficient balance!
