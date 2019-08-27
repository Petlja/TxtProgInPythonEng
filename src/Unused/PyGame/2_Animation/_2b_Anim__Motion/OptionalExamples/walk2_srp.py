# -*- acsection: general-init -*-
import pygame as pg

pg.init()  # inicijalizujemo biblioteku pygame

pg.display.set_caption("Шетање")  # otvaramo prozor
(sirina, visina) = (800, 600)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

sredina_y = visina / 2

def crtaj():
    prozor.blit(teren, (0, 0))
    pg.draw.circle(prozor, pg.Color("red"), (x, y), 10)
    
def novi_frejm():
    global x, y
    
    pxarray = pg.surfarray.pixels3d(teren)
    x = (x + 10) % (sirina)
    while pxarray[x, y][0] < 50: # trava
        y -= 1
    while pxarray[x, y][0] > 50: # nebo
        y += 1
    
teren = pg.image.load('walk_background1.png')
prozor.blit(teren, (0, 0))
(x, y) =  (0, visina // 2)

# -*- acsection: after-main -*-

kraj = False
sat = pg.time.Clock()  # sat koji određuje broj frejmova u sekundi
while not kraj:
    novi_frejm()
    # crtamo i ažuriramo sadržaj prozora
    crtaj()
    pg.display.update()

    # proveravamo da li je korisnik isključio prozor
    for dogadjaj in pg.event.get():
        if dogadjaj.type == pg.QUIT:
            kraj = True

    # pauziramo do sledeceg frejma
    sat.tick(5)

pg.quit() # isključujemo rad biblioteke PyGame
