# -*- acsection: general-init -*-
import pygame as pg, pygamebg
canvas = pygamebg.open_window(300, 300, "Fence")
# -*- acsection: main -*-

canvas.fill(pg.Color("skyblue")) # background
pg.draw.rect(canvas, pg.Color("green"), (0, 200, 300, 100))  # grass

boja = pg.Color('brown')
pg.draw.line(canvas, boja, ( 10, 100), (290, 100), 10) # top rail
pg.draw.line(canvas, boja, ( 10, 250), (290, 250), 10) # bottom rail

# pickets
pg.draw.polygon(canvas, boja, [(20, 80), (30, 70), (40, 80), (40, 270), (20, 270)])
pg.draw.polygon(canvas, boja, [(60, 80), (70, 70), (80, 80), (80, 270), (60, 270)])
pg.draw.polygon(canvas, boja, [(100, 80), (110, 70), (120, 80), (120, 270), (100, 270)])
pg.draw.polygon(canvas, boja, [(140, 80), (150, 70), (160, 80), (160, 270), (140, 270)])
pg.draw.polygon(canvas, boja, [(180, 80), (190, 70), (200, 80), (200, 270), (180, 270)])
pg.draw.polygon(canvas, boja, [(220, 80), (230, 70), (240, 80), (240, 270), (220, 270)])
pg.draw.polygon(canvas, boja, [(260, 80), (270, 70), (280, 80), (280, 270), (260, 270)])

# -*- acsection: after-main -*-
pygamebg.wait_loop()
