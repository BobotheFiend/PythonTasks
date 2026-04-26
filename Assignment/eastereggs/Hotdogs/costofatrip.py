# cost of a trip

distance = float(input("Enter drive distance: "))       
fuel = float(input("Enter fuel efficiency: "))
price = float(input("Enter price per gallon: "))

costPrice = (distance/fuel)*price
        
print(f"The cost of the trip = {costPrice}")
