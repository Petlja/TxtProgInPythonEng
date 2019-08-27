import pygame as pg, pygamebg
(width, height) = (400, 400)
canvas = pygamebg.open_window(width, height, "Ball following the mouse")

(x, y) = (width // 2, height // 2) # the ball starts from the center
trace = []

def new_frame():
    global x, y, trace
    (xm, ym) = pg.mouse.get_pos()     # coordinates of the mouse position
    # the ball moves toward the mouse, for the tenth of the distance to the mouse
    x += 0.1 * (xm - x)
    y += 0.1 * (ym - y)
    trace.append((x, y))
    if len(trace) > 20:
        trace = trace[1:]

    canvas.fill(pg.Color("white")) # white background
    n = len(trace)
    shade = 255 # shade changes from white to black
    for x, y in trace:
        color = (shade, shade, shade)
        pg.draw.circle(canvas, color, (int(x), int(y)), 10)
        shade -= 12

pygamebg.frame_loop(50, new_frame)
