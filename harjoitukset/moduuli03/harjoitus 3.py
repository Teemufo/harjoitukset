#Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä. Jos kuha on alamittainen, ohjelma käskee laskea
#kuhan takaisin järveen ilmoittaen samalla käyttäjälle,
#montako senttiä alimmasta sallitusta pyyntimitasta puuttuu. Kuha on alamittainen, jos sen pituus on alle 37 cm.

kuha = float(input("Anna kuhan pituus senttimetreinä: "))
if kuha<37:
    print(f"Kuha on {37-kuha:.0f} senttimetriä alimittainen ja se lasketaan takaisin järveen.")
