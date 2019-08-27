# -*- acsection: general-init -*-
import pygame as pg

# uključivanje rada biblioteke PyGame
pg.init()
# podešavamo naslov prozora
pg.display.set_caption("Кућа")
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

prozor.fill(BOJA_NEBA) # nebo
pg.draw.circle(prozor, BOJA_SUNCA, (300, 70), 40) # sunce
pg.draw.rect(prozor, BOJA_TRAVE, (0, 80, sirina, visina - 80)) # trava

pg.draw.rect(prozor, BOJA_KUCE_PREDNJA, (50, 200, 100, 76)) # prednja, pravougaona strana kuce
pg.draw.polygon(prozor, BOJA_KROVA_PREDNJA, [(50, 200), (100, 170), (150, 200)]) # prednji trougao krova
pg.draw.polygon(prozor, BOJA_KUCE_KA_SUNCU,  [(150, 200), (200, 100), (200, 175), (150, 275)]) # bocna strana kuce
pg.draw.polygon(prozor, BOJA_KROVA_KA_SUNCU, [(150, 200), (200, 100), (150, 70), (100, 170)]) # strana krova ka suncu
pg.draw.polygon(prozor, BOJA_KROVA_OD_SUNCA, [(50, 200), (100, 100), (150, 70), (100, 170)]) # strana krova od sunca

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
