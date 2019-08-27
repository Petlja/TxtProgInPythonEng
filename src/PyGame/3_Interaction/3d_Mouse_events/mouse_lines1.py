import pygame as pg, pygamebg
(width, height) = (400, 400)
canvas = pygamebg.open_window(400, 400, "Lines with mouse")

mosue_pos = (0, 0)
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
    global line_is_being_drawn, line_start, mosue_pos
    if event.type == pg.MOUSEBUTTONDOWN:
        line_is_being_drawn = True
        line_start = event.pos
    elif event.type == pg.MOUSEBUTTONUP:
        line_is_being_drawn = False
        line_ends = (line_start, event.pos)
        previous_lines.append(line_ends)
    elif event.type == pg.MOUSEMOTION:
        mosue_pos = event.pos

pygamebg.frame_loop(30, new_frame, handle_event)
