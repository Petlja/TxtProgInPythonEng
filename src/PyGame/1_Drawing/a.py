# -*- acsection: general-init -*-
import pygame as pg, petljapg
prozor = petljapg.open_window(400, 400, "Pygame")
# -*- acsection: main -*-

prozor.fill(pg.Color("white"))
pg.draw.line(prozor, pg.Color("black"), (100, 100), (300, 300), 5)

# -*- acsection: after-main -*-
petljapg.wait_loop()
