# -*- acsection: general-init -*-
import math, random
import pygame as pg

pg.init()   # uključujemo rad biblioteke PyGame
pg.display.set_caption("Пронађи сакривену тачку")  # otvaramo prozor
(visina, sirina) = (400, 400)
prozor = pg.display.set_mode((visina, sirina))

# -*- acsection: main -*-

# rastojanje između dve tačke (zadate parovima koordinata)

def rastojanje(A, B):
    (x1, y1) = A
    (x2, y2) = B
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def postavi_novu_tacku():
    global tacka, boje, prikazi_tacku
    
    tacka = (random.randint(0, sirina), random.randint(0, visina)) # nasumična tačka na ekranu
    prikazi_tacku = False                         # u početku je ona skrivena
    maks_r = max(rastojanje(tacka, (0, 0)),       # najveće rastojanje od
                 rastojanje(tacka, (0, visina)),  # nepoznate tačke do
                 rastojanje(tacka, (sirina, 0)),  # bilo koje tačke na ekranu
                 rastojanje(tacka, (sirina, visina)))
    # prelomna rastojanja i boje koje im odgovaraju
    # izmedju ovih rastojanja, boja bira izmedju prelomnih boja
    boje = (
        (-0.0001 * maks_r, (255, 0, 0)   ), # crvena
        (0.3     * maks_r, (255, 255, 0) ), # zuta
        (0.6     * maks_r, (0, 255, 255) ), # rezeda
        (1.0001  * maks_r, (0, 0, 255)   )  # plava
    )

def boja(d):
    # odredimo prelomna rastojanja d0 i d1, izmedju kojih je dato rastojanje d
    # i odgovarajuce prelomne boje (boja0 i boja1)
    for d1, boja1 in boje:
        if d1 > d: 
            break
        d0 = d1
        boja0 = boja1
        
    # odredimo boju izmedju prelomnih boja, koja odgovara rastojanju d
    r0, g0, b0 = boja0
    r1, g1, b1 = boja1
    k = (d - d0) / (d1 - d0)
    return(r0 + k*(r1-r0), g0 + k*(g1-g0), b0 + k*(b1-b0))

def crtanje():
    r = rastojanje(tacka, mis)  # rastojanje od nepoznate tačke do miša
    b = boja(r)
    prozor.fill(b)              # bojimo prozor
    if prikazi_tacku:           # ako je odabrano da se prikazuje nepoznata tačka, prikazujemo je
        pg.draw.circle(prozor, pg.Color("black"), tacka, 3)

def obradi_dogadjaj(dogadjaj):
    global mis, tacka, prikazi_tacku
    if dogadjaj.type == pg.MOUSEBUTTONDOWN:    # pritisak dugmeta miša
        if dogadjaj.button == 1:               #    levo dugme
            prikazi_tacku = not prikazi_tacku  #       menjamo prikaz nepoznate tačke
            return True                        #      treba ponovo iscrtati ekran
        elif dogadjaj.button == 3:             #    desno dugme
            postavi_novu_tacku()               #      biramo novu nepoznatu tačku
            return True                        #      treba ponovo iscrtati ekran
    elif dogadjaj.type == pg.MOUSEMOTION:      # pomeranje miša
        mis = dogadjaj.pos                     #    pamtimo poziciju miša
        return True                            #   treba ponovo iscrtati ekran
    return False                               # ne treba ponovo iscrtavati ekran
    
mis = (0, 0)
postavi_novu_tacku()

# -*- acsection: after-main -*-
treba_crtati = True
kraj = False
while not(kraj):
    if treba_crtati:
        crtanje()
        pg.display.update()  # ažuriramo prikaz sadržaja ekrana
        treba_crtati = False # ne treba crtati do daljnjeg

    dogadjaj = pg.event.wait()      # čekamo naredni dogadjaj
    if dogadjaj.type == pg.QUIT:    # isključivanje prozora
        kraj = True
    else:
        treba_crtati = obradi_dogadjaj(dogadjaj)

pg.quit()  # isključivanje rada biblioteke PyGame
