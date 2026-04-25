#monthly saving amount that displays the amount after each of the first six month

amount = float(input("Enter the amount you would like to save monthly: "))

month_one = int((1+0.003125)*amount)   
month_two = int((1+0.003125)*month_one)
month_three = int((1+0.003125)*month_two)    
month_four = int((1+0.003125)*month_three)        
month_five = int((1+0.003125)*month_four)       
month_six = int((1+0.003125)*month_five)

print(f"""
        The account after six months is 
____________________________________________________________________
|    For the first month the intrest rate was {month_one}
|    For the second month the balance was {month_two}
|    Month three the balance was {month_three}
|    Month Four the balance was {month_four}
|    Month Five the balance was {month_five}
|    Month Six the balance was {month_six}"""
)

