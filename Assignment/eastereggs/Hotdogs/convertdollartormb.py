# CHANGE DOLLAR TO RMB AND RMB TO DOLLAR


answer = bool(input("Exchage rate of $ to RMB = 1 Dollar$ = 6.88 Rmb (True/False) : "))

if answer==False: 
    print("Goodbye")        

if answer == True: 
    value = int(input("Enter exchage value $ or RMB: "))
              
dollarToRmb = value*6.88
rmbToDollar = value*0.15

convert0 = dollarToRmb
convert1 = rmbToDollar


choice1 = int(input("Input 0 to convert from $ to RMB or press 1 to skip: "))

choice2 = int(input("Input 1 to convert from RMB to $ : "))

if choice1==0:
    print(f"The exchange rate to RMB = {convert0}")
else:
    print("Skipping...")

if choice2==1:
    print(f"The exchange rate to Dollar = {convert1}")
else: 
    print("End")
