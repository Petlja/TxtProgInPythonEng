# -*- acsection: general-init -*-
import pygame as pg, random

pg.init()  # uključujemo rad biblioteke PyGame
pg.display.set_caption("Шетање лоптице тастатуром") # otvaramo prozor
(sirina, visina) = (400, 400)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

boja_zmije = (255, 0, 0)            # boja zmije
a = 10                              # velicina jednog polja
br_redova, br_kolona = visina // a, sirina // a # velicina table
pomaci = { pg.K_UP : (0, -1), pg.K_DOWN : (0, 1), pg.K_LEFT : (-1, 0), pg.K_RIGHT : (1, 0)}
pomak = pomaci[pg.K_RIGHT]
centar = (br_kolona // 2, br_redova // 2) # koordinate centra table
zmija = [centar for i in range(10)]
i_glava = 0

def crtanje():
    # bojimo prozor u sivo
    prozor.fill(pg.Color("gray"))
    # crtamo zmiju
    for tacka in zmija:
        x, y = tacka
        pg.draw.rect(prozor, boja_zmije, (x*a, y*a, a, a))

def novi_frejm():
    global zmija, i_glava, kraj
    x0, y0 = zmija[i_glava]
    dx, dy = pomak
    x = x0 + dx
    y = y0 + dy
    i_glava = (i_glava + 1) % len(zmija)
    zmija[i_glava] = (x, y)
    if x < 0 or x >= br_kolona or y < 0 or y >= br_redova:
        kraj = True  # zmija je izasla iz table

def obradi_dogadjaj(dogadjaj):
    global pomaci, pomak
    if dogadjaj.type == pg.KEYDOWN: # pritisnut je taster
        pomak = pomaci.get(dogadjaj.key, pomak)

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
        
    sat.tick(10)
    novi_frejm()

pg.quit()  # isključivanje rada biblioteke PyGame
