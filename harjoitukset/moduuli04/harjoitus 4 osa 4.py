#Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10. Kone arvuuttelee lukua pelaajalta siihen asti,
#kunnes tämä arvaa oikein. Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus
#tai Oikein. Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.

import random
luku = random.randint(1, 10)
arvaus = input("Arvaa luku yhden ja kymmenen välillä: ")
arvaus = int(arvaus)
while arvaus != luku:
    if arvaus < luku:
        print("Liian pieni luku. Arvaa uudestaan.")
        arvaus = input("Arvaa luku yhden ja kymmenen välillä: ")
        arvaus = int(arvaus)
    elif arvaus > luku:
        print("Liian suuri luku. Arvaa uudestaan.")
        arvaus = input("Arvaa luku yhden ja kymmenen välillä: ")
        arvaus = int(arvaus)
print("Arvasit oikein!")
