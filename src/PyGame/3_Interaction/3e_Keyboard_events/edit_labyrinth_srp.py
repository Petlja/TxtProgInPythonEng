import pygame as pg, petljapg, random
a = 50 # velicina polja
br_redova = 12
br_kolona = 20
(sirina, visina) = (br_kolona * a, br_redova * a)
prozor = petljapg.open_window(sirina, visina, "Лавиринт")

def nov_frejm():
    prozor.fill(pg.Color('white')) # bela pozadina
    for red in range(br_redova):
        for kol in range(br_kolona):
            if tabla[red][kol] == 1: # zid
                pg.draw.rect(prozor, pg.Color('black'), (kol * a, red * a, a, a))

    # okvir
    pg.draw.rect(prozor, pg.Color('red'), (okvir_kol * a, okvir_red * a, a, a), 3)
    
def obradi_dogadjaj(dogadjaj):
    global tabla, okvir_red, okvir_kol
    if dogadjaj.type == pg.KEYDOWN: # pritisnut je taster
        if dogadjaj.key == pg.K_LEFT:
            if okvir_kol > 0:
                okvir_kol -= 1
        elif dogadjaj.key == pg.K_RIGHT:
            if okvir_kol < br_kolona-1:
                okvir_kol += 1
        elif dogadjaj.key == pg.K_UP:
            if okvir_red > 0:
                okvir_red -= 1
        elif dogadjaj.key == pg.K_DOWN:
            if okvir_red < br_redova-1:
                okvir_red += 1
        elif dogadjaj.key == pg.K_SPACE:
            tabla[okvir_red][okvir_kol] = 1 - tabla[okvir_red][okvir_kol]

tabla = []
for j in range(br_redova):
    tabla.append([])
    for i in range(br_kolona):
        tabla[-1].append(random.randint(0, 1))
        
(okvir_red, okvir_kol) = (0, 0)
petljapg.frame_loop(10, nov_frejm, obradi_dogadjaj)
