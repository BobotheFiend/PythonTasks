#16

input_numbers = 0
average = 0
total = 0
count = 1
while(count<= 10):
    input_numbers = int(input("Enter a score: "))
    total += input_numbers
    count += 1

average = total / count
print(average) 
