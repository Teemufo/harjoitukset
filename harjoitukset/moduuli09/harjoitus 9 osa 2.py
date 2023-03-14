#Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan nopeuden muutoksen (km/h).
#Jos nopeuden muutos on negatiivinen, auto hidastaa. Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa.
#Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi. Jatka pääohjelmaa siten,
#että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h. Tulosta tämän jälkeen auton nopeus.
#Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus. Kuljettua matkaa ei tarvitse vielä päivittää.

class Auto:
    def __init__(self, register, maxspeed):
        self.register = register
        self.maxspeed = maxspeed
        self.nopeus = 0
        self.matka = 0
    def acceleration(self, change):
        if self.nopeus > 0 and self.nopeus <= self.maxspeed:
            self.nopeus = self.nopeus + change

auto = Auto("ABC-123", "142 km/h")
auto.acceleration(30)

print(f"Auton rekisteritunnus on {auto.register}, sen huippunopeus on {auto.maxspeed}, "
       f"sen tämän hetkinen nopeus on {auto.nopeus} km/h ja sen kulkema matka on {auto.matka} km.")
