#3.17
print('(a)')
for count in range(1, 11):
    for num in range(1, count):
        print('*', end=" ")
    print('*')

print('(b)')
for count in range(11, 1):
    for num in range(count, 1, -1):
        print('*', end=" ")
    print('*')

