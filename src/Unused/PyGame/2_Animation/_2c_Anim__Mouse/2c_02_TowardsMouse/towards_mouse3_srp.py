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

(x, y) = (sirina // 2, visina // 2) # vektor polozaja loptice
(vx, vy) = (0, 0)                   # vektor brzine loptice
(ax, ay) = (0, 0)                   # vektor ubrzanja loptice

def crtaj():
    # crtamo zelenu lopticu na beloj pozadini
    prozor.fill(pg.Color("white")) 
    ix, iy = round(x), round(y)
    pg.draw.line(prozor, pg.Color("black"), (ix, iy), (xm, ym), 2)
    pg.draw.circle(prozor, pg.Color("green"), (ix, iy), 10)

def novi_frejm():
    global x, y, vx, vy, ax, ay, xm, ym
    xm, ym = pg.mouse.get_pos()          # koordinate pozicije miša
    r = rastojanje((x, y), (xm, ym))     # rastojanje tačke od miša
    r0 = 10                              # duzina neistegnute niti
    if r > r0:
        a = 0.02*(r - r0)                # intenzitet ubrzanja
        a_jed = ((xm - x)/r, (ym - y)/r) # jedinicno ubrzanje ka misu
        ax, ay = a*a_jed[0], a*a_jed[1]  # novo ubrzanje
    else:
        ax, ay = 0, 0                        

    q = 0.99                             # prigusenje (otpor sredine)
    vx, vy = q*vx + ax, q*vy + ay        # nova brzina
    x, y = x + vx, y + vy                # novi polozaj

# -*- acsection: after-main -*-

kraj = False
sat = pg.time.Clock()  # sat koji određuje broj frejmova u sekundi
while not kraj:
    # ažuriramo model i sadržaj prozora
    novi_frejm()
    crtaj()
    pg.display.update()

    # proveravamo da li je korisnik isključio prozor
    for dogadjaj in pg.event.get():
        if dogadjaj.type == pg.QUIT:
            kraj = True

    # pauziramo do sledeceg frejma
    sat.tick(50)

pg.quit() # isključujemo rad biblioteke PyGame
