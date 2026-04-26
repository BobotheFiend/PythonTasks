#shipping weight cost 


num = int(input("Enter the weight of the package: "))

if num > 0 and num <= 2 :
    print(f" The package weighs {num}kg and it costs $2.5 to ship")

elif num > 2 and num <= 4:
    print(f" The package weighs {num}kg and it costs $4.5 to ship")

elif num > 4 and num <= 10:
    print(f" The package weighs {num}kg and it costs $7.5 to ship")
     
elif num > 10 and num <= 20:
    print(f" The package weighs {num}kg and it costs $10.5 to ship")

elif num > 20:
    print(f" The package weighs {num}kg, The pacakge cannot be shipped!")
