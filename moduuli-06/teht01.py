import random


def arvo():
    luku = random.randint(1, 6)
    return luku

while True:
    noppa = arvo()
    print(str(noppa))
    if(noppa == 6):
        print("Nopasta tuli luku 6!")
        break
    else:
        continue