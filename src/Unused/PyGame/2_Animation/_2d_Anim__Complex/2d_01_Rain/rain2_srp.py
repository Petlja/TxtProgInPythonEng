# -*- acsection: general-init -*-
import pygame as pg
import random

pg.init() # inicijalizujemo biblioteku PyGame
pg.display.set_caption("Киша")

# otvaramo prozor
(sirina, visina) = (940, 433) # dimenzije slike
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

def nova_kap():
    x = random.randint(margina, sirina - margina)
    y = 0
    y_max = random.randint(horizont_y + margina, visina - margina)
    d = random.randint(5, 15)
    return (x, y, y_max, d)
    
def crtaj():
    global kapi
    prozor.blit(voda, (0, 0))
    pg.draw.rect(prozor, pg.Color("skyblue"), (0, 0, sirina, horizont_y)) # nebo
    for kap in kapi:
        x, y, y_max, d = kap
        pg.draw.line(prozor, boja_kise, (x, y), (x, y+d), 1)

def novi_frejm():
    global kapi
    
    max_br_kapi = 50
    br_novih_kapi = min(5, max_br_kapi - len(kapi))
    nove_kapi = [nova_kap() for _ in range(br_novih_kapi)]
    for i in range(len(kapi)):
        x, y, y_max, d = kapi[i]
        y += 20
        if y < y_max:
            nove_kapi.append((x, y, y_max, d))
            
    kapi = nove_kapi
    
voda = pg.image.load('water.png')
margina = 30
horizont_y = int(visina * 0.6)
boja_kise = (46,99,113)
kapi = []

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
    sat.tick(20)
    novi_frejm()

pg.quit() # isključujemo rad biblioteke PyGame
