# -*- acsection: general-init -*-
import pygame as pg
import math

pg.init() # inicijalizujemo biblioteku PyGame
pg.display.set_caption("Сунце")

# otvaramo prozor
(sirina, visina) = (800, 600)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

BOJA_SUNCA = (247, 242, 81)
BOJA_NEBA = (153, 217, 234)
BOJA_TRAVE = (0, 50, 18)

horizont_y = visina / 2
putanja_sunca_x0 = 0.5 * sirina
putanja_sunca_y0 = 0.6 * visina
putanja_sunca_r = 0.4 * visina
sunce_r = int(0.1 * visina)
sunce_ugao = math.pi
promena_ugla_za_minut = 2*math.pi / (60 * 24)  # 24 * 60 minuta ~ 2*pi radijana

def novi_frejm():
    global sunce_ugao, sunce_x, sunce_y # ove vrednosti izracunavamo
    sunce_ugao += 5 * promena_ugla_za_minut # 1 frejm simulira 5 minuta 'kretanja' sunca
    sunce_x = putanja_sunca_x0 + putanja_sunca_r * math.cos(sunce_ugao)
    sunce_y = putanja_sunca_y0 + putanja_sunca_r * math.sin(sunce_ugao)
    
def crtaj():
    pg.draw.rect(prozor, BOJA_NEBA, (0, 0, sirina, horizont_y)) # nebo
    pg.draw.circle(prozor, BOJA_SUNCA, (int(sunce_x), int(sunce_y)), sunce_r) # sunce
    pg.draw.rect(prozor, BOJA_TRAVE, (0, horizont_y, sirina, visina - horizont_y)) # trava
        
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
    sat.tick(10)
    
pg.quit()
