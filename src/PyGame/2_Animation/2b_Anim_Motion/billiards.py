import pygame as pg, pygamebg
(width, height) = (800, 400)
canvas = pygamebg.open_window(width, height, "billiards")

(cx, cy) = (width // 2, height // 2) # position of the ball center (initially at canvas center)
(dx, dy) = (3, 2)  # ball displacement (initially 3 pixels to the right and 2 downwards per frame)
r = 15             # ball radius


def new_frame():
    global cx, cy, dx, dy  # there variables will be changed
    # moving the ball
    cx += dx
    cy += dy
    
    if cx - r < 0 or cx + r > width: # if the ball penetrated trough the left or right edge
        dx = -dx # change the x-direction (if it was going rightwards, now will go leftwards and vice versa)
    if cy - r < 0 or cy + r > height: # if the ball penetrated trough the upper of lower edge
        dy = -dy # change the y-direction (if it was going downwards, now will go upwards and vice versa)

    canvas.fill(pg.Color("darkgreen"))
    pg.draw.circle(canvas, pg.Color("white"), (cx, cy), r)

pygamebg.frame_loop(100, new_frame)
