#Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit. Ohjelma ilmoittaa lentokenttien välisen
#etäisyyden kilometreinä. Laskenta perustuu tietokannasta haettuihin koordinaatteihin. Laske etäisyys geopy-kirjaston
#avulla: https://geopy.readthedocs.io/en/stable/. Asenna kirjasto valitsemalla View / Tool Windows / Python Packages.
#Kirjoita hakukenttään geopy ja vie asennus loppuun.

import mysql.connector

from geopy import distance

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

def get_airport(icao, icao2):
    sql = f"select latitude_deg from airport where ident='{icao}'"
        f"select longitude_deg from airport where ident ='{icao}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    lat1 = cursor.fetchall()
    lentokenttä1 = (lat1, lon1)
    lentokenttä2 = (lat2, lon2)
    result = print(distance.distance(lentokenttä1, lentokenttä2).km)
    return (result)

icao = input("Anna ensimmäisen lentokentän ICAO koodi: ")
icao2 = input("Anna toisen lentokentän ICAO koodi: ")
result = get_airport(icao, icao2)
print(result)