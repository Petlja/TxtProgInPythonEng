# -*- acsection: general-init -*-
import pygame as pg, petljapg
prozor = petljapg.open_window(500, 300, "Кућа")

# -*- acsection: main -*-
prozor.fill(pg.Color("darkgreen")) # bojimo pozadinu ekrana u tamno zeleno

def kuca(x, y, boja_zidova):
    pg.draw.polygon(prozor, pg.Color("red"), [(x, y), (x+70, y-50), (x+140, y)]) # krov
    pg.draw.rect(prozor, boja_zidova,       (x,       y,     140, 100)) # kuca
    pg.draw.rect(prozor, pg.Color("brown"), (x +  10, y + 20, 30,  30)) # levi prozor
    pg.draw.rect(prozor, pg.Color("brown"), (x + 100, y + 20, 30,  30)) # desni prozor
    pg.draw.rect(prozor, pg.Color("brown"), (x +  50, y + 30, 40,  70)) # vrata
    
kuca(150,  90, (220, 220, 220))
kuca(220, 130, pg.Color("white"))
kuca(350, 160, (255, 255, 150))
kuca( 50, 150, pg.Color("khaki"))

# -*- acsection: after-main -*-
petljapg.wait_loop()
