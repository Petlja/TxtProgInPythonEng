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
prozor.blit(drvo_slika, (0, 0))

# -*- acsection: after-main -*-
pg.display.update()   # prikazujemo nacrtano na ekranu

# petlja obrade događaja - čekamo dok korisnik ne isključi prozor
while pg.event.wait().type != pg.QUIT:
    pass

# isključivanje rada biblioteke PyGame
pg.quit()
