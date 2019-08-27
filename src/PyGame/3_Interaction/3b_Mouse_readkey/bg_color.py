import pygame as pg, pygamebg
canvas = pygamebg.open_window(400, 400, "Background color")

shade = 128

def new_frame():
    global shade
    pressed_mouse_button = pg.mouse.get_pressed()
    if pressed_mouse_button[0] and shade < 255: # 0 is left button
        shade += 1
    if pressed_mouse_button[2] and shade > 0: # 2 is ringt button
        shade -= 1
            
    color = (shade, shade, shade)
    canvas.fill(color) 

pygamebg.frame_loop(100, new_frame)
