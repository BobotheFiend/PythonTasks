
principle = int(input("Enter amount you wish to borrow: "))
annualintrestrate = int(input("Enter the annual interest rate: "))
duration = int(input("Enter the duration of mortgage in years: "))

monthlyrate= annualintrestrate / 100 / 12
months = duration * 12

mortgage = principle * (monthlyrate * (1 + monthlyrate) ** months)//((1 + monthlyrate) ** months - 1)

print("Your monthly mortgage payment is = ",mortgage)
