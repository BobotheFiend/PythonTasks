#11.

user_input = int(input("Enter a number: "))
add = 0
while(user_input != 0):
    add +=user_input
    user_input = int(input("Enter a number: "))
    print(add)
print(f"Your total nume = {add}")
