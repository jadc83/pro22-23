
"""distancia(1,30,0,30) 60"""

distancia = lambda hora1, minuto1, hora2, minuto2: \
    ( ( hora1 * 60 ) + minuto1 ) - ( ( hora2 * 60 ) + minuto2 ) \
         if ( hora1 >= 0 \
              and minuto1 >= 0 \
              and hora2 >= 0 \
              and minuto2 >= 0 ) \
         else 'Negativos no'
