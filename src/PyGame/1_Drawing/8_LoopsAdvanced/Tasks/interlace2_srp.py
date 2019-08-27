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

for i in range(brojPolja): # bele vodoravne pruge
    pg.draw.rect(prozor, pg.Color("white"), (0, i*visinaPolja + d, sirina, d))

for i in range(brojPolja): # crne uspravne pruge
    pg.draw.rect(prozor, pg.Color("black"), (i*sirinaPolja + d, 0, d, visina))

# prolazimo kroz sve preseke
for i in range(brojPolja):
    for j in range(brojPolja):
        # bojimo preseke gde treba da je bela preko crne
        if (i + j) % 2 != 0:
            pg.draw.rect(prozor, pg.Color("white"), (i*sirinaPolja + d, j*visinaPolja + d, d, d))

# -*- acsection: after-main -*-
petljapg.wait_loop()
