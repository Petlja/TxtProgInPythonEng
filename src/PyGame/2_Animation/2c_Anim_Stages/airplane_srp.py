import pygame as pg, petljapg
(sirina, visina) = (800, 350)
prozor = petljapg.open_window(sirina, visina, "Авион")

sunce_slika = pg.image.load("sun.png")      # slika sunca
avion_slika = pg.image.load("airplane.png") # slika aviona
avion_sirina = avion_slika.get_width()      # sirina slike aviona
avion_visina = avion_slika.get_height()     # visina slike aviona

# položaj aviona - na pocetku sredina leve ivice prozora
(avion_x, avion_y) = (0, (visina - avion_visina)  // 2)
i_frejm = 0
KRAJ_PRVE_FAZE = 20
UKUPNO_FREJMOVA = 40
def nov_frejm():
    global avion_x, avion_y, i_frejm    # menjacemo položaj aviona i brojac frejmova
    i_frejm = (i_frejm + 1) % UKUPNO_FREJMOVA
    if i_frejm < KRAJ_PRVE_FAZE:
        avion_y -= 2  # u prvoj fazi pomeramo avion 1 piksel na gore
    else:
        avion_y += 2  # u drugoj fazi pomeramo avion 1 piksel na dole

    avion_x += 2      # pomeramo avion 1 piksel na desno
    if avion_x > sirina:
        avion_x = -avion_sirina

    prozor.fill(pg.Color("skyblue"))               # bojimo pozadinu u plavo
    prozor.blit(sunce_slika, (0, 0))               # crtamo sunce
    prozor.blit(avion_slika, (avion_x, avion_y))   # crtamo avion

petljapg.frame_loop(50, nov_frejm)
