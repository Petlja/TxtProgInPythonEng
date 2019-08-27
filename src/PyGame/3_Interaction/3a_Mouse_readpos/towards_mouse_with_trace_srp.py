import pygame as pg, petljapg
(sirina, visina) = (400, 400)
prozor = petljapg.open_window(sirina, visina, "Лоптица прати миша")

(x, y) = (sirina // 2, visina // 2) # loptica krece iz centra
trag = []

def nov_frejm():
    global x, y, trag
    (xm, ym) = pg.mouse.get_pos()     # koordinate pozicije misa
    # loptica se pomera ka misu, za deseti deo rastojanja do misa
    x += 0.1 * (xm - x)
    y += 0.1 * (ym - y)
    trag.append((x, y))
    if len(trag) > 20:
        trag = trag[1:]

    prozor.fill(pg.Color("white")) # bela pozadina
    n = len(trag)
    nijansa = 255 # nijansa se menja od bele ka crnoj
    for x, y in trag:
        boja = (nijansa, nijansa, nijansa)
        pg.draw.circle(prozor, boja , (int(x), int(y)), 10)
        nijansa -= 12

petljapg.frame_loop(50, nov_frejm)
