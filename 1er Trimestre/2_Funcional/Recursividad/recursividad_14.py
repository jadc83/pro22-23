"""
14. La función enesimo tiene la siguiente especificación:

Pre : t ≠ () ∧ 0 ≤ t < len(t)
enesimo(n: int, t: tuple)
Post : enesimo(n, t) = el n-ésimo elemento de t
Escribir una función recursiva que satisfaga dicha especificación.


"""
enesimo = lambda n, t, c : () if t == () else \
    t[0] if c == n - 1 else enesimo(n , t[1:], c + 1)
        
enesimoiter = lambda n, t : enesimo(n,t,0)     
