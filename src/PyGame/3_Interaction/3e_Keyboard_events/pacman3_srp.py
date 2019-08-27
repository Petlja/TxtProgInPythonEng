import pygame as pg, petljapg, random
tabla = [
    '.........',
    '...XXX...',
    '..XXXXX..',
    '.........',
    '.........'
]
br_redova = len(tabla)
br_kolona = len(tabla[0])
a = 50 # velicina polja
(sirina, visina) = (a* br_kolona, a * br_redova)
prozor = petljapg.open_window(sirina, visina, "Пакмен")

(pakmen_red, pakmen_kol) = (br_redova // 2, br_kolona // 2)
(d_red, d_kol) = (0, 0)

def nov_frejm():
    global pakmen_red, pakmen_kol
    nov_red = pakmen_red + d_red
    nova_kol = pakmen_kol + d_kol
    if (nova_kol >= 0 and nova_kol < br_kolona
        and nov_red >= 0 and nov_red < br_redova
        and tabla[nov_red][nova_kol] == '.'):
        pakmen_kol = nova_kol
        pakmen_red = nov_red

    prozor.fill(pg.Color("black"))   # bojimo prozor u crno

    # tabla

    for red in range(br_redova):
        for kol in range(br_kolona):
            x, y = a * kol, a * red
            if tabla[red][kol] == 'X':
                pg.draw.rect(prozor, pg.Color("blue"), (x, y, a, a), 3)
            else:
                pg.draw.circle(prozor, pg.Color("white"), (x+a//2, y+a//2), 3)
   
    # crtamo 'pakmena'
    (x, y) = (pakmen_kol * a + a//2, pakmen_red * a + a//2)
    pg.draw.circle(prozor, pg.Color('yellow'), (x, y), a // 3)
    
def obradi_dogadjaj(dogadjaj):
    global pakmen_red, pakmen_kol, d_red, d_kol
    if dogadjaj.type == pg.KEYDOWN:
        if dogadjaj.key == pg.K_LEFT:
            d_red, d_kol = 0, -1
        elif dogadjaj.key == pg.K_RIGHT:
            d_red, d_kol = 0, 1
        elif dogadjaj.key == pg.K_UP:
            d_red, d_kol = -1, 0
        elif dogadjaj.key == pg.K_DOWN:
            d_red, d_kol = 1, 0
        # else:
            # d_red, d_kol = 0, 0

petljapg.frame_loop(10, nov_frejm, obradi_dogadjaj)
