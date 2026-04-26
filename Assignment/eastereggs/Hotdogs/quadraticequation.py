#the quadratic equation

a = int(input("Enter for a: "))        
b = int(input("Enter for b: "))
c = int(input("Enter for c: "))

bac = (b*b)-4*a*c
bacSquPlus = -b + math.sqrt((bac)/(2*a))
bacSquMinus = -b - math.sqrt((bac)/2*a)

if (bac > 0.0):
    print(f"the root = {bacSquPlus} and {bacSquMinus}")
   
elif (bac == 0.0):
    print(f"the root = {bacSquPlus}")

elif (bac != 0.0):
    print("No Real Root")
