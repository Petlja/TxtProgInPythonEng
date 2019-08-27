# -*- acsection: general-init -*-
import random
import pygame as pg


pg.init()  # inicijalizujemo rad biblioteke PyGame
pg.display.set_caption("Бацање коцкице")  # otvaramo prozor
(sirina, visina) = (300, 300)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

PAPIR = 0
KAMEN = 1
MAKAZE = 2

slike = [pg.image.load("paper.png"),
         pg.image.load("rock.png"),
         pg.image.load("scissors.png")]

covek = 0
racunar = 0
covek_poeni = 0
racunar_poeni = 0

def pobedio(igracA, igracB):
    return (igracA == PAPIR and igracB == KAMEN) or \
           (igracA == KAMEN and igracB == MAKAZE) or \
           (igracA == MAKAZE and igracB == PAPIR)

def crtaj_igraca(igrac, tekst, cx, cy, pobednik):
    dim = 150
    if pobednik:
        pg.draw.rect(prozor, pg.Color("gray"), (cx - dim/2, cy - dim/2, dim, dim))
    (x, y) = (cx - slike[igrac].get_width() / 2, cy - slike[igrac].get_height() / 2)
    pg.draw.rect(prozor, pg.Color("black"), (x-1, y-1, slike[igrac].get_width() + 1, slike[igrac].get_height() + 1), 2)
    prozor.blit(slike[igrac], (x, y))
    font = pg.font.SysFont("Arial", 20)
    tekst = font.render(tekst, True, pg.Color("black"))
    prozor.blit(tekst, (cx - tekst.get_width() / 2, cy - dim / 2 - tekst.get_height() - 10))
    
    

def crtaj():
    prozor.fill(pg.Color("white"))
    crtaj_igraca(covek, "Човек: " + str(covek_poeni), sirina / 4, visina / 2, pobedio(covek, racunar))
    crtaj_igraca(racunar, "Рачунар: " + str(racunar_poeni), 3 * sirina / 4, visina / 2, pobedio(racunar, covek))
    
    
def obradi_dogadjaj(dogadjaj):
    global covek, racunar, covek_poeni, racunar_poeni
    if dogadjaj.type == pg.KEYDOWN:
        racunar = random.randint(0, 2)
        if dogadjaj.key == pg.K_p:
            covek = PAPIR
        elif dogadjaj.key == pg.K_k:
            covek = KAMEN
        elif dogadjaj.key == pg.K_m:
            covek = MAKAZE
        if pobedio(covek, racunar):
            covek_poeni += 1
        if pobedio(racunar, covek):
            racunar_poeni += 1
        return True
    return False
    
# -*- acsection: after-main -*-

kraj = False
treba_crtati = True
while not kraj:
    if treba_crtati:
        crtaj()
        pg.display.update()
        treba_crtati = False

    dogadjaj = pg.event.wait()
    if dogadjaj.type == pg.QUIT:
        kraj = True
    else:
        treba_crtati = obradi_dogadjaj(dogadjaj)

pg.quit() # isključujemo rad biblioteke PyGame
