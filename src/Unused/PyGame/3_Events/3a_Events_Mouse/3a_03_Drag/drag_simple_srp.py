# -*- acsection: general-init -*-
import pygame as pg, random

pg.init()   # uključujemo rad biblioteke PyGame

pg.display.set_caption("Превлачење мишем") 

# otvaramo prozor
(sirina, visina) = (600, 400)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

jabuka_slika = pg.image.load("apple.png")  # učitavamo sliku jabuke
jabuka_poz = (300, 200)
prevlacenje = False        # da li se jabuka trenutno prevlaci

def mis_je_na_slici(mis_poz):
    x, y = mis_poz
    x0, y0 = jabuka_poz # gornje levo teme
    dx, dy = jabuka_slika.get_width(), jabuka_slika.get_height() # velicina slike
    return x0 <= x and x <= x0 + dx and y0 <= y and y <= y0 + dy

def crtanje():
    prozor.fill(pg.Color("darkgreen"))          # bojimo pozadinu ekrana u zeleno
    prozor.blit(jabuka_slika, jabuka_poz)   # crtamo jabuku

def obradi_dogadjaj(dogadjaj):
    global jabuka_poz, prevlacenje
    treba_ctrati = False
    if dogadjaj.type == pg.MOUSEBUTTONDOWN:     # pritisnuto je dugme miša
        # ako se miš nalazi na jabuci
        if mis_je_na_slici(dogadjaj.pos):
            prevlacenje = True                  # započinjemo prevlačenje
    elif dogadjaj.type == pg.MOUSEBUTTONUP:     # otpušteno je dugme miša
        prevlacenje = False                     # završavamo prevlačenje
    elif dogadjaj.type == pg.MOUSEMOTION:       # miš je pomeren
        if prevlacenje:                         # ako je u toku prevlačenje
            # postavljamo jabuku (gornji levi ugao) tako da je centar na mestu miša
            mis_x, mis_y = dogadjaj.pos
            dx = jabuka_slika.get_width() // 2
            dy = jabuka_slika.get_height() // 2
            jabuka_poz = (mis_x - dx, mis_y - dy)
            return True                         # ponovo iscrtavamo scenu
    return False                                # nema potrebe da iscrtavamo scenu

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
