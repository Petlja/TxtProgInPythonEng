import pygame as pg, petljapg
(sirina, visina) = (400, 400)
prozor = petljapg.open_window(sirina, visina, "Лоптица прати миша")

(x, y) = (sirina // 2, visina // 2) # loptica krece iz centra

def nov_frejm():
    global x, y
    (xm, ym) = pg.mouse.get_pos()     # koordinate pozicije misa
    # loptica se pomera ka misu, za deseti deo rastojanja do misa
    x += 0.1 * (xm - x)
    y += 0.1 * (ym - y)

    # crtamo zelenu lopticu na beloj pozadini
    prozor.fill(pg.Color("white")) 
    pg.draw.circle(prozor, pg.Color("green"), (int(x), int(y)), 10)

petljapg.frame_loop(50, nov_frejm)
