airports = {}

while True:
    command = input("Haluatko lisätä lentoaseman(lisaa), hakea tietoja vanhasta(hae) vai lopettaa(stop)?")
    if(command == "stop"):
        break
    elif(command == "lisaa"):
        code = input("Anna lentoaseman ICAO-koodi")
        name = input("Anna vielä lentoaseman nimi")
        airports[code] = name
    elif(command == "hae"):
        code = input("Anna lentoaseman ICAO-koodi")
        if code in airports:
            print(f"{airports[code]}")
        else:
            print("Lentokenttää ei ole lisätty/ICAO-koodi on väärin")
    else:
        print("Väärä komento. Anna uusi komento.")