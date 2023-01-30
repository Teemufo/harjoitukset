#Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän. Muokatun funktion avulla
#voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa. Edellisestä tehtävästä poiketen nopan heittelyä jatketaan
#pääohjelmassa kunnes saadaan nopan maksimisilmäluku, joka kysytään käyttäjältä ohjelman suorituksen alussa.

import random

tahkot = int(input("Anna nopan tahkojen lukumäärä: "))

def nopan_heitto():
    return random.randint(1, tahkot)

while nopan_heitto():
    result = nopan_heitto()
    print(result)
    if result == tahkot:
        break