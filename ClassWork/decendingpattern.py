"""
collect a number
initalize a count
multiply the number using the count variable to go with the times the loop runs
"""
count = 5
while count >= 0:
    for num in range (count, 0, -1):
        print(num, end=' ')
    print(num)    
    count-= 1

