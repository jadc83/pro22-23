"""
x = 4
y = 5

igual = ( str(y) + "," + str(x) ) if x >= y  else ( str(x) + "," + str(y) )
"""

igual = lambda x, y : ( str(y) + "," + str(x) ) if x >= y  \
                                                else ( str(x) + "," + str(y) )
