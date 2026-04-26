# Displays a leap year


number = int(input("Enter a year: "))

if number % 4 == 0:
    print(f"{number} is a leap year")
elif number % 4 != 0:
    print(f"{number} is not a leap year")
