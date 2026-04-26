#annual intrest 

balance = float(input("Enter Balance: "))       
interestRate = float(input("Enter Annual% Interest Rate: "))

annual_intrest_rate = interestRate*12/1200
interest = balance * annual_intrest_rate

print(f"The intrest for next month = {interest}")
