#opettajan esimerkki

def say_hello(name):
    name = name.upper()
    print(f"terve {name}!")
    print(f"ja heippa, {name}")


    return "valmista tuli"



name = "kalle"
result = say_hello("Kalle")
print(result)
print(say_hello("Viivi"))
print(name)
#globaalin arvo ei muutu

def calculatesum(number1, number2):
    return number1 + number2

print(calculatesum(11, 34))
import random

correct_int = random.randint(1, 10)
print(correct_int)
def checkguess(guess):
    if guess < correct_int:
        return "Liian pieni arvaus"
    elif guess > correct_int:
        return "Liian suuri arvaus"
    else:
        return "oikein"
#pääohjelma omassa funktiossaan

def guessgame():
    game_on = True
    while game_on:
        user_guess = int(input("Arvaa luku:"))
        result = checkguess(user_guess)
        print(result)
        if checkguCess(user_guess) == "oikein":
            print("peli loppui")
            game_on = False
# guessgame()

def inventaario(tavarat):
    tavarat.append("tussi")
    print("Sinulla on seuraavat tavarat:")
    for tavara in tavarat:
        print("- " + tavara)


koulureppu = ["kynä", "kumi", "viivotin"]
inventaario(koulureppu)
print(koulureppu)
#tulosta kaikki alkiot
lista = [1, 3, 4, 5, 6]
for number in lista:
    print(number)
print("-------------")
#tulosta joka toisen alkion arvo
for i in range(len(lista)):
    if i%2==0:
        print(lista[i])
#listan kopiointi

lista2 = lista
lista2.remove(3)
print(lista)

#Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6.
#Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen.
#Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.
import random
def nopan_heitto():
    return random.randint(1, 6)

result=0
while nopan_heitto()!=6:
    result = nopan_heitto()
    print(result)
