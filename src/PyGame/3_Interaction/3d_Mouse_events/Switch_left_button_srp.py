# -*- acsection: general-init -*-
import pygame as pg, petljapg
(sirina, visina) = (800, 500)
prozor = petljapg.open_window(sirina, visina, "Прекидач")

shema_slike = (pg.image.load('Shema1_Off.png'), pg.image.load('Shema1_On.png'))
prekidac_slike = (pg.image.load('SwitchOff.png'), pg.image.load('SwitchOn.png'))
sijalica_slike = (pg.image.load('BulbOff.png'), pg.image.load('BulbOn.png'))
prekidac_poz = (100, 200)
sijalica_poz = (500, 100)

ukljucen_prekidac = False

def nov_frejm():
    prozor.blit(shema_slike[ukljucen_prekidac], (0, 0))
    prozor.blit(prekidac_slike[ukljucen_prekidac], prekidac_poz)
    prozor.blit(sijalica_slike[ukljucen_prekidac], sijalica_poz)
    
def tacka_u_pravougaoniku(tacka, gornje_levo_teme, sirina, visina):
    x, y = tacka
    x0, y0 = gornje_levo_teme
    return x0 <= x and x <= x0 + sirina and y0 <= y and y <= y0 + visina
    
# -*- acsection: main -*-
def obradi_dogadjaj(dogadjaj):
    global ukljucen_prekidac
    # ako je pritisnuto levo dugme miša
    if dogadjaj.type == pg.MOUSEBUTTONDOWN and dogadjaj.button == 1:
        mis_tacka = dogadjaj.pos
        if tacka_u_pravougaoniku(mis_tacka, prekidac_poz, 80, 80):
            ukljucen_prekidac = not ukljucen_prekidac

petljapg.frame_loop(10, nov_frejm, obradi_dogadjaj)
# -*- acsection: after-main -*-
