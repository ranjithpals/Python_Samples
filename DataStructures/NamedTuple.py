from collections import namedtuple

DivMod = namedtuple("DivMod", "Numerator Remainder")
x, y = 12, 5
dm = DivMod(*divmod(x,y))
print(dm)

print(dm.Numerator)
print(dm.Remainder)

cities = ['Chennai', 'Hyderabad', 'Bangalore']
temp = [45, 40, 35]

weather = namedtuple("weather", "city temperature")
l_weather = []
for c, t in zip(cities, temp):
    l_weather.append(weather(c, t))

print(l_weather[0].city)
print(l_weather[0].temperature)

def addWeather(ci, te):
    return ci, te

l_weather.append(weather("Vizag", "45"))
print(l_weather)