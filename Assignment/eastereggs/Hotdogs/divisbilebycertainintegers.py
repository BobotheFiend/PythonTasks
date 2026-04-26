#chech if number is divisible by, 2 , 3, 5, and or 7


number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is divisible by 2")
if number % 3 == 0:
    print(f"{number} is divisible by 3")
if number % 5 == 0:
    print(f"{number} is divisible by 5 ")
if number % 7 == 0:
    print(f"{number} is divisible by 7 ")
