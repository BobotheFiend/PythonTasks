#calculates the energy needed to heat water from an inital temprature to final temperature. using Q = M x (final temp - initial temp) x 4184

waterKg = int(input("Enter the amount of water : "))
initial_tempreature = float(input("Enter the  initial Temperature : "))
final_tempreature = float(input("Enter the final Temperature : "))
        
bracket = final_tempreature-initial_tempreature;

q = waterKg*bracket*4184;

print(f"Q = {q}")
