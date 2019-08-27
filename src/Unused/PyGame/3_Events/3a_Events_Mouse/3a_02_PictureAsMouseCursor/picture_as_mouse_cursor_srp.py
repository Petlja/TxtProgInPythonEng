# -*- acsection: general-init -*-
import pygame as pg, random

pg.init()   # uključujemo rad biblioteke PyGame

pg.display.set_caption("Слика као курсор миша") 

# otvaramo prozor
(sirina, visina) = (400, 400)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

mis_slika = (pg.image.load("HammerUp.png"), pg.image.load("HammerDown.png"))
i_slika = 0
mis_poz = (sirina // 2, visina // 2)
pg.mouse.set_pos(mis_poz)
pg.mouse.set_visible(False)

def crtanje():
    # bojimo prozor u belo
    prozor.fill(pg.Color("white"))
    # crtamo sliku tako da je mis na sredini slike
    slika_sirina = mis_slika[i_slika].get_width()
    slika_visina = mis_slika[i_slika].get_height()
    (x, y) = mis_poz
    gore_levo = (x - slika_sirina // 2, y - slika_visina // 2)
    prozor.blit(mis_slika[i_slika], gore_levo)

def obradi_dogadjaj(dogadjaj):
    global mis_poz, i_slika
    if dogadjaj.type == pg.MOUSEBUTTONDOWN:
        i_slika = 1
        return True
    elif dogadjaj.type == pg.MOUSEBUTTONUP:
        i_slika = 0
        return True
    elif dogadjaj.type == pg.MOUSEMOTION:
        mis_poz = dogadjaj.pos
        return True
    return False

# -*- acsection: after-main -*-
treba_crtati = True
kraj = False
while not kraj:
    if treba_crtati:    # ako je potrebno nacrtati lopticu
        crtanje()
        pg.display.update()        # ažuriramo prikaz sadržaja prozora
        treba_crtati = False

    dogadjaj = pg.event.wait()     # čekamo naredni događaj
    if dogadjaj.type == pg.QUIT:   # isključivanje prozora
        kraj = True
    else:
        treba_crtati = obradi_dogadjaj(dogadjaj)

pg.quit()  # isključujemo rad biblioteke PyGame
