#Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan
#(kevät, kesä, syksy, talvi). Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
#Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi.

#opettajan esimerkki

vuodenajat = ("kevät", "kesä", "syksy", "talvi")

kuukaus = int(input("Anna kuukauden numero (1-12): "))

if kuukaus == 1 or kuukaus == 2 or kuukaus 12:
    vuodenaika = vuodenajat[3]
elif 3>= kuukaus >=5:
    vuodenaika = vuodenajat[0]
elif 6 >= kuukaus >= 8:
    vuodenaika = vuodenajat[1]
elif 9 >= kuukaus >= 11:
else vuodenaika = "tuntematon":

print(f"{kuukaus}")