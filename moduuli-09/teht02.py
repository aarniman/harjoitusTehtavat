
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



auto = Auto("ABC-123", 142)
print(f"Auton rekkari: {auto.rekisteri}, "
      f"huippunopeus: {auto.huippunopeus} km/h, "
      f"nykyinen nopeus: {auto.nopeus} km/h, "
      f"Kuljettu matka: {auto.kuljettu} km")
auto.kiihdyta(30)
print(f"Nykyinen auton nopeus on {auto.nopeus} km/h")
auto.kiihdyta(70)
print(f"Nykyinen auton nopeus on {auto.nopeus} km/h")
auto.kiihdyta(50)
print(f"Nykyinen auton nopeus on {auto.nopeus} km/h")
auto.kiihdyta(-200)
print(f"Nykyinen auton nopeus on {auto.nopeus} km/h")