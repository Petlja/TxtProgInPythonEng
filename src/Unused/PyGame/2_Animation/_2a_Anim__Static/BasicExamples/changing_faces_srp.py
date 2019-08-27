# -*- acsection: general-init -*-
import pygame as pg

pg.init()  # inicijalizujemo rad biblioteke PyGame
pg.display.set_caption("Смајлић и тужић")  # otvaramo prozor
(sirina, visina) = (230, 230)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

smajlic_slika = pg.image.load("smiling_face.png")
tuzic_slika = pg.image.load("sad_face.png")

smajlic = True  # da li treba crtati smajlića ili tužića

def crtaj():
    prozor.fill(pg.Color("skyblue"))
    if smajlic:
        prozor.blit(smajlic_slika, (0, 0))
    else:
        prozor.blit(tuzic_slika, (0, 0))

def novi_frejm():
    global smajlic
    # smajlic = not smajlic
    if smajlic == True:
        smajlic = False
    else:
        smajlic = True

# -*- acsection: after-main -*-

kraj = False
sat = pg.time.Clock()  # sat koji određuje broj frejmova u sekundi
while not kraj:
    # crtamo i ažuriramo sadržaj prozora
    crtaj()
    pg.display.update()

    # proveravamo da li je korisnik isključio prozor
    for dogadjaj in pg.event.get():
        if dogadjaj.type == pg.QUIT:
            kraj = True

    # pauziramo do sledeceg frejma
    sat.tick(2)
    novi_frejm()

pg.quit() # isključujemo rad biblioteke PyGame
