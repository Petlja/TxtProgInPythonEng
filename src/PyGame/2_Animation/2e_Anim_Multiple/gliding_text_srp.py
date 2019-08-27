import pygame as pg, petljapg

(sirina, visina) = (700, 250)
prozor = petljapg.open_window(sirina, visina, "Прича")
tekst = (
    "Мала деца уче да ходају",
    "тако што почну да ходају.",
    "У почетку често падају,",
    "али устају и настављају",
    "и са временом",
    "постају све боља.",
    "Зашто не бисмо тако учили",
    "и све остале вештине?",
    " "
)

font = pg.font.SysFont("Arial", 40) # font kojim će biti prikazan tekst
MARGINA_GORE_DOLE = 30
VISINA_JEDNOG_REDA = 50
y_pocetka_teksta = 200
i_prvi_vidljivi_red = 0
br_vidljivih_redova = 1

def crtaj():
    prozor.fill(pg.Color("skyblue"))        # bojimo pozadinu
    
    i_red = i_prvi_vidljivi_red
    y = y_pocetka_teksta
    for _ in range(br_vidljivih_redova):
        # gradimo i prikazujemo sliku jednog reda tekstа
        siva = min(230 - y, 192)
        boja = (siva, siva, siva)
        slika_teksta = font.render(tekst[i_red], True, boja)
        prozor.blit(slika_teksta, (20, y)) 
        i_red = (i_red + 1) % len(tekst)
        y += VISINA_JEDNOG_REDA

def nov_frejm():
    global i_prvi_vidljivi_red, y_pocetka_teksta, br_vidljivih_redova
    y_pocetka_teksta -= 1 # ceo tekst klizi 1 piksel gore
    
    # da li je prvi red izasao na gore
    if y_pocetka_teksta < MARGINA_GORE_DOLE:
        i_prvi_vidljivi_red = (i_prvi_vidljivi_red + 1) % len(tekst)
        y_pocetka_teksta += VISINA_JEDNOG_REDA
    
    # da li ima mesta za jos jedan red
    poz_sl_reda = y_pocetka_teksta + VISINA_JEDNOG_REDA * br_vidljivih_redova
    if poz_sl_reda + VISINA_JEDNOG_REDA + MARGINA_GORE_DOLE < visina:
        br_vidljivih_redova += 1
        
    crtaj()

petljapg.frame_loop(30, nov_frejm)
