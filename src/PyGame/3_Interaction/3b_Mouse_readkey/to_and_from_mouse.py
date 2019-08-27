import pygame as pg, pygamebg
(width, height) = (400, 400)
canvas = pygamebg.open_window(width, height, "Ball following the mouse")

(x, y) = (width // 2, height // 2) # ball starts from center of the window

def new_frame():
    global x, y
    (xm, ym) = pg.mouse.get_pos()     # mouse position coordinates 
    # displacement is the tenth of the distance to the mouse
    dx = 0.1 * (xm - x)
    dy = 0.1 * (ym - y)
    
    pressed_mouse_button = pg.mouse.get_pressed()
    if pressed_mouse_button[0]:
        x, y = x - dx, y - dy # ball moves away from the mouse
    else:
        x, y = x + dx, y + dy # ball moves towards the mouse

    # draw a green ball on a white background
    canvas.fill(pg.Color("white")) 
    pg.draw.circle(canvas, pg.Color("green"), (int(x), int(y)), 10)

pygamebg.frame_loop(50, new_frame)
