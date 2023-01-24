names = set()

while True:
    name = input("Anna nimiä. Tyhjä lopettaa.")
    if name == "":
        break
    if names.__contains__(name):
        print("Aiemmin syötetty nimi")
        names.add(name)
    else:
        print("Uusi nimi")
        names.add(name)
for n in names:
    print(n)