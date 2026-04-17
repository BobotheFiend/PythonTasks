"""
create a requirement for a passwaord to be met
collect the users password
evaluate the users password to check if it checks the requirements
if it is lessthan 8 lengths it's very strong
if it is 8 it is weak
if it is above 8 and up to 16 it is strong
if it above 16 it is very strong
 """

user_password = input('Enter a password: ')



if len(user_password) > 0 and len(user_password) < 8:
    print('Your password is VERY WEAK')
elif len(user_password) == 8:
    print('Your password is WEAK')
elif len(user_password) > 8 and len(user_password) <= 16:
    print('Your password is STRONG')
elif len(user_password) > 16:
    print('Your password is VERY STRONG')
