#Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi.
#Vuosi on karkausvuosi, jos se on jaollinen neljällä. Sadalla jaolliset vuodet ovat karkausvuosia
#vain jos ne ovat jaollisia myös neljälläsadalla.

vuosi = int(input("Anna vuosiluku: "))
if vuosi%400==0:
    print("Vuosi on karkausvuosi.")
elif vuosi%100==0:
    print("Vuosi ei ole karkausvuosi.")
elif vuosi%4==0:
    print("Vuosi on karkausvuosi")
else:
    print("Vuosi ei ole karkausvuosi.")