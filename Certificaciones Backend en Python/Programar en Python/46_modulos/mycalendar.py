import sys

locations = sys.path
print(type(locations))

for i in locations:
    print(i)

import calendar

leaddays = calendar.leapdays(2024, 2050) # arroja la cantidad de días bisiestos en ese periodo
print(leaddays)

isitleap = calendar.isleap(2024) 
print(isitleap) # devuelve un valor booleano si el año, True si es bisiesto