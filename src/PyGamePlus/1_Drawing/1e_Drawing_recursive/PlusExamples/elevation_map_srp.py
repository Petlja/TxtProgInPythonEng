# -*- acsection: general-init -*-
import pygame as pg
import random

# uključivanje rada biblioteke PyGame
pg.init()
# podešavamo naslov prozora
pg.display.set_caption("Рељеф")
# otvaramo prozor 
(sirina, visina) = (200, 200)
prozor = pg.display.set_mode((sirina, visina))
# -*- acsection: main -*-

visine_i_boje = (
#   (   h, (r, g,  b,  a))
    (-200, (0, 0, 128, 255)), 
    (   0, (0, 0, 255, 255)),
    ( 200, (0, 255, 0, 255)),
    ( 500, (0,  80, 0, 255)),
    (1000, (128, 64, 0, 255)),
    (1500, (255, 255, 255, 255))
)

def racunaj_boju(h):
    if h < visine_i_boje[0][0]: 
        return  pg.Color(*visine_i_boje[0][1]) # vrati prvu boju kao najblizu
    
    for h1, (r1, g1, b1, a1) in visine_i_boje:
        if h < h1:
            q = (h - h0) / (h1 - h0)
            return  pg.Color(round(r0 + (r1-r0)*q),  round(g0 + (g1-g0)*q), round(b0 + (b1-b0)*q), 255)
            
        h0, r0, g0, b0 = h1, r1, g1, b1 # zapamti prethodnu visinu i boju
            
    return pg.Color(*visine_i_boje[-1][1]) # vrati poslednju boju kao najblizu
    
def popuni(x1, y1, dx, dy, h11, h21, h12, h22):
    x2 = x1 + dx
    y2 = y1 + dy
    if dx == 1:
        for y in range(y1, y2):
            prozor.set_at((x1, y), boja.get(h11, (255,255,255)))
        return
    if dy == 1:
        for x in range(x1, x2):
            prozor.set_at((x, y1), boja.get(h11, (255,255,255)))
        return
       
    xm = x1 + dx // 2
    ym = y1 + dy // 2
    h1m = (h11 + h12) // 2
    hm1 = (h11 + h21) // 2
    h2m = (h21 + h22) // 2
    hm2 = (h12 + h22) // 2
    hmm = (h1m + hm1 + h2m + hm2) // 4 + round(random.gauss(0, 0.1*min(dx, dy)))
   
    popuni(x1, y1, dx//2, dy//2, h11, hm1, h1m, hmm)
    popuni(xm, y1, dx-dx//2, dy//2, hm1, h21, hmm, h2m)
    popuni(x1, ym, dx//2, dy-dy//2, h1m, hmm, h12, hm2)
    popuni(xm, ym, dx-dx//2, dy-dy//2, hmm, h2m, hm2, h22)

    
boja = { h : racunaj_boju(h) for h in range(-500, 3800) }

poc_visine = [
    random.randint(-400, 0), 
    random.randint(-100, 500), 
    random.randint(600, 1200), 
    random.randint(1100, 2500)
]
random.shuffle(poc_visine)

popuni(0, 0, sirina, visina, *poc_visine)

# -*- acsection: after-main -*-
# ažuriramo prikaz sadržaja ekrana
pg.display.update()

# čekamo da korisnik isključi prozor
while pg.event.wait().type != pg.QUIT:
    pass
    
# isključivanje rada biblioteke PyGame
pg.quit()
