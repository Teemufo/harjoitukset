#Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto. Sähköautolla on ominaisuutena
#akkukapasiteetti kilowattitunteina. Polttomoottoriauton ominaisuutena on bensatankin koko litroina. Kirjoita aliluokille
#alustajat. Esimerkiksi sähköauton alustaja saa parametreinaan rekisteritunnuksen, huippunopeuden ja akkukapasiteetin.
#Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi sekä asettaa oman kapasiteettinsa. Kirjoita pääohjelma,
#jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh) ja yhden polttomoottoriauton (ACD-123, 165 km/h, 32.3 l).
#Aseta kummallekin autolle haluamasi nopeus, käske autoja ajamaan kolmen tunnin verran ja tulosta autojen matkamittarilukemat.

class Auto:
    def __init__(self, register, maxspeed):
        self.register = register
        self.maxspeed = maxspeed
        self.nopeus = 0
        self.matka = 0

    def acceleration(self, change):
        self.nopeus = self.nopeus + change
        if self.nopeus >= self.maxspeed:
            self.nopeus = self.maxspeed
        elif self.nopeus < 0:
            self.nopeus = 0
        return

    def travel(self, time):
        self.matka = self.nopeus * time + self.matka
        return


class Sähköauto(Auto):
    def __init__(self, register, maxspeed, kapasiteetti):
        super().__init__(register, maxspeed)
        self.kapasiteetti = kapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self, register, maxspeed, tankinkoko):
        super().__init__(register, maxspeed)
        self.tankinkoko = tankinkoko

sähköauto = Sähköauto("ABC-15", 180, 52.5)
polttoauto = Polttomoottoriauto("ACD-123", 165, 32.3)

sähköauto.nopeus = 100
polttoauto.nopeus = 150

sähköauto.travel(3)
polttoauto.travel(3)

print(f"Sähköauton kulkema matka: {sähköauto.matka} km. Polttomoottoriauton kulkema matka: {polttoauto.matka} km.")

