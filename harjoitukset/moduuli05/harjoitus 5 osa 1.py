#Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän. Ohjelma heittää kerran kaikkia arpakuutioita
#ja tulostaa silmälukujen summan. Käytä for-toistorakennetta.
import random
arpaluku = int(input("Kuinka monta arpakuutiota heitetään: "))
lukulista = []
lukulista.append((random.randint(1, 6))*arpaluku)
for summa in lukulista:
    print(f"Arpakuutioiden silmälukujen summa on {summa}")

