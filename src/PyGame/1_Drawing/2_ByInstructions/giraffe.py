# -*- acsection: general-init -*-
import pygame as pg, pygamebg
canvas = pygamebg.open_window(300, 300, "giraffe_srp.py")

points = [(40, 208), (40, 107), (88, 82), (134, 13), (128, 9), (134, 13), 
    (137, 11), (128, 6), (160, 25), (159, 28), (136, 28), (98, 101),
    (100, 106), (101, 207), (97, 207), (95, 164), (83, 121), (85, 128),
    (54, 128), (55, 119), (44, 165), (44, 208)]
    
# -*- acsection: main -*-

canvas.fill(pg.Color("darkgreen")) # paint background

# we draw a polygon with the 'khaki' color 
pg.draw.polygon(canvas, pg.Color("khaki"), points)
    
# -*- acsection: after-main -*-
pygamebg.wait_loop()
