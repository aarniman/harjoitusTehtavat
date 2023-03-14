
class Auto:
    def __init__(self, rekisteri, huippunopeus, nopeus = 0, kuljettu = 2000):
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




auto = Auto("ABC-123", 142)
print(f"Auton rekkari: {auto.rekisteri}, "
      f"huippunopeus: {auto.huippunopeus} km/h, "
      f"nykyinen nopeus: {auto.nopeus} km/h, "
      f"Kuljettu matka: {auto.kuljettu} km")

print(f"Auto on kulkenut {auto.kuljettu} km/h.")
auto.kiihdyta(60)
auto.kulje(1.5)
print(f"Auto on kulkenut {auto.kuljettu} km/h.")