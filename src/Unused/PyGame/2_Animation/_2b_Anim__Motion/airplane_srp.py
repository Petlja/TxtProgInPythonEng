import pygame as pg, petljapg
(sirina, visina) = (800, 350)
prozor = petljapg.init(sirina, visina, "Авион")

sunce_slika = pg.image.load("sun.png")   # slika sunca
avion_slika = pg.image.load("airplane.png")   # slika aviona
avion_visina = avion_slika.get_height()    # visina slike aviona

# položaj aviona - na pocetku u donjem levom uglu prozora
(avion_x, avion_y) = (0, visina - avion_visina) 
avion_dy = -1   # promena visine aviona - avion se prvo diže

def nov_frejm():
    global avion_x, avion_y, avion_dy    # menjamo položaj i smer kretanja aviona
    avion_x += 1                         # pomeramo avion 1 piksel na desno
    avion_y += avion_dy                  # menjamo mu visinu
    if avion_y < 0:                      # ako je dodirnuo vrh ekrana
        avion_dy = 1                     # menjamo mu smer tako da počne da se spušta
    if avion_y + avion_visina == visina: # ako je dodirnuo dno ekrana
        avion_dy = 0                     # prestaje da menja visinu

    prozor.fill(pg.Color("skyblue"))               # bojimo pozadinu u plavo
    prozor.blit(sunce_slika, (0, 0))               # crtamo sunce
    prozor.blit(avion_slika, (avion_x, avion_y))   # crtamo avion

petljapg.run(50, nov_frejm)
