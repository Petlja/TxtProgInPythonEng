# -*- acsection: general-init -*-
import pygame as pg, math

# uključivanje rada biblioteke PyGame
pg.init()

# podešavamo naslov prozora
pg.display.set_caption("Облак")
# uključujemo prozor dimenzije 400x400 piksela
(sirina, visina) = (400, 400)
prozor = pg.display.set_mode((sirina, visina))

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
# osvežavamo sadržaj prozora
pg.display.update()

# petlja obrade događaja - čekamo dok korisnik ne isključi prozor
while pg.event.wait().type != pg.QUIT:
    pass

# isključivanje rada biblioteke PyGame
pg.quit()
