#weighing two bags of rice and displays the better price per unit weight


weight1 = float(input("Enter weight of first rice: "))
price1 = float(input("Enter price of the first rice: "))     
 
weight2 = float(input("Enter weight of second rice: "))
price2 = float(input("Enter price of second rice: "))

riceOne = price1/weight1
riceTwo = price2/weight2

if riceOne > riceTwo: 
    print(f"the first bag {riceOne} has the better price per unit weight");
        
elif riceTwo > riceOne:   
    print(f"the second bag {riceTwo} has the better price per unit weight")
        
elif riceOne==riceTwo:
    print(f"both bags {riceOne} and {riceTwo} are equal")
