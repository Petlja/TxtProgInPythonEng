# -*- acsection: general-init -*-
import pygame as pg
import math

# uključivanje rada biblioteke PyGame
pg.init()
# podešavamo naslov prozora
pg.display.set_caption("Фрактал - Кохова крива")

# otvaramo prozor dimenzije 800x600
(sirina, visina) = (800, 600)
prozor = pg.display.set_mode((sirina,visina))
# -*- acsection: main -*-

def desno(k=1):
    global smer
    smer += k

def levo(k=1):
    global smer
    smer -= k

def napred(d):
    global tekuca_tacka
    if  d > 10:
        napred(d/3); desno()
        napred(d/3); levo(2)
        napred(d/3); desno()
        napred(d/3)
    else:
        x, y = tekuca_tacka
        dx, dy = smerovi[smer % br_smerova]
        sledeca_tacka = (x + d*dx, y + d*dy)
        pg.draw.line(prozor, pg.Color("yellow"), tekuca_tacka, sledeca_tacka )
        tekuca_tacka = sledeca_tacka

br_smerova = 6
phi = 2 * math.pi / br_smerova
smerovi = tuple((math.cos(k * phi), math.sin(k * phi)) for k in range(br_smerova))
velicina = 200
tekuca_tacka = ((sirina - velicina) // 2, visina // 2 + round(velicina * 1.73/6))
smer = 0

prozor.fill(pg.Color("black")) # bojimo pozadinu u crno
for _ in range(3):
    napred(200)
    levo(2)

# -*- acsection: after-main -*-
# ažuriramo prikaz sadržaja ekrana
pg.display.update()

# čekamo da korisnik isključi prozor
while pg.event.wait().type != pg.QUIT:
    pass
    
# isključivanje rada biblioteke PyGame
pg.quit()
