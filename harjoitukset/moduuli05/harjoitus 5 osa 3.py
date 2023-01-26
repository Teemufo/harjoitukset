#Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku.
#Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.

#Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
#Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.

luku = input("Anna kokonaisluku: ")
luku = int(luku)
if luku >= 1:
    for check in range(2, int(luku/2)+1):
        if (luku%check)==0:
            print("Antamasi luku ei ole alkuluku")
            break
    else:
        print("Antamasi luku on alkuluku.")
else:
    print("Antamasi luku ei ole alkuluku")