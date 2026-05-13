#If i have a tempreature, and i wan to know the degree of temp. when i convert it to either fahrenheit or celsius
#when i pass my value, i should speficify what degree it is
#if i dont specify it should alway read as celsius
#i should convert the value passed into celsius or fahrenheit depending on the mesurement type
#if either tempreature results in a lower tempreature i should notifiy that the degree of that tempreature is cold
#if either tempreature results in a higher tempreature i should notifiy that the degree of that tempreature is hot
#test that it works

def temperature_alert(temperature_value, temperature_degree):
    if temperature_degree is None or (temperature_degree.lower() not in ['c','f']):
        temperature_degree = 'C'

    
    if temperature_degree.lower() == 'F'.lower():
        converter = float((temperature_value - 32) * 5/9)
        #if converter <
    elif temperature_degree.lower() == 'c'.lower():
        converter = float((temperature_value * 9/5) + 32)

    if converter >= 40:
        converter = "Heat Alert"
    elif converter < 40:
        converter = "Cold Advisory"

    return converter


#print(temperature_alert(50,"c"))
