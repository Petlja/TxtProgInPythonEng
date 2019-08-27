import pygame as pg, petljapg, random
br_redova, br_kolona = 10, 10
a = 50 # velicina polja
(sirina, visina) = (a* br_kolona, a * br_redova)
prozor = petljapg.open_window(sirina, visina, "Пакмен")

(pakmen_red, pakmen_kol) = (br_redova // 2, br_kolona // 2)

def nov_frejm():
    global pakmen_red, pakmen_kol

    pritisnut = pg.key.get_pressed()
    if pritisnut[pg.K_LEFT] and (pakmen_kol > 0):            pakmen_kol -= 1
    if pritisnut[pg.K_RIGHT] and (pakmen_kol < br_kolona-1): pakmen_kol += 1
    if pritisnut[pg.K_UP] and (pakmen_red > 0):              pakmen_red -= 1
    if pritisnut[pg.K_DOWN] and (pakmen_red < br_redova-1):  pakmen_red += 1

    # crtanje
    prozor.fill(pg.Color("black"))   # bojimo prozor u crno
    # bele kuglice
    for x in range(a // 2, sirina, a):
        for y in range(a // 2, visina, a):
            pg.draw.circle(prozor, pg.Color("white"), (x, y), 3)
   
    # crtamo 'pakmena'
    (x, y) = (pakmen_kol * a + a//2, pakmen_red * a + a//2)
    pg.draw.circle(prozor, pg.Color('yellow'), (x, y), a // 3)
    
petljapg.frame_loop(30, nov_frejm)
