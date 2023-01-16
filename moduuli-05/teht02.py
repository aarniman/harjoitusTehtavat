lista = []
while True:
    luku = input("Anna luku. Tyhjä lopettaa.")
    if luku == "":
        break
    lista.append(int(luku))
lista.sort(reverse=True)
print(lista[0:5])
