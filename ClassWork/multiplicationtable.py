"""
collect a number
initalize a count
multiply the number using the count variable to go with the times the loop runs
"""

number = int(input('Enter a number to multiply: '))
multiply = 1;
count = 1;
        
for count in range(1,11):
    multiply = number*count
    print(number, " x ", count, " = ", multiply)

