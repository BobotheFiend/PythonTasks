#collect the number
#check if it a palindrome
#check if it is a prime number
#if it matches one condition return false fails
#if matches both condition return true
#test 


def palindrome_and_prime_checker(number):

    number_as_string = str(number)
    palindrome_checker = number_as_string[::-1]
    palindrome_integer = int(palindrome_checker)
    
    def prime_checker(palindrome_integer):
        if palindrome_integer <= 1:
            return False
        for count in range(2, int(palindrome_integer**0.5)+1):
            if palindrome_integer % count == 0:
                return False
        return True
        
    if  palindrome_integer == number and prime_checker(palindrome_integer) == True:
        return True
    else:
        return False
    

print(palindrome_and_prime_checker(1))
