# -*- acsection: general-init -*-
import pygame as pg
import pygamebg as pgbg

(width, height) = (800, 800)
window = pgbg.open_window(width, height, "Rocket")

# -*- acsection: main -*-
# load images
rocket  = pg.image.load("rocket.png")
planet  = pg.image.load("planet.png")
martian = pg.image.load("martian.png")

# martian parameters - position and speed
martian_x = 0
martian_y = planet.get_height()
martian_speed = 3

def draw():
    # these variables are changed during animation
    global martian_x, martian_speed
    
    # clear screen
    window.fill(pg.Color("black"))

    # draw rocket
    window.blit(rocket, (0, height - rocket.get_height()))

    # draw planets
    for i in range(8):
        window.blit(planet, (100*i, 0))

    # draw martian
    window.blit(martian, (martian_x, martian_y))

    # move martian
    martian_x += martian_speed
    # change direction if it falls of screen
    if martian_x < 0 or martian_x + martian.get_width()> width:
        martian_speed = -martian_speed


# -*- acsection: after-main -*-
pgbg.frame_loop(100, draw)
