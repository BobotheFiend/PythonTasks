# program that reads in an investemnt amount, annual interest rate, and number of years


investAmount = float(input("Enter amount: "))        
annualIntrestRate = float(input("Enter Annual% Interest Rate: "))
years = float(input("Enter years: "))

monthlyIntrest = annualIntrestRate/1200
futureInvestment = investAmount*(1+(monthlyIntrest**(years*12)))

print(f"The future investment value = {futureInvestment}")
