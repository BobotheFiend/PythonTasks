# rock paper scissors

import random

scissor = random.randint(1, 3)
rock = random.randint(1, 3)
paper = random.randint(1, 3)
        
enter = int(input("Enter either  1, 2,3: "))

if enter == scissor and enter == rock and enter == paper:
    print(" A draw")
elif enter < scissor and enter < paper and enter < rock:
    print("Computer wins")
elif  enter > scissor and enter > paper and enter > rock:
    print(" User Wins")
