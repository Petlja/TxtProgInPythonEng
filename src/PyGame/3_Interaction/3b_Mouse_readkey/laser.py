import pygame as pg, pygamebg
width, height = 400, 400
canvas = pygamebg.open_window(width, height, "Laser")

laser_on = False
energy = 25 # how full is the laser from 0 to 100

def draw():
    canvas.fill(pg.Color("black")) # background
    
    # the indicator shows how full the laser is
    pg.draw.rect(canvas, pg.Color("green"), (10, 10, 100, 10), 1)
    pg.draw.rect(canvas, pg.Color("green"), (10, 10, energy, 10))
    
    if laser_on:
        reach = (4 * energy, height - 4 * energy)
        pg.draw.line(canvas, pg.Color("red"), (0, height), reach, 5)

def new_frame():
    global energy, laser_on
    
    pressed_mouse_button = pg.mouse.get_pressed()
    laser_on = pressed_mouse_button[0] # left button
    if laser_on:
        if energy > 0:  # if the laser did not empty
            energy -= 1 # it empties
    else:
        # the laser is charged, but up to the maximum of 100
        energy = min(energy + 2, 100)

    draw()

pygamebg.frame_loop(15, new_frame)
