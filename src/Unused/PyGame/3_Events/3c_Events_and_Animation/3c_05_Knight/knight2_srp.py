# -*- acsection: general-init -*-

import pygame as pg

pg.init()   # inicijalizujemo biblioteku pygame
pg.display.set_caption("Konj")  # otvaramo prozor
a = 40 # velicina polja
vel_table = 20
(sirina, visina) = (vel_table * a, vel_table * a)
prozor = pg.display.set_mode((sirina, visina))
# -*- acsection: main -*-

font = pg.font.SysFont("Arial", (a*3)//5) # font kojim će biti prikazan tekst

def trazi(x, y, k):
    global pauza, nasao
    if nasao: return
    if (x < 0 or y < 0 or x >= vel_table or y >= vel_table): return
    if (tabla[x][y] > 0): return

    tabla[x][y] = k
    yield
    if k == vel_table * vel_table:
        nasao = True
        pauza = True
        return
        
    potezi = [[0, 0, 0] for i in range(8)]
    for potez1 in range(8):
        x1 = x + dx[potez1]
        y1 = y + dy[potez1]
        potezi[potez1][0] = dx[potez1]
        potezi[potez1][1] = dy[potez1]
        if x1 >= 0 and y1 >= 0 and x1 < vel_table and y1 < vel_table and tabla[x1][y1] == 0:
            for potez2 in range(8):
                x2 = x1 + dx[potez2]
                y2 = y1 + dy[potez2]
                if x2 >= 0 and y2 >= 0 and x2 < vel_table and y2 < vel_table and tabla[x2][y2] == 0:
                    potezi[potez1][2] += 1

    potezi = sorted(potezi, key=lambda p: p[2])
    for dx1, dy1, br_nast in potezi:
        yield from trazi(x + dx1, y + dy1, k + 1)

    if not nasao:
        tabla[x][y] = 0
        yield

def crtaj():
    # cela tabla - prazna polja
    prozor.fill(pg.Color('white'))
    for red in range(vel_table):
        for kol in range(red%2, vel_table, 2):
            pg.draw.rect(prozor, pg.Color('black'), (kol * a, (vel_table-1-red) * a, a, a))

    for red in range(vel_table):
        for kol in range(vel_table):
            if tabla[kol][red] > 0:
                br_slika = font.render(str(tabla[kol][red]), True, pg.Color("red"))
                dx, dy = (a - br_slika.get_width())//2, (a - br_slika.get_height())//2, 
                prozor.blit(br_slika, (kol * a + dx, (vel_table-1-red) * a + dy))
 
def novi_frejm():
    global pozicije
    nema_vise_pozicija = next(pozicije, True)
    # if nema_vise_pozicija:
        # pozicije = ispitaj_sve_pozicije()  # ispocetka
        # next(pozicije)
        
def obradi_dogadjaj(dogadjaj):
    global FPS, pauza
    if dogadjaj.type == pg.KEYDOWN: # ima li ulaza sa tastature
        if dogadjaj.key == pg.K_DOWN: # uspori
             # najvise 2 sekunde po frejmu
             FPS = (0.8 * FPS if FPS > 0.5 else 0.5)
        if dogadjaj.key == pg.K_UP:
            FPS *= 1.25 # ubrzaj
        if dogadjaj.unicode == 'p': # pauza
            pauza = not pauza
        if dogadjaj.key == pg.K_RIGHT:
            if pauza:
                novi_frejm()

FPS = 10
pauza = False
dx = [2, 2, 1, 1, -2, -2, -1, -1]
dy = [1, -1, 2, -2, 1, -1, 2, -2]
tabla = [[0 for i in range(100)]  for j in range(100)]
nasao = False

pozicije = trazi(0, 0, 1) # generator

# -*- acsection: after-main -*-
kraj = False
sat = pg.time.Clock()  # sat koji određuje broj frejmova u sekundi
while not kraj:
    # crtamo i ažuriramo sadržaj prozora
    crtaj()
    pg.display.update()
 
    # obradimo pristigle dogadjaje
    for dogadjaj in pg.event.get():
        if dogadjaj.type == pg.QUIT:    # isključivanje prozora
            kraj = True
        else:
            obradi_dogadjaj(dogadjaj)
 
    if not pauza:
        novi_frejm()
        
    # sacekamo do sledeceg frejma
    sat.tick(FPS)
 
pg.quit() # isključujemo rad biblioteke PyGame