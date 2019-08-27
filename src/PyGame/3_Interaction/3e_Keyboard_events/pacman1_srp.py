import pygame as pg, petljapg
br_redova, br_kolona = 10, 10
a = 50 # velicina polja
(sirina, visina) = (a* br_kolona, a * br_redova)
prozor = petljapg.open_window(sirina, visina, "Пакмен")

(lik_red, lik_kol) = (br_redova // 2, br_kolona // 2)

def nov_frejm():
    prozor.fill(pg.Color("black"))   # bojimo prozor u crno

    # bele kuglice
    for x in range(a // 2, sirina, a):
        for y in range(a // 2, visina, a):
            pg.draw.circle(prozor, pg.Color("white"), (x, y), 3)
   
    # crtamo 'lika'
    (x, y) = (lik_kol * a + a//2, lik_red * a + a//2)
    pg.draw.circle(prozor, pg.Color('yellow'), (x, y), a // 3)
    
def obradi_dogadjaj(dogadjaj):
    global lik_red, lik_kol
    if dogadjaj.type == pg.KEYDOWN:
        if dogadjaj.key == pg.K_LEFT and (lik_kol > 0):
            lik_kol -= 1
        if dogadjaj.key == pg.K_RIGHT and (lik_kol < br_kolona-1):
            lik_kol += 1
        if dogadjaj.key == pg.K_UP and (lik_red > 0):
            lik_red -= 1
        if dogadjaj.key == pg.K_DOWN and (lik_red < br_redova-1):  
            lik_red += 1

petljapg.frame_loop(30, nov_frejm, obradi_dogadjaj)

