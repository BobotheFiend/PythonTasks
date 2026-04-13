userfirstinput = input("Enter first number: ")
usersecondinput = input("Enter second number: ")
userthirdinput = input("Enter third number: ")


if userfirstinput > usersecondinput and usersecondinput > userthirdinput:
    largest = userfirstinput
    middle = usersecondinput
    smallest = userthirdinput

if userfirstinput < usersecondinput and userfirstinput > userthirdinput:
    largest = usersecondinput
    middle = userfirstinput
    smallest = userthirdinput

if usersecondinput > userthirdinput and userthirdinput> userfirstinput:
    largest = usersecondinput
    middle = userthirdinput
    smallest = userfirstinput

if userthirdinput > usersecondinput and usersecondinput > userfirstinput:
    largest = userthirdinput
    middle = usersecondinput
    smallest = userfirstinput

if userthirdinput > userfirstinput and userfirstinput > usersecondinput:
    largest = userthirdinput
    middle = userfirstinput
    smallest = usersecondinput 

if userthirdinput < userfirstinput and userthirdinput > usersecondinput:
    largest = userfirstinput
    middle = userthirdinput
    smallest = usersecondinput 

print("The largest down to the smallest number is: ",largest,'--->', middle,'--->', smallest)







