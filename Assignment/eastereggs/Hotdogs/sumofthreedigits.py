#sum of three digits

number = int(input("Enter a number from 0-1000: "))

digit_one = number / 10
remainder_digit_one = number % 10

digit_two = digit_one / 10
remainder_Digit_two = digit_one % 10

digit_three = digit_two / 10
remainder_Digit_three = digit_two % 10

sum = int(remainder_digit_one+remainder_Digit_two+remainder_Digit_three)
print(f"The sum of {number} = {sum}")
