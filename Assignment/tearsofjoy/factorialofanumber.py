#10


user_input = int(input("Enter a number: "))
factorial = 1
while(user_input >= 1):
    factorial *= user_input
    print(f"{user_input} x ", end='') 
    user_input -= 1
print("=",factorial)
