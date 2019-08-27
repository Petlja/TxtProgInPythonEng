# -*- acsection: general-init -*-
import pygame as pg, pygamebg
canvas = pygamebg.open_window(500, 300, "House")
# -*- acsection: main -*-
canvas.fill(pg.Color("darkgreen")) # paint background

def house(x, y, a, wall_color):
    pg.draw.polygon(canvas, pg.Color("red"), [(x, y), (x+7*a, y-5*a), (x+14*a, y)]) # roof
    pg.draw.rect(canvas, wall_color,        (x,        y,      14*a, 10*a)) # walls
    pg.draw.rect(canvas, pg.Color("brown"), (x +  1*a, y + 2*a, 3*a,  3*a)) # left window
    pg.draw.rect(canvas, pg.Color("brown"), (x + 10*a, y + 2*a, 3*a,  3*a)) # right window
    pg.draw.rect(canvas, pg.Color("brown"), (x +  5*a, y + 3*a, 4*a,  7*a)) # door

house(150,  90,  8, (220, 220, 220))
house(250, 130,  9, pg.Color("white"))
house(350, 160, 10, (255, 255, 150))
house( 50, 150, 10, pg.Color("khaki"))

# -*- acsection: after-main -*-
pygamebg.wait_loop()
