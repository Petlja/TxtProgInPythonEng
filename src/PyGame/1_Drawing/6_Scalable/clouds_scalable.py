# -*- acsection: general-init -*-
import pygame as pg, pygamebg
canvas = pygamebg.open_window(400, 400, "Clouds")
# -*- acsection: main -*-

canvas.fill(pg.Color("skyblue")) # paint background

# draw the sun
pg.draw.circle(canvas, pg.Color("yellow"), (100, 100), 80)

# function draws a cloud at a given position, given size and shade of gray
def cloud(x, y, r, gray):
    # draw a cloud of three circles
    color = (gray, gray, gray)
    pg.draw.circle(canvas, color, (x, y), r)
    r_small = round(3 * r / 5)
    pg.draw.circle(canvas, color, (x - r, y), r_small)
    pg.draw.circle(canvas, color, (x + r, y), r_small)

cloud(240, 200, 40, 180)
cloud(270, 250, 50, 210)
cloud(230, 100, 50, 230)
cloud( 80,  80, 30, 190)
cloud(110, 320, 60, 255)
cloud(280,  70, 20, 210)
cloud(310,  80, 15, 220)
cloud(330,  55, 15, 240)

# -*- acsection: after-main -*-
pygamebg.wait_loop()
