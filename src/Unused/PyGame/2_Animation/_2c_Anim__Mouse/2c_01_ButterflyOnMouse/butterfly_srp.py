# -*- acsection: general-init -*-
import random, math
import pygame as pg

pg.init() # inicijalizujemo biblioteku PyGame
pg.display.set_caption("Лептир прати миша") 

# otvaramo prozor
(sirina, visina) = (400, 400)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

# učitavamo dve slike leptira u listu
leptir_slike = []
for i in range(2):
    naziv_slike = "butterfly" + str(i+1) + ".png"
    leptir_slike.append(pg.image.load(naziv_slike))

broj_frejma = 0 # redni broj tekućeg frejma

def crtaj():
    prozor.fill(pg.Color("white"))                        # bojimo pozadinu u belo
    (mis_x, mis_y) = pg.mouse.get_pos()                   # koordinate miša
    broj_slike = (broj_frejma // 10) % len(leptir_slike)  # redni broj slike - svaka se slika prikazuje 10 frejmova
    slika = leptir_slike[broj_slike]                      # slika koja se prikazuje
    slika_sirina = slika.get_width()                      # prikazujemo sliku centrirano
    slika_visina = slika.get_height()
    (x, y) = (mis_x - slika_sirina / 2, mis_y - slika_visina / 2)
    prozor.blit(slika, (x, y))

def novi_frejm():
    global broj_frejma
    broj_frejma += 1    # uvećavamo redni broj frejma

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
    sat.tick(50)
    novi_frejm()

pg.quit() # isključujemo rad biblioteke PyGame
