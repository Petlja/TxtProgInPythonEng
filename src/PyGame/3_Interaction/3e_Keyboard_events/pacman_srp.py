import pygame as pg, petljapg, random
br_redova, br_kolona = 10, 10
a = 50 # velicina polja
(sirina, visina) = (a* br_kolona, a * br_redova)
prozor = petljapg.open_window(sirina, visina, "Пакмен")

ima_kuglica = []
for _ in range(br_redova):
    ima_kuglica.append([True] * br_kolona)

(pakmen_red, pakmen_kol) = (br_redova // 2, br_kolona // 2)

def crtaj():
    prozor.fill(pg.Color("gray"))   # bojimo prozor u sivo
    
    # crtamo kuglice
    for red in range(br_redova):
        for kol in range(br_kolona):
            if ima_kuglica[red][kol]:
                (x, y) = (kol * a + a//2, red * a + a//2)
                pg.draw.circle(prozor, pg.Color('white'), (x, y), 5)
                
    # crtamo 'pakmena'
    (x, y) = (pakmen_kol * a + a//2, pakmen_red * a + a//2)
    pg.draw.circle(prozor, pg.Color('yellow'), (x, y), a // 3)

def nov_frejm():
    global pakmen_red, pakmen_kol
    
    pritisnut = pg.key.get_pressed()
    if pritisnut[pg.K_LEFT] and (pakmen_kol > 0): 
        pakmen_kol -= 1
    if pritisnut[pg.K_RIGHT] and (pakmen_kol < br_kolona-1):
        pakmen_kol += 1
    if pritisnut[pg.K_UP] and (pakmen_red > 0):
        pakmen_red -= 1
    if pritisnut[pg.K_DOWN] and (pakmen_red < br_redova-1):
        pakmen_red += 1

    ima_kuglica[pakmen_red][pakmen_kol] = False # 'pojedena' kuglica
    
    crtaj()   
    
petljapg.frame_loop(15, nov_frejm)
