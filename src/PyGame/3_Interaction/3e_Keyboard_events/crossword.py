# -*- acsection: general-init -*-
import pygame as pg, pygamebg
num_rows, num_cols = 5, 5
a = 50 # square size
(width, height) = (a* num_cols, a * num_rows)
canvas = pygamebg.open_window(width, height, "Crossword")

font = pg.font.SysFont("Arial", 30)
board = []
for row in range(num_rows):
    board.append([' '] * num_cols)
    
(frame_row, frame_col) = (0, 0)

# -*- acsection: main -*-
def handle_event(event):
    global frame_row, frame_col
    if event.type == pg.KEYDOWN:
        if event.key == pg.K_LEFT:
            if frame_col > 0:
                frame_col -= 1
        elif event.key == pg.K_RIGHT:
            if frame_col < num_cols-1:
                frame_col += 1
        elif event.key == pg.K_UP:
            if frame_row > 0:
                frame_row -= 1
        elif event.key == pg.K_DOWN:
            if frame_row < num_rows-1:
                frame_row += 1
        else:
            letter = chr(event.key).upper()
            if letter in ' ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                board[frame_row][frame_col] = letter
# -*- acsection: after-main -*-

def display_letter(text, row, col):
    if text == ' ':
        d = 6
        square = (a*col + d, a*row + d, a - 2*d, a - 2*d)
        pg.draw.rect(canvas, pg.Color("black"), square)
    else:
        text_image = font.render(text, True, pg.Color("black"))
        x = a * col + (a - text_image.get_width()) // 2
        y = a * row + (a - text_image.get_height()) // 2
        canvas.blit(text_image, (x, y))

def new_frame():
    canvas.fill(pg.Color("white"))   # paint background
    for x in range(0, width+1, a): # vertical lines
        pg.draw.line(canvas, pg.Color("black"), (x, 0), (x, height), 2)
    for y in range(0, height+1, a): # horizontal lines
        pg.draw.line(canvas, pg.Color("black"), (0, y), (width, y), 2)

    pg.draw.rect(canvas, pg.Color("blue"), (a*frame_col, a*frame_row, a, a), 4) # frame

    for row in range(num_rows): # letters
        for col in range(num_cols):
            display_letter(board[row][col], row, col)
            
pygamebg.frame_loop(30, new_frame, handle_event)
