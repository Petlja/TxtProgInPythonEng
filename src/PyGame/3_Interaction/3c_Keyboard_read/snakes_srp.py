import pygame as pg, petljapg
(sirina, visina) = (400, 400)
prozor = petljapg.open_window(sirina, visina, "Змије")

a = 10                                          # velicina jednog polja
br_redova, br_kolona = visina // a, sirina // a # velicina table

GORE, DOLE, LEVO, DESNO = 0, 1, 2, 3
tasteri_1 = (pg.K_w, pg.K_s, pg.K_a, pg.K_d)
tasteri_2 = (pg.K_UP, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT)
telo_zmije_1 = [(br_redova//2, br_kolona//3)] * 20
telo_zmije_2 = [(br_redova//2, 2*br_kolona//3)] * 20

#          boja              polozaj       smer,   U D L R    indeks glave
zmija_1 = [pg.Color('red'),  telo_zmije_1, (0,1),  tasteri_1,      0]
zmija_2 = [pg.Color('blue'), telo_zmije_2, (0,-1), tasteri_2,      0]
zmije = [zmija_1, zmija_2]
kraj = False

def crtanje():
    prozor.fill(pg.Color("gray"))     # bojimo prozor u sivo
    if kraj:
        font = pg.font.SysFont("Arial", 60)
        sl_tekst = font.render("Крај!", True, pg.Color("black"))
        x = (sirina - sl_tekst.get_width()) // 2
        y = (visina - sl_tekst.get_height()) // 2
        prozor.blit(sl_tekst, (x, y))
    else:
        # crtamo zmije
        for boja, telo, smer, tasteri, i_glava in zmije:                
            for red, kol in telo:
                pg.draw.rect(prozor, boja, (kol*a, red*a, a, a))

def nov_frejm():
    global zmije, kraj
    pritisnut = pg.key.get_pressed()
    for i_zmija in range(2):
        boja, telo, (d_red, d_kol), tasteri, i_glava = zmije[i_zmija]
        if pritisnut[tasteri[LEVO]]:  (d_red, d_kol) = (0, -1)
        if pritisnut[tasteri[DESNO]]: (d_red, d_kol) = (0, 1)
        if pritisnut[tasteri[GORE]]:  (d_red, d_kol) = (-1, 0)
        if pritisnut[tasteri[DOLE]]:  (d_red, d_kol) = (1, 0)        
        red, kol = telo[i_glava]
        i_glava = (i_glava + 1) % len(telo)
        telo[i_glava] = (red + d_red, kol + d_kol)
        if kol < 0 or kol >= br_kolona or red < 0 or red >= br_redova:
            kraj = True  # zmija je izasla iz table
        zmije[i_zmija] = boja, telo, (d_red, d_kol), tasteri, i_glava

    crtanje()

petljapg.frame_loop(3, nov_frejm)
