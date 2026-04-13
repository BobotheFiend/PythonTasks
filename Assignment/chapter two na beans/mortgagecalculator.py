
principle = int(input("Enter amount you wish to borrow: "))
annual_intrest_rate = int(input("Enter the annual interest rate: "))
duration = int(input("Enter the duration of mortgage in years: "))

monthly_rate= annualintrestrate / 100 / 12
months = duration * 12

mortgage = principle * (monthly_rate * (1 + monthly_rate) ** months)//((1 + monthly_rate) ** months - 1)

print("Your monthly mortgage payment is = ",mortgage)
