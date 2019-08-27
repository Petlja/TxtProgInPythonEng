import pygame as pg, petljapg
(sirina, visina) = (600, 400)
prozor = petljapg.open_window(sirina, visina, "Превлачење мишем")

jabuka_slika = pg.image.load("apple.png")  # učitavamo sliku jabuke
jabuka_poz = (300, 200)
prevlacenje = False        # da li se jabuka trenutno prevlaci

def mis_je_na_slici(mis_poz):
    x, y = mis_poz
    x0, y0 = jabuka_poz # gornje levo teme
    dx, dy = jabuka_slika.get_width(), jabuka_slika.get_height() # velicina slike
    return x0 <= x and x <= x0 + dx and y0 <= y and y <= y0 + dy

def nov_frejm():
    prozor.fill(pg.Color("darkgreen"))      # bojimo pozadinu ekrana u zeleno
    prozor.blit(jabuka_slika, jabuka_poz)   # crtamo jabuku

def obradi_dogadjaj(dogadjaj):
    global jabuka_poz, prevlacenje
    if dogadjaj.type == pg.MOUSEBUTTONDOWN:     # pritisnuto je dugme miša
        if mis_je_na_slici(dogadjaj.pos):       # ako se miš nalazi na jabuci
            prevlacenje = True                  # započinjemo prevlačenje
    elif dogadjaj.type == pg.MOUSEBUTTONUP:     # otpušteno je dugme miša
        prevlacenje = False                     # završavamo prevlačenje
    elif dogadjaj.type == pg.MOUSEMOTION:       # miš je pomeren
        if prevlacenje:                         # ako je u toku prevlačenje
            mis_x, mis_y = dogadjaj.pos
            # racunamo gornji levi ugao слике tako da centar jabuke bude na mestu miša
            x = mis_x - jabuka_slika.get_width() // 2
            y = mis_y - jabuka_slika.get_height() // 2
            jabuka_poz = (x, y)

petljapg.frame_loop(30, nov_frejm, obradi_dogadjaj)
