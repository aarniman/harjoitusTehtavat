kanta = int(input("Anna suorakulmion kanta metreinä"))
korkeus = int(input("Anna myös korkeus metreinä"))

piiri = kanta + kanta + korkeus + korkeus
pa = kanta * korkeus

print("Piiri on " + str(piiri) + "m")
print("Pinta-ala on " + str(pa) + "m\u00b2")