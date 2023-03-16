#Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi. Tee pääohjelman alussa lista
#, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta. Jokaisen auton huippunopeus arvotaan 100 km/h
#ja 200 km/h väliltä. Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne. Sitten kilpailu alkaa. Kilpailun aikana
#tehdään tunnin välein seuraavat toimenpiteet:

#Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä.
#Tämä tehdään kutsumalla kiihdytä-metodia.
#Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.
#Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä. Lopuksi tulostetaan kunkin auton
#kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.

import random

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

autolista = []

for i in range(10):
    autolista.append(Auto("ABC-" + str(i+1), random.randint(100, 200)))

kilpailu = True

while kilpailu is True:
    for auto in autolista:
        auto.acceleration(random.randint(-10, 15))
        auto.travel(1)
        if auto.matka >= 10000:
            kilpailu = False

for auto in autolista:
    print(f"{auto.register}, {auto.maxspeed}, {auto.nopeus}, {auto.matka}")

