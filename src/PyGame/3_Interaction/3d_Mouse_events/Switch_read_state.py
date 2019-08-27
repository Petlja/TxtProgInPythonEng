# -*- acsection: general-init -*-
import pygame as pg, pygamebg
(width, height) = (800, 500)
canvas = pygamebg.open_window(width, height, "Switch")

schema_images = (pg.image.load('Shema1_Off.png'), pg.image.load('Shema1_On.png'))
switch_images = (pg.image.load('SwitchOff.png'), pg.image.load('SwitchOn.png'))
bulb_images = (pg.image.load('BulbOff.png'), pg.image.load('BulbOn.png'))
switch_pos = (100, 200)
bulb_pos = (500, 100)

def point_in_rectangle(point, upper_left_point, width, height):
    x, y = point
    x0, y0 = upper_left_point
    return x0 <= x and x <= x0 + width and y0 <= y and y <= y0 + height

# -*- acsection: main -*-
switch_on = False
fps = 50

def new_frame():
    global switch_on
    pressed_mouse_button = pg.mouse.get_pressed()
    if pressed_mouse_button[0]:
        mouse_point = pg.mouse.get_pos()
        if point_in_rectangle(mouse_point, switch_pos, 80, 80):
            switch_on = not switch_on
# -*- acsection: after-main -*-
 
    canvas.blit(schema_images[switch_on], (0, 0))
    canvas.blit(switch_images[switch_on], switch_pos)
    canvas.blit(bulb_images[switch_on], bulb_pos)
    
pygamebg.frame_loop(fps, new_frame)
