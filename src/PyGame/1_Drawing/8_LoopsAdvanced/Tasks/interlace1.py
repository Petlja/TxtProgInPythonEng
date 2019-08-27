# -*- acsection: general-init -*-
import pygame as pg, pygamebg
width, height = 300, 300
canvas = pygamebg.open_window(width, height, "Interlace")
# -*- acsection: main -*-

canvas.fill(pg.Color("gray"))

# square size
num_squares = 10
square_width = width // num_squares
square_height = height // num_squares
d = 10

# we go through all the knots
for i in range(num_squares):
    for j in range(num_squares):
        if (i + j) % 2 != 0:
            # white over black
            pg.draw.rect(canvas, pg.Color("black"), (i*square_width + d, j*square_height, d, square_height))
            pg.draw.rect(canvas, pg.Color("white"), (i*square_width, j*square_height + d, square_width, d))
        else:
            # black over white
            pg.draw.rect(canvas, pg.Color("white"), (i*square_width, j*square_height + d, square_width, d))
            pg.draw.rect(canvas, pg.Color("black"), (i*square_width + d, j*square_height, d, square_height))

# -*- acsection: after-main -*-
pygamebg.wait_loop()
