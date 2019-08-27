# -*- acsection: general-init -*-
import pygame as pg, random

pg.init()  # uključujemo rad biblioteke PyGame
pg.display.set_caption("Пакмен") # otvaramo prozor
(sirina, visina) = (600, 400)
prozor = pg.display.set_mode((sirina, visina))

# podešavamo događaje tastaturom - prvi događaj se generiše nakon
# 100ms, a svaki naredni nakon 25ms
pg.key.set_repeat(100, 25)

# -*- acsection: main -*-

a = 50 # velicina polja
br_redova, br_kolona = visina // a, sirina // a
ima_kuglica = [[True for y in range(br_redova)] for x in range(br_kolona)]
br_kuglica = br_redova * br_kolona
(pakmen_x, pakmen_y) = (br_redova // 2, br_kolona // 2)

def crtanje():
    prozor.fill(pg.Color("gray"))   # bojimo prozor u sivo
    
    # crtamo kuglice
    for x in range(br_kolona):
        for y in range(br_redova):
            if ima_kuglica[x][y]:
                pg.draw.circle(prozor, pg.Color('white'), (x * a + a//2, y * a + a//2), 5)
                
    # crtamo 'pakmena'
    pg.draw.circle(prozor, pg.Color('yellow'), (pakmen_x * a + a//2, pakmen_y * a + a//2), a // 3)

def obradi_dogadjaj(dogadjaj):
    global pakmen_x, pakmen_y, br_kuglica, kraj

    treba_crtati = False
    if dogadjaj.type == pg.KEYDOWN:
        if dogadjaj.key == pg.K_LEFT:    # strelica na levo
            if pakmen_x > 0:             # ako ne ispada van prozora
                pakmen_x -= 1            # pomeramo lopticu na levo
                treba_crtati = True      # treba ponovo nacrtati scenu
        if dogadjaj.key == pg.K_RIGHT:   # strelica na desno
            if pakmen_x < br_kolona - 1: # ako ne ispada van prozora
                pakmen_x += 1            # pomeramo lopticu na desno
                treba_crtati = True      # treba ponovo nacrtati scenu
        if dogadjaj.key == pg.K_UP:      # strelica na gore
            if pakmen_y > 0:             # ako ne ispada van prozora
                pakmen_y -= 1            # pomeramo lopticu na gore
                treba_crtati = True      # treba ponovo nacrtati scenu
        if dogadjaj.key == pg.K_DOWN:    # strelica na dole
            if pakmen_y < br_redova - 1: # ako ne ispada van prozora
                pakmen_y += 1            # pomeramo lopticu na dole
                treba_crtati = True      # treba ponovo nacrtati scenu
        if ima_kuglica[pakmen_x][pakmen_y]:
            ima_kuglica[pakmen_x][pakmen_y] = False    # 'pojedena' kuglica
            br_kuglica -= 1              # jedna manje
            if br_kuglica == 0:
                kraj = True
        return treba_crtati              # ne treba ponovo nacrtati scenu

# -*- acsection: after-main -*-

treba_crtati = True
kraj = False
while not(kraj):
    if treba_crtati:
        crtanje()
        pg.display.update()  # ažuriramo prikaz sadržaja ekrana
        treba_crtati = False # ne treba crtati do daljnjeg

    dogadjaj = pg.event.wait()      # čekamo naredni dogadjaj
    if dogadjaj.type == pg.QUIT:    # isključivanje prozora
        kraj = True
    else:
        treba_crtati = obradi_dogadjaj(dogadjaj)

pg.quit()  # isključivanje rada biblioteke PyGame
