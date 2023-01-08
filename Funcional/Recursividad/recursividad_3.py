"""
3) La funcion repite tiene la siguiente especificacion

pre >>> >= 0
repite(s: str, n: int) >>> str
post >>> repite(s,n) = s * n

recrepite = s * ( s * (n - 1) )

sn = s * ( s * ( n - 1 ) )
"""

repite = lambda s, n : s * n

repite2 = lambda a, b : a if b <= 0 else a + repite2( a, ( b - 1 ) )
