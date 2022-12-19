
"""tomar_mientras = lambda c, sec, i: i if sec == () else \
    tomar_mientras(c, sec[1:], i + (sec[0],)) if sec[0] < c else \
        i
"""
        
aux = lambda x, y: x < y

tomar = lambda cond, sec, acu: sec if sec == () else \
    tomar(cond, sec[1:], acu + (sec[0],)) if aux(sec[0], cond) else \
        acu
    
tomar_mientras = lambda con, sec: tomar(con, sec, ())