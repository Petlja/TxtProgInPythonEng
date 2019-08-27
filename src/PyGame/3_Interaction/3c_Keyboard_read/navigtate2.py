import pygame as pg, pygamebg
w, h = 400, 400
canvas = pygamebg.open_window(w, h, "Navigate with the arrows")

x, y = w//2, h//2
dx, dy = 1, 0

def new_frame():
    global x, y, dx, dy

    pressed = pg.key.get_pressed()
    if pressed[pg.K_LEFT]:  dx -= 1
    if pressed[pg.K_RIGHT]: dx += 1
    if pressed[pg.K_UP]:    dy -= 1
    if pressed[pg.K_DOWN]:  dy += 1
    
    x = (x + dx) % w
    y = (y + dy) % h
    
    canvas.fill(pg.Color("black"))   # paint canvas to black
    pg.draw.circle(canvas, pg.Color('yellow'), (x, y), 20)
    
pygamebg.frame_loop(15, new_frame)
