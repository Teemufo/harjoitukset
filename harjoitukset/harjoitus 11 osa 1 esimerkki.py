class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self, kirjailija, sivumäärä):
        self.kirjailija = kirjailija
        self.sivumäärä = sivumäärä