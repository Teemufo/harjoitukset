#Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin. Ohjelma hakee ja tulostaa koodia vastaavan lentokentän
#nimen ja sen sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta. ICAO-koodi on tallennettuna airport-taulun
#ident-sarakkeeseen.

import mysql.connector

#funktio hakee ja tulostaa pelaajan nimen ja paikan
#funktio tarvitsee parametreinä pelaajan nimen.
#funktio ei palauta mitään

def pelaajan_paikka(nimi):
    sql = "SELECT screen_name, location " +\
          "FROM game " +\
          "WHERE screen_name = '" + nimi + "'"

    print(sql) #tulostetaan lopullinen sql-lause
    kursori = yhteys.cursor()  #kursorin avulla välitetään tietoa python-koodin ja tietokannan välillä
    kursori.execute(sql) #suoritetaan sql-lause
    tulos = kursori.fetchall() #haetaan haun tulos ja sijoitetaan se muuttujaan tulos
    if kursori.rowcount >= 1: #saatiinko dataa
        for rivi in tulos:
            print(f"Pelaaja {rivi[0]} on paikassa {rivi[1]}.")
    return
#funktio hakee ja tulostaa kaikkien pelaajien nimet ja paikat
#funktio ei tarvitse parametrejä eikä palauta mitään
#funktio käyttää pääohjelmassa luotua tietokantayhteyttä.

def tulosta_pelaajat():
    sql = "SELECT screen_name, location " +\
          "FROM game"
    print(sql) #tulostetaan lopullinen sql-lause
    kursori = yhteys.cursor()  #kursorin avulla välitetään tietoa python-koodin ja tietokannan välillä
    kursori.execute(sql) #suoritetaan sql-lause
    tulos = kursori.fetchall() #haetaan haun tulos ja sijoitetaan se muuttujaan tulos
    if kursori.rowcount >= 1: #saatiinko dataa
        for rivi in tulos:
            print(f"Pelaaja {rivi[0]} on paikassa {rivi[1]}.")
    return

#def lentokenttä(koodi):
#    sql = "SELECT ident, municipality FROM airport"
 #   print(sql)
  #  kursori = yhteys.cursor()
   # kursori.execute(sql)
#    tulos = kursori.fetchall()
    #if kursori.rowcount >= 1:
   #     for rivi in tulos:
  #          print(f"{rivi}")
 #   return


#pääohjelma alkaa
#muodostetaan yhteys
yhteys = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='flight_game',
         user='user1',
         password='salasana',
         autocommit=True  # muutokset tietokantaan tehdään heti
         )

#kutsutaan funkiota, joka tulostaa pelaajien nimet ja paikat
#koodi = input("Anna lentokentän ICAO koodi: ")
#lentokenttä(koodi)

#funktio tulostaa halutun pelaajan nimen
pelaaja = input("Anna pelaajan nimi: ")
pelaajan_paikka(pelaaja)

#suljetaan yhteys
yhteys.close()
