import pygame as pg, petljapg

(sirina, visina) = (500, 200)
prozor = petljapg.open_window(sirina, visina, "Прича")
tekst = (
    "Ово је једна стара прича",
    "о једном човеку",
    "који је желео",
    "да му неко исприча причу"
)

font = pg.font.SysFont("Arial", 40)     # font kojim će biti prikazan tekst
MARGINA_GORE_DOLE = 10
VISINA_JEDNOG_REDA = 50
y_teksta = 80
i_prvi_vidljivi_red = 0
br_vidljivih_redova = 1

def crtaj():
    prozor.fill(pg.Color("skyblue"))        # bojimo pozadinu
    
    i_red = i_prvi_vidljivi_red
    y = y_teksta
    for _ in range(br_vidljivih_redova):
        # gradimo i prikazujemo sličicu од jednog reda tekstа
        slika_teksta = font.render(tekst[i_red], True, pg.Color("black"))
        prozor.blit(slika_teksta, (20, y)) 
        i_red += 1
        if i_red == len(tekst):
            i_red = 1
        y += VISINA_JEDNOG_REDA

def nov_frejm():
    global i_prvi_vidljivi_red, y_teksta, br_vidljivih_redova
    y_teksta -= 1
    
    # da li je prvi red izasao gore
    if y_teksta < MARGINA_GORE_DOLE:
        y_teksta += VISINA_JEDNOG_REDA
        i_prvi_vidljivi_red += 1
        if i_prvi_vidljivi_red == len(tekst):
            i_prvi_vidljivi_red = 1
        br_vidljivih_redova -= 1
    
    # da li ima mesta za jos jedan red
    poz_sl_reda = y_teksta + VISINA_JEDNOG_REDA * br_vidljivih_redova
    if poz_sl_reda + VISINA_JEDNOG_REDA + MARGINA_GORE_DOLE < visina:
        br_vidljivih_redova += 1
        
    crtaj()

petljapg.frame_loop(15, nov_frejm)
