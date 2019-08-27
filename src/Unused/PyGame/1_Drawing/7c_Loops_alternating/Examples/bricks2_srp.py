# -*- acsection: general-init -*-
import pygame as pg

pg.init()                          # uključivanje rada biblioteke PyGame
pg.display.set_caption("Вежба")  # podešavamo naslov prozora
(sirina, visina) = (300, 300)      # otvaramo prozor dimenzije 300x300
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-
prozor.fill(pg.Color("red"))
a_cigle, h_cigle = 80, 40
for y0 in range(0, visina, 2 * h_cigle):
    for x0 in range(0, sirina, a_cigle):
        #crtamo prvu ciglu
        pg.draw.rect(prozor, pg.Color("black"), (x0, y0, a_cigle, h_cigle), 1)
        
        # druga cigla je u sledecem redu, pomerena za pola sirine
        x1, y1 = x0 - a_cigle//2, y0 + h_cigle 
        pg.draw.rect(prozor, pg.Color("black"), (x1, y1, a_cigle, h_cigle), 1)

# -*- acsection: after-main -*-
pg.display.update()   # prikazujemo nacrtano na ekranu

# petlja obrade događaja - čekamo dok korisnik ne isključi prozor
while pg.event.wait().type != pg.QUIT:
    pass

# isključivanje rada biblioteke PyGame
pg.quit()
