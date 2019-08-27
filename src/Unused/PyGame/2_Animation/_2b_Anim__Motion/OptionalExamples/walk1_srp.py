# -*- acsection: general-init -*-
import pygame as pg

pg.init()  # inicijalizujemo biblioteku pygame

pg.display.set_caption("Шетање")  # otvaramo prozor
(sirina, visina) = (150, 180)
prozor = pg.display.set_mode((sirina, visina))
sredina_y = visina / 2

# -*- acsection: main -*-

# učitavamo u listu slike setanje1.png, setanje2.png, ..., setanje5.png
slike = []   # niz u koji dodajemo slike
for i in range(1, 6):
    naziv_slike = "walk" + str(i) + ".png"  # gradimo naziv slike od delova
    slike.append(pg.image.load(naziv_slike))   # učitavamo sliku i dodajemo je na kraj niza

slika = 0  # indeks tekuće slike

def crtaj():
    prozor.fill(pg.Color("white"))     # bojimo pozadinu prozora u belo
    prozor.blit(slike[slika], (0, 0))  # prikazujemo sliku

def novi_frejm():
    global slika  # ovu globalnu promenljivu menjamo
    slika = (slika + 1) % len(slike)  # prelazimo na sledeću sliku

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
    sat.tick(5)
    novi_frejm()

pg.quit() # isključujemo rad biblioteke PyGame
