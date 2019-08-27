# -*- acsection: general-init -*-
import pygame as pg

pg.init()  # inicijalizujemo biblioteku pygame
pg.display.set_caption("Семафор")

# otvaramo prozor
(sirina, visina) = (100, 300)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

trajanje_faze = (5, 2, 5, 2)
svetla_faze = (
    (True,  False, False), # faza crveno
    (True,  True,  False), # faza crveno_zuto
    (False, False, True),  # faza zeleno
    (False, True,  False), # faza zuto
)

crvena_ukljucena  = (255,   0, 0)
crvena_iskljucena = (128,   0, 0)
zuta_ukljucena    = (255, 255, 0)
zuta_iskljucena   = (128, 128, 0)
zelena_ukljucena  = (  0, 255, 0)
zelena_iskljucena = (  0, 128, 0)
br_faza = len(svetla_faze)
i_faza = 0
do_promene = 0

def novi_frejm():
    global i_faza, do_promene # ove vrednosti izracunavamo
    if do_promene == 0:
        i_faza = (i_faza + 1) % br_faza
        do_promene = trajanje_faze[i_faza]
    do_promene -= 1
    
def crtaj():
    prozor.fill(pg.Color("darkgray")) # bojimo pozadinu prozora u sivo
    svetli_crveno, svetli_zuto, svetli_zeleno = svetla_faze[i_faza]
    if svetli_crveno:
        pg.draw.circle(prozor, crvena_ukljucena,  (50,  50), 40)
    else:
        pg.draw.circle(prozor, crvena_iskljucena, (50,  50), 40)
    if svetli_zuto:
        pg.draw.circle(prozor, zuta_ukljucena,    (50, 150), 40)
    else:
        pg.draw.circle(prozor, zuta_iskljucena,   (50, 150), 40)
    if svetli_zeleno:
        pg.draw.circle(prozor, zelena_ukljucena,  (50, 250), 40)
    else:
        pg.draw.circle(prozor, zelena_iskljucena, (50, 250), 40)

# -*- acsection: after-main -*-

kraj = False
sat = pg.time.Clock()  # sat koji određuje broj frejmova u sekundi

while not kraj:
    novi_frejm()
    crtaj()
    pg.display.update()
    
    # proveravamo da li je korisnik isključio prozor
    for dogadjaj in pg.event.get():
        if dogadjaj.type == pg.QUIT:
            kraj = True
            
    # pauziramo do sledeceg frejma
    sat.tick(2)
pg.quit() # isključujemo rad biblioteke PyGame

