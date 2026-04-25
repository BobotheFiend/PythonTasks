# distance between two points


x1 = int(input("Enter your x1: "))
x2 = int(input("Enter your x2: "))

y1 = int(input("Enter your y1: "))
y2 = int(input("Enter your y2: "))

xOne = x2-x1
yOne = y2-y1
xSq = xOne*xOne
ySq = yOne*yOne
addBoth = xSq+ySq
squareAnswer = addBoth**0.5

print(f"The distance between them = {squareAnswer}")
