# -*- acsection: general-init -*-
import pygame as pg, math

# uključivanje rada biblioteke PyGame
pg.init()

# podešavamo naslov prozora
pg.display.set_caption("Јелка")
# uključujemo prozor dimenzije 300x300 piksela
(sirina, visina) = (300, 300)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-
# bojimo pozadinu u belo
prozor.fill(pg.Color("white"))

# boje koje cemo koristiti
ZELENA = (0, 100, 36)
BRAON = (97, 26, 9)

# stablo
pg.draw.rect(prozor, BRAON, (130, 250, 40, 50))
# krošnja
pg.draw.polygon(prozor, ZELENA, [(50, 250), (150, 150), (250, 250)])
pg.draw.polygon(prozor, ZELENA, [(75, 200), (150, 100), (225, 200)])
pg.draw.polygon(prozor, ZELENA, [(100, 150), (150, 50), (200, 150)])


# -*- acsection: after-main -*-
# osvežavamo sadržaj prozora
pg.display.update()

# petlja obrade događaja - čekamo dok korisnik ne isključi prozor
while pg.event.wait().type != pg.QUIT:
    pass

# isključivanje rada biblioteke PyGame
pg.quit()
