principle = int(input("Enter the principle: "))
rate = int(input("Enter the rate in %: "))
time = int(input("Enter the time in years: "))

formula_si = (principle*rate*time)/100

amount = principle + formula_si

print("The SI = ", formula_si, "and the Amount = ", amount)
