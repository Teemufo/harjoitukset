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
from prettytable import PrettyTable

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

t = PrettyTable(['Rekisteri', 'Huippunopeus (km/h)', 'Nopeus (km/h)', 'Kuljettu matka (km)' ])

t.add_row([(autolista[0].register), (autolista[0].maxspeed), (autolista[0].nopeus), (autolista[0].matka)])
t.add_row([(autolista[1].register), (autolista[1].maxspeed), (autolista[1].nopeus), (autolista[1].matka)])
t.add_row([(autolista[2].register), (autolista[2].maxspeed), (autolista[2].nopeus), (autolista[2].matka)])
t.add_row([(autolista[3].register), (autolista[3].maxspeed), (autolista[3].nopeus), (autolista[3].matka)])
t.add_row([(autolista[4].register), (autolista[4].maxspeed), (autolista[4].nopeus), (autolista[4].matka)])
t.add_row([(autolista[5].register), (autolista[5].maxspeed), (autolista[5].nopeus), (autolista[5].matka)])
t.add_row([(autolista[6].register), (autolista[6].maxspeed), (autolista[6].nopeus), (autolista[6].matka)])
t.add_row([(autolista[7].register), (autolista[7].maxspeed), (autolista[7].nopeus), (autolista[7].matka)])
t.add_row([(autolista[8].register), (autolista[8].maxspeed), (autolista[8].nopeus), (autolista[8].matka)])
t.add_row([(autolista[9].register), (autolista[9].maxspeed), (autolista[9].nopeus), (autolista[9].matka)])

print(t)