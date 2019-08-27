# -*- acsection: general-init -*-
import pygame as pg, petljapg
br_redova, br_kolona = 5, 5
a = 50 # velicina polja
(sirina, visina) = (a* br_kolona, a * br_redova)
prozor = petljapg.open_window(sirina, visina, "Укрштене речи")

font = pg.font.SysFont("Arial", 30) # font kojim će biti prikazan tekst
tabla = []
for red in range(br_redova):
    tabla.append([' '] * br_kolona)
    
(okvir_red, okvir_kol) = (0, 0)

# -*- acsection: main -*-
def obradi_dogadjaj(dogadjaj):
    global okvir_red, okvir_kol
    if dogadjaj.type == pg.KEYDOWN:
        if dogadjaj.key == pg.K_LEFT:
            if okvir_kol > 0:
                okvir_kol -= 1
        elif dogadjaj.key == pg.K_RIGHT:
            if okvir_kol < br_kolona-1:
                okvir_kol += 1
        elif dogadjaj.key == pg.K_UP:
            if okvir_red > 0:
                okvir_red -= 1
        elif dogadjaj.key == pg.K_DOWN:
            if okvir_red < br_redova-1:
                okvir_red += 1
        else:
            slovo = dogadjaj.unicode.upper()
            if slovo in ' АБВГДЂЕЖЗИЈКЛЉМНЊОПРСТЋУФХЦЧЏШ':
                tabla[okvir_red][okvir_kol] = slovo
# -*- acsection: after-main -*-

def prikazi_slovo(tekst, red, kol):
    if tekst == ' ':
        d = 6
        kvadrat = (a*kol + d, a*red + d, a - 2*d, a - 2*d)
        pg.draw.rect(prozor, pg.Color("black"), kvadrat)
    else:
        slika_teksta = font.render(tekst, True, pg.Color("black"))
        x = a * kol + (a - slika_teksta.get_width()) // 2
        y = a * red + (a - slika_teksta.get_height()) // 2
        prozor.blit(slika_teksta, (x, y))

def nov_frejm():
    prozor.fill(pg.Color("white"))   # bojimo prozor u belo
    for x in range(0, sirina+1, a): # uspravne linije
        pg.draw.line(prozor, pg.Color("black"), (x, 0), (x, visina), 2)
    for y in range(0, visina+1, a): # vodoravne linije
        pg.draw.line(prozor, pg.Color("black"), (0, y), (sirina, y), 2)

    pg.draw.rect(prozor, pg.Color("blue"), (a*okvir_kol, a*okvir_red, a, a), 4) # okvir

    for red in range(br_redova): # slova
        for kol in range(br_kolona):
            prikazi_slovo(tabla[red][kol], red, kol)
            
petljapg.frame_loop(30, nov_frejm, obradi_dogadjaj)
