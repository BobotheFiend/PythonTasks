# 3 points of a triangle


x1 = int(input("Enter your x1: "))        
x2 = int(input("Enter your x2: "))
x3 = int(input("Enter your x3: ")) 

y1 = int(input("Enter your y1: "))
y2 = int(input("Enter your y2: ")) 
y3 = int(input("Enter your y3: "))

sideOne = x1*y1
sideTwo = x2*y2
sideThree = x3*y3

s = (sideOne+sideTwo+sideThree)/2
bracketOne = s-sideOne
bracketTwo = s-sideTwo
bracketThree = s-sideThree
bracket = bracketOne*bracketTwo*bracketThree
sBracket = s*bracket
area = float(sBracket**0.5)

print(f"The area = {area}")
