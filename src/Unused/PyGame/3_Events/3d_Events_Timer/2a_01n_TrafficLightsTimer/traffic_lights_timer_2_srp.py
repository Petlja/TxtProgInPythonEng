# -*- acsection: general-init -*-
import pygame as pg

# ukljucivanje rada biblioteke PyGame
pg.init()

# postavljamo naslov prozora
pg.display.set_caption("Семафор")

# ukljucujemo prozor dimenzije 200x450 piksela
(sirina, visina) = (200, 450)
prozor = pg.display.set_mode((sirina, visina))
prozor.fill(pg.Color("white"))

# -*- acsection: main -*-

# redosled kojim se svetla pale i njihovo trajanje
faze = [
    ((True,  False, False), 3000), # crveno
    ((True,  True,  False), 1000), # crveno-žuto
    ((False, False, True),  4000), # zeleno
    ((False, False, False),  200), # ni jedno
    ((False, False, True),   200), # zeleno
    ((False, False, False),  200), # ni jedno
    ((False, False, True),   200), # zeleno
    ((False, False, False),  200), # ni jedno
    ((False, False, True),   200), # zeleno
    ((False, True,  False), 1000)  # žuto
]
          

i_faza = 0   # redni broj faze koja nastupa

razmak = 10                   # razmak između susednih svetala i između svetla i gornje tj. donje ivice prozora
r = (visina - 4 * razmak) / 6 # poluprečnik svakog svetla (3 prečnika, dva razmaka između svetala i dva razmaka od ivice daju visinu prozora)
cx = sirina // 2              # centar svakog svetla je horizontalno na sredini prozora
cy = (round(r + razmak), round(3*r + 2*razmak), round(5*r + 3*razmak))
boja = (pg.Color('red'), pg.Color('yellow'), pg.Color('green'))
r = round(r)

def crtaj():
    # crtamo semafor
    prozor.fill(pg.Color("black"))        # bojimo pozadinu prozora u crno
    (ukljuceno, trajanje) = faze[i_faza]  # čitamo raspored i trajanje trenutne faze
    for i_svetlo in range(3):
        if ukljuceno[i_svetlo]:           # crtamo svetlo ako je potrebno
            pg.draw.circle(prozor, boja[i_svetlo], (cx, cy[i_svetlo]), r)

def na_otkucaj_tajmera():
    global i_faza                             # otkucao je tajmer i menja se svetlo
    i_faza = (i_faza + 1) % len(faze)         # prelazimo na naredno svetlo
    trajanje = faze[i_faza][1]                # čitamo trajanje naredne faze
    pg.time.set_timer(pg.USEREVENT, trajanje) # zakazujemo sledeći otkucaj tajmera

# -*- acsection: after-main -*-

# zakazujemo prvi otkucaj tajmera na osnovu trajanja prve faze
pg.time.set_timer(pg.USEREVENT, faze[i_faza][1])

# glavna petlja programa
kraj = False
treba_crtati = True
while not kraj:
    if treba_crtati:
        crtaj()               # crtamo semafor
        pg.display.update()   # osvežavamo prikaz sadržaja prozora
    
    dogadjaj = pg.event.wait()    # čekamo na naredni dogadjaj
    if dogadjaj.type == pg.QUIT:  # isključen je prozor
        kraj = True
    elif dogadjaj.type == pg.USEREVENT: # otkucaj tajmera
        na_otkucaj_tajmera()
        treba_crtati = True


pg.quit() # isključujemo rad biblioteke PyGame
