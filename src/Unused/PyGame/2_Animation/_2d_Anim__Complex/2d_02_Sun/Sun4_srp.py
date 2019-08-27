# -*- acsection: general-init -*-
import pygame as pg
import math

pg.init() # inicijalizujemo biblioteku PyGame
pg.display.set_caption("Сунце")

# otvaramo prozor
(sirina, visina) = (800, 600)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

BOJA_NEBA_DAN = (153, 217, 234)
BOJA_NEBA_NOC = (0, 0, 80)
BOJA_TRAVE = (0, 50, 18)

horizont_y = visina / 2
putanja_sunca_x0 = 0.5 * sirina
putanja_sunca_y0 = 0.6 * visina
putanja_sunca_r = 0.4 * visina
sunce_r = int(0.1 * visina)
vreme = 6 # u satima od 0 do 23.999999
font = pg.font.SysFont("Arial", 40)     # font kojim će biti prikazan tekst

def srednja_boja(boja0, boja1, sredina):
    r0, g0, b0 = boja0
    r1, g1, b1 = boja1
    return (r0 + sredina * (r1-r0), g0 + sredina * (g1-g0), b0 + sredina * (b1-b0))

def novi_frejm():
    # ove vrednosti izracunavamo
    global vreme, sunce_x, sunce_y, sunce_boja, nebo_boja
    
    vreme += 5/60 # 1 frejm simulira 5 minuta 'kretanja' sunca
    if vreme >= 20:
        vreme = 5.0 # preskoci noc, nije bas zanimljivo
    sunce_ugao = (0.25 + vreme / 24) * 2 * math.pi
    sunce_x = putanja_sunca_x0 + putanja_sunca_r * math.cos(sunce_ugao)
    sunce_y = putanja_sunca_y0 + putanja_sunca_r * math.sin(sunce_ugao)
    
    vidljivi_deo_sunca = (1 + (horizont_y - sunce_y) / sunce_r) / 2
    vidljivi_deo_sunca = min(max(vidljivi_deo_sunca, 0), 1)
    sunce_boja = (255, int(255 * vidljivi_deo_sunca), 0)
    nebo_boja = srednja_boja(BOJA_NEBA_NOC, BOJA_NEBA_DAN, vidljivi_deo_sunca)
    
def crtaj():
    pg.draw.rect(prozor, nebo_boja, (0, 0, sirina, horizont_y)) # nebo
    pg.draw.circle(prozor, sunce_boja, (int(sunce_x), int(sunce_y)), sunce_r) # sunce
    pg.draw.rect(prozor, BOJA_TRAVE, (0, horizont_y, sirina, visina - horizont_y)) # trava
    
    sati = int(vreme)
    minuta = int(round(60 * (vreme - sati)))
    vreme_string = str(sati).rjust(2, "0") + ":" + str(minuta).rjust(2, "0")
    vreme_slika = font.render(vreme_string, True, pg.Color("orange"))
    prozor.blit(vreme_slika, (10, 10))

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
