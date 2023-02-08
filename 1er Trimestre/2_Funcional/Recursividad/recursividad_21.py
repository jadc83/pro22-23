mayor = lambda t: t[0] if len(t) == 1 else \
   mayor(t[1:]) if t[0] < t[1] else \
      mayor(t[:1] + t[1:][1:])

menor = lambda t: t[0] if len(t) == 1 else \
   menor(t[1:]) if t[0] > t[1] else \
      menor(t[:1] + t[1:][1:])

mayorymenor = lambda t: (mayor(t),) + (menor(t),)