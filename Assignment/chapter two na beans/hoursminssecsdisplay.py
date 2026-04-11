seconds = int(input("Enter the amount of seconds: "))

hours = seconds//3600
remainder = hours % 3600
minutes = seconds//60
minutesremainder = minutes %  60
secs = seconds % 60

print(seconds,"secs", " = ", hours,"hour(s)", minutesremainder,"minute(s)", secs, "second(s)")
