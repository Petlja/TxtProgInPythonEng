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
x_left = margin_left_right
x_right = width - margin_left_right - line_length

# coordinates of the start of the current line 
x_start = x_left
y = margin_up_down

while y < height - margin_up_down:
    x_end = x_start + line_length
    pg.draw.line(canvas, pg.Color("yellow"), (x_start, y), (x_end, y), 6);
    
    # preparing to draw the next line
    y += d_y              # y coordinate of the next line
    if x_start == x_left: # x_start is the opposite of the previous one
        x_start = x_right
    else:
        x_start = x_left
 
# -*- acsection: after-main -*-
pygamebg.wait_loop()
