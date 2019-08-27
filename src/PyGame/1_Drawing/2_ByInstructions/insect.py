# -*- acsection: general-init -*-
import pygame as pg, pygamebg
canvas = pygamebg.open_window(300, 300, "Ant")

# -*- acsection: main -*-
canvas.fill(pg.Color("white")) # paint background

pg.draw.ellipse(canvas, pg.Color("limegreen"), (75, 100, 150, 180))    # head
pg.draw.line(canvas, pg.Color("limegreen"), (130, 110), (120, 20), 6)  # left antenna
pg.draw.line(canvas, pg.Color("limegreen"), (170, 110), (180, 20), 6)  # right antenna
pg.draw.circle(canvas, pg.Color("limegreen"), (120, 20), 10)           # top of the left antenna
pg.draw.circle(canvas, pg.Color("limegreen"), (180, 20), 10)           # top of the right antenna
pg.draw.ellipse(canvas, pg.Color("black"), (110, 140, 30, 50))         # left eye
pg.draw.ellipse(canvas, pg.Color("black"), (160, 140, 30, 50))         # right eye

# -*- acsection: after-main -*-
pygamebg.wait_loop()
