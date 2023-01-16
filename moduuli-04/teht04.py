import random
oikea = random.randint(1, 10)
arvaus = int(input("Arvaa oikea luku!"))
while True:
    if(arvaus == oikea):
        print("Oikein!")
        break
    if arvaus < oikea:
        print("Liian pieni arvaus")
    if(arvaus > oikea):
        print("Liian suuri arvaus")
    arvaus = int(input("Arvaa uudelleen!"))