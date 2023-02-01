#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa listassa olevien lukujen summan.
#Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.

def summafunktio():
    tulos = sum(lukulista)
    return tulos

lukulista = []

luku = input("Anna kokonaisluku: ")
while luku !="":
    lukulista.append(int(luku))
    luku = input("Anna kokonaisluku: ")

tulos = summafunktio()
print(summafunktio())







