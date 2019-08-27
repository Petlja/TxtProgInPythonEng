# Crtanje drveta zadate velicine
# Perspektiva, automatsko odredjivanje velicine iz pozicije
# Z-buffer - crtaju se prvo najdalje jelke

import pygame as pg
import random

pg.init()
pg.display.set_caption("Drvece")
(sirina, visina) = (800, 400)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

def crtaj_jelku(boja_krosnje, boja_stabla, centar_x, dno_y):
    # izracunavamo velicinu iz y koordinate dna
    vel = (dno_y - horizont_y) / visina_ociju_izrazena_u_jelkama
    (vrh_x, vrh_y) = (centar_x, dno_y - vel) # koordinate vrha
    
    # stablo
    pg.draw.rect(prozor, boja_stabla, (vrh_x - 0.1 * vel, vrh_y + 0.6 * vel, 0.2 * vel, 0.4 * vel))
    
    # tri trougla koja cine krosnju
    for i in [0, 0.1, 0.2]:
        vrh_yi = vrh_y + i * vel # vrh trougla
        vel_i = (i + 0.2) * vel  # velicina trougla
        pg.draw.polygon(prozor, boja_krosnje, [(vrh_x - vel_i, vrh_yi + vel_i), (vrh_x, vrh_yi), (vrh_x + vel_i, vrh_yi + vel_i)])

def crtanje():
    pg.draw.rect(prozor, BOJA_NEBA, (0, 0, sirina, horizont_y)) # nebo
    pg.draw.circle(prozor, BOJA_SUNCA, (int(sunce_x), int(sunce_y)), sunce_vel) # sunce
    pg.draw.rect(prozor, BOJA_TRAVE, (0, horizont_y, sirina, visina - horizont_y)) # trava
    
    # drvece
    for drvo in drvece:
        x, y = drvo
        crtaj_jelku(BOJA_KROSNJE, BOJA_STABLA, x, horizont_y + y)

def obradi_dogadjaj(dogadjaj):
    global visina_ociju_izrazena_u_jelkama
    treba_crtati = False
    if dogadjaj.type == pg.KEYDOWN: # ima li ulaza sa tastature
        if dogadjaj.key == pg.K_DOWN and visina_ociju_izrazena_u_jelkama > 0.3:
            visina_ociju_izrazena_u_jelkama -= 0.05
            treba_crtati = True   # ponovo cemo da iscrtamo scenu
        elif dogadjaj.key == pg.K_UP and visina_ociju_izrazena_u_jelkama < 5:
            visina_ociju_izrazena_u_jelkama += 0.05
            treba_crtati = True   # ponovo cemo da iscrtamo scenu
    return treba_crtati
    
BOJA_SUNCA = (247, 242, 81) # zuckasta
BOJA_NEBA = (153, 217, 234) # neka plava
BOJA_TRAVE = (0, 50, 18) # neka tamna zelena
BOJA_KROSNJE = (0, 150, 54) # neka srednja zelena
BOJA_STABLA = (97, 26, 9) # neka braon

horizont_y = visina / 2

# polozaj sunca
sunce_x = 0.1 * sirina 
sunce_y = 0.9 * horizont_y
sunce_vel = random.randint(30, 60)

# Oci su na pocetku postavljene na 2/3 visine jelke, 
# tako da je tacka na 2/3 visine svake jelke na nivou horizonta.
# Ako se ova vrednost smanji (moze do 0.3) imamo utisak da gledamo odozdo (zablja perspektiva),
# a ako se poveca (moze do 5.0), imamo utisak da gledamo odozgo (pticija perspektiva).
visina_ociju_izrazena_u_jelkama = 2/3 

drvece = []
y = 2 # rastojanje dna jelke od horizonta
max_y = (visina - horizont_y) * 0.9
while y < max_y:
    x = random.randint(0, sirina)
    drvece.append([x, y])
    y *= 1.1
    
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
