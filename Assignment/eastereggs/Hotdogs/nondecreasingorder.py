# non decreasing order 


number_one = int(input("Enter First Number: "))        
number_two = int(input("Enter Second Number: "))
number_three = int(input("Enter Third Number: "))

if (number_one >= number_two and number_two >= number_three):
    print(number_three,number_two,number_one)
elif (number_two >= number_three and number_three >= number_one):
    print(number_one,number_three,number_two)
elif (number_three >= number_two and number_two >= number_one):
    print(number_one,number_two,number_three)
elif (number_three >= number_one and number_one >= number_two):
    print(number_two,number_one,number_three)
if (number_two >= number_one and number_one >= number_three):
    print(number_three,number_one,number_two)
elif (number_one >= number_three and number_three >= number_two):
    print(number_two,number_three,number_one)

