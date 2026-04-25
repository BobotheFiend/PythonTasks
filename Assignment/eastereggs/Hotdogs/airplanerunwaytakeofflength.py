#display minimum runway length using length = v^2/(2a)


velocity = float(input("Enter the Vm/s : "))
acceleration = float(input("Enter the a m/s : "))
        
velocity_square = velocity*velocity;
length = velocity_square/2*acceleration;

print(f"length = {length}")
