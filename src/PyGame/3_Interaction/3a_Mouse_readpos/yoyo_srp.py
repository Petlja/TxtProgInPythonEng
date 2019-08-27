import pygame as pg, petljapg, math
(sirina, visina) = (250, 250)
prozor = petljapg.open_window(sirina, visina, "Лоптица прати миша")

def rastojanje(A, B):
    (xa, ya) = A
    (xb, yb) = B
    return math.sqrt((xa - xb)**2 + (ya - yb)**2)

(x, y) = (sirina // 2, visina // 2) # polozaj loptice
(vx, vy) = (0, 0)                   # brzina loptice
duzina_lastisa = 80

def nov_frejm():
    global x, y, vx, vy
    xm, ym = pg.mouse.get_pos()       # koordinate pozicije miša
    r = rastojanje((x, y), (xm, ym))  # rastojanje tačke od miša
    ax, ay = 0, 0                     # vektor ubrzanja loptice
    if r > duzina_lastisa:
        # elasticna sila proizvodi ubrzanje ka misu (osloncu)
        k = 0.0001*(r-duzina_lastisa) 
        ax, ay = k * (xm - x), k * (ym - y)
    ay += 0.3                         # ubrzanje od tezine loptice

    vx, vy = vx + ax, vy + ay         # nova brzina
    x, y   = x + vx, y + vy           # novi polozaj

    # crtamo zelenu lopticu sa crnim "lastisem" na beloj pozadini
    prozor.fill(pg.Color("white")) 
    ix, iy = int(x), int(y)
    pg.draw.line(prozor, pg.Color("black"), (ix, iy), (xm, ym), 2)
    pg.draw.circle(prozor, pg.Color("green"), (ix, iy), 10)

petljapg.frame_loop(40, nov_frejm)
