#enter both sides of a triangle

number = int(input('Enter the length: '))
 
length_Sq = number*number
area = (3/4)**0.5 *length_Sq
    
height = int(input("Enter height: "))

volume = area*height

print(f"The volume of the Triangle = {volume}")
        
