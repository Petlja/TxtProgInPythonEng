# -*- acsection: general-init -*-
import pygame as pg, petljapg
(sirina, visina) = (100, 600)
prozor = petljapg.open_window(sirina, visina, "Патент затварач")

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
petljapg.wait_loop()
