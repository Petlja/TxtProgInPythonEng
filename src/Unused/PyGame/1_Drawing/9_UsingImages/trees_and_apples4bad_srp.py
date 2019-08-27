# -*- acsection: general-init -*-
import pygame as pg
import random

pg.init()                          # uključivanje rada biblioteke PyGame
pg.display.set_caption("Јабуке")   # podešavamo naslov prozora
(sirina, visina) = (800, 600)      # otvaramo prozor dimenzije 800x600
prozor = pg.display.set_mode((sirina, visina))
# -*- acsection: main -*-

drvo_slika = pg.image.load("tree.png")  # slika drveta
jabuka_slika = pg.image.load("apple_small.png")  # slika jabuke
jabuke_poz = ((43,191), (61, 158), (124, 145), (134, 175), (160, 180))

prozor.fill(pg.Color("darkgreen")) # bojimo pozadinu ekrana u tamno zeleno
for drvo_x, drvo_y in ((240, 290), (120, 150), (200, 70), (400, 200), (0, 0), (550, 170)):
    prozor.blit(drvo_slika, (drvo_x, drvo_y))

for drvo_x, drvo_y in ((240, 290), (120, 150), (200, 70), (400, 200), (550, 170)):
    for x, y in jabuke_poz:
        prozor.blit(jabuka_slika, (drvo_x + x, drvo_y + y))
    
pg.image.save(prozor, 'trees_and_apples_bad.png')
# -*- acsection: after-main -*-
pg.display.update()   # prikazujemo nacrtano na ekranu

# petlja obrade događaja - čekamo dok korisnik ne isključi prozor
while pg.event.wait().type != pg.QUIT:
    pass

# isključivanje rada biblioteke PyGame
pg.quit()
