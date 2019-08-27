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

for i in range(num_squares): # white horizontal stripes
    pg.draw.rect(canvas, pg.Color("white"), (0, i*square_height + d, width, d))

for i in range(num_squares): # black vertical stripes
    pg.draw.rect(canvas, pg.Color("black"), (i*square_width + d, 0, d, height))

# we go through all the intersections
for i in range(num_squares):
    for j in range(num_squares):
        # paint the cross sections where it should be white over black
        if (i + j) % 2 != 0:
            pg.draw.rect(canvas, pg.Color("white"), (i*square_width + d, j*square_height + d, d, d))

# -*- acsection: after-main -*-
pygamebg.wait_loop()
