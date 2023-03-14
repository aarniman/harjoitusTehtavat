import random
from prettytable import PrettyTable

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

lista = []
rek = 1
for i in range(10):
    r = random.randint(100, 200)
    auto = Auto("ABC-"+str(i+1), r)
    lista.append(auto)

pisin = 0;
while pisin <= 10000:
    for i in lista:
        i.kiihdyta(random.randint(-10, 15))
        i.kulje(1)
        if(i.kuljettu >= pisin):
            pisin = i.kuljettu

taulukko = PrettyTable()
taulukko.field_names = ["Rekkari", "Huippu nopeus", "Kuljettu matka"]
for i in lista:
    taulukko.add_row([i.rekisteri, i.huippunopeus, i.kuljettu])
taulukko.sortby = "Kuljettu matka"
taulukko.reversesort = True
print(taulukko)
