# -*- acsection: general-init -*-
import pygame as pg, petljapg
prozor = petljapg.open_window(400, 400, "Паткица")
# -*- acsection: main -*-

# bojimo pozadinu u zeleno
prozor.fill(pg.Color("green"))

# crtamo glavu
pg.draw.ellipse(prozor, pg.Color("yellow"), (40, 50, 320, 300))
pg.draw.ellipse(prozor, pg.Color("black"), (40, 50, 320, 300), 1)
# crtamo oči
pg.draw.ellipse(prozor, pg.Color("black"), (130, 130, 40, 40))
pg.draw.ellipse(prozor, pg.Color("black"), (280, 120, 40, 40))
# crtamo usta
pg.draw.ellipse(prozor, pg.Color("red"), (200, 170, 120, 140))
pg.draw.ellipse(prozor, pg.Color("black"), (200, 170, 120, 140), 1)

# -*- acsection: after-main -*-
petljapg.wait_loop()
