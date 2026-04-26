#Displayd corresponding score leteer grade


number = int(input("Enter a score from (0-100): "))

if number >= 90 and number <= 100:
    print(f"{number} = Your grade is A")
#elif number >100:
#    print(f"{number} is not a valid score")

elif number >= 80 and number <= 89:
    print(f"{number} = Your grade is B")

elif number >= 70 and number <= 79:
    print(f"{number} = Your grade is C")

elif number >= 60 and number <= 69:
    print(f"{number} = Your grade is D")

elif number >= 0 and number < 60:
    print(f"{number} = Your grade is F")
else:
    print(f"{number} is not a vaild score")
