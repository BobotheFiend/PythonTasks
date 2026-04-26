# palindrome integer


 
number = int(input("Enter a 3 digit number: "))     
        
digit1 = number % 10
digitdiv = number/10
digit2 = digitdiv % 10
digitdiv2 = digitdiv / 10
digit3 = digitdiv2 % 10

if digit3 == digit1:
    print(digit3,digit1,digit1, " is a Palindrome")
else:
    print("Not a Plindrome")
