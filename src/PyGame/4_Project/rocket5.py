# -*- acsection: general-init -*-
import pygame as pg
import pygamebg as pgbg

(width, height) = (800, 500)
window = pgbg.open_window(width, height, "Rocket")

pg.key.set_repeat(10,10)

# -*- acsection: main -*-
# load images
rocket  = pg.image.load("rocket.png")
martian = pg.image.load("martian.png")
planet  = pg.image.load("planet.png")

# martian parameters - position and speed
martian_x = 0
martian_y = planet.get_height()
martian_speed = 3

# rocket position
rocket_x = 0
rocket_y = height - rocket.get_height()

# handle events
def keydown(e):
    # variable that is changed
    global rocket_x
    dx = 5
    # right and left arrow moves the rocket by 5 pixels
    if e.key == pg.K_RIGHT:
        rocket_x += dx
    elif e.key == pg.K_LEFT:
        rocket_x -= dx

# draw sceen
def draw():
    # variables that are changed in this function
    global martian_x, martian_speed

    # clear screen
    window.fill(pg.Color("black"))

    # draw planets
    for i in range(8):
        window.blit(planet, (100*i, 0))

    # draw martian
        window.blit(martian, (martian_x, martian_y))
        
    # draw rocket
    window.blit(rocket, (rocket_x, rocket_y))
    
    # move martian
    martian_x += martian_speed
    # change direction if it falls of screen
    if martian_x < 0 or martian_x > width - martian.get_width():
        martian_speed = -martian_speed

# -*- acsection: after-main -*-
pgbg.frame_loop(100, draw, {pg.KEYDOWN: keydown})
