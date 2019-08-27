# -*- acsection: general-init -*-
import pygame as pg

pg.init()  # inicijalizujemo rad biblioteke PyGame
pg.display.set_caption("Смајлић и тужић")  # otvaramo prozor
(sirina, visina) = (230, 230)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-
slika = (pg.image.load("smiling_face.png"), pg.image.load("sad_face.png"))
i_slika = 0  # da li treba crtati smajlića ili tužića

def crtaj():
    prozor.fill(pg.Color("skyblue"))
    prozor.blit(slika[i_slika], (0, 0))

def novi_frejm():
    global i_slika
    i_slika = 1 - i_slika
    
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
