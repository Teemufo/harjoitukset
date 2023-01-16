import random
numero1 = random.randint(0, 9)
numero2 = random.randint(0, 9)
numero3 = random.randint(0, 9)
numero4 = random.randint(1, 6)
numero5 = random.randint(1, 6)
numero6 = random.randint(1, 6)
numero7 = random.randint(1, 6)
koodi1 = f"{numero1}{numero2}{numero3}"
koodi2 = f"{numero4}{numero5}{numero6}{numero7}"
print(f"Numerolukon kolminumeroinen koodi on {koodi1}")
print(f"Numerolukon nelinumeroinen koodi on {koodi2}")