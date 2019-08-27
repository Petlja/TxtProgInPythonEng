# -*- acsection: general-init -*-
import pygame as pg, math

# uključivanje rada biblioteke PyGame
pg.init()

# podešavamo naslov prozora
pg.display.set_caption("Облаци")
# uključujemo prozor dimenzije 400x400 piksela
(sirina, visina) = (400, 400)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-
# bojimo pozadinu u plavo
prozor.fill(pg.Color("skyblue"))

# crtamo sunce
pg.draw.circle(prozor, pg.Color("yellow"), (100, 130), 80)

# procedura koja crta oblak na datoj poziciji, date velicine
# u datoj nijansi sive boje
def oblak(x, y, siva):
    # crtamo oblak od tri kruga
    boja = (siva, siva, siva)
    pg.draw.circle(prozor, boja, (x,      y), 50)
    pg.draw.circle(prozor, boja, (x - 50, y), 30)
    pg.draw.circle(prozor, boja, (x + 50, y), 30)

oblak(240, 200, 180)
oblak(270, 250, 210)
oblak(230, 100, 230)
oblak( 80,  80, 190)
oblak(110, 320, 255)

# -*- acsection: after-main -*-
# osvežavamo sadržaj prozora
pg.display.update()

# petlja obrade događaja - čekamo dok korisnik ne isključi prozor
while pg.event.wait().type != pg.QUIT:
    pass

# isključivanje rada biblioteke PyGame
pg.quit()
