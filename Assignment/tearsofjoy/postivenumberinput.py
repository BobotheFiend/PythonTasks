#9



user_input = int(input("Enter a number: "))
if user_input > 0:
    print(f"you entered {user_input}")
while(user_input <= 0):
    print('wrong input')
    user_input = int(input(" Enter number: "))
    print(f"you entered {user_input}")
        
