# -*- acsection: general-init -*-
import pygame as pg, random

pg.init()  # uključujemo rad biblioteke PyGame
pg.display.set_caption("Шетање лоптице тастатуром") # otvaramo prozor
(sirina, visina) = (400, 400)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

a = 10                                          # velicina jednog polja
br_redova, br_kolona = visina // a, sirina // a # velicina table

smerovi_1 = { pg.K_w : (0, -1), pg.K_s : (0, 1), pg.K_a : (-1, 0), pg.K_d : (1, 0)}
smerovi_2 = { pg.K_UP : (0, -1), pg.K_DOWN : (0, 1), pg.K_LEFT : (-1, 0), pg.K_RIGHT : (1, 0)}
telo_zmije_1 = [(br_kolona//3, br_redova//2) for i in range(20)]
telo_zmije_2 = [(2*br_kolona//3, br_redova//2) for i in range(20)]

#          boja              polozaj       smer,                 mapa pomeranja  indeks glave
zmija_1 = [pg.Color('red'),  telo_zmije_1, smerovi_1[pg.K_d],    smerovi_1,      0]
zmija_2 = [pg.Color('blue'), telo_zmije_2, smerovi_2[pg.K_LEFT], smerovi_2,      0]
zmije = [zmija_1, zmija_2]

def crtanje():
    prozor.fill(pg.Color("gray"))     # bojimo prozor u sivo
    for zmija in zmije:                # crtamo zmije
        boja, telo, smer, mapa, i_glava = zmija
        for x, y in telo:
            pg.draw.rect(prozor, boja, (x*a, y*a, a, a))

def novi_frejm():
    global zmije, kraj
    for i in range(2):
        boja, telo, smer, mapa, i_glava = zmije[i]
        x0, y0 = telo[i_glava]
        dx, dy = smer
        x = x0 + dx
        y = y0 + dy
        i_glava = (i_glava + 1) % len(telo)
        telo[i_glava] = (x, y)
        zmije[i] = boja, telo, smer, mapa, i_glava
        if x < 0 or x >= br_kolona or y < 0 or y >= br_redova:
            kraj = True  # zmija je izasla iz table

def obradi_dogadjaj(dogadjaj):
    global zmije
    if dogadjaj.type == pg.KEYDOWN: # pritisnut je taster
        for i in range(2):
            boja, telo, smer, mapa, i_glava = zmije[i]
            smer = mapa.get(dogadjaj.key, smer)
            zmije[i] = boja, telo, smer, mapa, i_glava

# -*- acsection: after-main -*-

kraj = False
sat = pg.time.Clock()    # sat koji određuje broj frejmova u sekundi
while not(kraj):
    crtanje()
    pg.display.update()  # ažuriramo prikaz sadržaja ekrana

    for dogadjaj in pg.event.get():
        if dogadjaj.type == pg.QUIT:    # isključivanje prozora
            kraj = True
        else:
            obradi_dogadjaj(dogadjaj)
        
    sat.tick(2)
    novi_frejm()

pg.quit()  # isključivanje rada biblioteke PyGame
