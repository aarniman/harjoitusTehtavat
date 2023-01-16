import sys
min = sys.maxsize
max = -99999999999999999999999999999999999999999999999999999999999999999999999
while True:
    luku = input("Anna luku. Laita tyhjä lopettaaksesi.")
    if(luku == ""):
        break
    if(int(luku) > max):
        max = int(luku)
    if(int(luku) < min):
        min = int(luku)
print("Suurin luku on " + str(max) + " ja pienin on " + str(min) + ".")