class BankAccount:

    def __init__(self, owner, balance, pin):
        self.owner    = owner
        self.__balance = balance   # private
        self.__pin     = pin       # private

    def get_balance(self, pin):
        # return balance if pin matches, else 'Incorrect PIN'
        if self.__pin == pin:
            return self.__balance
        else:
            return 'Incorrect PIN'

    def deposit(self, amount):
        # validate amount > 0, then add to __balance
        # raise ValueError if amount <= 0
        if amount>0:
            self.__balance = self.__balance + amount
            print(f"Deposited {amount}")
        else:
            raise ValueError("Amount must be positive'")

    def withdraw(self, amount, pin):
        # check pin, then check balance, then deduct
        # raise appropriate errors
        if self.__pin == pin:
            if self.__balance >= amount:
                self.__balance -=amount
                print(f"Withdraw {amount}")

acc = BankAccount('Rahul', 10000, '1234')
print(acc.get_balance('1234'))    # 10000
print(acc.get_balance('0000'))    # Incorrect PIN
acc.deposit(5000)                 # Deposited ₹5000
acc.withdraw(3000, '1234')        # Withdrawn ₹3000
# print(acc.__balance)            # AttributeError — private!
