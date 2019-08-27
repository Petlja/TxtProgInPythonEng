# -*- acsection: general-init -*-                                 
import pygame as pg

pg.init()  # inicijalizujemo rad biblioteke PyGame
pg.display.set_caption("Бројање")  # otvaramo prozor
(sirina, visina) = (180, 300)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-
def crtaj():
    margina = 20
    debljina = 20
    visina = 100
    sirina = 100
    d2 = debljina / 2
    razmaci_x = [margina + d2, d2, sirina, d2]
    razmaci_y = [margina + d2, d2, visina, d2, d2, visina, d2]
    
    for i in range(1, len(razmaci_x)):
        razmaci_x[i] += razmaci_x[i-1]
    for i in range(1, len(razmaci_y)):
        razmaci_y[i] += razmaci_y[i-1]

    x1, x1p, x2m, x2 = razmaci_x
    y1, y1p, y2m, y2, y2p, y3m, y3 = razmaci_y
    seg_poc  = ( (x1p, y1), (x1, y1p), (x2, y1p), (x1p, y2), (x1, y2p), (x2, y2p), (x1p, y3) )
    seg_kraj = ( (x2m, y1), (x1, y2m), (x2, y2m), (x2m, y2), (x1, y3m), (x2, y3m), (x2m, y3) )
    signali = ["1110111", "0010010", "1011101", "1011011", "0111010",
               "1101011", "1101111", "1010010", "1111111", "1111011"]

    prozor.fill(pg.Color("white"))
    signal = signali[broj]
    for i_seg in range(7):
        if signal[i_seg] == '1':
            pg.draw.line(prozor, pg.Color("black"), seg_poc[i_seg], seg_kraj[i_seg], debljina)

def novi_frejm():
    global broj
    broj = (broj + 1) % 10  # brojimo od 0 do 9 u krug

broj = 0  # broj

# -*- acsection: main -*-

kraj = False
sat = pg.time.Clock()  # sat koji određuje broj frejmova u sekundi
while not kraj:
    # crtamo i ažuriramo sadržaj prozora
    crtaj()
    pg.display.update()

    # proveravamo da li je korisnik isključio prozor
    for dogadjaj in pg.event.get():
        if dogadjaj.type == pg.QUIT:
            kraj = True

    # pauziramo do sledeceg frejma
    sat.tick(2)
    novi_frejm()

pg.quit() # isključujemo rad biblioteke PyGame
