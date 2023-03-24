import json
import requests

paikkakunta = input("Anna paikkakunnan nimi\n")
pyynto = "https://api.openweathermap.org/data/2.5/weather?q="+ paikkakunta +"&appid=b39ce9e7d9bc0803b3e88892d6423c4c&units=metric"
vastaus = requests.get(pyynto).json()

lampotila = vastaus["main"]
celsius = lampotila["temp"]

tem = vastaus["weather"]
saa = tem[0]["description"]
print(f"Kaupungin {paikkakunta} lämpötila on {celsius} °C ja säätila on {saa}.")