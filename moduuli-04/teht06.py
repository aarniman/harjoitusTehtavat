import random

piste = int(input("Anna pisteiden määrä"))
i = 0
oikein = 0
while i <= piste:
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    if(x**2 + y**2 < 1):
        oikein = oikein +1
    i = i +1
vastaus = (4 * oikein / piste)

print(vastaus)
