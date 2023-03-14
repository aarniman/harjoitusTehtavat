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

    def nykyinen_kerros(self):
        return self.nykyinen

class Talo:

    def __init__(self, alin, ylin, hissit):
        self.alin = alin
        self.ylin = ylin
        self.lista = []
        self.hissit = hissit
        for i in range (self.hissit):
            self.lista.append(Hissi(self.alin, self.ylin))

    def aja_hissia(self, nro, kerros):
        self.lista[nro-1].siirry_kerrokseen(kerros)
        print(f"Talon hissi nro {nro} on nyt kerroksessa {self.lista[nro-1].nykyinen_kerros()}\n")


    def vitun_PANIK(self):
        for i in self.lista:
            i.siirry_kerrokseen(self.alin)
            print(f"Kaikki hissit ovat alimmassa kerroksessa eli kerroksessa {i.nykyinen}")


t = Talo(1, 8, 3)

t.aja_hissia(3, 5)
t.aja_hissia(2, 2)
t.aja_hissia(3, 8)
t.vitun_PANIK()