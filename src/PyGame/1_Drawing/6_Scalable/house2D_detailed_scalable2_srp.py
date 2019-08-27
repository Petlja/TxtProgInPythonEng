# -*- acsection: general-init -*-
import pygame as pg, petljapg
prozor = petljapg.open_window(400, 300, "Кућа")

# -*- acsection: main -*-
prozor.fill(pg.Color("darkgreen")) # bojimo pozadinu ekrana u tamno zeleno

def kuca(x, y, a, boja_zidova):
    pg.draw.polygon(prozor, pg.Color("red"), [(x, y), (x+7*a, y-5*a), (x+14*a, y)]) # krov
    pg.draw.rect(prozor, boja_zidova,       (x,        y,      14*a, 10*a)) # kuca
    pg.draw.rect(prozor, pg.Color("brown"), (x +  1*a, y + 2*a, 3*a,  3*a)) # levi prozor
    pg.draw.rect(prozor, pg.Color("brown"), (x + 10*a, y + 2*a, 3*a,  3*a)) # desni prozor
    pg.draw.rect(prozor, pg.Color("brown"), (x +  5*a, y + 3*a, 4*a,  7*a)) # vrata

kuca(278, 110, 1, (211, 207, 169))
kuca(231, 119, 2, (217, 211, 164))
kuca(174, 130, 3, (228, 221, 152))
kuca(112, 142, 4, (231, 222, 150))
kuca( 18, 160, 6, (240, 230, 140))

# -*- acsection: after-main -*-
petljapg.wait_loop()
