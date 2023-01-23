#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
#Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

#opettajan esimerkki
#kysytään
lukuStr = input("Anna kokonaisluku, tyhjä lopettaa: ")

#eka luku on alkuarvo suurimmalle ja pienimmälle jos se ei ole tyhjä

pienin = suurin = 0

if lukuStr != "":
    pienin = suurin = int(lukuStr)

#toistetaan niin kauan, kunnes käyttäjä antaa tyhjän merkkijonon

while lukuStr != "":
    luku = int(lukuStr)

#tarkistetaan että annattu luku suurin tähän astisista
    if luku > suurin:
        suurin = luku
    elif luku < pienin:
        pienin = luku
        #muista uusi arvo
    lukuStr = input("Anna kokonaisluku, tyhjä lopettaa: ")


print(f"Suurin antamasi luku on {suurin} ja pienin antamasi luku on {pienin}.")


