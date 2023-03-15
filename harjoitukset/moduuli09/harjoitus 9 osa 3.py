#Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän.
#Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt.
#Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km. Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5)
#kasvattaa kuljetun matkan lukemaan 2090 km.

class Auto:
    def __init__(self, register, maxspeed):
        self.register = register
        self.maxspeed = maxspeed
        self.nopeus = 0
        self.matka = 2000

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

auto = Auto("ABC-123", 142)

auto.acceleration(60)
auto.travel(1.5)

print(f"Auton nopeus on {auto.nopeus} km/h.")
print(f"Auton kulkema matka on {auto.matka} km.")
