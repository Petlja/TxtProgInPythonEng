# -*- acsection: general-init -*-
import pygame as pg, petljapg
sirina, visina = 300, 300
prozor = petljapg.open_window(sirina, visina, "Преплет")
# -*- acsection: main -*-

# bojimo pozadinu prozora u sivo
prozor.fill(pg.Color("gray"))

# dimenzije table i polja
brojPolja = 10
sirinaPolja = sirina // brojPolja
visinaPolja = visina // brojPolja
d = 10

# prolazimo kroz sva polja
for i in range(brojPolja):
    for j in range(brojPolja):
        # bojimo crna polja
        if (i + j) % 2 != 0:
            pg.draw.rect(prozor, pg.Color("black"), (i*sirinaPolja + d, j*visinaPolja, d, visinaPolja))
            pg.draw.rect(prozor, pg.Color("white"), (i*sirinaPolja, j*visinaPolja + d, sirinaPolja, d))
        else:
            pg.draw.rect(prozor, pg.Color("white"), (i*sirinaPolja, j*visinaPolja + d, sirinaPolja, d))
            pg.draw.rect(prozor, pg.Color("black"), (i*sirinaPolja + d, j*visinaPolja, d, visinaPolja))

# -*- acsection: after-main -*-
petljapg.wait_loop()
