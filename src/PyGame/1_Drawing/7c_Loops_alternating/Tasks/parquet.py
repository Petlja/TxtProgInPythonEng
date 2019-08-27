# -*- acsection: general-init -*-
import pygame as pg, pygamebg
(width, height) = (300, 300)
canvas = pygamebg.open_window(width, height, "Parquet")

# -*- acsection: main -*-
canvas.fill(pg.Color("goldenrod"))
a = 10    # width of one block
b = 6 * a # length of one block
num_squares_x = width // b
num_squares_y = height // b
for row in range(num_squares_y):
    for column in range(num_squares_y):
        (x0, y0) = (column*b, row*b)
        if (row + column) % 2 == 0:
            for i in range(6):
                pg.draw.rect(canvas, pg.Color("brown"), (x0+i*a, y0, a, b), 1)
        else:
            for i in range(6):
                pg.draw.rect(canvas, pg.Color("brown"), (x0, y0+i*a, b, a), 1)

# -*- acsection: after-main -*-
pygamebg.wait_loop()
