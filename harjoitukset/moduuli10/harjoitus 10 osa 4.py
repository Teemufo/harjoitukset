class kilpailu:
    def __init__(self):
        self.nimi = nimi
        self.pituus = pituus
        self.lista = lista
    def tunti_kuluu(self):
        for i in self.lista:
            i.kiihdyta(random.randit(-10, 15)
            i.kulje(1)
    def tulosta_tilanne(self):
        taulukko = PrettyTable()
        taulukko.field_nam
        for i in taulukko:
            taulukko.add_row([i.rekisteri, i.huippunopeus, i.kuljettu])
        taulukko.sortby = "Kuljettu matka"
        taulukko.reversesort = True
        print(taulukko)