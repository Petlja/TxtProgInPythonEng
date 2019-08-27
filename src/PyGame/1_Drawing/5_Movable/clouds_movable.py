# -*- acsection: general-init -*-
import pygame as pg, pygamebg
canvas = pygamebg.open_window(400, 400, "Clouds")

# -*- acsection: main -*-

canvas.fill(pg.Color("skyblue")) # paint background

# draw the sun
pg.draw.circle(canvas, pg.Color("yellow"), (100, 130), 80)

# function draws a cloud at a given position, given size and shade of gray
def cloud(xc, yc, gray):
    # draw a cloud of three circles
    color = (gray, gray, gray)
    pg.draw.circle(canvas, color, (xc,      yc), 50)
    pg.draw.circle(canvas, color, (xc - 50, yc), 30)
    pg.draw.circle(canvas, color, (xc + 50, yc), 30)

cloud(240, 200, 180)
cloud(270, 250, 210)
cloud(230, 100, 230)
cloud( 80,  80, 190)
cloud(110, 320, 255)

# -*- acsection: after-main -*-
pygamebg.wait_loop()
