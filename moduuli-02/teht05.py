leiviska = float(input("Anna leiviskät"))
naula = float(input("Anna naulat"))
luoti = float(input("Anna luodit"))

pNaula = leiviska * 20 + naula
pLuoti = pNaula * 32 + luoti
paino = pLuoti * 13.3

kilo = (int(paino / 1000))
gramma = (float(paino % 1000))
gramma = round(gramma, 2)
print("Massa nykymittojen mukaan:")
print(str(kilo) + " kilogrammaa ja " + str(gramma) + " grammaa.")