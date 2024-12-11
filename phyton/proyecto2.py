import random

moneda_tirada = random.randint(0, 1)

if (moneda_tirada == 0):
    print("ha salido cara")

elif (moneda_tirada == 1):
    print("ha salido cruz")