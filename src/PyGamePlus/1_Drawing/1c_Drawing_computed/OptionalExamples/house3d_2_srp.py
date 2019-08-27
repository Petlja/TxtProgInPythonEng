# -*- acsection: general-init -*-
import pygame as pg

# uključivanje rada biblioteke PyGame
pg.init()
# podešavamo naslov prozora
pg.display.set_caption("Медведићи")
# otvaramo prozor dimenzije 400x450
(sirina, visina) = (400, 450)
prozor = pg.display.set_mode((sirina, visina))
# -*- acsection: main -*-

BOJA_SUNCA = (247, 242, 81) # zuta
BOJA_NEBA = (153, 217, 234) # plava
BOJA_TRAVE = (0, 100, 36) # zelena
BOJA_KUCE_PREDNJA = (255, 183, 111) # tamnija 'krem'
BOJA_KUCE_KA_SUNCU = (255, 185, 151) # svetlija 'krem'
BOJA_KROVA_PREDNJA = (255, 0, 0) # srednja crvena
BOJA_KROVA_KA_SUNCU = (255, 64, 64) # svetlo crvena
BOJA_KROVA_OD_SUNCA = (192, 0, 0) # tamno crvena
BOJA_PUTA = (128, 128, 128) # siva

X, Y = 0, 1 # indeksi
horizont_y = 80

def crtaj_kucu(x, y, a):
    visina_kuce = 8*a
    sirina_kuce = 10*a # sirina prednje strane kuce
    krov_prednja_leva = (5*a, -3*a)
    krov_prednja_desna = (5*a, 3*a)
    bocna = (5*a, -12*a)
    ptE = (x, y)
    ptA = (ptE[X], ptE[Y] + visina_kuce)
    ptB = (ptA[X] + sirina_kuce, ptA[Y])
    ptC = (ptE[X] + sirina_kuce, ptE[Y])
    ptD = (ptE[X] + krov_prednja_leva[X], ptE[Y] + krov_prednja_leva[Y])
    ptB1 = (ptB[X] + bocna[X], ptB[Y] + bocna[Y])
    ptC1 = (ptC[X] + bocna[X], ptC[Y] + bocna[Y])
    ptD1 = (ptD[X] + bocna[X], ptD[Y] + bocna[Y])
    ptE1 = (ptE[X] + bocna[X], ptE[Y] + bocna[Y])
    
    pg.draw.rect(prozor, BOJA_KUCE_PREDNJA, (x, y, sirina_kuce, visina_kuce)) # prednja, pravougaona strana kuce
    pg.draw.polygon(prozor, BOJA_KROVA_PREDNJA, [ptE, ptD, ptC]) # prednji trougao krova
    pg.draw.polygon(prozor, BOJA_KUCE_KA_SUNCU,  [ptC,  ptC1, ptB1, ptB]) # bocna strana kuce
    pg.draw.polygon(prozor, BOJA_KROVA_KA_SUNCU, [ptC, ptC1, ptD1, ptD]) # strana krova ka suncu
    pg.draw.polygon(prozor, BOJA_KROVA_OD_SUNCA, [ptE, ptE1, ptD1, ptD]) # strana krova od sunca

prozor.fill(BOJA_NEBA) # nebo
pg.draw.circle(prozor, BOJA_SUNCA, (300, 70), 40) # sunce
pg.draw.rect(prozor, BOJA_TRAVE, (0, horizont_y, sirina, visina - horizont_y)) # trava
crtaj_kucu(175, 100, 3)
crtaj_kucu(30, 200, 10)
pg.draw.line(prozor, BOJA_PUTA, (0, 350), (sirina, 350), 60) # put
pg.draw.line(prozor, pg.Color("white"), (0, 350), (sirina, 350), 3) # bela traka na putu

# -*- acsection: after-main -*-
# ažuriramo prikaz sadržaja ekrana
pg.display.update()

# čekamo da korisnik isključi prozor
while pg.event.wait().type != pg.QUIT:
    pass
    
# isključivanje rada biblioteke PyGame
pg.quit()
