#Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi. Ohjelma kysyy käyttäjältä, haluaako tämä syöttää
#uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa. Jos käyttäjä valitsee uuden lentoaseman syöttämisen,
#ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen. Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja
#tulostaa sitä vastaavan lentoaseman nimen. Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy. Käyttäjä saa valita
#uuden toiminnon miten monta kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa. (ICAO-koodi on lentoaseman
#yksilöivä tunniste. Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät koodeja helposti selaimen avulla.)

def lisää():
    tunnus = input("Anna lentoaseman tunnus: ")
    nimi = input("Anna lentoaseman nimi: ")
    lentoasemat[tunnus] = nimi
    return

def hae():
    koodi = input("Anna lentoaseman koodi: ")
    if koodi in lentoasemat:
        print(f"{lentoasemat[koodi]}")
        return

lentoasemat = {"EFHK" : "Helsinki-Vantaan lentoasema"}

toiminto = 0

while toiminto != 2:
    print("0 = Lisää uusi lentoasema.")
    print("1 = Hae lentoasema.")
    print("2 = Lopetus.")
    toiminto = int(input("Valitse toiminto: "))
    if toiminto == 0:
        lisää()
    elif toiminto == 1:
        hae()