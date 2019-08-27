# -*- acsection: general-init -*-
import pygame as pg, pygamebg
canvas = pygamebg.open_window(500, 300, "House")

# -*- acsection: main -*-
canvas.fill(pg.Color("darkgreen")) # paint background

def draw_house(x, y, wall_color):
    pg.draw.polygon(canvas, pg.Color("red"), [(x, y), (x+70, y-50), (x+140, y)]) # roof
    pg.draw.rect(canvas, wall_color,       (x,       y,     140, 100)) # walls
    pg.draw.rect(canvas, pg.Color("brown"), (x +  10, y + 20, 30,  30)) # left window
    pg.draw.rect(canvas, pg.Color("brown"), (x + 100, y + 20, 30,  30)) # right window
    pg.draw.rect(canvas, pg.Color("brown"), (x +  50, y + 30, 40,  70)) # door
    
draw_house(150,  90, (220, 220, 220))
draw_house(220, 130, pg.Color("white"))
draw_house(350, 160, (255, 255, 150))
draw_house( 50, 150, pg.Color("khaki"))

# -*- acsection: after-main -*-
pygamebg.wait_loop()
