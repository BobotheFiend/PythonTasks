principle = int(input("Enter the principle: "))
rate = int(input("Enter the rate in %: "))
time = int(input("Enter the time in years: "))

formulasi = (principle*rate*time)/100

amount = principle + formulasi

print("The SI = ", formulasi, "and the Amount = ", amount)
