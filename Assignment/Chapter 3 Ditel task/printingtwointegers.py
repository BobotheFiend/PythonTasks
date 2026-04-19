#3.6

print ('Enter two integers,and I will tell you', 'the relationship they satisfy.')

number_one = int(input('Enter first integer: '))
number_two = int(input('Enter the second integer: '))

if number_one == number_two:
    print(number_one, 'is = ', number_two)
else: 
    print(number_one, 'is not = ', number_two)
if number_one < number_two:
    print(number_one, 'is < ', number_two)
else:
    print(number_one, 'is > ', number_two)
if number_one <= number_two:
    print(number_one, 'is less than or eqauls to: ', number_two)
else:
    print(number_one, 'is greater than or equals to: ', number_two)


