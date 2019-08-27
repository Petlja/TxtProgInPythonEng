# -*- acsection: general-init -*-
import pygame as pg, pygamebg
canvas = pygamebg.open_window(300, 300, "Cat")

# -*- acsection: main -*-
canvas.fill(pg.Color("white")) # paint background

pg.draw.circle(canvas, pg.Color("gray"), (150, 160), 100) # head
pg.draw.polygon(canvas, pg.Color("gray"), [(50, 30), (70, 100), (110, 100)]) # left ear
pg.draw.polygon(canvas, pg.Color("gray"), [(250, 30), (230, 100), (190, 100)]) # right ear
pg.draw.ellipse(canvas, pg.Color("yellow"), ( 90, 110, 40, 60)) # left eye
pg.draw.ellipse(canvas, pg.Color("yellow"), (170, 110, 40, 60)) # right eye
pg.draw.ellipse(canvas, pg.Color("green"),  (105, 135, 20, 30)) # left pupil
pg.draw.ellipse(canvas, pg.Color("green"),  (175, 135, 20, 30)) # right pupil
pg.draw.ellipse(canvas, pg.Color("darkgray"),  (80, 180, 70, 30))  # left part of the snout
pg.draw.ellipse(canvas, pg.Color("darkgray"),  (150, 180, 70, 30)) # right part of the snout
pg.draw.circle(canvas, pg.Color("black"), (150, 190), 10) # snout top
pg.draw.line(canvas, pg.Color("black"), (90, 190), (20, 160), 2) # left upper mustache
pg.draw.line(canvas, pg.Color("black"), (90, 195), (20, 195), 2) # left middle mustache
pg.draw.line(canvas, pg.Color("black"), (90, 200), (20, 220), 2) # left lower mustache
pg.draw.line(canvas, pg.Color("black"), (210, 190), (280, 160), 2) # right upper mustache
pg.draw.line(canvas, pg.Color("black"), (210, 195), (280, 195), 2) # right middle mustache
pg.draw.line(canvas, pg.Color("black"), (210, 200), (280, 220), 2) # right lower mustache

# -*- acsection: after-main -*-
pygamebg.wait_loop()
