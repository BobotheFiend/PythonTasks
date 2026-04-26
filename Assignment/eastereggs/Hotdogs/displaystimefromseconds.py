#displays number of hours minutes and seconds from number of seconds input


seconds = int(input("Enter the number of Seconds: "))
hours = int(seconds/3600)
minutes= int(hours%60)
remaninder = int(seconds%60)

print(f" {hours}hour(s) {minutes}minutes {remaninder}seconds")
