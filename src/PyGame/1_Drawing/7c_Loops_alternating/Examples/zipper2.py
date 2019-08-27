# -*- acsection: general-init -*-
import pygame as pg, pygamebg
(width, height) = (100, 600)
canvas = pygamebg.open_window(width, height, "Zipper")

canvas.fill(pg.Color("blue"))
# -*- acsection: main -*-

line_length = 50       # length of one zipper line 
margin_left_right = 15 # margin to left and right edge of the window
margin_up_down = 40    # margin to upper and lower edge of the window
d_y = 15               # vertical space between zipper lines

# x coordinates of line starts and ends
x_left_start = margin_left_right
x_left_end = x_left_start + line_length
x_right_start = width - margin_left_right - line_length
x_right_end = x_right_start + line_length

y = margin_up_down # y coordinate of the current line 
while y < height - margin_up_down:
    pg.draw.line(canvas, pg.Color("yellow"), (x_left_start, y), (x_left_end, y), 6);
    y += d_y # preparing to draw the next line
    pg.draw.line(canvas, pg.Color("yellow"), (x_right_start, y), (x_right_end, y), 6);
    y += d_y # preparing to draw the next line
 
# -*- acsection: after-main -*-
pygamebg.wait_loop()
