import pygame as pg, pygamebg
(width, height) = (400, 400)
canvas = pygamebg.open_window(width, height, "Lines with mouse")

mosue_pos = (width // 2, height // 2)
line_start = mosue_pos
line_is_being_drawn = False
previous_lines = []

def new_frame():
    canvas.fill(pg.Color("white")) # paint canvas
    if line_is_being_drawn:
        pg.draw.line(canvas, pg.Color('black'), line_start, mosue_pos)
    for a, b in previous_lines:
        pg.draw.line(canvas, pg.Color('black'), a, b)

def handle_event(event):
    global line_is_being_drawn, line_start, previous_lines, mosue_pos
    if event.type == pg.MOUSEBUTTONDOWN:
        if (event.button  == 1): # left
            line_is_being_drawn = True
            line_start = event.pos
        if (event.button  == 3): # right
            previous_lines = []
    elif event.type == pg.MOUSEBUTTONUP:
        if (event.button  == 1): # left
            line_is_being_drawn = False
            line_ends = (line_start, event.pos)
            previous_lines.append(line_ends)
    elif event.type == pg.MOUSEMOTION:
        mosue_pos = event.pos

pygamebg.frame_loop(30, new_frame, handle_event)
