# -*- acsection: general-init -*-
import pygame as pg

pg.init()   # uključujemo rad biblioteke PyGame

pg.display.set_caption("Прекидач") 

# otvaramo prozor
(sirina, visina) = (800, 500)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

shema_slike = (pg.image.load('Shema1_Off.png'), pg.image.load('Shema1_On.png'))
prekidac_slike = (pg.image.load('SwitchOff.png'), pg.image.load('SwitchOn.png'))
sijalica_slike = (pg.image.load('BulbOff.png'), pg.image.load('BulbOn.png'))

ukljucen_prekidac = False
prekidac_poz = (100, 200)
sijalica_poz = (500, 100)

def crtanje():
    prozor.blit(shema_slike[ukljucen_prekidac], (0, 0))
    prozor.blit(prekidac_slike[ukljucen_prekidac], prekidac_poz)
    prozor.blit(sijalica_slike[ukljucen_prekidac], sijalica_poz)
    
def tacka_u_pravougaoniku(tacka, gornje_levo_teme, sirina, visina):
    x, y = tacka
    x0, y0 = gornje_levo_teme
    return x0 <= x and x <= x0 + sirina and y0 <= y and y <= y0 + visina
    
def obradi_dogadjaj(dogadjaj):
    global ukljucen_prekidac
    treba_crtati = False
    if dogadjaj.type == pg.MOUSEBUTTONDOWN:   # pritisnuto je dugme miša
        mis_tacka = dogadjaj.pos
        if tacka_u_pravougaoniku(mis_tacka, prekidac_poz, 80, 80):
            ukljucen_prekidac = not ukljucen_prekidac
            treba_crtati = True   # ponovo cemo da iscrtamo scenu
    return treba_crtati

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
