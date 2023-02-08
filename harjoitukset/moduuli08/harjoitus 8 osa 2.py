#Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja tulostaa kyseisessä maassa olevien
#lentokenttien lukumäärät tyypeittäin. Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä, että pieniä
#lentokenttiä on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne.

import mysql.connector


def connect_db():
    return mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='user1',
        password='salasana',
        autocommit=True
    )
connection = connect_db()

def maakoodi(koodi):
    sql = f"select count(type) from airport where iso_country='{koodi}' group by type"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return (result)


koodi = input("Anna maakoodi: ")
result = maakoodi(koodi)
print(f"Maakoodissa {koodi} on {result[-1][-1]} pientä lentokenttää, {result[1][-1]} helikopterikenttää, "
      f"{result[2][-1]} suurta lentokenttää, {result[0][-1]} käyttämätöntä lentokenttää ja {result[-2][-1]} keskiverto suurta lentokenttää.")