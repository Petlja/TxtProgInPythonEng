# -*- acsection: general-init -*-
import pygame as pg
import pygamebg as pgbg

(width, height) = (800, 800)
window = pgbg.open_window(width, height, "Rocket")

# -*- acsection: main -*-
# load image of the rocket
rocket  = pg.image.load("rocket.png")

# clear screen
window.fill(pg.Color("black"))

# draw rocket
window.blit(rocket, (0, height - rocket.get_height()))

# -*- acsection: after-main -*-
pgbg.wait_loop()
