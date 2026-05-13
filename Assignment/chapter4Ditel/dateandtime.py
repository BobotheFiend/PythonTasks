#4.7 Date and Time 
from datetime import datetime


def date_and_time():
    date_time = datetime.now()
    display = date_time.strftime("%d-%m-%Y %H:%M:%S")
    return display
print(date_and_time())


