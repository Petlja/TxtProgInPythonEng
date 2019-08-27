# -*- acsection: general-init -*-
import pygame as pg, petljapg, random
(sirina, visina) = (400, 400)
prozor = petljapg.open_window(sirina, visina, "Змија")

boja_zmije = (255, 0, 0)            # boja zmije
a = 10                              # velicina jednog polja
br_redova, br_kolona = visina // a, sirina // a # velicina table
(d_red, d_kol) = (0, 1) # inicijalno po jednu kolonu udesno
centar = (br_redova // 2, br_kolona // 2) # koordinate centra table
zmija = [centar] * 10 # na pocetku je zmija sklupcana u centru
i_glava = 0 # indeks kvadratica u listi koji predstavlja glavu zmije
kraj = False

def crtanje():
    prozor.fill(pg.Color("gray")) # bojimo prozor u sivo
    if kraj:
        # ispisujemo poruku da je kraj
        font = pg.font.SysFont("Arial", 60)
        sl_tekst = font.render("Крај!", True, pg.Color("black"))
        x = (sirina - sl_tekst.get_width()) // 2
        y = (visina - sl_tekst.get_height()) // 2
        prozor.blit(sl_tekst, (x, y))
    else:
        # crtamo zmiju
        for red, kol in zmija:
            pg.draw.rect(prozor, boja_zmije, (kol*a, red*a, a, a))


def nov_frejm():
    global zmija, i_glava, d_red, d_kol, kraj
# -*- acsection: main -*-

    pritisnut = pg.key.get_pressed()
    if pritisnut[pg.K_LEFT]:  (d_red, d_kol) = (0, -1)
    if pritisnut[pg.K_RIGHT]: (d_red, d_kol) = (0, 1)
    if pritisnut[pg.K_UP]:    (d_red, d_kol) = (-1, 0)
    if pritisnut[pg.K_DOWN]:  (d_red, d_kol) = (1, 0)
    
# -*- acsection: after-main -*-
    # izracunavamo nov polozaj glave zmije
    red, kol = zmija[i_glava]
    i_glava = (i_glava + 1) % len(zmija)
    zmija[i_glava] = (red + d_red, kol + d_kol)
    if kol < 0 or kol >= br_kolona or red < 0 or red >= br_redova:
        kraj = True  # zmija je izasla iz table
    
    crtanje()


petljapg.frame_loop(10, nov_frejm)
