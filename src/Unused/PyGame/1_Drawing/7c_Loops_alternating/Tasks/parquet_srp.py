# -*- acsection: general-init -*-
import pygame as pg

pg.init()                        # uključivanje rada biblioteke PyGame
pg.display.set_caption("Паркет") # podešavamo naslov prozora
(sirina, visina) = (300, 300)    # otvaramo prozor dimenzije 300x300
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-
prozor.fill(pg.Color("goldenrod"))
a = 10    # sirina dascice
b = 6 * a # duzina dascice
br_kvadrata_x = sirina // b
br_kvadrata_y = visina // b
for red in range(br_kvadrata_y):
    for kolona in range(br_kvadrata_y):
        (x0, y0) = (kolona*b, red*b)
        if (red + kolona) % 2 == 0:
            for i in range(6):
                pg.draw.rect(prozor, pg.Color("brown"), (x0+i*a, y0, a, b), 1)
        else:
            for i in range(6):
                pg.draw.rect(prozor, pg.Color("brown"), (x0, y0+i*a, b, a), 1)

# -*- acsection: after-main -*-
pg.display.update()   # prikazujemo nacrtano na ekranu

# petlja obrade događaja - čekamo dok korisnik ne isključi prozor
while pg.event.wait().type != pg.QUIT:
    pass

# isključivanje rada biblioteke PyGame
pg.quit()
