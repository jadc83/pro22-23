hanoi = lambda a, b, c, n: () if n == 0 else \
                                hanoi(a, c, b, n - 1) + \
                                ("Muevo 1 disco de " + str(a) + " " + "a " + " " + str(b),) + \
                                hanoi(c, b, a, n - 1)