# -*- acsection: general-init -*-
import pygame as pg, pygamebg
(width, height) = (400, 400)
canvas = pygamebg.open_window(width, height, "Space ship - left, right, fire")

ship = pg.image.load('spaceship.png')  # read the image of the space ship
(ship_width, ship_height) = (ship.get_width(), ship.get_height())

(ship_x, ship_y) = (width // 2, height - ship_height // 2) # middle of lower edge
DX = 10 # ship displacement left-right
DY = 10 # bullet displacement up
bullets = []

def new_frame():
    global ship_x, ship_y, bullets
    
    # move all the bullets up
    new_bullets = []
    for x, y in bullets:
        if y > DY: 
            new_bullets.append((x, y - DY))
    bullets = new_bullets
    
# -*- acsection: main -*-
    # check key presses (left, right, space)
    
    # read the status of all buttons
    pressed = pg.key.get_pressed()
    
    # if the left arrow is pressed and the ship can go left
    if pressed[pg.K_LEFT] and (ship_x > DX): 
        ship_x -= DX # move the ship to the left
        
    # if the right arrow is pressed and the ship can go right
    if pressed[pg.K_RIGHT] and (ship_x < width - ship_width - DX):
        ship_x += DX # move the ship to the rihgt
    
    if pressed[pg.K_SPACE]:               # if space is pressed
        bullets.append((ship_x, round(0.8 * height))) # add a bullet to the list
# -*- acsection: after-main -*-

    # draw
    canvas.fill(pg.Color("black"))    
    canvas.blit(ship, (ship_x - ship_width // 2, ship_y - ship_height // 2))
    for bullet in bullets:
        pg.draw.circle(canvas, pg.Color('white'), bullet, 3)

pygamebg.frame_loop(30, new_frame)
