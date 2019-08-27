# -*- acsection: general-init -*-
import pygame as pg, petljapg
prozor = petljapg.open_window(800, 600, "Јабуке")

# -*- acsection: main -*-
drvo_slika = pg.image.load("tree.png")  # slika drveta
jabuka_slika = pg.image.load("apple_small.png")  # slika jabuke
korpa_slika = pg.image.load("basket.png")  # slika korpe
jabuke_na_drvetu_poz = ((43,191), (61, 158), (124, 145), (134, 175), (160, 180))
jabuke_u_korpi_poz = ((15, 38), (60, 41), (22, 43), (49, 45), (34, 48))
drvece_poz = ((200, 70), (120, 150), (240, 290), (550, 170), (400, 200))

def drvo_korpa_jabuke(drvo_x, drvo_y):
    korpa_x = drvo_x  + drvo_slika.get_width() - korpa_slika.get_width()
    korpa_y = drvo_y + drvo_slika.get_height() - korpa_slika.get_height()
    prozor.blit(drvo_slika, (drvo_x, drvo_y))
    prozor.blit(korpa_slika, (korpa_x, korpa_y))
    for x, y in jabuke_na_drvetu_poz:
        prozor.blit(jabuka_slika, (drvo_x + x, drvo_y + y))
    for x, y in jabuke_u_korpi_poz:
        prozor.blit(jabuka_slika, (korpa_x + x, korpa_y + y))
    
prozor.fill(pg.Color("darkgreen")) # bojimo pozadinu ekrana u tamno zeleno
for drvo_x, drvo_y in drvece_poz:
    drvo_korpa_jabuke(drvo_x, drvo_y)
    
# -*- acsection: after-main -*-
petljapg.wait_loop()
