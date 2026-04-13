number_one = int(input("Enter first integer: "))
number_two = int(input("Enter second integer: "))
number_three = int(input("Enter third integer: "))

sum = number_one+number_two+number_three
product = number_one*number_two*number_three
average = (number_one+number_two+number_three)/2
smallest = min(number_one,number_two,number_three)
largest = max(number_one,number_two,number_three)

print("The sum = ", sum, "The product = ", product, "The average = ", average, "The smallest = ", smallest, "The largest = ", largest)

