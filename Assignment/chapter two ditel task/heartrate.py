usersage = input("What is your age: ")

heartrate = 220 - int(usersage)

usertargetheartrateforfiftypercent = heartrate * 0.50
usertargetheartrateforeightyfivepercent = heartrate * 0.85
 
print("Your heart rate = ", heartrate, "and your targeted heart range = ", usertargetheartrateforfiftypercent, "-", usertargetheartrateforeightyfivepercent)
