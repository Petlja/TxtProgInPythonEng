# -*- acsection: general-init -*-
import pygame as pg, pygamebg
canvas = pygamebg.open_window(300, 300, "House")
canvas.fill(pg.Color("white"))

# -*- acsection: main -*-
pg.draw.rect(canvas, pg.Color("yellow"), (60, 120, 180, 160))
pg.draw.polygon(canvas, pg.Color("red"), [(60, 120), (150, 20), (240, 120)])
pg.draw.rect(canvas, pg.Color("skyblue"), (80, 140, 50, 50))
pg.draw.line(canvas, pg.Color("black"), (80, 165), (130, 165))
pg.draw.line(canvas, pg.Color("black"), (105, 140), (105, 190))
pg.draw.rect(canvas, pg.Color("skyblue"), (170, 140, 50, 50))
pg.draw.line(canvas, pg.Color("black"), (170, 165), (220, 165))
pg.draw.line(canvas, pg.Color("black"), (195, 140), (195, 190))
pg.draw.rect(canvas, pg.Color("brown"), (120, 200, 60, 80))


# -*- acsection: after-main -*-
pygamebg.wait_loop()