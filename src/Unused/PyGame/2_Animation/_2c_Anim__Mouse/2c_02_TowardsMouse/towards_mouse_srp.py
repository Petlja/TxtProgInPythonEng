# -*- acsection: general-init -*-
import random, math
import pygame as pg

pg.init() # inicijalizujemo biblioteku PyGame
pg.display.set_caption("Лоптица прати миша")  # otvaramo prozor
(sirina, visina) = (250, 250)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

# rastojanje između dve date tačke (zadate parovima koordinata)
def rastojanje(A, B):
    (xa, ya) = A
    (xb, yb) = B
    return math.sqrt((xa - xb)**2 + (ya - yb)**2)

# pozicija loptice
(x, y) = (sirina // 2, visina // 2)

def crtaj():
    # crtamo zelenu lopticu na beloj pozadini
    prozor.fill(pg.Color("white")) 
    pg.draw.circle(prozor, pg.Color("green"), (round(x), round(y)), 10)

def novi_frejm():
    global x, y
    (xm, ym) = pg.mouse.get_pos()     # koordinate pozicije miša
    d = rastojanje((x, y), (xm, ym))  # rastojanje tačke od miša
    v = 2                             # brzina kretanja loptice
    if d < v:                         # ako je loptica dovoljno blizu miša pomera
        (x, y) = (xm, ym)             #    pomera se tačno na poziciju miša
    else:                             # u suprotnom
        x = x + v * (xm - x) / d      #    pomera se malo u smeru ka mišu
        y = y + v * (ym - y) / d

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
