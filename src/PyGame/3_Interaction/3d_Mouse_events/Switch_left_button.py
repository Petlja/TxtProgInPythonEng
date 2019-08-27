# -*- acsection: general-init -*-
import pygame as pg, pygamebg
(width, height) = (800, 500)
canvas = pygamebg.open_window(width, height, "Switch")

schema_images = (pg.image.load('Shema1_Off.png'), pg.image.load('Shema1_On.png'))
switch_images = (pg.image.load('SwitchOff.png'), pg.image.load('SwitchOn.png'))
bulb_images = (pg.image.load('BulbOff.png'), pg.image.load('BulbOn.png'))
switch_pos = (100, 200)
bulb_pos = (500, 100)

switch_on = False

def new_frame():
    canvas.blit(schema_images[switch_on], (0, 0))
    canvas.blit(switch_images[switch_on], switch_pos)
    canvas.blit(bulb_images[switch_on], bulb_pos)

def point_in_rectangle(point, upper_left_point, width, height):
    x, y = point
    x0, y0 = upper_left_point
    return x0 <= x and x <= x0 + width and y0 <= y and y <= y0 + height
    
# -*- acsection: main -*-
def handle_event(event):
    global switch_on
    # if left mouse button is pressed
    if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
        mouse_point = event.pos
        if point_in_rectangle(mouse_point, switch_pos, 80, 80):
            switch_on = not switch_on

pygamebg.frame_loop(10, new_frame, handle_event)
# -*- acsection: after-main -*-
