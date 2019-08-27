# -*- acsection: general-init -*-
import pygame as pg, petljapg
prozor = petljapg.open_window(300, 300, "Чича Глиша")

# -*- acsection: main -*-
prozor.fill(pg.Color("white")) # bojimo pozadinu ekrana u belo

pg.draw.circle(prozor, pg.Color("black"), (150, 70), 20, 2)      # glava

pg.draw.line(prozor, pg.Color("blue"), (120, 50), (180,50), 3)   # obod šešira
pg.draw.rect(prozor, pg.Color("blue"), (130, 10, 40, 40))        # šešir

pg.draw.circle(prozor, pg.Color("black"), (145, 60), 2, 2)       # levo oko
pg.draw.circle(prozor, pg.Color("black"), (155, 60), 2, 2)       # desno oko

pg.draw.ellipse(prozor, pg.Color("red"), (145, 70, 10, 7))       # usta

pg.draw.line(prozor, pg.Color("black"), (150, 90), (150,170), 3) # telo

pg.draw.line(prozor, pg.Color("black"), (150, 110), (100, 120), 3) # leva ruka
pg.draw.line(prozor, pg.Color("black"), (100, 120), (80, 100), 3)

pg.draw.line(prozor, pg.Color("black"), (150, 110), (200, 150), 3) # desna ruka
pg.draw.line(prozor, pg.Color("black"), (200, 150), (210, 170), 3)

pg.draw.line(prozor, pg.Color("black"), (150, 170), (130, 200), 3) # leva noga
pg.draw.line(prozor, pg.Color("black"), (130, 200), (140, 250), 3)

pg.draw.line(prozor, pg.Color("black"), (150, 170), (170, 200), 3) # desna noga
pg.draw.line(prozor, pg.Color("black"), (170, 200), (160, 250), 3)

# -*- acsection: after-main -*-
petljapg.wait_loop()
