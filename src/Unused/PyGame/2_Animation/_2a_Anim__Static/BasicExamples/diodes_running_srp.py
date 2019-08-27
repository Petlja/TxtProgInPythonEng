# -*- acsection: general-init -*-
import pygame as pg

pg.init()  # inicijalizujemo rad biblioteke PyGame
pg.display.set_caption("Диоде")  # otvaramo prozor
(sirina, visina) = (400, 100)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

broj_dioda = 30                     # ukupan broj dioda na displeju
fps = 10                            # broj frejmova po sekundi

sirina_jedne = sirina // broj_dioda # prostor za jednu diodu (u pikselima)
x = [sirina_jedne // 2]             # x koordinata centra prve diode
for i in range(1, broj_dioda):
    x.append(x[-1] + sirina_jedne)  # svaka sledeca dioda je za 'sirina_jedne' desno
y = visina // 2                     # y koordinata centara svih dioda

ukljucena = 0                       # redni broj trenutno uključene diode
r = sirina_jedne // 2               # poluprečnik jedne diode (moze i manji)

def novi_frejm():
    global ukljucena
    ukljucena = (ukljucena + 1) % broj_dioda # prelazimo na narednu diodu

    # bojimo pozadinu u crno i crtamo diodu belom bojom
    prozor.fill(pg.Color("black"))
    pg.draw.circle(prozor, pg.Color("white"), (x[ukljucena], y), r)

# -*- acsection: after-main -*-

kraj = False
sat = pg.time.Clock()  # sat koji određuje broj frejmova u sekundi
while not kraj:
    # crtamo i ažuriramo sadržaj prozora
    novi_frejm()
    pg.display.update()

    # proveravamo da li je korisnik isključio prozor
    for dogadjaj in pg.event.get():
        if dogadjaj.type == pg.QUIT:
            kraj = True

    # pauziramo do sledeceg frejma
    sat.tick(fps)

pg.quit() # isključujemo rad biblioteke PyGame
