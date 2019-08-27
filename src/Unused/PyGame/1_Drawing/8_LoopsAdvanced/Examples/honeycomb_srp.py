# -*- acsection: general-init -*-
import pygame as pg

pg.init()                          # uključivanje rada biblioteke PyGame
pg.display.set_caption("Вежба")  # podešavamo naslov prozora
(sirina, visina) = (300, 300)      # otvaramo prozor dimenzije 300x300
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-
def crtaj_mnogougao(temena, boja, x0, y0):
    pomerena_temena = []
    for x, y in temena:
        pomerena_temena.append((x+x0, y+y0))
    pg.draw.polygon(prozor, boja, pomerena_temena, 1)

sestougao = [(10, 0), (30, 0), (40, 17), (30, 34), (10, 34), (0, 17)]
prozor.fill(pg.Color("goldenrod"))
for y0 in range(-17, visina, 34):
    for x0 in range(-10, sirina, 60):
        crtaj_mnogougao(sestougao, pg.Color("brown"), x0, y0)
        crtaj_mnogougao(sestougao, pg.Color("brown"), x0 + 30, y0 + 17)

# -*- acsection: after-main -*-
pg.display.update()   # prikazujemo nacrtano na ekranu

# petlja obrade događaja - čekamo dok korisnik ne isključi prozor
while pg.event.wait().type != pg.QUIT:
    pass

# isključivanje rada biblioteke PyGame
pg.quit()
