# -*- acsection: general-init -*-
import pygame as pg

# inicijalizujemo rad biblioteke PyGame
pg.init()

# postavljamo naslov prozora
pg.display.set_caption("Концентрични кругови")
# otvaramo prozor dimenzije 300x300 piksela
(sirina, visina) = (300, 300)
prozor = pg.display.set_mode((sirina, visina))
# -*- acsection: main -*-

# bojimo pozadinu prozora u belu
prozor.fill(pg.Color("white"))

# centar kruga je u centru prozora
centar = (sirina // 2, visina // 2)

# crtamo krugove
# poluprecnik se menja od 25 do 150, sa korakom 25
pg.draw.circle(prozor, pg.Color("red"), centar,  25, 2)
pg.draw.circle(prozor, pg.Color("red"), centar,  50, 2)
pg.draw.circle(prozor, pg.Color("red"), centar,  75, 2)
pg.draw.circle(prozor, pg.Color("red"), centar, 100, 2)
pg.draw.circle(prozor, pg.Color("red"), centar, 125, 2)
pg.draw.circle(prozor, pg.Color("red"), centar, 150, 2)
# -*- acsection: after-main -*-
# osvezavamo sadrzaja prozora
pg.display.update()

# petlja obrade dogadjaja - cekamo dok korisnik ne iskljuci prozor
while pg.event.wait().type != pg.QUIT:
    pass

# iskljucujemo rad biblioteke PyGame
pg.quit()
