import random


def arvo(tahko):
    luku = random.randint(1, tahko)
    return luku

tahko = int(input("Anna nopan tahkojen määrä"))
while True:
    noppa = arvo(tahko)
    print(str(noppa))
    if(noppa == tahko):
        print(f"Nopasta tuli luku {tahko}!")
        break
    else:
        continue