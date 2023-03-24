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

class Sahkoauto(Auto):

    def __init__(self, rekisteri, huippunopeus,akkukapasiteetti):
        super().__init__(rekisteri, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti
        self.nopeus = 0
        self.kuljettu = 0



class Polttomoottoriauto(Auto):

    def __init__(self, rekisteri, huippunopeus, bensatankki):
        super().__init__(rekisteri, huippunopeus)
        self.bensatankki = bensatankki
        self.nopeus = 0
        self.kuljettu = 0

s = Sahkoauto("ABC-15", 180, 52.5)
p = Polttomoottoriauto("ACD-123", 165, 32.3)

s.kiihdyta(200)
p.kiihdyta(200)

s.kulje(3)
p.kulje(3)

print(s.kuljettu)
print(p.kuljettu)