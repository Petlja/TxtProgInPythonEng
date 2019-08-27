import pygame as pg, pygamebg
num_rows, num_cols = 10, 10
a = 50 # square size
(width, height) = (a* num_cols, a * num_rows)
canvas = pygamebg.open_window(width, height, "Dot-eater")

(character_row, character_col) = (num_rows // 2, num_cols // 2)

def new_frame():
    canvas.fill(pg.Color("black"))   # paint canvas

    # white dots
    for x in range(a // 2, width, a):
        for y in range(a // 2, height, a):
            pg.draw.circle(canvas, pg.Color("white"), (x, y), 3)
   
    # draw dot-eater
    (x, y) = (character_col * a + a//2, character_row * a + a//2)
    pg.draw.circle(canvas, pg.Color('yellow'), (x, y), a // 3)
    
def handle_event(event):
    global character_row, character_col
    if event.type == pg.KEYDOWN:
        if event.key == pg.K_LEFT and (character_col > 0):
            character_col -= 1
        if event.key == pg.K_RIGHT and (character_col < num_cols-1):
            character_col += 1
        if event.key == pg.K_UP and (character_row > 0):
            character_row -= 1
        if event.key == pg.K_DOWN and (character_row < num_rows-1):  
            character_row += 1

pygamebg.frame_loop(30, new_frame, handle_event)

