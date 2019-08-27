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

centar = (sirina // 2, visina // 2) # centar kruga je u centru prozora
br_krugova = 6
r_korak = sirina / (2*br_krugova)

for i in range(1, br_krugova + 1):
    pg.draw.circle(prozor, pg.Color("red"), centar, round(i * r_korak), 2)

# -*- acsection: after-main -*-
# osvezavamo sadrzaja prozora
pg.display.update()

# petlja obrade dogadjaja - cekamo dok korisnik ne iskljuci prozor
while pg.event.wait().type != pg.QUIT:
    pass

# iskljucujemo rad biblioteke PyGame
pg.quit()
