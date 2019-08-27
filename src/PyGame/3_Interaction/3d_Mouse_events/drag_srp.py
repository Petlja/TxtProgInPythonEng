import pygame as pg, petljapg, random
(sirina, visina) = (600, 400)
prozor = petljapg.open_window(sirina, visina, "Превлачење мишем")

korpa_slika  = pg.image.load("basket.png") # učitavamo sliku korpe
jabuka_slika = pg.image.load("apple.png")  # učitavamo sliku jabuke
scena_slika = pg.image.load("drag_scene.png")   # učitavamo sliku scene
pozicije_jabuka = []
for i in range(5):
    pozicije_jabuka.append((random.randint(50, 200), random.randint(80, 130)))
korpa_poz = (300, 200)
i_jabuka = -1             # koja jabuka se trenutno prevlaci (-1 znaci nijedna)
kraj = False

def mis_je_na_slici(mis_poz, slika_poz, slika):
    x, y = mis_poz
    x0, y0 = slika_poz # gornje levo teme
    dx, dy = slika.get_width(), slika.get_height() # velicina slike
    return x0 <= x and x <= x0 + dx and y0 <= y and y <= y0 + dy

def nov_frejm():    
    prozor.blit(scena_slika, (0, 0)) # crtamo scenu
    if not kraj:
        prozor.blit(korpa_slika, korpa_poz) # crtamo korpu
        for jabuka_poz in pozicije_jabuka: # crtamo jabuke
            prozor.blit(jabuka_slika, jabuka_poz)

def obradi_dogadjaj(dogadjaj):
    global pozicije_jabuka, i_jabuka, kraj
    if dogadjaj.type == pg.MOUSEBUTTONDOWN:     # pritisnuto je dugme miša
        for i in range(len(pozicije_jabuka)):
            # ako se miš nalazi na nekoj od jabuka
            if mis_je_na_slici(dogadjaj.pos, pozicije_jabuka[i], jabuka_slika):
                i_jabuka = i                    # započinjemo prevlačenje
                
    elif dogadjaj.type == pg.MOUSEBUTTONUP:     # otpušteno je dugme miša
        if mis_je_na_slici(dogadjaj.pos, korpa_poz, korpa_slika):
            del pozicije_jabuka[i_jabuka]
            if len(pozicije_jabuka) == 0:
                kraj = True
        i_jabuka = -1                           # završavamo prevlačenje
        
    elif dogadjaj.type == pg.MOUSEMOTION:       # miš je pomeren
        if i_jabuka >= 0:                       # ako je u toku prevlačenje
            # racunamo poziciju jabuke (gornji levi ugao слике) 
            # tako da centar jabuke bude na mestu miša
            mis_x, mis_y = dogadjaj.pos
            x = mis_x - jabuka_slika.get_width() // 2
            y = mis_y - jabuka_slika.get_height() // 2
            pozicije_jabuka[i_jabuka] = (x, y)

petljapg.frame_loop(30, nov_frejm, obradi_dogadjaj)
