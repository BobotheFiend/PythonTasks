passes = 0
failures= 0
result = 0
count = 0  
for students in range(10):
    result = int(input('Enter result(1=pass, 2=fail): '))
    count += 1
    while (result !=1 and result != 2):
        print('The result is invalid, try again')
        result = int(input('Enter result(1=pass, 2=fail): '))
        count += 1
    if result == 1:
        passes = passes + 1
    else:
        failures = failures + 1

print('Passed:', passes)
print('Failed:', failures)

print('Attempts not valid = ', count - 10)



if passes > 8:
    print('Bonus to instructor for 8 passes')
