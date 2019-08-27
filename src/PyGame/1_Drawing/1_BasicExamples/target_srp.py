# -*- acsection: general-init -*-
import pygame as pg, petljapg
(sirina, visina) = (200, 200)
prozor = petljapg.open_window(sirina, visina, "Три круга")
# -*- acsection: main -*-

prozor.fill(pg.Color("white")) # bojimo pozadinu u belo
(cx, cy) = (sirina // 2, visina // 2) # centar krugova je u sredni ekrana
pg.draw.circle(prozor, pg.Color("red"), (cx, cy), 100)   # crveni krug
pg.draw.circle(prozor, pg.Color("blue"), (cx, cy), 75)   # plavi krug
pg.draw.circle(prozor, pg.Color("green"), (cx, cy), 50)  # zeleni krug

# -*- acsection: after-main -*-
petljapg.wait_loop()
