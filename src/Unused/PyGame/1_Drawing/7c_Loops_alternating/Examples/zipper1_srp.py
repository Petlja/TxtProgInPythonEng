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
razmak_gore_dole = 20 # do gornje i donje ivice prozora
razmak_izmedju_linija = 15 # izmedju linija rasjferslusa

# x koordinate pocetaka linija sa leve i desne strane
x_levo = razmak_sa_strana
x_desno = sirina - razmak_sa_strana - duzina_linije

# koordinate pocetka tekuce linije
x_poc = x_levo
y = razmak_gore_dole

while y < visina - razmak_gore_dole:
    x_kraj = x_poc + duzina_linije
    pg.draw.line(prozor, pg.Color("yellow"), (x_poc, y), (x_kraj, y), 6);
    
    # pripremamo crtanje sledece linije
    y += razmak_izmedju_linija # y je zadati broj piksela nize
    if x_poc == x_levo: # x_poc je suprotno od prethodnog
        x_poc = x_desno
    else:
        x_poc = x_levo
 
# -*- acsection: after-main -*-
# ažuriramo prikaz sadržaja prozora
pg.display.update()

# program radi sve dok ne nastupi događaj pg.QUIT
while pg.event.wait().type != pg.QUIT:
    pass

# isključivanje rada biblioteke PyGame
pg.quit()
