import random


def arvo():
    luku = random.randint(1, 6)
    return luku

noppa = 0
while noppa < 6:
    noppa = arvo()
    print(str(noppa))
    if(noppa == 6):
        print("Nopasta tuli luku 6!")

