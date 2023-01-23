import math


def yksikkoHinta(koko, hinta):
    pa = (math.pi*(koko/2)**2) /10000
    yksikkohinta = hinta / pa
    return yksikkohinta

halkaisija1 = int(input("Anna ensimmäisen pitsan halkaisija"))
halkaisija2 = int(input("Anna toisen pitsan halkaisija"))
hinta1 = int(input("Anna vielä ensimmäisen pitsan hinta"))
hinta2 = int(input("Anna vielä toisen pitsan hinta"))
yh1 = yksikkoHinta(halkaisija1, hinta1)
yh2 = yksikkoHinta(halkaisija2, hinta2)
print(str(yh1))
print(str(yh2))
print()

if yh1 < yh2:
    hinta = yh2 - yh1
    print(f"Ensimmäisen pizzan hinta on parempi {hinta} eurolla")
else:
    hinta = yh1 - yh2
    print(f"Toisen pizzan hinta on parempi {hinta} eurolla")
