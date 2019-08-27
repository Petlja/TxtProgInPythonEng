# -*- acsection: general-init -*-
import pygame as pg

pg.init()                          # uključivanje rada biblioteke PyGame
pg.display.set_caption("Кућа")     # podešavamo naslov prozora
(sirina, visina) = (500, 300)      # otvaramo prozor dimenzije 500x300
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-
prozor.fill(pg.Color("darkgreen")) # bojimo pozadinu ekrana u svetlo plavo

def kuca(x, y, a, boja_zidova):
    pg.draw.polygon(prozor, pg.Color("red"), [(x, y), (x+7*a, y-5*a), (x+14*a, y)]) # krov
    pg.draw.rect(prozor, boja_zidova,       (x,        y,      14*a, 10*a)) # kuca
    pg.draw.rect(prozor, pg.Color("brown"), (x +  1*a, y + 2*a, 3*a,  3*a)) # levi prozor
    pg.draw.rect(prozor, pg.Color("brown"), (x + 10*a, y + 2*a, 3*a,  3*a)) # desni prozor
    pg.draw.rect(prozor, pg.Color("brown"), (x +  5*a, y + 3*a, 4*a,  7*a)) # vrata

kuca(150,  90,  8, (220, 220, 220))
kuca(250, 130,  9, pg.Color("white"))
kuca(350, 160, 10, (255, 255, 150))
kuca( 50, 150, 10, pg.Color("khaki"))

# -*- acsection: after-main -*-
pg.display.update()   # prikazujemo nacrtano na ekranu

# petlja obrade događaja - čekamo dok korisnik ne isključi prozor
while pg.event.wait().type != pg.QUIT:
    pass

# isključivanje rada biblioteke PyGame
pg.quit()
