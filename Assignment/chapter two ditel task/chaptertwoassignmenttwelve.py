principle = int(1000)
rate = int(7) 
time = int(10)

r = int(1 + rate)
p = int(principle * r)
amountfortenyears = p**time

time=int(20)
amountfor20years = p**time

time = int(30)
amountforthirtyyears = p**time

print("after ten years: amount = ", amountfortenyears, "after twenty years: amount = ", amountfor20years, "after thirty years: amount = ", amountforthirtyyears)
