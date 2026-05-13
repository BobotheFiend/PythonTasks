#4.6 Modified average Function

def average(*args):
    return sum(args) / len(args)

average(5, 10)
average(5, 10, 15)
average(5, 10, 15, 20)
grades = [88, 75, 96, 55, 83]
average(*grades)

print(average())
