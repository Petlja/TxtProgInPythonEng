# Crtanje drveta zadate velicine
# Perspektiva, automatsko odredjivanje velicine iz pozicije
# Z-buffer - crtaju se prvo najdalje jelke

# -*- acsection: general-init -*-
import pygame as pg
import random

# uključivanje rada biblioteke PyGame
pg.init()
# podešavamo naslov prozora
pg.display.set_caption("Перспектива")
# otvaramo prozor dimenzije 800x400
(sirina, visina) = (800, 400)
prozor = pg.display.set_mode((sirina, visina))
# -*- acsection: main -*-

def crtaj_trougao(boja, vrh_x, vrh_y, vel):
    pg.draw.polygon(prozor, boja, [(vrh_x - vel, vrh_y + vel), (vrh_x, vrh_y), (vrh_x + vel, vrh_y + vel)])

def crtaj_jelku_vel(boja_krosnje, boja_stabla, vrh_x, vrh_y, vel):
    pg.draw.rect(prozor, boja_stabla, (vrh_x - 0.1 * vel, vrh_y + 0.6 * vel, 0.2 * vel, 0.4 * vel))
    for i in [0, 0.1, 0.2]:
        crtaj_trougao(boja_krosnje, vrh_x, vrh_y + i * vel, (i + 0.2) * vel)
    
def crtaj_jelku(boja_krosnje, boja_stabla, centar_x, dno_y):
    vel = (dno_y - horizont_y) / visina_ociju_izrazena_u_jelkama
    vrh_y = dno_y - vel
    crtaj_jelku_vel(boja_krosnje, boja_stabla, centar_x, vrh_y, vel)

def crtaj():
    pg.draw.rect(prozor, BOJA_NEBA, (0, 0, sirina, horizont_y)) # nebo
    pg.draw.circle(prozor, BOJA_SUNCA, (int(sunce_x), int(sunce_y)), sunce_vel) # sunce
    pg.draw.rect(prozor, BOJA_TRAVE, (0, horizont_y, sirina, visina - horizont_y)) # trava
        
    # drvece
    for drvo in drvece:
        x, y = drvo
        crtaj_jelku(BOJA_KROSNJE, BOJA_STABLA, x, horizont_y + y)

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

crtaj()
# -*- acsection: after-main -*-
# ažuriramo prikaz sadržaja ekrana
pg.display.update()

# čekamo da korisnik isključi prozor
while pg.event.wait().type != pg.QUIT:
    pass
    
# isključivanje rada biblioteke PyGame
pg.quit()
