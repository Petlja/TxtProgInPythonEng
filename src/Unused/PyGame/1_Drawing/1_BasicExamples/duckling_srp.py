# -*- acsection: general-init -*-
import pygame as pg, math

# uključivanje rada biblioteke PyGame
pg.init()

# podešavamo naslov prozora
pg.display.set_caption("Паткица")
# uključujemo prozor dimenzije 400x400 piksela
(sirina, visina) = (400, 400)
prozor = pg.display.set_mode((sirina, visina))

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
# osvežavamo sadržaj prozora
pg.display.update()

# petlja obrade događaja - čekamo dok korisnik ne isključi prozor
while pg.event.wait().type != pg.QUIT:
    pass

# isključivanje rada biblioteke PyGame
pg.quit()
