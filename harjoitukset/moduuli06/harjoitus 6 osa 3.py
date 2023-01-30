#Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina ja palauttaa paluuarvonaan vastaavan
#litramäärän. Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi. Muunnos on tehtävä aliohjelmaa
#hyödyntäen. Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.
#Yksi gallona on 3,785 litraa.

def muunnosohjelma():
    muunnos = gallona*3.785
    return muunnos

gallona = float(input("Anna gallona määrä: "))

while gallona >= 0:
    litra = muunnosohjelma()
    print(f"{gallona} gallonaa on {litra} litraa.")
    gallona = float(input("Anna gallona määrä: "))
    if gallona < 0:
        break
