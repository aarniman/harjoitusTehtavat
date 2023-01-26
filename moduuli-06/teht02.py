import random


def arvo(sivut):
    luku = random.randint(1, sivut)
    return luku

noppa = 0
tahko = int(input("Anna nopan tahkojen määrä"))
while noppa < tahko:
    noppa = arvo(tahko)
    print(str(noppa))
    if(noppa == tahko):
        print(f"Nopasta tuli luku {tahko}!")
