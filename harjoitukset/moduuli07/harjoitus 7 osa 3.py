#Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi. Ohjelma kysyy käyttäjältä, haluaako tämä syöttää
#uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa. Jos käyttäjä valitsee uuden lentoaseman syöttämisen,
#ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen. Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja
#tulostaa sitä vastaavan lentoaseman nimen. Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy. Käyttäjä saa valita
#uuden toiminnon miten monta kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa. (ICAO-koodi on lentoaseman
#yksilöivä tunniste. Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät koodeja helposti selaimen avulla.)

#funktio lisää lentoaseman sanakirjaan

def lisaa():
    print("vaiheessa")
    tunnus = input("Anna lentoaseman tunnus: ")
    nimi = input("Anna lentoaseman nimi: ")
    # lisätään uusi lentoasema sanakirjaan
    lentoasemat[tunnus] = nimi
    return

#funktio hakee lentoaseman nimen ICAO-koodin perusteella sanakirjasta

def hae():
    print("vaiheessa")
    return

#luon sanakirjan jolle annan yhden alkion

lentoasemat = {"Helsinki-Vantaan lentoasema" : " EFHK"}

toiminto = -1 #annetaan sellainen alkuarvo että päästään toiston sisään


while toiminto != 3:
    print("1 = lisää uusi lentoasema")
    print("2 = hae lentoasema")
    print("3 = lopeta")
    toiminto = int(input("Valitse toiminto"))
    if toiminto == 0:
        tulosta()
    elif toiminto == 1:
        lisää()
# TODO lisää toiminnot

print("Kiitos ja näkemiin.")
