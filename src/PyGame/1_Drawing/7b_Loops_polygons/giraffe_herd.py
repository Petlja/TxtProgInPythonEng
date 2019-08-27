# -*- acsection: general-init -*-
import pygame as pg, pygamebg
canvas = pygamebg.open_window(300, 300, "giraffes")
# -*- acsection: main -*-

def draw_polygon(points, color, x0, y0):
    shifted_points = []
    for x, y in points:
        shifted_points.append((x+x0, y+y0))
    pg.draw.polygon(canvas, color, shifted_points)

giraffe = [(40, 208), (40, 107), (88, 82), (134, 13), (128, 9), (134, 13), 
    (137, 11), (128, 6), (160, 25), (159, 28), (136, 28), (98, 101),
    (100, 106), (101, 207), (97, 207), (95, 164), (83, 121), (85, 128),
    (54, 128), (55, 119), (44, 165), (44, 208)]
    

canvas.fill(pg.Color("darkgreen")) # paint background

#for (x, y) in ... (finish the program)
    
# -*- acsection: after-main -*-
pygamebg.wait_loop()
