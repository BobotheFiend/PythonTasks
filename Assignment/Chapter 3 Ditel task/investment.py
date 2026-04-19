#3.10

principle = int(1000)
rate = int(0.07) 
time = 1

r = 1 + rate

for time in range (1,31):
    amount = principle * ((r)**time)
    if time == 10:
        print("after ten years: amount = ", amount, time)
    if time == 20:
        print("after twenty years: amount = ", amount, time)
    if time == 30:
        print("after thirty years: amount = ", amount, time)

