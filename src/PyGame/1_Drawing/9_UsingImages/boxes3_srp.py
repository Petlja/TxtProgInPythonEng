# -*- acsection: general-init -*-
import pygame as pg, petljapg
prozor = petljapg.open_window(800, 600, "Сандуци 3")
# -*- acsection: main -*-

sanduk_slika = pg.image.load("box.png")  # slika drveta

prozor.fill(pg.Color("lightgray")) # bojimo pozadinu ekrana u svetlo sivo

for ix in range(4):
    for iy in range(ix+1):
        prozor.blit(sanduk_slika, (60+120*ix, 400-95*iy))

# -*- acsection: after-main -*-
petljapg.wait_loop()
