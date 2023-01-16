import math
leiviskä = input("Anna leiviskät: ")
naula =input("Anna naulat: ")
luoti = input("Anna luodit: ")
leiviskä = float(leiviskä)
naula = float(naula)
luoti = float(luoti)
luoti2 = luoti*13.3
naula2 = naula*13.3*32
leiviskä2 = leiviskä*13.3*32*20
massa = luoti2+leiviskä2+naula2
kilo = math.floor(massa/1000)
gramma = massa-kilo*1000
print(f"Massa nykymittojen mukaan: {kilo:.0f} kilogrammaa ja {gramma:2.2f} grammaa")