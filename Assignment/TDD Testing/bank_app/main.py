from pybank import *

print ("""
        Welcome to PY Bank

1. To get Started
0. To Leave
3. Calculate Balance
4. Apply Interest
5. Summary
6. Exit : """
)
in_bank_app = True
while (in_bank_app):

    user_input = int(input("Select an option: "))
    match user_input:
        case "1":
            email = input("Enter email: ")
            password = input("Enter password: ")
            if validate_email(email) and is_strong_password(password):
                print("Registration successful")
            else:
                print("Registration failed")
                
        case "2":
            email = input("Enter email: ")
            password = input("Enter password: ")
            if validate_email(email) and is_strong_password(password):
                print("Login successful")
            else:
                print("Login failed")
                
        case "3":
            transactions = []
            amount = float(input("Enter amount or 0 to stop: "))
            while amount != 0:
                transactions.append(amount)
                amount = float(input("Enter amount or 0 to stop: "))
            total_transactions = calculate_balance(transactions)
            print("Your balance is ", total_transactions)
                
          
