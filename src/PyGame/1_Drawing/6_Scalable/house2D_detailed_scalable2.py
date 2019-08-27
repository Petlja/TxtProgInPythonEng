# -*- acsection: general-init -*-
import pygame as pg, pygamebg
canvas = pygamebg.open_window(400, 300, "House")

# -*- acsection: main -*-
canvas.fill(pg.Color("darkgreen")) # paint background

def house(x, y, a, wall_color):
    pg.draw.polygon(canvas, pg.Color("red"), [(x, y), (x+7*a, y-5*a), (x+14*a, y)]) # roof
    pg.draw.rect(canvas, wall_color,        (x,        y,      14*a, 10*a)) # walls
    pg.draw.rect(canvas, pg.Color("brown"), (x +  1*a, y + 2*a, 3*a,  3*a)) # left window
    pg.draw.rect(canvas, pg.Color("brown"), (x + 10*a, y + 2*a, 3*a,  3*a)) # right window
    pg.draw.rect(canvas, pg.Color("brown"), (x +  5*a, y + 3*a, 4*a,  7*a)) # door

house(278, 110, 1, (211, 207, 169))
house(231, 119, 2, (217, 211, 164))
house(174, 130, 3, (228, 221, 152))
house(112, 142, 4, (231, 222, 150))
house( 18, 160, 6, (240, 230, 140))

# -*- acsection: after-main -*-
pygamebg.wait_loop()
