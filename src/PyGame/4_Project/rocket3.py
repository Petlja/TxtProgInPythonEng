# -*- acsection: general-init -*-
import pygame as pg
import pygamebg as pgbg

(width, height) = (800, 500)
window = pgbg.open_window(width, height, "Rocket")

# -*- acsection: main -*-
# load images
rocket  = pg.image.load("rocket.png")
planet  = pg.image.load("planet.png")

# clear screen
window.fill(pg.Color("black"))

# draw rocket
window.blit(rocket, (0, height - rocket.get_height()))

# draw planets
for i in range(8):
    window.blit(planet, (100*i, 0))

# -*- acsection: after-main -*-
pgbg.wait_loop()
