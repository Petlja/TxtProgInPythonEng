# -*- acsection: general-init -*-

import pygame as pg, random

pg.init()   # inicijalizujemo biblioteku pygame
pg.display.set_caption("Лавиринт")  # otvaramo prozor
a = 50 # velicina polja
br_redova = 12
br_kolona = 20
(sirina, visina) = (br_kolona * a, br_redova * a)
prozor = pg.display.set_mode((sirina, visina))
# -*- acsection: main -*-

def crtaj():
    # cela tabla - prazna polja
    prozor.fill(pg.Color('white'))
    for red in range(br_redova):
        for kol in range(br_kolona):
            if tabla[red][kol] == -1: # zid
                pg.draw.rect(prozor, pg.Color('black'), (kol * a, red * a, a, a))
            elif tabla[red][kol] == 1: # tekuca putanja
                pg.draw.circle(prozor, pg.Color('gray'), (kol * a + a//2, red * a + a//2), 10)
            elif tabla[red][kol] == 2: # bili i vratili se
                pg.draw.circle(prozor, pg.Color('black'), (kol * a + a//2, red * a + a//2), 10)

def novi_frejm():
    if traganje:
        next(pozicije, 0)
        
def obradi_dogadjaj(dogadjaj):
    global FPS, pauza, nasao, traganje, pozicije, tabla
    if dogadjaj.type == pg.MOUSEBUTTONDOWN:   # pritisnuto je dugme miša
        mis_x, mis_y = dogadjaj.pos
        x, y = mis_x // a, mis_y // a
        tabla[y][x] = -1 if (tabla[y][x] == 0) else 0
    if dogadjaj.type == pg.KEYDOWN: # pritisnut je taster
        if dogadjaj.key == pg.K_DOWN: # uspori
             # najvise 2 sekunde po frejmu
             FPS = (0.8 * FPS if FPS > 0.5 else 0.5)
        if dogadjaj.key == pg.K_UP:
            FPS *= 1.25 # ubrzaj
        if dogadjaj.unicode == 's': # (re)start
            for red in range(br_redova):
                for kol in range(br_kolona):
                    if tabla[red][kol] > 0:
                        tabla[red][kol] = 0
            traganje = True
            nasao = False
            pozicije = trazi(poc[0], poc[1]) # generator
        if dogadjaj.unicode == 'p': # pauza
            pauza = not pauza
        if dogadjaj.key == pg.K_RIGHT:
            if pauza:
                novi_frejm()

def trazi(x, y):
    global nasao
    if nasao: return
    if (x < 0 or y < 0 or x >= br_kolona or y >= br_redova): return
    if (tabla[y][x] != 0): return

    tabla[y][x] = 1
    yield
    if (x, y) == cilj:
        nasao = True
        return

    yield from trazi(x + 1, y)
    yield from trazi(x - 1, y)
    yield from trazi(x, y + 1)
    yield from trazi(x, y - 1)

    if not nasao:
        tabla[y][x] = 2
        yield

FPS = 5
pauza = False
poc, cilj = (0,0), (br_kolona-1, br_redova-1)
tabla = [[random.randint(-1, 0) for i in range(br_kolona)]  for j in range(br_redova)]
traganje = False
nasao = False

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