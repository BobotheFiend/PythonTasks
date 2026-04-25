#Distance covered using Newton's equation s = ut + 1/2at^2

velocity = float(input('Enter the initial velocity : '))
time = float(input("Enter the time : "))
acceleration = float(input('Enter the acceleration : '))

ut = velocity*time;

time_square = time**2

at = 0.5*acceleration*time_square

s = ut+at;

print(f"The distance covered d ={s}")
