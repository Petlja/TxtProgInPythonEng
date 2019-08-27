# -*- acsection: general-init -*-
import pygame as pg

pg.init()                          # uključivanje rada biblioteke PyGame
pg.display.set_caption("Зграда")  # podešavamo naslov prozora
(sirina, visina) = (300, 300)      # otvaramo prozor dimenzije 300x300
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-
prozor.fill(pg.Color("lightgray")) # bojimo pozadinu ekrana u svetlo sivo

pg.draw.rect(prozor, pg.Color("darkgray"), (120, 50, 60, 140))   # zgrada
pg.draw.rect(prozor, pg.Color("yellow"), (130, 60, 15, 15))      # levi prozor, prvi red
pg.draw.rect(prozor, pg.Color("yellow"), (155, 60, 15, 15))      # desni prozor, prvi red
pg.draw.rect(prozor, pg.Color("yellow"), (130, 80, 15, 15))      # levi prozor, drugi red
pg.draw.rect(prozor, pg.Color("black"),  (155, 80, 15, 15))      # desni prozor, drugi red
pg.draw.rect(prozor, pg.Color("black"),  (130, 100, 15, 15))     # levi prozor, treci red
pg.draw.rect(prozor, pg.Color("yellow"), (155, 100, 15, 15))     # desni prozor, treci red
pg.draw.rect(prozor, pg.Color("yellow"), (130, 120, 15, 15))     # levi prozor, cetvrti red
pg.draw.rect(prozor, pg.Color("yellow"), (155, 120, 15, 15))     # desni prozor, cetvrti red
pg.draw.rect(prozor, pg.Color("black"),  (130, 140, 15, 15))     # levi prozor, peti red
pg.draw.rect(prozor, pg.Color("black"),  (155, 140, 15, 15))     # desni prozor, peti red
pg.draw.rect(prozor, pg.Color("black"),  (140, 160, 20, 30))     # kapija

# -*- acsection: after-main -*-
pg.display.update()   # prikazujemo nacrtano na ekranu

# petlja obrade događaja - čekamo dok korisnik ne isključi prozor
while pg.event.wait().type != pg.QUIT:
    pass

# isključivanje rada biblioteke PyGame
pg.quit()
