# -*- acsection: general-init -*-
import pygame as pg, random

pg.init()   # uključujemo rad biblioteke PyGame

pg.display.set_caption("Превлачење мишем") 

# otvaramo prozor
(sirina, visina) = (600, 400)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

korpa_slika  = pg.image.load("basket.png") # učitavamo sliku korpe
jabuka_slika = pg.image.load("apple.png")  # učitavamo sliku jabuke
scena_slika = pg.image.load("drag_scene.png")   # učitavamo sliku scene
pozicije_jabuka = [(random.randint(50, 200), random.randint(80, 130)) for i in range(5)]
korpa_poz = (300, 200)
i_jabuka = -1             # koja jabuka se trenutno prevlaci (-1 znaci nijedna)

def mis_je_na_slici(mis_poz, slika_poz, slika):
    x, y = mis_poz
    x0, y0 = slika_poz # gornje levo teme
    dx, dy = slika.get_width(), slika.get_height() # velicina slike
    return x0 <= x and x <= x0 + dx and y0 <= y and y <= y0 + dy

def crtanje():    
    prozor.blit(scena_slika, (0, 0)) # crtamo scenu    
    prozor.blit(korpa_slika, korpa_poz) # crtamo scenu    
    for jabuka_poz in pozicije_jabuka: # crtamo jabuke
        prozor.blit(jabuka_slika, jabuka_poz)

def obradi_dogadjaj(dogadjaj):
    global pozicije_jabuka, i_jabuka, kraj
    treba_ctrati = False
    if dogadjaj.type == pg.MOUSEBUTTONDOWN:     # pritisnuto je dugme miša
        for i, poz_jabuke in enumerate(pozicije_jabuka):
            # ako se miš nalazi na nekoj od jabuka
            if mis_je_na_slici(dogadjaj.pos, poz_jabuke, jabuka_slika):
                i_jabuka = i                    # započinjemo prevlačenje
    elif dogadjaj.type == pg.MOUSEBUTTONUP:     # otpušteno je dugme miša
        if mis_je_na_slici(dogadjaj.pos, korpa_poz, korpa_slika):
            del pozicije_jabuka[i_jabuka]
            if len(pozicije_jabuka) == 0:
                kraj = True
            else:
                treba_ctrati = True             # ponovo iscrtavamo scenu
        i_jabuka = -1                           # završavamo prevlačenje
    elif dogadjaj.type == pg.MOUSEMOTION:       # miš je pomeren
        if i_jabuka >= 0:                       # ako je u toku prevlačenje
            # postavljamo jabuku (gornji levi ugao) tako da je centar na mestu miša
            mis_x, mis_y = dogadjaj.pos
            dx = jabuka_slika.get_width() // 2
            dy = jabuka_slika.get_height() // 2
            pozicije_jabuka[i_jabuka] = (mis_x - dx, mis_y - dy)
            treba_ctrati = True                 # ponovo iscrtavamo scenu
    return treba_ctrati

# -*- acsection: after-main -*-
treba_crtati = True
kraj = False
while not kraj:
    if treba_crtati:    # ako je potrebno nacrtati lopticu
        crtanje()
        pg.display.update()        # ažuriramo prikaz sadržaja prozora
        treba_crtati = False

    dogadjaj = pg.event.wait()     # čekamo naredni događaj
    if dogadjaj.type == pg.QUIT:   # isključivanje prozora
        kraj = True
    else:
        treba_crtati = obradi_dogadjaj(dogadjaj)

pg.quit()  # isključujemo rad biblioteke PyGame
