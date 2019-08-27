# -*- acsection: general-init -*-
import pygame as pg, petljapg
sirina, visina = 400, 400
prozor = petljapg.open_window(sirina, visina, "Кретање помоћу стрелица")

x, y = sirina//2, visina//2

def nov_frejm():
    global x, y

# -*- acsection: main -*-
    pritisnut = pg.key.get_pressed()
    if pritisnut[pg.K_LEFT] and (x > 0):
        x -= 1
    if pritisnut[pg.K_RIGHT] and (x < sirina-1):
        x += 1
    if pritisnut[pg.K_UP] and (y > 0):
        y -= 1
    if pritisnut[pg.K_DOWN] and (y < visina-1):
        y += 1
# -*- acsection: after-main -*-

    prozor.fill(pg.Color("black"))   # bojimo prozor u crno
    pg.draw.circle(prozor, pg.Color('yellow'), (x, y), 20)
    
petljapg.frame_loop(50, nov_frejm)
