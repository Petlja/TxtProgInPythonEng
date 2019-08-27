# -*- acsection: general-init -*-
import random
import pygame as pg

pg.init()  # uključivanje rada biblioteke PyGame
pg.display.set_caption("Релативно цртање")   # otvaramo prozor
(sirina, visina) = (300, 300)
prozor = pg.display.set_mode((sirina, visina))

x = sirina // 2
y = visina // 2
a = 5

# -*- acsection: main -*-
def crtanje():
    prozor.fill(pg.Color("white"))
    pg.draw.circle(prozor, pg.Color("blue"), (x, y), 12*a)
    pg.draw.circle(prozor, pg.Color("yellow"), (x - 5*a, y - 5*a), 3*a)
    pg.draw.circle(prozor, pg.Color("black"), (x - 4*a, y - 4*a), a)
    pg.draw.circle(prozor, pg.Color("yellow"), (x + 5*a, y - 5*a), 3*a)
    pg.draw.circle(prozor, pg.Color("black"), (x + 4*a, y - 4*a), a)
    pg.draw.ellipse(prozor, pg.Color("red"), (x-5*a, y+2*a, 10*a, 2*a))
    
# -*- acsection: after-main -*-
def obradi_dogadjaj(dogadjaj):
    global x, y, a
    if dogadjaj.type == pg.MOUSEMOTION:
            (x, y) = dogadjaj.pos
            return True
    elif dogadjaj.type == pg.MOUSEBUTTONDOWN:
        if dogadjaj.button == 1:
            a += 1
            return True
        elif dogadjaj.button == 3:
            a -= 1
            return True
    return False

treba_crtati = True
kraj = False
while not(kraj):
    if treba_crtati:
        crtanje()
        pg.display.update()  # ažuriramo prikaz sadržaja ekrana
        treba_crtati = False # ne treba crtati do daljnjeg

    dogadjaj = pg.event.wait()      # čekamo naredni dogadjaj
    if dogadjaj.type == pg.QUIT:    # isključivanje prozora
        kraj = True
    else:
        treba_crtati = obradi_dogadjaj(dogadjaj)

pg.quit()  # isključivanje rada biblioteke PyGame

