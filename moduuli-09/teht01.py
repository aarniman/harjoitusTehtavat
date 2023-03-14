
class Auto:
    def __init__(self, rekisteri, huippunopeus, nopeus = 0, kuljettu = 0):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettu = kuljettu

auto = Auto("ABC-123", 142)
print(f"Auton rekkari: {auto.rekisteri}, "
      f"huippunopeus: {auto.huippunopeus} km/h, "
      f"nykyinen nopeus: {auto.nopeus} km/h, "
      f"Kuljettu matka: {auto.kuljettu} km")

