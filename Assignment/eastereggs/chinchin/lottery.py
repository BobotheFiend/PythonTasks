#lottery 

import random

lottery = random.randint(100)
       
splitLottery = lottery/10
remLottery = lottery % 10
        

number = int(input("Enter a 2 digit number 00-99: "))
        
splitNumber = number/10
remNumber = number % 10

if number == lottery:
    print(f"lottery is {lottery} and your guess is {number} Congratulations! You win $10,000%n")
elif  splitLottery == splitNumber||splitLottery == remNumber||remLottery == splitNumber|| remLottery == remNumber :
    print(f" lottery is {lottery} and your guess is {number} Congratulations! You win $1,000%n")
elif splitLottery == splitNumber and splitLottery == remNumber and remLottery == splitNumber and remLottery == remNumber:
    print(f" lottery is {lottery} and your guess is {number} Congratulations! You Win $3,000%n")
elif number != lottery:
    print(f" lottery is {lottery} and your guess is {number} Better luck next time%n")
