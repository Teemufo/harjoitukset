#Toteuta seuraava luokkahierarkia Python-kielellä: Julkaisu voi olla kirja tai lehti. Jokaisella julkaisulla on nimi.
#Kirjalla on lisäksi kirjoittaja ja sivumäärä, kun taas lehdellä on päätoimittaja. Kirjoita luokkiin myös tarvittavat
#alustajat. Tee aliluokkiin metodi tulosta_tiedot, joka tudostaa kyseisen julkaisun kaikki tiedot. Luo pääohjelmassa
#julkaisut Aku Ankka (päätoimittaja Aki Hyyppä) ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua). Tulosta molempien
#kaikki tiedot toteuttamiesi metodien avulla.

class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjailija, sivumäärä):
        super().__init__(nimi)
        self.kirjailija = kirjailija
        self.sivumäärä = sivumäärä

    def tulosta_tiedot(self):
        print(f"Kirjan tiedot: ")
        print(f"Nimi: {self.nimi}. Kirjailija: {self.kirjailija}. Pituus: {self.sivumäärä} sivua.")
        return

class Lehti(Julkaisu):
    def __init__(self, nimi, toimittaja):
        super().__init__(nimi)
        self.toimittaja = toimittaja
    def tulosta_tiedot(self):
        print(f"Lehden tiedot:")
        print(f"Nimi: {self.nimi}. Toimittaja: {self.toimittaja}.")
        return


julkaisut = []

julkaisut.append(Lehti("Aku Ankka", "Aki Hyyppä"))
julkaisut.append(Kirja("Hytti no 6", "Rosa Liksom", 200))


for i in julkaisut:
    i.tulosta_tiedot()

