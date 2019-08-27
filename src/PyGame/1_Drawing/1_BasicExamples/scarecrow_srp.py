# -*- acsection: general-init -*-
import pygame as pg, petljapg
prozor = petljapg.open_window(300, 500, "Страшило")
# -*- acsection: main -*-
prozor.fill(pg.Color("white")) # bojimo pozadinu ekrana u belo

pg.draw.circle(prozor, pg.Color("black"), (150, 70), 50, 6)        # glava
pg.draw.line(prozor, pg.Color("black"), (150, 120), (150, 300), 6) # telo
pg.draw.line(prozor, pg.Color("black"), (80, 170), (220, 170), 6)  # ruke
pg.draw.line(prozor, pg.Color("black"), (150, 300), (90, 480), 6)  # leva noga
pg.draw.line(prozor, pg.Color("black"), (150, 300), (210, 480), 6) # desna noga

# -*- acsection: after-main -*-
petljapg.wait_loop()
