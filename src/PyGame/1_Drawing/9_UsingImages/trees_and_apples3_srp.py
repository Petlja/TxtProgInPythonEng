# -*- acsection: general-init -*-
import pygame as pg, petljapg
prozor = petljapg.open_window(800, 600, "Јабуке")
# -*- acsection: main -*-

drvo_slika = pg.image.load("tree.png")  # slika drveta

prozor.fill(pg.Color("darkgreen")) # bojimo pozadinu ekrana u tamno zeleno
for drvo_x, drvo_y in ((200, 70), (120, 150), (240, 290), (550, 170), (400, 200)):
    prozor.blit(drvo_slika, (drvo_x, drvo_y))

# -*- acsection: after-main -*-
petljapg.wait_loop()
