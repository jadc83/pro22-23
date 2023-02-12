import random


def dados(tiradas):
    total = 0
    for x in range(1,tiradas):
        num = random.randint(1,6)
        total += num
    return total


def prueba():
    "Esta funcion testea la suma de las tiradas"
    num = 0
    while num != 18:
        num = dados(3)
        print(num)