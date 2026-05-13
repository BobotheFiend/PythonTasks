# DIVISIBLE BY 4


number = int(input("Enter a number: "))

if number % 4 == 0 and number % 5 == 0:
    print(f" {number} is divisible by both 4 and 5")
#if number % 4 == 0 or number % 5 == 0:
#    print(f"{number} is divisible either by 4 or 5")
if number % 4 == 0:
    print(f" {number} is divisible by 4 and not 5")
if number % 5 == 0:
    print(f" {number} is divisible by 5 not 4")
if number % 5 != 0 and number % 4 != 0:
    print(f" {number} is not divisible by 5 and or 4")
