# -*- acsection: general-init -*-
import pygame as pg, petljapg
(sirina, visina) = (400, 400)
prozor = petljapg.open_window(sirina, visina, "Шаховска табла")
# -*- acsection: main -*-

# bojimo pozadinu prozora u sivo
prozor.fill(pg.Color("gray"))

# dimenzije table i polja
brojPolja = 8
sirinaPolja = sirina / brojPolja
visinaPolja = visina / brojPolja

# prolazimo kroz sva polja
for i in range(brojPolja):
    for j in range(brojPolja):
        # bojimo crna polja
        if (i + j) % 2 != 0:
            pg.draw.rect(prozor, pg.Color("black"), (i*sirinaPolja, j*visinaPolja, sirinaPolja, visinaPolja))

# -*- acsection: after-main -*-
petljapg.wait_loop()
