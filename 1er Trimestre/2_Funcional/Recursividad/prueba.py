
# T = (2,5,7,1,8)



menor = lambda t: t[0] if len(t) == 1 else \
    menor( (t[0],) + t[1:][1:] ) if t[0] < t[1:][0] else \
        menor(t[1:])

menormin = lambda t: t[0] if len(t) == 1 else \
    menormin( (min(t[0], t[1:][0]),) + t[1:][1:]  )

mayormax = lambda t: t[0] if len(t) == 1 else \
    mayormax( (max(t[0], t[1:][0]),) + t[1:][1:]  )


factorial = lambda x: 1 if x == 0 else \
    x * factorial(x - 1)

fact = lambda cont, acu: acu if cont == 0 else \
    fact( cont - 1, cont * acu)

factiter1 = lambda n: fact(n, 1)

digitos = lambda n, acu: acu if n == 0 else \
    digitos(n // 10, acu + 1)

dig = lambda n: len(str(n))

voltea = lambda n: n if n < 10 else \
    (n % 10) * 10 ** (dig(n) - 1) + voltea(n // 10)

volteac = lambda n: n if len(n) == 1 else \
    volteac(n[1:]) + n[0]

x = 5
suma = lambda x: x + 1

fibo = lambda n: 0 if n == 0 else 1 if n == 1 else \
    fibo(n - 1) + fibo(n - 2)