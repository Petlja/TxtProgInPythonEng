# -*- acsection: general-init -*-

import pygame as pg

slika_polje = [
    [pg.image.load('Square0_Queen0.png'), pg.image.load('Square1_Queen0.png')], 
    [pg.image.load('Square0_Queen1.png'), pg.image.load('Square1_Queen1.png')],
    [pg.image.load('Square0_Queen2.png'), pg.image.load('Square1_Queen2.png')]
]

vel_polja = slika_polje[0][0].get_width()

pg.init()   # inicijalizujemo biblioteku pygame
pg.display.set_caption("N dama")  # otvaramo prozor
vel_table = 8
(sirina, visina) = (vel_table * vel_polja, vel_table * vel_polja)
prozor = pg.display.set_mode((sirina, visina))
# -*- acsection: main -*-

def pozicija_je_regularna(): # proverava se samo poslednja dama protiv ostalih
    if len(redovi) < 2:
        return True
    nova_kolona = len(redovi) - 1
    nov_red = redovi[nova_kolona]
    for preth_kolona in range(nova_kolona):
        preth_red = redovi[preth_kolona]
        if (nov_red == preth_red or
           nov_red + nova_kolona == preth_red + preth_kolona or
           nov_red - nova_kolona == preth_red - preth_kolona):
            return False
    return True
    
def ispitaj_sve_pozicije():
    global pauza, i_posl_dama, redovi
    d = len(redovi)
    redovi.append(0)
    u_poslednjoj_koloni = (d + 1 == vel_table)
    for red in range(vel_table):
        redovi[d] = red
        if pozicija_je_regularna():
            if u_poslednjoj_koloni:
                pauza = True
            i_posl_dama = 1
            yield
            if not u_poslednjoj_koloni:
                yield from ispitaj_sve_pozicije()
        else:
            i_posl_dama = 2
            yield
    redovi.pop()

def crtaj():
    # cela tabla - prazna polja
    for red in range(vel_table):
        for kol in range(vel_table):
            prozor.blit(slika_polje[0][(kol+red) % 2], (kol * vel_polja, (vel_table-1-red) * vel_polja))
            
    # sve dame osim poslednje
    k = len(redovi) - 1
    for i in range(k):
        prozor.blit(slika_polje[1][(i+redovi[i]) % 2], (i * vel_polja, (vel_table-1-redovi[i]) * vel_polja))
        
    # poslednja dama
    if k >= 0:
        prozor.blit(slika_polje[i_posl_dama][(k+redovi[k]) % 2], (k * vel_polja, (vel_table-1-redovi[k]) * vel_polja))
 
def novi_frejm():
    global pozicije
    nema_vise_pozicija = next(pozicije, True)
    if nema_vise_pozicija:
        pozicije = ispitaj_sve_pozicije()  # ispocetka
        next(pozicije)
        
def obradi_dogadjaj(dogadjaj):
    global FPS, pauza
    if dogadjaj.type == pg.KEYDOWN: # ima li ulaza sa tastature
        if dogadjaj.key == pg.K_DOWN: # uspori
             # najvise 2 sekunde po frejmu
             FPS = (0.8 * FPS if FPS > 0.5 else 0.5)
        if dogadjaj.key == pg.K_UP:
            FPS *= 1.25 # ubrzaj
        if dogadjaj.unicode == 'p': # pauza
            pauza = not pauza
        if dogadjaj.key == pg.K_RIGHT:
            if pauza:
                novi_frejm()

FPS = 20
pauza = False
i_posl_dama = 0
redovi = []
pozicije = ispitaj_sve_pozicije() # generator

# -*- acsection: after-main -*-
kraj = False
sat = pg.time.Clock()  # sat koji određuje broj frejmova u sekundi
while not kraj:
    # crtamo i ažuriramo sadržaj prozora
    crtaj()
    pg.display.update()
 
    # obradimo pristigle dogadjaje
    for dogadjaj in pg.event.get():
        if dogadjaj.type == pg.QUIT:    # isključivanje prozora
            kraj = True
        else:
            obradi_dogadjaj(dogadjaj)
 
    if not pauza:
        novi_frejm()
        
    # sacekamo do sledeceg frejma
    sat.tick(FPS)
 
pg.quit() # isključujemo rad biblioteke PyGame