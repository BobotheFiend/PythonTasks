#4.5 Fill in the Missing Code?

def seconds_since_midnight(hours,minute, seconds):
    hour_in_seconds = hours*3600
    minute_in_seconds = minute * 60
    total_seconds = hour_in_seconds + minute_in_seconds + seconds
    return total_seconds


total = seconds_since_midnight(13,30,45)
print(total)

