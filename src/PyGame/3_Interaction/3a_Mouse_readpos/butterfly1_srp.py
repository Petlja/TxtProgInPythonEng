import pygame as pg, petljapg, random
(sirina, visina) = (400, 400)
prozor = petljapg.open_window(sirina, visina, "Лептир прати миша")

leptir_slike = [pg.image.load("butterfly1.png"), pg.image.load("butterfly2.png")]
i_slika = 0

def nov_frejm():
    global i_slika
    i_slika = 1 - i_slika # slike se prikazuju naizmenicno 
    prozor.fill(pg.Color("white"))
    (mis_x, mis_y) = pg.mouse.get_pos()
    slika = leptir_slike[i_slika] # slika koja se prikazuje
    # prikazujemo sliku centrirano
    (x, y) = (mis_x - slika.get_width() / 2, mis_y - slika.get_height() / 2)
    prozor.blit(slika, (x, y))

petljapg.frame_loop(5, nov_frejm)
