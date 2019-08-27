# -*- acsection: general-init -*-
import random
import pygame as pg

pg.init()  # inicijalizujemo biblioteku pygame

pg.display.set_caption("Кртице")  # otvaramo prozor
(sirina, visina) = (600, 600)
prozor = pg.display.set_mode((sirina, visina))

pg.key.set_repeat(10, 10)  # podešavamo dogadjaje tastature

# -*- acsection: main -*-

krtice = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pogodjena = [[False, False, False], [False, False, False], [False, False, False]]

# učitavamo u listu slike setanje1.png, setanje2.png, ..., setanje5.png
slike_krtica = []   # niz u koji dodajemo slike
for i in range(1, 11):
    naziv_slike = "krtica" + str(i) + ".png"  # gradimo naziv slike od delova
    slika = pg.image.load(naziv_slike)
    slike_krtica.append(slika)

def gornji_levi_ugao_slike_krtice(i, j):
    x = j * (sirina / 3)
    y = (i + 1) * (visina / 3) - slike_krtica[abs(krtice[i][j])].get_height()
    return (x, y)

def broj_vidljivih_nepogodjenih():
    broj = 0
    for i in range(len(krtice)):
        for j in range(len(krtice[i])):
            if krtice[i][j] != 0 and not pogodjena[i][j]:
                broj += 1
    return broj

def broj_nepogodjenih():
    broj = 0
    for i in range(len(krtice)):
        for j in range(len(krtice[i])):
            if not pogodjena[i][j]:
                broj += 1
    return broj

def tekst_centar(x, y, tekst, velicina):
    font = pg.font.SysFont("Arial", velicina)
    tekst = font.render(tekst, True, pg.Color("black"))
    (sirina_teksta, visina_teksta) = (tekst.get_width(), tekst.get_height())
    (x, y) = (x - sirina_teksta / 2, y - visina_teksta / 2)
    prozor.blit(tekst, (x, y))

def crtaj():
    prozor.fill(pg.Color("white"))     # bojimo pozadinu prozora u belo
    if broj_nepogodjenih() == 0:
        tekst_centar(sirina / 2, visina / 2, "Браво", 100)
    else:
        for i in range(len(krtice)):
            for j in range(len(krtice[i])):
                (x, y) = gornji_levi_ugao_slike_krtice(i, j)
                prozor.blit(slike_krtica[abs(krtice[i][j])], (x, y))

def novi_frejm():
    if broj_vidljivih_nepogodjenih() == 0:
        verovatnoca = 20
    else:
        verovatnoca = 100
    for i in range(len(krtice)):
        for j in range(len(krtice[i])):
            if krtice[i][j] == 0:
                if random.randint(1, verovatnoca) == 1:
                    krtice[i][j] = 1
            elif krtice[i][j] == 9 and not pogodjena[i][j]:
                if random.randint(1, 20) == 1:
                    krtice[i][j] = -9
            elif krtice[i][j] < 9:
                krtice[i][j] += 1
            elif krtice[i][j] < 0 and not pogodjena[i][j]:
                krtice[i][j] += 1


def obradi_dogadjaj(dogadjaj):
    global pogodak
    if dogadjaj.type == pg.MOUSEBUTTONDOWN:
        for i in range(len(krtice)):
            for j in range(len(krtice[i])):
                if abs(krtice[i][j]) >= 5:
                    (x, y) = gornji_levi_ugao_slike_krtice(i, j)
                    (xm, ym) = dogadjaj.pos
                    if x <= xm and xm <= x + slike_krtica[abs(krtice[i][j])].get_width() and\
                       y <= ym and ym <= y + slike_krtica[0].get_height():
                        pogodjena[i][j] = True
    
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
        else:
            obradi_dogadjaj(dogadjaj)

    # pauziramo do sledeceg frejma
    sat.tick(10)
    novi_frejm()

pg.quit() # isključujemo rad biblioteke PyGame
