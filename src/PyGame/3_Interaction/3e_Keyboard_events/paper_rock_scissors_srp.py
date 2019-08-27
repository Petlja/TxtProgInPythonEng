import pygame as pg, petljapg, random
(sirina, visina) = (300, 300)
prozor = petljapg.open_window(sirina, visina, "Папир, камен, маказе")

PAPIR, KAMEN, MAKAZE = 0, 1, 2
slike = [
    pg.image.load("paper.png"), 
    pg.image.load("rock.png"), 
    pg.image.load("scissors.png")
]
x_slike = sirina // 4 - slike[0].get_width() // 2
y_slike = visina // 2 - slike[0].get_height() // 2

# znacenje elemenata u listama covek i racunar
IME, IZBOR, POENI, X_SL, Y_SL, X_TEKST, Y_TEKST = 0, 1, 2, 3, 4, 5, 6
covek =   ["Човек",   -1, 0, x_slike,             y_slike,         0, 0]
racunar = ["Рачунар", -1, 0, x_slike + sirina//2, y_slike, sirina//2, 0]
font = pg.font.SysFont("Arial", 20)

def crtaj_igraca(igrac):
    if igrac[IZBOR] >= 0:
        prozor.blit(slike[igrac[IZBOR]], (igrac[X_SL], igrac[Y_SL]))
    tekst = igrac[IME] + ": " + str(igrac[POENI])
    slika_teksta = font.render(tekst, True, pg.Color("black"))
    prozor.blit(slika_teksta, (igrac[X_TEKST], igrac[Y_TEKST]))
    
def nov_frejm():
    prozor.fill(pg.Color("white"))
    crtaj_igraca(covek)
    crtaj_igraca(racunar)
    
def obradi_dogadjaj(dogadjaj):
    global covek, racunar
    if dogadjaj.type == pg.KEYDOWN:
        pkm = {pg.K_p : PAPIR, pg.K_k : KAMEN, pg.K_m : MAKAZE}
        if dogadjaj.key in pkm.keys():
            covek[IZBOR] = pkm[dogadjaj.key]
            racunar[IZBOR] = random.randint(0, 2)
            if racunar[IZBOR] == (covek[IZBOR] + 1) % 3:
                covek[POENI] += 1
            elif covek[IZBOR] == (racunar[IZBOR] + 1) % 3:
                racunar[POENI] += 1
    
petljapg.frame_loop(15, nov_frejm, obradi_dogadjaj)
