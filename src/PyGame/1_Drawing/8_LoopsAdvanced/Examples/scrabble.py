# -*- acsection: general-init -*-
import pygame as pg, pygamebg, random
width, height = 300, 300
canvas = pygamebg.open_window(width, height, "Scrabble")

# -*- acsection: main -*-

canvas.fill(pg.Color("white"))

step_x = 3
step_y = 15
d_y = 5

# leave a small space at the top of the window
y = d_y
# until the line hits the bottom of the window
while y + d_y < height:
    # start from the left edge of the screen
    x = 0
    # remember the coordinates of the previous point
    previous_x, previous_y = x, y
    # until the current point reaches the right edge of the window
    while x < width:
        # a random value in the interval [-d_y, d_y]
        dy = random.random() * 2 * d_y - d_y
        # draw a line from the previous point to the current point
        pg.draw.line(canvas, pg.Color("black"), (previous_x, previous_y), (x, y + dy))
        # the current point becomes the previous one for the next iteration
        previous_x, previous_y = x, y + dy
        # move to the right
        x += step_x
    # we move on to the next horizontal row
    y += step_y

# -*- acsection: after-main -*-
pygamebg.wait_loop()
