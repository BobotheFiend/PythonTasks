
def largest(number_one, number_two, number_three):
    largest_number = number_one
    if number_two > number_one:
        largest_number = number_two
    if number_three > number_two:
        largest_number = number_three
    return largest_number

print(largest(44,13,77))
