# -*- acsection: general-init -*-
import pygame as pg, petljapg
prozor = petljapg.open_window(400, 400, "Облак")

# -*- acsection: main -*-
# bojimo pozadinu u plavo
prozor.fill(pg.Color("skyblue"))

# crtamo sunce
pg.draw.circle(prozor, pg.Color("yellow"), (100, 130), 80)

# crtamo oblak od tri kruga
pg.draw.circle(prozor, pg.Color("white"), (200, 200), 50)
pg.draw.circle(prozor, pg.Color("white"), (150, 200), 30)
pg.draw.circle(prozor, pg.Color("white"), (250, 200), 30)

# -*- acsection: after-main -*-
petljapg.wait_loop()
