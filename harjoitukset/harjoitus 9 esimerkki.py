class Dog:

    dog_count = 0

    def __init__(self, name, weight, age):
        Dog.dog_count += 1
        print(f"{Dog.dog_count}. Uusi koira luotu, nimi: {name}")
        self.name = name
        self.weight = weight
        self.age = age
        self.energyLevel = 50
        self.distance = 0

    def eat(self):
        self.energyLevel = 100

    def run(self, meters):
        while meters > 0 and self.energyLevel - 0.1 > 0:
            meters -= 1
            self.distance = self.distance + 1
            self.energyLevel = self.energyLevel - 0.1

    def say_hello(self):
        print(f"Hei olen {self.name}," 
        f"paino: {self.weight} kg, ikä: {self.age} vuotta, "
        f"energiaa jäljellä {self.energyLevel}, "
        f"juoksemani matka on {self.distance} metriä")


dog1 = Dog("Rekku", 5, 2)
dog2 = Dog("Ruffe", 8, 12)

dog1.say_hello()
dog2.say_hello()
dog1.eat()
dog1.run(1000)
dog2.run(2000)

dog3 = Dog("Jannu", 12, 10)


# lisää koiria, sijoitetaan viittaukset listaan

dogs = []
for i in range(5):
    dogs.append(Dog("Koira " + str(i+1), 5+i, 5+i*2))

for dog in dogs:
    dog.say_hello()


print(f"Koiria luotu yhteensä: {Dog.dog_count}")
