# -*- acsection: general-init -*-
import pygame as pg

pg.init()  # inicijalizujemo biblioteku pygame

pg.display.set_caption("Кртица")  

# otvaramo prozor
(sirina, visina) = (150, 150)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

slike = []   # niz koji ce da sadrzi slike
for i in range(1, 11): # učitavamo u listu slike mole1.png, ..., mole10.png
    naziv_slike = "mole" + str(i) + ".png"  # gradimo naziv slike od delova
    slike.append(pg.image.load(naziv_slike))

# sekvenca se sastoji od 10 frejmova izlazenja, 5 frejmova gore, 10 frejmova spustanja i 3 frejma dole
# to jest [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] + [9, 9, 9, 9, 9] + [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] + [0, 0, 0]
sekvenca = list(range(10)) + [9] * 5 + list(range(9,-1,-1)) + [0] * 3
i_frejm = 0 # redni broj frejma u sekvenci
braon = (60, 42, 3)

def crtaj():
    prozor.fill(pg.Color("skyblue"))     # bojimo pozadinu prozora u nebo-plavo
    pg.draw.rect(prozor, braon, (0, 125, 150, 25)) # bojimo donjih 25 piksela prozora u braon
    i_slika = sekvenca[i_frejm] # redni broj slike koja se prikazuje
    prozor.blit(slike[i_slika], (0, 0))  # prikazujemo sliku

def novi_frejm():
    global i_frejm
    i_frejm = (i_frejm + 1) % len(sekvenca)

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
    sat.tick(10)
    novi_frejm()

pg.quit() # isključujemo rad biblioteke PyGame
