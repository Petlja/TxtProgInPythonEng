# -*- acsection: general-init -*-
import random, math
import pygame as pg

pg.init() # inicijalizujemo biblioteku PyGame
pg.display.set_caption("Лоптица прати миша")  # otvaramo prozor
(sirina, visina) = (250, 250)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

trag = []

def rastojanje(A, B):
    (xa, ya) = A
    (xb, yb) = B
    return math.sqrt((xa - xb)**2 + (ya - yb)**2)

(x, y) = (sirina // 2, visina // 2)

def crtaj():
    # postavljanje boje pozadine na belu
    prozor.fill(pg.Color("white"))
    n = len(trag)
    for i in range(n):
        (x, y) = trag[i]
        nijansa = 0 if n == 1 else (-255 / (n - 1)) * i + 255
        boja = (nijansa, nijansa, nijansa)
        pg.draw.circle(prozor, boja , (round(x), round(y)), 10)

def novi_frejm():
    global x, y
    (xm, ym) = pg.mouse.get_pos()
    d = rastojanje((x, y), (xm, ym))
    v = 3
    if d < v:
        (x, y) = (xm, ym)
    else:
        x = x + v * (xm - x) / d
        y = y + v * (ym - y) / d
    trag.append((x, y))
    if len(trag) > 20:
        trag.pop(0)

# -*- acsection: after-main -*-

kraj = False
sat = pg.time.Clock()  # sat koji određuje broj frejmova u sekundi
while not kraj:
    # crtamo i ažuriramo sadržaj prozora
    crtaj()
    pg.display.update()

    # proveravamo da li je korisnik isključio prozor
    for dogadjaj in pg.event.get():
        if dogadjaj.type == pg.QUIT:
            kraj = True

    # pauziramo do sledeceg frejma
    sat.tick(50)
    novi_frejm()

pg.quit() # isključujemo rad biblioteke PyGame
