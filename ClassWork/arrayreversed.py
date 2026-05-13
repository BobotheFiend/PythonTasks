


numbers = [19,6,33,2,84,1,57]
even = 0
odd = 0

srebmun = numbers[::-1] #the start stop and step; start from begining, stop at end, then take one step backwars.

print(f"The reversed list is = {srebmun}")


for count in numbers:
    if count % 2 == 0:
        print(count)
        even+=1
        
    else:
        #print(count)
        odd+=1

print(f"the even indexs = {even},  The odd indexes = {odd}")

#LEARN ABOUT LIST, COOLECTIONS IN JAVA
