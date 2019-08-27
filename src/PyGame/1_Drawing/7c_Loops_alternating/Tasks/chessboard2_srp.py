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
    for j in range(1 - i%2, brojPolja, 2):
        # bojimo crna polja
        pg.draw.rect(prozor, pg.Color("black"), (i*sirinaPolja, j*visinaPolja, sirinaPolja, visinaPolja))

# -*- acsection: after-main -*-
petljapg.wait_loop()
