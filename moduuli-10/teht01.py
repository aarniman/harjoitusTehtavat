class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.nykyinen = alin

    def siirry_kerrokseen(self, kerros):
        if self.nykyinen < kerros:
            while self.nykyinen != kerros:
                self.kerros_ylos()
                if(self.nykyinen == self.ylin):
                    break
            print(f"\nOlet nyt saapunut kerrokseen {self.nykyinen}\n")
        elif self.nykyinen > kerros:
            while self.nykyinen != kerros:
                self.kerros_alas()
                if(self.nykyinen == self.alin):
                    break
            print(f"\nOlet nyt saapunut kerrokseen {self.nykyinen}\n")
        else:
            print(f"Olet jo kerroksessa {kerros}\n")

    def kerros_ylos(self):
        if self.nykyinen < self.ylin:
            self.nykyinen += 1
            print(f"Kerros {self.nykyinen}")

    def kerros_alas(self):
        if self.nykyinen > self.alin:
            self.nykyinen -= 1
            print(f"Kerros {self.nykyinen}")


h = Hissi(1, 8)
h.siirry_kerrokseen(5)
h.siirry_kerrokseen(5)
h.siirry_kerrokseen(1)
h.siirry_kerrokseen(10)
h.siirry_kerrokseen(-1222)