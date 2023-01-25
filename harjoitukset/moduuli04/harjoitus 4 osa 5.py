#Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan. Jos jompikumpi tai molemmat ovat väärin,
#tunnus ja salasana kysytään uudelleen. Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on
#syötetty viisi kertaa. Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.
#(Oikea käyttäjätunnus on python ja salasana rules).
arvaukset = 1
tunnus = input("Anna käyttäjätunnus:")
salasana = input("Anna salasana:")
while tunnus != "python" and salasana != "rules":
    tunnus = input("Anna käyttäjätunnus uudestaan: ")
    salasana = input("Anna salasana uudestaan: ")
    arvaukset = arvaukset + 1
    if arvaukset == 5:
        print("Pääsy evätty.")
        break
if tunnus == "python" and salasana == "rules":
    print("Tervetuloa.")