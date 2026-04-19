#3.9

number_entry = int(input("Enter a five digit number: "))
sum = 0
digit_remainder = 0
digit = 0
     
while number_entry > 0:
    digit_remainder = number_entry % 10
    number_entry = number_entry / 10
    print(number_entry, ' ... ', digit_remainder)
        
