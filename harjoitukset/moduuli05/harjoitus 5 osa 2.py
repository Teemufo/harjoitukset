#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
#Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen. Vihje:
#listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.

lukulista = []
luku = input("Anna kokonaisluku: ")
while luku != "":
    luku = int(luku)
    lukulista.append(luku)
    luku = input("Anna kokonaisluku: ")
lukulista.sort(reverse=True)
print(lukulista[0:5])
