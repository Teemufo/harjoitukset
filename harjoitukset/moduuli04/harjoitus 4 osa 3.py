#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
#Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.


lukuStr = input("Anna kokonaisluku, tyhjä lopettaa: ")


pienin = suurin = 0

if lukuStr != "":
    pienin = suurin = int(lukuStr)
while lukuStr != "":
    luku = int(lukuStr)
    if luku > suurin:
        suurin = luku
    elif luku < pienin:
        pienin = luku
    lukuStr = input("Anna kokonaisluku, tyhjä lopettaa: ")


print(f"Suurin antamasi luku on {suurin} ja pienin antamasi luku on {pienin}.")


