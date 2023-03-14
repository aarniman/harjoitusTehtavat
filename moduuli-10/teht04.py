import random
from prettytable import PrettyTable

class Kilpailu:
    def __init__(self, nimi, pituus, lista):
        self.nimi = nimi
        self.pituus = pituus
        self.lista = lista

    def tunti_kuluu(self):
        for i in self.lista:
            i.kiihdyta(random.randint(-10, 15))
            i.kulje(1)

    def tulosta_tilanne(self):
        taulukko = PrettyTable()
        taulukko.field_names = ["Rekkari", "Huippunopeus", "Kuljettu matka"]
        for i in self.lista:
            taulukko.add_row([i.rekisteri, i.huippunopeus, i.kuljettu])
        taulukko.sortby = "Kuljettu matka"
        taulukko.reversesort = True
        print(taulukko)

    def kilpailu_ohi(self):
        for i in self.lista:
            if(i.kuljettu >= self.pituus):
                return True
        return False

class Auto:
    def __init__(self, rekisteri, huippunopeus, nopeus = 0, kuljettu = 0):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettu = kuljettu

    def kiihdyta(self, muutos):
        if self.huippunopeus < self.nopeus + muutos:
            self.nopeus = self.huippunopeus
        elif self.nopeus + muutos < 0:
            self.nopeus = 0
        else:
            self.nopeus += muutos

    def kulje(self, tunti):
        self.kuljettu += tunti * self.nopeus

    def status(self):
        print(f"|{self.rekisteri}|{self.huippunopeus}|{self.nopeus}|{self.kuljettu}|")

autot = []
rek = 1
for i in range(10):
    r = random.randint(100, 200)
    auto = Auto("ABC-"+str(i+1), r)
    autot.append(auto)

k = Kilpailu("Suuri romuralli", 8000, autot)
tunti = 10
while k.kilpailu_ohi() is False:
    for i in range(10):
        if k.kilpailu_ohi():
            break
        k.tunti_kuluu()
    tunti = tunti + 10
    k.tulosta_tilanne()
print("\nKilpailu on ohi ja tulokset ovat:\n")
k.tulosta_tilanne()