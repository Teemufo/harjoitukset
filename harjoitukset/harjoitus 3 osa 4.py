#Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi.
#Vuosi on karkausvuosi, jos se on jaollinen neljällä. Sadalla jaolliset vuodet ovat karkausvuosia
#vain jos ne ovat jaollisia myös neljälläsadalla.

vuosi = int(input("Anna vuosiluku: "))
if vuosi/400:
    print("Vuosi on karkausvuosi.")
elif vuosi/100:
    print("Vuosi ei ole karkausvuosi.")
elif vuosi/4:
    print("Vuosi on karkausvuosi")
else:
    print("Vuosi ei ole karkausvuosi.")
#uuten jos vuosi ole karkausvuosi