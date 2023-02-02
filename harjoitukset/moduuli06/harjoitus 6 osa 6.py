#Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan euroina.
#Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri. Pääohjelma kysyy käyttäjältä kahden
#pizzan halkaisijat ja hinnat sekä ilmoittaa, kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi
#yksikköhinta). Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.
import math

halkaisija1 = float(input("Anna ensimmäisen pizzan halkaisija senttimetreinä: "))
hinta1 = float(input("Anna ensimmäisen pizzan hinta euroina: "))
halkaisija2 = float(input("Anna toisen pizzan halkaisija senttimetreinä: "))
hinta2 = float(input("Anna toisen pizzan hinta euroina: "))

def hintalaskuri():
    tulos1 = hinta1/(halkaisija1/2)**2*math.pi
    tulos2 = hinta2/(halkaisija2/2)**2*math.pi
    if tulos1 < tulos2:
        tulos = "Ensimmäisen pizzan yksikköhinta on parempi."
    else:
        tulos = "Toisen pizzan yksikköhinta on parempi."
    return(tulos)

print(hintalaskuri())