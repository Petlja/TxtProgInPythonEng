import pygame as pg, petljapg
(sirina, visina) = (150, 150)
prozor = petljapg.open_window(sirina, visina, "Кртица")

slike = []   # niz koji ce da sadrzi slike
for i in range(1, 11): # učitavamo u listu slike mole1.png, ..., mole10.png
    naziv_slike = "mole" + str(i) + ".png"  # gradimo naziv slike od delova
    slike.append(pg.image.load(naziv_slike))

braon = (60, 42, 3)
Y_HORIZONT = 125
ZEMLJA = (0, Y_HORIZONT, sirina, visina - Y_HORIZONT) # deo slike ispod horizonta
i_frejm = 0 # redni broj frejma u sekvenci

def nov_frejm():
    global i_frejm, i_slika
    i_frejm = (i_frejm + 1) % 28 # ukupan broj frejmova je 28
    if i_frejm < 10:
        i_slika = i_frejm        # prva faza - podizanje
    elif i_frejm < 15:
        i_slika = 9              # druga faza - krtica je gore
    elif i_frejm < 25:
        i_slika = 24 - i_frejm   # treca faza - spustanje
    else:
        i_slika = 0              # cetvrta faza - krtica je dole

    prozor.fill(pg.Color("skyblue"))     # bojimo pozadinu prozora u nebo-plavo
    pg.draw.rect(prozor, braon, ZEMLJA)  # bojimo pravougaonik ZEMLJA u braon
    prozor.blit(slike[i_slika], (0, 0))  # prikazujemo sliku

petljapg.frame_loop(10, nov_frejm)
