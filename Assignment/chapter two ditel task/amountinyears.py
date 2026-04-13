principle = int(1000)
rate = int(7) 
time = int(10)

r = int(1 + rate)
p = int(principle * r)
amount_for_tenyears = p**time

time=int(20)
amount_for_20years = p**time

time = int(30)
amount_for_thirtyyears = p**time

print("after ten years: amount = ", amount_for_tenyears, "after twenty years: amount = ", amount_for_20years, "after thirty years: amount = ", amount_for_thirtyyears)
