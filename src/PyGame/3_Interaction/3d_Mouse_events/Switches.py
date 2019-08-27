import pygame as pg, pygamebg
(width, height) = (800, 500)
canvas = pygamebg.open_window(width, height, "Switches")

schema_images = (pg.image.load('Shema3_Off.png'), pg.image.load('Shema3_On.png'))
switch_images = (pg.image.load('SwitchOff.png'), pg.image.load('SwitchOn.png'))
bulb_images = (pg.image.load('BulbOff.png'), pg.image.load('BulbOn.png'))

switch_on = [False, False, False]
switch_pos = [(100, 200), (300, 150), (300, 250)]
bulb_pos = (500, 100)

def new_frame():
    light_is_on = switch_on[0] and (switch_on[1] or switch_on[2])
    canvas.blit(schema_images[light_is_on], (0, 0))
    for i in range(3):
        canvas.blit(switch_images[switch_on[i]], switch_pos[i])
    canvas.blit(bulb_images[light_is_on], bulb_pos)
    
def point_in_rectangle(point, upper_left_point, width, height):
    x, y = point
    x0, y0 = upper_left_point
    return x0 <= x and x <= x0 + width and y0 <= y and y <= y0 + height
    
def handle_event(event):
    global switch_on
    if event.type == pg.MOUSEBUTTONDOWN:   # mouse button pressed 
        mouse_point = event.pos
        for i in range(3):
            if point_in_rectangle(mouse_point, switch_pos[i], 80, 80):
                switch_on[i] = not switch_on[i]

pygamebg.frame_loop(10, new_frame, handle_event)
