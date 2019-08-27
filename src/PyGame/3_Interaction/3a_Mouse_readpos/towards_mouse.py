import pygame as pg, pygamebg
(width, height) = (400, 400)
canvas = pygamebg.open_window(width, height, "Ball following the mouse")

(x, y) = (width // 2, height // 2) # the ball starts from the center

def new_frame():
    global x, y
    (xm, ym) = pg.mouse.get_pos()     # coordinates of the mouse position
    # the ball moves toward the mouse, for the tenth of the distance to the mouse
    x += 0.1 * (xm - x)
    y += 0.1 * (ym - y)

    # draw a green ball on a white background
    canvas.fill(pg.Color("white")) 
    pg.draw.circle(canvas, pg.Color("green"), (int(x), int(y)), 10)

pygamebg.frame_loop(50, new_frame)
