#sum of digits


three = int(input("Enter a number from 100-999: "))

digit1 = three/10
digitRem1 = three % 10

digit2 = digit1/10
digitRem2 = digit1 % 10
    
digit3 = digit2/10
digitRem3 = digit2 % 10
       
sum = int(digitRem1+digitRem2+digitRem3)
        
print(f"The Sum of its digits = {sum}")
