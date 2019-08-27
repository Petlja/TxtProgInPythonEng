# -*- acsection: general-init -*-
import pygame as pg
import random

pg.init()                          # uključivanje rada biblioteke PyGame
pg.display.set_caption("Јабуке")   # podešavamo naslov prozora
(sirina, visina) = (800, 600)      # otvaramo prozor dimenzije 800x600
prozor = pg.display.set_mode((sirina, visina))
# -*- acsection: main -*-

drvo_slika = pg.image.load("tree.png")  # slika drveta

prozor.fill(pg.Color("darkgreen")) # bojimo pozadinu ekrana u tamno zeleno
for drvo_x, drvo_y in ((200, 70), (120, 150), (240, 290), (550, 170), (400, 200)):
    prozor.blit(drvo_slika, (drvo_x, drvo_y))

# -*- acsection: after-main -*-
pg.display.update()   # prikazujemo nacrtano na ekranu

# petlja obrade događaja - čekamo dok korisnik ne isključi prozor
while pg.event.wait().type != pg.QUIT:
    pass

# isključivanje rada biblioteke PyGame
pg.quit()
