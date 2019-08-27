import pygame as pg, petljapg

br_slika = 8
slike = []   # niz koji ce da sadrzi slike
for i in range(1, br_slika+1): # učitavamo u listu slike running1.png, ..., running8.png
    naziv_slike = "running" + str(i) + ".png"  # gradimo naziv slike od delova
    slike.append(pg.image.load(naziv_slike))

# podesavamo da prozor bude iste velicine kao i ucitana slika
(sirina, visina) = (slike[0].get_width(), slike[0].get_height())
prozor = petljapg.open_window(sirina, visina, "Трчање")

indeks_slike = 0 # redni broj slike koju cemo prikazati

def nov_frejm():
    global indeks_slike
    indeks_slike = indeks_slike + 1 # prelazimo na sledecu sliku
    if indeks_slike == br_slika:    # ako nema sledece slike ...
        indeks_slike = 0            # vracamo se na prvu sliku
    prozor.blit(slike[indeks_slike], (0, 0))

petljapg.frame_loop(15, nov_frejm)
