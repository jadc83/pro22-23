
from itertools import count, chain, groupby


a = list(count())
lista = ()

def divisores(num):
    acu = 0
    nums = []
    for i in range(1, num + 1):
        if num % i == 0:
            acu += 1
            nums.append(i)
    if acu == 2:
        print(nums)
