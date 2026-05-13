#4.4 what does this code do? prints out the lists of numbers

def mystery(x):
    y = 0
    for value in x:
        y += value ** 2
    return y


x = [1,2,3,4,5]
print(f"What is the mystery behind x.....{x}")
