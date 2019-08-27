# -*- acsection: general-init -*-
import pygame as pg, pygamebg
canvas = pygamebg.open_window(400, 400, "Cloud")

# -*- acsection: main -*-

canvas.fill(pg.Color("skyblue")) #paint background

# draw the sun
pg.draw.circle(canvas, pg.Color("yellow"), (100, 130), 80)

# draw a cloud of three circles
pg.draw.circle(canvas, pg.Color("white"), (200, 200), 50)
pg.draw.circle(canvas, pg.Color("white"), (150, 200), 30)
pg.draw.circle(canvas, pg.Color("white"), (250, 200), 30)

# -*- acsection: after-main -*-
pygamebg.wait_loop()
