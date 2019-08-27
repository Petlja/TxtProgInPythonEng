# -*- acsection: general-init -*-
import math
import pygame as pg

pg.init()  # započinje rad biblioteke PyGame
pg.display.set_caption("Очи")  # otvaramo prozor
(sirina, visina) = (400, 400)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

# crta oko čiji je centar u (cx, cy), poluprečnik r, a zenica mu je
# postavljena tako da gleda ka pozicji misa (mx, my)
def nacrtaj_oko(cx, cy, r, mx, my):
    pg.draw.circle(prozor, pg.Color("black"), (cx, cy), 2*r, 1)        # crtamo oko
    D = math.sqrt((mx-cx)**2 + (my-cy)**2)          # rastojanje misa od centra oka
    k = r/D if D > r else 1 # k je deo vektora CM za koji se pomeramo od centra oka
    centar_zenice = (cx + round(k*(mx-cx)), cy + round(k*(my-cy))) 
    pg.draw.circle(prozor, pg.Color("black"), centar_zenice, r)     # crtamo zenicu

def crtaj():  # crta oči koje gledaju ka poziciji miša
    prozor.fill(pg.Color("white"))   # bojimo pozadinu prozora u belo
    # crtamo oba oka primenom pomocne funkcije
    nacrtaj_oko(levo_oko_xc, levo_oko_yc, r_zenice, mis_x, mis_y)
    nacrtaj_oko(desno_oko_xc, desno_oko_yc, r_zenice, mis_x, mis_y)

def novi_frejm():
    global mis_x, mis_y
    (mis_x, mis_y) = pg.mouse.get_pos()     # koordinate pozicije miša
    
(prozor_xc, prozor_yc) = (sirina // 2, visina // 2) # centar prozora
r_oka = sirina // 8                                 # poluprečnik oka
r_zenice = r_oka // 2                               # poluprečnik zenice
levo_oko_xc = prozor_xc - 3 * r_zenice              # x koordinata centra levog oka
desno_oko_xc = prozor_xc + 3 * r_zenice             # x koordinata centra desno oka
levo_oko_yc = desno_oko_yc = prozor_yc              # y koordinata centara oba oka
(mis_x, mis_y) = pg.mouse.get_pos()
    
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

    # pauziramo do sledeceg frejma
    sat.tick(50)
    novi_frejm()

pg.quit() # isključujemo rad biblioteke PyGame
