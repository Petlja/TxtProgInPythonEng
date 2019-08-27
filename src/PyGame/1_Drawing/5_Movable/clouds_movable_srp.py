# -*- acsection: general-init -*-
import pygame as pg, petljapg
prozor = petljapg.open_window(400, 400, "Облаци")

# -*- acsection: main -*-
# bojimo pozadinu u plavo
prozor.fill(pg.Color("skyblue"))

# crtamo sunce
pg.draw.circle(prozor, pg.Color("yellow"), (100, 130), 80)

# procedura koja crta oblak na datoj poziciji, date velicine
# u datoj nijansi sive boje
def oblak(xc, yc, siva):
    # crtamo oblak od tri kruga
    boja = (siva, siva, siva)
    pg.draw.circle(prozor, boja, (xc,      yc), 50)
    pg.draw.circle(prozor, boja, (xc - 50, yc), 30)
    pg.draw.circle(prozor, boja, (xc + 50, yc), 30)

oblak(240, 200, 180)
oblak(270, 250, 210)
oblak(230, 100, 230)
oblak( 80,  80, 190)
oblak(110, 320, 255)

# -*- acsection: after-main -*-
petljapg.wait_loop()
