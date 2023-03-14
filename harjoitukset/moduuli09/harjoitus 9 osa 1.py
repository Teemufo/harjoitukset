#Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus, tämänhetkinen nopeus ja kuljettu matka.
#Kirjoita luokkaan alustaja, joka asettaa ominaisuuksista kaksi ensin mainittua parametreina saatuihin arvoihin.
#Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi. Kirjoita pääohjelma, jossa luot
#uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h). Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.

class Auto:
    def __init__(self, register, maxspeed):
        self.register = register
        self.maxspeed = maxspeed
        self.nopeus = 0
        self.matka = 0

auto = Auto("ABC-123", "142 km/h")

print(f"Auton rekisteritunnus on {auto.register}, sen huippunopeus on {auto.maxspeed}, "
       f"sen tämän hetkinen nopeus on {auto.nopeus} km/h ja sen kulkema matka on {auto.matka} km.")
