#Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l). Ohjelma ilmoittaa,
#onko hemoglobiiniarvo alhainen, normaali vai korkea.

#Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
#Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

sukupuoli = input("Anna biologinen sukupuolesi (mies/nainen):")
hemo = float(input("Anna hemoglobiini arvosi:"))
if sukupuoli=="mies" and hemo<134:
    print("Hemoglobiiniarvosi on alhainen.")
elif sukupuoli=="mies" and 134<=hemo<=195:
    print("Hemoglobiiniarvosi on normaali.")
elif sukupuoli=="mies" and hemo>195:
    print("Hemoglobiiniarvosi on korkea.")
if sukupuoli=="nainen" and hemo<117:
    print("Hemoglobiiniarvosi on alhainen.")
elif sukupuoli=="nainen" and 117<=hemo<=175:
    print("Hemoglobiiniarvosi on normaali.")
elif sukupuoli=="nainen" and hemo>175:
    print("Hemoglobiiniarvosi on korkea.")





