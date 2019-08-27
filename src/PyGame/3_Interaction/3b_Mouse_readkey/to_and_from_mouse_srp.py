import pygame as pg, petljapg
(sirina, visina) = (400, 400)
prozor = petljapg.open_window(sirina, visina, "Лоптица прати миша")

(x, y) = (sirina // 2, visina // 2) # loptica krece iz centra

def nov_frejm():
    global x, y
    (xm, ym) = pg.mouse.get_pos()     # koordinate pozicije misa
    # pomeraj je deseti deo rastojanja do misa
    dx = 0.1 * (xm - x)
    dy = 0.1 * (ym - y)
    
    pritisnut_taster_misa = pg.mouse.get_pressed()
    if pritisnut_taster_misa[0]:
        x, y = x - dx, y - dy # loptica se pomera od misa
    else:
        x, y = x + dx, y + dy # loptica se pomera ka misu

    # crtamo zelenu lopticu na beloj pozadini
    prozor.fill(pg.Color("white")) 
    pg.draw.circle(prozor, pg.Color("green"), (int(x), int(y)), 10)

petljapg.frame_loop(50, nov_frejm)
