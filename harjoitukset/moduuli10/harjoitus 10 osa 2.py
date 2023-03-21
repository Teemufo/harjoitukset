#Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan. Talon alustajaparametreina annetaan alimman ja ylimmän
#kerroksen numero sekä hissien lukumäärä. Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä. Hissien lista
#tallennetaan talon ominaisuutena. Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin numeron ja
#kohdekerroksen. Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.

class Hissi:
    def __init__(self, alinkerros, ylinkerros):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros
        self.kerros = alinkerros

    def siirry_kerrokseen(self, uusi_kerros):
        while uusi_kerros > self.kerros:
            self.kerros_ylös()
        while uusi_kerros < self.kerros:
            self.kerros_alas()
        print(f"Hissi on määränpäässä.")
        return
    def kerros_ylös(self):
        self.kerros = self.kerros + 1
        print(f"Hissi on kerroksessa {self.kerros}")
        return

    def kerros_alas(self):
        self.kerros = self.kerros - 1
        print(f"Hissi on kerroksessa {self.kerros}")
        return

class Talo:
    def __init__(self, alin, ylin, lkm):
        self.hissit = []
        for nro in range(lkm):
            hissi = Hissi(alin, ylin)
            self.hissit.insert({nro+1}, hissi)
    def aja_hissiä(self):
        hissi = self.hissit[hissin_nro]
        hissi.siirry_kerrokseen(kerros)
#    def paniikki(self):
#        for i in self.lista:
#            i.siirry_kerrokseen

#TODO Tee pääohjelma, jossa luot talon ja ajat sen hissejä