# -*- acsection: general-init -*-
import pygame as pg, petljapg
(sirina, visina) = (100, 600)
prozor = petljapg.open_window(sirina, visina, "Патент затварач")

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
petljapg.wait_loop()
