#Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api. Kirjoita ohjelma, joka kysyy käyttäjältä
#paikkakunnan nimen ja tulostaa sitä vastaavan säätilan tekstin sekä lämpötilan Celsius-asteina. Perehdy rajapinnan
#dokumentaatioon riittävästi. Palveluun rekisteröityminen on tarpeen, jotta saat rajapintapyynnöissä tarvittavan
#API-avaimen (API key). Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi.

import json
import requests

hakusana = input("Anna kaupungin nimi: ")

pyyntö = "https://api.openweathermap.org/data/2.5/weather?q=" + hakusana + "&appid=1dd7ced90414a2ae1f1c985cac643cb3" + "&units=metric"

try:
    vastaus = requests.get(pyyntö)
    if vastaus.status_code==200:
        json_vastaus = vastaus.json()
        print(f"Lämpötila celcius-asteina kaupungissa {hakusana}:")
        print(json_vastaus['main']['temp'])

except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa.")


