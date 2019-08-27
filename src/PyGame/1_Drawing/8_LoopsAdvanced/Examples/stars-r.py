# -*- acsection: general-init -*-
import pygame as pg, pygamebg, random
width, height = 400, 400
canvas = pygamebg.open_window(width, height, "Stars")

# -*- acsection: main -*-

def star(x, y, r):
    d = 2
    pg.draw.line(canvas, pg.Color("white"), (x-r, y), (x+r, y), d)
    pg.draw.line(canvas, pg.Color("white"), (x, y-r), (x, y+r), d)
    pg.draw.line(canvas, pg.Color("white"), (x-r/2, y-r/2), (x+r/2, y+r/2), d)
    pg.draw.line(canvas, pg.Color("white"), (x+r/2, y-r/2), (x-r/2, y+r/2), d)

canvas.fill(pg.Color("black"))

num_stars = 10
d_x = width // (num_stars + 1)
d_y = height // (num_stars + 1)
for i in range(num_stars):
    for j in range(num_stars):
        x = (i + 1) * d_x + random.randint(-d_x//2, d_x//2)
        y = (j + 1) * d_y + random.randint(-d_y//2, d_y//2)
        r = random.randint(10, 16)
        star(x, y, r)

# -*- acsection: after-main -*-
pygamebg.wait_loop()
