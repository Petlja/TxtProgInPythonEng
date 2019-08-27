import pygame as pg, petljapg
w, h = 400, 400
prozor = petljapg.open_window(w, h, "Кретање помоћу стрелица")

x, y = w//2, h//2
dx, dy = 1, 0

def nov_frejm():
    global x, y, dx, dy

    pritisnut = pg.key.get_pressed()
    if pritisnut[pg.K_LEFT]:  dx -= 1
    if pritisnut[pg.K_RIGHT]: dx += 1
    if pritisnut[pg.K_UP]:    dy -= 1
    if pritisnut[pg.K_DOWN]:  dy += 1
    
    x = (x + dx) % w
    y = (y + dy) % h
    
    prozor.fill(pg.Color("black"))   # bojimo prozor u crno
    pg.draw.circle(prozor, pg.Color('yellow'), (x, y), 20)
    
petljapg.frame_loop(15, nov_frejm)
