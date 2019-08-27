# -*- acsection: general-init -*-
import pygame as pg, petljapg
prozor = petljapg.open_window(800, 600, "Сандуци 1")
# -*- acsection: main -*-

sanduk_slika = pg.image.load("box.png")  # slika drveta

prozor.fill(pg.Color("lightgray")) # bojimo pozadinu ekrana u svetlo sivo

for i in range(4):
    prozor.blit(sanduk_slika, (60+120*i, 400))

# -*- acsection: after-main -*-
petljapg.wait_loop()
