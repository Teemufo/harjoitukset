#Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi. Ohjelma kysyy käyttäjältä, haluaako tämä syöttää
#uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa. Jos käyttäjä valitsee uuden lentoaseman syöttämisen,
#ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen. Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja
#tulostaa sitä vastaavan lentoaseman nimen. Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy. Käyttäjä saa valita
#uuden toiminnon miten monta kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa. (ICAO-koodi on lentoaseman
#yksilöivä tunniste. Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät koodeja helposti selaimen avulla.)

#funktio lisää lentoaseman sanakirjaan

def lisää():
    print("vaiheessa")
    tunnus = input("Anna lentoaseman tunnus: ")
    nimi = input("Anna lentoaseman nimi: ")
    # lisätään uusi lentoasema sanakirjaan
    lentoasemat[tunnus] = nimi
    return

#funktio hakee lentoaseman nimen ICAO-koodin perusteella sanakirjasta

def hae():
    koodi = input("Anna lentoaseman koodi: ")
    if koodi in lentoasemat:
        print(f"{koodi}")
        return

def tulosta():

#luon sanakirjan jolle annan yhden alkion

lentoasemat = {"EFHK" : "Helsinki-Vantaan lentoasema"}

toiminto = -1 #annetaan sellainen alkuarvo että päästään toiston sisään

while toiminto != 3:
    print("0 = Tulosta lentoasemien tiedot.")
    print("1 = Lisää uusi lentoasema.")
    print("2 = Hae lentoasema.")
    print("3 = Lopetus.")
    toiminto = int(input("Valitse toiminto: "))
    if toiminto == 0:
        tulosta()
    elif toiminto == 1:
        lisää()
    elif toiminto == 2:
        hae()
# TODO lisää toiminnot

print("Kiitos ja näkemiin.")
