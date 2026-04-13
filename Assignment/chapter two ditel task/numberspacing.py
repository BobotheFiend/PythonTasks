user_input = input("Enter a five digit integer: ")

first_digit = int(userinput)//10
first_digitrem = int(userinput) % 10

second_digit = first_digit//10
second_digitrem = first_digit % 10

third_digit = second_digit//10
third_digitrem = second_digit % 10

fourth_digit = third_digit//10
fourth_digitrem = third_digit % 10

fifth_digit = fourth_digit//10
fifth_digitrem = fourth_digit % 10

print(first_digitrem, "   ", second_digitrem, "    ", third_digitrem, "     ", fourth_digitrem, "    ",fifth_digitrem)
