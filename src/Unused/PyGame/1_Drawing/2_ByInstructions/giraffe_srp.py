# -*- acsection: general-init -*-
import pygame as pg, math

# uključivanje rada biblioteke PyGame
pg.init()

# podešavamo naslov prozora
pg.display.set_caption("Жирафа")
# uključujemo prozor zeljene velicine
(sirina, visina) = (300, 300)
prozor = pg.display.set_mode((sirina, visina))

tacke = [(40, 208), (40, 107), (88, 82), (134, 13), (128, 9), (134, 13), 
    (137, 11), (128, 6), (160, 25), (159, 28), (136, 28), (98, 101),
    (100, 106), (101, 207), (97, 207), (95, 164), (83, 121), (85, 128),
    (54, 128), (55, 119), (44, 165), (44, 208)]
    
# -*- acsection: main -*-

# bojimo pozadinu u tamno zeleno
prozor.fill(pg.Color("darkgreen"))

# iscrtavamo mnogougao bojom 'khaki'
pg.draw.polygon(prozor, pg.Color("khaki"), tacke)
    
# -*- acsection: after-main -*-
# osvežavamo sadržaj prozora
pg.display.update()

# petlja obrade događaja - čekamo dok korisnik ne isključi prozor
while pg.event.wait().type != pg.QUIT:
    pass

# isključivanje rada biblioteke PyGame
pg.quit()
