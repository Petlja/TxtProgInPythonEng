# -*- acsection: general-init -*-
import pygame as pg, petljapg
prozor = petljapg.open_window(400, 400, "Облаци")
# -*- acsection: main -*-

# bojimo pozadinu u plavo
prozor.fill(pg.Color("skyblue"))

# crtamo sunce
pg.draw.circle(prozor, pg.Color("yellow"), (100, 100), 80)

# procedura koja crta oblak na datoj poziciji, date velicine
# u datoj nijansi sive boje
def oblak(x, y, r, siva):
    # crtamo oblak od tri kruga
    boja = (siva, siva, siva)
    pg.draw.circle(prozor, boja, (x, y), r)
    r_malo = round(3 * r / 5)
    pg.draw.circle(prozor, boja, (x - r, y), r_malo)
    pg.draw.circle(prozor, boja, (x + r, y), r_malo)

oblak(240, 200, 40, 180)
oblak(270, 250, 50, 210)
oblak(230, 100, 50, 230)
oblak( 80,  80, 30, 190)
oblak(110, 320, 60, 255)
oblak(280,  70, 20, 210)
oblak(310,  80, 15, 220)
oblak(330,  55, 15, 240)

# -*- acsection: after-main -*-
petljapg.wait_loop()
