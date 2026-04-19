#3.12

palindromes = int(input("Enter a five digit number(12345): "))

digit_one = palindromes/10
digit_one_remainder = palindromes % 10

digit_two = digit_one/10
digit_two_remainder = digit_one % 10
    
digit_three = digit_two/10
digit_three_remainder = digit_two % 10

digit_four = digit_three/10
digit_four_remainder = digit_three % 10

digit_five = digit_four/10
digit_five_remainder = digit_four % 10

if digit_one_remainder == digit_five_remainder:
    print(palindromes,' ---> ',digit_five_remainder,digit_four_remainder,digit_three_remainder,digit_two_remainder,digit_one_remainder, 'the number is a Palindrome')        
else:
    print(palindromes,' ---> ',digit_five_remainder,digit_four_remainder,digit_three_remainder,digit_two_remainder,digit_one_remainder, 'the number is not a Palindrome') 
 
