import pygame as pg, petljapg, random
(sirina, visina) = (400, 400)
prozor = petljapg.open_window(sirina, visina, "Лептир прати миша")

leptir_slike = [pg.image.load("butterfly1.png"), pg.image.load("butterfly2.png")]
i_frejm = 0
frejmova_po_slici = 10

def nov_frejm():
    global i_frejm
    i_frejm += 1
    i_slika = (i_frejm % (len(leptir_slike) * frejmova_po_slici)) // frejmova_po_slici
    (mis_x, mis_y) = pg.mouse.get_pos()

    prozor.fill(pg.Color("white"))
    slika = leptir_slike[i_slika] # slika koja se prikazuje
    # prikazujemo sliku centrirano
    (x, y) = (mis_x - slika.get_width() / 2, mis_y - slika.get_height() / 2)
    prozor.blit(slika, (x, y))

petljapg.frame_loop(5 * frejmova_po_slici, nov_frejm)
