i = 0
while True:
    tunnus = input("Anna käyttäjätunnus")
    salis = input("Anna salasana")
    if(tunnus == "python" and salis == "rules"):
        print("Tervetuloa")
        break
    else:
        print("Käyttäjätunnus/salasana on väärin")
        i = i + 1
    if(i == 5):
        print("Pääsy evätty")
        break