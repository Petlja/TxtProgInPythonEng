# -*- acsection: general-init -*-
import pygame as pg, random

# uključivanje rada biblioteke PyGame
pg.init()

# postavljamo naslov prozora
pg.display.set_caption("Патент затварач")
# uključujemo prozor dimenzije 100x600 piksela
(sirina, visina) = (100, 600)
prozor = pg.display.set_mode((sirina, visina))
# bojimo pozadinu prozora u plavo
prozor.fill(pg.Color("blue"))
# -*- acsection: main -*-

duzina_linije = 50    # duzina linije rajsferslusa
razmak_sa_strana = 15 # do leve i desne ivice prozora
razmak_gore_dole = 40 # do gornje i donje ivice prozora
razmak_izmedju_linija = 15 # izmedju linija rasjferslusa

# x koordinate pocetaka i krajeva linija
x_levo_poc = razmak_sa_strana
x_levo_kraj = x_levo_poc + duzina_linije
x_desno_poc = sirina - razmak_sa_strana - duzina_linije
x_desno_kraj = x_desno_poc + duzina_linije

y = razmak_gore_dole # y koordinata tekuce linije
while y < visina - razmak_gore_dole:
    pg.draw.line(prozor, pg.Color("yellow"), (x_levo_poc, y), (x_levo_kraj, y), 6);
    y += razmak_izmedju_linija # pripremamo crtanje sledece linije
    pg.draw.line(prozor, pg.Color("yellow"), (x_desno_poc, y), (x_desno_kraj, y), 6);
    y += razmak_izmedju_linija # pripremamo crtanje sledece linije
 
# -*- acsection: after-main -*-
# ažuriramo prikaz sadržaja prozora
pg.display.update()

# program radi sve dok ne nastupi događaj pg.QUIT
while pg.event.wait().type != pg.QUIT:
    pass

# isključivanje rada biblioteke PyGame
pg.quit()
