# -*- acsection: general-init -*-
import pygame as pg, petljapg
prozor = petljapg.open_window(300, 300, "Жирафе")
# -*- acsection: main -*-

def crtaj_mnogougao(temena, boja, x0, y0):
    pomerena_temena = []
    for x, y in temena:
        pomerena_temena.append((x+x0, y+y0))
    pg.draw.polygon(prozor, boja, pomerena_temena)

zirafa = [(40, 208), (40, 107), (88, 82), (134, 13), (128, 9), (134, 13), 
    (137, 11), (128, 6), (160, 25), (159, 28), (136, 28), (98, 101),
    (100, 106), (101, 207), (97, 207), (95, 164), (83, 121), (85, 128),
    (54, 128), (55, 119), (44, 165), (44, 208)]
    

# bojimo pozadinu u tamno zeleno
prozor.fill(pg.Color("darkgreen"))


#for (x, y) in ... (dovrsite)
    
# -*- acsection: after-main -*-
petljapg.wait_loop()
