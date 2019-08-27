# -*- acsection: general-init -*-
import pygame as pg, pygamebg
width, height = 400, 400
canvas = pygamebg.open_window(width, height, "Chessboard")
# -*- acsection: main -*-

canvas.fill(pg.Color("gray")) # background - light squares

# square size
num_squares = 8
square_width = width / num_squares
square_height = height / num_squares

# go through all the squares
for i in range(num_squares):
    for j in range(num_squares):
        # paint black squares
        if (i + j) % 2 != 0:
            pg.draw.rect(canvas, pg.Color("black"), (i*square_width, j*square_height, square_width, square_height))

# -*- acsection: after-main -*-
pygamebg.wait_loop()
