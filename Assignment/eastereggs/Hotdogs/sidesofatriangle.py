#Enter the sides of a triangle to determine wheter it is equilateral, isosceles, or scalene, using sides a,b,c

a = int(input("Enter side one: "))
b = int(input("Enter side two: "))
c = int(input("Enter side three: "))
        
if a+b > c and a+c > b and c+b > a: 
    print("It is a valid triangle");
else:
    print("It is not a valid triangle")

if a == b and b == c:
   print(f" = Your triangle is an Equilateral")
elif a == b or b == c or c == a:
   print(f" = Your triangle is an Isoceles")
elif a != b and b != c:
   print(f" = Your triangle is Scalene")
