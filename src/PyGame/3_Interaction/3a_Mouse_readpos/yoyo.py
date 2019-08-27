import pygame as pg, pygamebg, math
(width, height) = (250, 250)
canvas = pygamebg.open_window(width, height, "yoyo")

def distance(A, B):
    (xa, ya) = A
    (xb, yb) = B
    return math.sqrt((xa - xb)**2 + (ya - yb)**2)

(x, y) = (width // 2, height // 2) # ball position
(vx, vy) = (0, 0)                   # ball speed
rubber_band_length = 80

def new_frame():
    global x, y, vx, vy
    xm, ym = pg.mouse.get_pos()       # mouse position coordinates
    r = distance((x, y), (xm, ym))    # ball to mouse distance
    ax, ay = 0, 0                     # ball acceleration vector
    if r > rubber_band_length:
        # elastic force produces acceleration toward the mouse
        k = 0.0001*(r-rubber_band_length) 
        ax, ay = k * (xm - x), k * (ym - y)
    ay += 0.3                         # acceleration from ball weight

    vx, vy = vx + ax, vy + ay         # new speed
    x, y   = x + vx, y + vy           # new position

    # draw a green ball with a black rubber band on a white background
    canvas.fill(pg.Color("white")) 
    ix, iy = int(x), int(y)
    pg.draw.line(canvas, pg.Color("black"), (ix, iy), (xm, ym), 2)
    pg.draw.circle(canvas, pg.Color("green"), (ix, iy), 10)

pygamebg.frame_loop(40, new_frame)
