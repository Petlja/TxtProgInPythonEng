# -*- acsection: general-init -*-
import pygame as pg, petljapg
prozor = petljapg.open_window(300, 300, "Жирафа")

tacke = [(40, 208), (40, 107), (88, 82), (134, 13), (128, 9), (134, 13), 
    (137, 11), (128, 6), (160, 25), (159, 28), (136, 28), (98, 101),
    (100, 106), (101, 207), (97, 207), (95, 164), (83, 121), (85, 128),
    (54, 128), (55, 119), (44, 165), (44, 208)]
    
# -*- acsection: main -*-

# bojimo pozadinu u tamno zeleno
prozor.fill(pg.Color("darkgreen"))

# iscrtavamo mnogougao bojom 'khaki'
pg.draw.polygon(prozor, pg.Color("khaki"), tacke)
    
# -*- acsection: after-main -*-
petljapg.wait_loop()
