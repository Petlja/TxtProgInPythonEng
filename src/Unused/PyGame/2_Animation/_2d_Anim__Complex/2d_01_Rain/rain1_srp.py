# -*- acsection: general-init -*-
import pygame as pg
import random

pg.init() # inicijalizujemo biblioteku PyGame
pg.display.set_caption("Киша")

# otvaramo prozor
(sirina, visina) = (940, 433) # dimenzije slike
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

def novi_kolut():
    x = random.randint(margina, sirina - margina)
    y = random.randint(margina, visina - margina)
    r0 = 10
    r_max = random.randint(2, 5) * 10
    return (x, y, r0, r_max)
    
def crtaj():
    global kolutovi
    prozor.blit(voda, (0, 0))
    # prozor.fill(pg.Color("skyblue"))
    for kolut in kolutovi:
        x, y, r, r_max = kolut
        ra, rb = r, r/3
        pg.draw.ellipse(prozor, (46,99,113), (x-ra, y-rb, 2*ra, 2*rb), 1)

def novi_frejm():
    global kolutovi
    for i in range(len(kolutovi)):
        x, y, r, r_max = kolutovi[i]
        if r > r_max:
            kolutovi[i] = novi_kolut()
        else:
            kolutovi[i] = (x, y, r + 10, r_max)
        
voda = pg.image.load('water.png')
margina = 30
kolutovi = [novi_kolut() for _ in range(20)]

# -*- acsection: after-main -*-

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
    sat.tick(10)
    novi_frejm()

pg.quit() # isključujemo rad biblioteke PyGame
