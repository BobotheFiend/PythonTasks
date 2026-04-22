#number = int(input('Enter a number: '))
print ("\t                           Multiplication Table")

count = 0
num = 0
for count in range (1,11):
    print(f"{num:>4}", end=' ')
    print (count, end=' | \t')
    for num in range (1,11):
        multiply = count*num
        print(f"{multiply:>3}", end='  ')
    print()
