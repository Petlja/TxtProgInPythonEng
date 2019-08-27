# -*- acsection: general-init -*-
import pygame as pg

pg.init()                          # uključivanje rada biblioteke PyGame
pg.display.set_caption("Сандуци") # podešavamo naslov prozora
(sirina, visina) = (800, 600)      # otvaramo prozor dimenzije 800x600
prozor = pg.display.set_mode((sirina, visina))
# -*- acsection: main -*-

sanduk_slika = pg.image.load("box.png")  # slika drveta

prozor.fill(pg.Color("lightgray")) # bojimo pozadinu ekrana u svetlo sivo

for i in range(4):
    prozor.blit(sanduk_slika, (60+120*i, 400))
pg.display.update()
pg.image.save(prozor, 'x4.png')

prozor.fill(pg.Color("lightgray")) # bojimo pozadinu ekrana u svetlo sivo
for i in range(4):
    prozor.blit(sanduk_slika, (420, 400-95*i))
pg.display.update()
pg.image.save(prozor, 'y4.png')

prozor.fill(pg.Color("lightgray")) # bojimo pozadinu ekrana u svetlo sivo
for ix in range(4):
    for iy in range(ix+1):
        prozor.blit(sanduk_slika, (60+120*ix, 400-95*iy))
pg.display.update()
pg.image.save(prozor, 'x4yi.png')

# -*- acsection: after-main -*-

# petlja obrade događaja - čekamo dok korisnik ne isključi prozor
while pg.event.wait().type != pg.QUIT:
    pass

# isključivanje rada biblioteke PyGame
pg.quit()
