# -*- acsection: general-init -*-
import random
import pygame as pg

pg.init()  # inicijalizujemo biblioteku pygame

pg.display.set_caption("Понг")  # otvaramo prozor
(sirina, visina) = (700, 400)
prozor = pg.display.set_mode((sirina, visina))

pg.key.set_repeat(10, 10)   # podešavamo događaje tastature


# funkcija ispisuje dati tekst date veličine, tako da mu je centar u datoj tački
def tekst_centar(x, y, tekst, velicina):
    font = pg.font.SysFont("Arial", velicina)
    tekst = font.render(tekst, True, pg.Color("white"))
    (sirina_teksta, visina_teksta) = (tekst.get_width(), tekst.get_height())
    (x, y) = (x - sirina_teksta / 2, y - visina_teksta / 2)
    prozor.blit(tekst, (x, y))

# -*- acsection: main -*-

# nasimično određena brzina po x-koordinati
def nasumicna_brzina_x():
    return random.choice([-2, 2])

# nasimično određena brzina po y-koordinati
def nasumicna_brzina_y():
    return random.randint(-3, 3)

# nasimično određena brzina po obe koordinate
def nasumicna_brzina():
    vx = nasumicna_brzina_x()
    vy = nasumicna_brzina_y()
    return (vx, vy)

margina = 100                                          # udaljenost reketa od leve tj. desne ivice prozora
debljina_reketa = 10                                   # debljina reketa
duzinaL = 50                                           # dužina levog reketa
(xL, yL) = (margina, visina // 2)                      # pozicija centra levog reketa
brzinaL = 5                                            # brzina levog reketa
duzinaD = 50                                           # dužina desnog reketa
(xD, yD) = (sirina - margina, visina // 2)             # pozicija centra desnog reketa
brzinaD = 5                                            # brzina desnog reketa
(loptica_x, loptica_y) = (sirina // 2, visina // 2)    # pozicija centra loptice
(vx, vy) = nasumicna_brzina()                          # brzina loptice (u smeru x i y ose)

poeniL = 0                                             # broj poena levog igrača
poeniD = 0                                             # broj poena desnog igrača

def crtaj():
    prozor.fill(pg.Color("black"))                                                     # bojimo pozadinu u crno
    pg.draw.line(prozor, pg.Color("white"),                                            # crtamo levi reket
                 (xL, yL - duzinaL // 2), (xL, yL + duzinaL // 2), debljina_reketa)
    pg.draw.line(prozor, pg.Color("white"),                                            # crtamo desni reket
                 (xD, yD - duzinaD // 2), (xD, yD + duzinaD // 2), debljina_reketa)

    pg.draw.circle(prozor, pg.Color("white"),
                   (round(loptica_x), round(loptica_y)), 5)

    # crtamo mrežicu
    x = sirina // 2
    y = 0
    duzina_linijice = 30
    while y < visina:
        pg.draw.line(prozor, pg.Color("white"),
                     (x, y), (x, y + duzina_linijice), 2)
        y += 1.5 * duzina_linijice

    tekst_centar(sirina // 2 - 50, 50, str(poeniL), 40)       # ispisujemo broj poena levog igrača
    tekst_centar(sirina // 2 + 50, 50, str(poeniD), 40)       # ispisujemo broj poena desnog igrača

def obradi_dogadjaj(dogadjaj):
    global yL, yD
    if dogadjaj.type == pg.KEYDOWN:       # pritisnut je taster na tastaturi
        if dogadjaj.key == pg.K_p:        #   taster p diže desni reket
            yD -= brzinaD
        elif dogadjaj.key == pg.K_l:      #   taster l spušta desni reket
            yD += brzinaD
        elif dogadjaj.key == pg.K_q:      #   taster q diže levi reket
            yL -= brzinaL
        elif dogadjaj.key == pg.K_a:      #   taster a spušta levi reket
            yL += brzinaL

# provera da li tačka (x, y) pripada pravougaoniku sa centrom u (cx, cy), širine s i visine v
def tacka_u_pravougaoniku(x, y, cx, cy, s, v):
    return cx - s // 2 <= x and x <= cx + s // 2 and\
           cy - v // 2 <= y and y <= cy + v // 2

def novi_frejm():
    global loptica_x, loptica_y, vx, vy, poeniL, poeniD

    # pomeramo lopticu
    loptica_x += vx
    loptica_y += vy

    # odbijanje od gornje i donje ivice prozora
    if loptica_y >= visina or loptica_y <= 0:
        vy = -vy

    # provera sudara sa levim reketom
    if tacka_u_pravougaoniku(loptica_x, loptica_y, xL, yL, debljina_reketa, duzinaL):
        vx = -vx                               # loptica horizontalno menja smer, a vertikalno se odbija nasumično
        vy = nasumicna_brzina_y()
        loptica_x = xL + debljina_reketa // 2  # izbacujemo je van reketa

    # provera sudara sa desnim reketom
    if tacka_u_pravougaoniku(loptica_x, loptica_y, xD, yD, debljina_reketa, duzinaD):
        vx = -vx                               # loptica horizontalno menja smer, a vertikalno se odbija nasumično
        vy = nasumicna_brzina_y()
        loptica_x = xD - debljina_reketa // 2  # izbacujemo je van reketa

    # provera da li je loptica ispala iza levog reketa
    if loptica_x < xL - margina // 2:
        loptica_x = sirina // 2            # vraćamo je na sredinu
        (vx, vy) = nasumicna_brzina()      # i nasumično joj određujemo brzinu
        poeniD += 1                        # uvećavamo poene desnog igrača

    # provera da li je loptica ispala iza desnog reketa
    if loptica_x > xD + margina // 2:
        loptica_x = sirina // 2            # vraćamo je na sredinu
        (vx, vy) = nasumicna_brzina()      # i nasumično joj određujemo brzinu
        poeniL += 1                        # uvećavamo poene levog igrača

# -*- acsection: after-main -*-

kraj = False
sat = pg.time.Clock()  # sat koji određuje broj frejmova u sekundi
while not kraj:
    # crtamo i ažuriramo sadržaj prozora
    crtaj()
    pg.display.update()

    # proveravamo da li je korisnik isključio prozor
    for dogadjaj in pg.event.get():
        if dogadjaj.type == pg.QUIT:
            kraj = True
        else:
            obradi_dogadjaj(dogadjaj)

    # pauziramo do sledeceg frejma
    sat.tick(25)
    novi_frejm()

pg.quit() # isključujemo rad biblioteke PyGame
