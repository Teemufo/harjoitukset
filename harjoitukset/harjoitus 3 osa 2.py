#Kirjoita ohjelma, joka kysyy käyttäjältä laivan hyttiluokan (LUX, A, B, C) ja tulostaa sen sanallisen kuvauksen alla olevan
#luettelon mukaisesti. Tehtävässä on käytettävä if/elif/else-toistorakennetta.

#LUX on parvekkeellinen hytti yläkannella.
#A on ikkunallinen hytti autokannen yläpuolella.
#B on ikkunaton hytti autokannen yläpuolella.
#C on ikkunaton hytti autokannen alapuolella.
#Jos käyttäjä syöttää kelvottoman hyttiluokan, ohjelma tulostaa Virheellinen hyttiluokka.

luokka = input("Anna hyttiluokkasi (LUX, A, B, C) saadaksesi kuvauksen: ")
if luokka==str("LUX"):
    print("LUX on parvekkeellinen hytti yläkannella.")
elif luokka==str("A"):
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif luokka==str("B"):
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif luokka==str("C"):
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Antamasi hyttiluokka on virheellinen.")