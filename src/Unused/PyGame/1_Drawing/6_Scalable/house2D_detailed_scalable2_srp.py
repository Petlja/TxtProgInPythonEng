# -*- acsection: general-init -*-
import pygame as pg

pg.init()                          # uključivanje rada biblioteke PyGame
pg.display.set_caption("Кућа")     # podešavamo naslov prozora
(sirina, visina) = (400, 300)      # otvaramo prozor dimenzije 400x300
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-
prozor.fill(pg.Color("darkgreen")) # bojimo pozadinu ekrana u svetlo plavo

def kuca(x, y, a, boja_zidova):
    pg.draw.polygon(prozor, pg.Color("red"), [(x, y), (x+7*a, y-5*a), (x+14*a, y)]) # krov
    pg.draw.rect(prozor, boja_zidova,       (x,        y,      14*a, 10*a)) # kuca
    pg.draw.rect(prozor, pg.Color("brown"), (x +  1*a, y + 2*a, 3*a,  3*a)) # levi prozor
    pg.draw.rect(prozor, pg.Color("brown"), (x + 10*a, y + 2*a, 3*a,  3*a)) # desni prozor
    pg.draw.rect(prozor, pg.Color("brown"), (x +  5*a, y + 3*a, 4*a,  7*a)) # vrata

kuca(278, 110, 1, (211, 207, 169))
kuca(231, 119, 2, (217, 211, 164))
kuca(174, 130, 3, (228, 221, 152))
kuca(112, 142, 4, (231, 222, 150))
kuca( 18, 160, 6, (240, 230, 140))

# -*- acsection: after-main -*-
pg.display.update()   # prikazujemo nacrtano na ekranu

# petlja obrade događaja - čekamo dok korisnik ne isključi prozor
while pg.event.wait().type != pg.QUIT:
    pass

# isključivanje rada biblioteke PyGame
pg.quit()
