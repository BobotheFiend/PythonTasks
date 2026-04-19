#3.8

count = 0
smallest = 0
largest = 0
sum = 0
hold = 0
product = 1
number = 0

user_input = int(input('Enter a number: '))

for number in range(3):
 
    sum += user_input
    product *= user_input
    hold = user_input
    count += 1
    user_input = int(input('Enter a number: '))
    if user_input < hold:
        smallest = user_input
    if user_input > hold:
        largest = user_input
average = sum / count


print("The sum = ", sum, "The product = ", product, "The average = ", average, "The smallest = ", smallest, "The largest = ", largest)

