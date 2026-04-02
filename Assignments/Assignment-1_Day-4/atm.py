pin = 1234
balance = 5000

use_pin=int(input("Enter The PIN: "))

if use_pin == pin:
    print("PIN Verified:")

    amount = float(input("Enter The Withdraw amount: "))

    if amount<0:
        print("Enter Positive Numbers Only.!")
    elif amount > balance:
        print("Insuficient Balance.!")
    else:
        balance=balance - amount
        print("Withdraw Successdul.")
        print("Remaining Balance: ",balance)

else:
    print("Incorrect PIN.!")