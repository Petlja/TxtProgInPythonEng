# -*- acsection: general-init -*-
import pygame as pg, petljapg
prozor = petljapg.open_window(300, 300, "Емотикон")

# -*- acsection: main -*-
prozor.fill(pg.Color("white")) # bojimo pozadinu ekrana u belo

pg.draw.circle(prozor, pg.Color("yellow"), (150, 150), 100) # glava
pg.draw.ellipse(prozor, pg.Color("black"), (100, 90, 30, 60)) # levo oko
pg.draw.ellipse(prozor, pg.Color("black"), (170, 90, 30, 60)) # desno oko
pg.draw.ellipse(prozor, pg.Color("white"), (100, 190, 100, 20)) # unutrasnjost usta
pg.draw.ellipse(prozor, pg.Color("black"), (100, 190, 100, 20), 2) # ivica usta

# -*- acsection: after-main -*-
petljapg.wait_loop()
