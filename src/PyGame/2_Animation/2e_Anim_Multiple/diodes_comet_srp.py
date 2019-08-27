import pygame as pg, petljapg
(sirina, visina) = (400, 100)
prozor = petljapg.open_window(sirina, visina, "Диоде")

MAX_KASNJENJE = 10   # broj dioda koje svetle (takodje broj frejmova tokom kojih dioda svetli)
BROJ_DIODA = 20                                  # ukupan broj dioda na displeju
r = sirina // (2 * BROJ_DIODA)                   # poluprečnik jedne diode
boja = []
for i in range(MAX_KASNJENJE + 1):
    nijansa = 255 * (1 - i/MAX_KASNJENJE)
    boja.append((nijansa, nijansa, nijansa)) # sivi tonovi od bele do crne
    
x = []              # x koordinate centara dioda
for i in range(BROJ_DIODA):
    x.append(r + i * 2 * r)
y = visina // 2     # y koordinata centra svih dioda
i_vodeca_dioda = 0  # redni broj poslednje uključene diode

def nov_frejm():
    global i_vodeca_dioda
    i_vodeca_dioda = (i_vodeca_dioda + 1) % BROJ_DIODA   # prelazimo na narednu diodu

    prozor.fill(pg.Color("black"))               # bojimo pozadinu u crno
    for kasnjenje in range(MAX_KASNJENJE + 1):   # za svaku diodu koja trenutno svetli
        # odredimo redni broj diode koja je uključena pre 'kasnjenje' frejmova
        i_dioda = (i_vodeca_dioda + BROJ_DIODA - kasnjenje) % BROJ_DIODA  
        pg.draw.circle(prozor, boja[kasnjenje], (x[i_dioda], y), r)  # crtamo diodu

petljapg.frame_loop(25, nov_frejm)
