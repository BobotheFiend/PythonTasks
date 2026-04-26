#reverse number


four = int(input("Enter a number from 1000-9999: "))

digit1 = four/10
digitRem1 = four % 10

digit2 = digit1/10
digitRem2 = int(digit1 % 10)
    
digit3 = digit2/10
digitRem3 = int(digit2 % 10)

digit4 = digit3/10
digitRem4 = int(digit3 % 10)
        
print(f" {four} ---> {digitRem1}{digitRem2}{digitRem3}{digitRem4}")
