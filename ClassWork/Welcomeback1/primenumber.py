#a function that takes a number and return true if it is prime number or false if it is not

""" Get number, find if number is divisible by a range of number from 2 up to the number, if non- of those number divide the number expect the number itself, then it is a prime number."""

def prime_number(number):
    #count = 2
    #while(number != 0):
    for count in range(2,(number//2)+1):
        #count+1
        if (number % count == 0):
            return False
    return True
        #count+1
number = int(input("Enter a number to check if it is a prime number: "))
print(f"is {number} a prime number? {prime_number(number)}")
