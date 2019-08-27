import pygame as pg, petljapg, random
a = 50 # velicina polja
br_redova = 12
br_kolona = 20
(sirina, visina) = (br_kolona * a, br_redova * a)
prozor = petljapg.open_window(sirina, visina, "Лавиринт")

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
    
    if not traganje:
        pg.draw.rect(prozor, pg.Color('red'), (okvir_kol * a, okvir_red * a, a, a), 3)
    

def nov_frejm():
    if traganje and not pauza:
        next(pozicije, 0)
    crtaj()
        
def obradi_dogadjaj(dogadjaj):
    global pauza, nasao, traganje, pozicije, tabla, okvir_red, okvir_kol
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
            if (tabla[okvir_red][okvir_kol] == 0) :
                tabla[okvir_red][okvir_kol] = -1
            else: 
                tabla[okvir_red][okvir_kol] = 0

        if chr(dogadjaj.key) == 's': # (re)start
            for red in range(br_redova):
                for kol in range(br_kolona):
                    if tabla[red][kol] > 0:
                        tabla[red][kol] = 0
            traganje = True
            nasao = False
            pozicije = trazi(poc[0], poc[1]) # generator
        if chr(dogadjaj.key) == 'p': # pauza
            if traganje:
                pauza = not pauza

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
(okvir_red, okvir_kol) = (0, 0)
traganje = False
nasao = False

petljapg.frame_loop(FPS, nov_frejm, obradi_dogadjaj)
