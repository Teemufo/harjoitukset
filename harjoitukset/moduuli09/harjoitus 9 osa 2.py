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
        self.nopeus = self.nopeus + change
        if self.nopeus >= self.maxspeed:
            self.nopeus = self.maxspeed
        elif self.nopeus < 0:
            self.nopeus = 0
        return

auto = Auto("ABC-123", 142)

auto.acceleration(30)
auto.acceleration(70)
auto.acceleration(50)

print(f"Auton nopeus on {auto.nopeus} km/h.")

auto.acceleration(-200)

print(f"Auton nopeus on {auto.nopeus} km/h.")
