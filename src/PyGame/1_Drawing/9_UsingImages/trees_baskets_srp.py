# -*- acsection: general-init -*-
import pygame as pg, petljapg
prozor = petljapg.open_window(800, 600, "Јабуке")

# -*- acsection: main -*-

drvo_slika = pg.image.load("tree.png")  # slika drveta
korpa_slika = pg.image.load("basket.png")  # slika korpe
drvece_poz = ((200, 70), (120, 150), (240, 290), (550, 170), (400, 200))

prozor.fill(pg.Color("darkgreen")) # bojimo pozadinu ekrana u tamno zeleno
for drvo_x, drvo_y in drvece_poz:
    korpa_x = drvo_x  + drvo_slika.get_width() - korpa_slika.get_width()
    korpa_y = drvo_y + drvo_slika.get_height() - korpa_slika.get_height()
    prozor.blit(drvo_slika, (drvo_x, drvo_y))
    prozor.blit(korpa_slika, (korpa_x, korpa_y))
    
# -*- acsection: after-main -*-
petljapg.wait_loop()
