#displays the maximum numbe rof years and remaining days


minute = int(input("Enter the number of Minutes: "))
hours = minute/60
days = int(hours/24)
years = int(days/365)
remaninder = int(days%365)
print(f"Maximum number is {years}Year(s) remaining {days}day(s)")
