# -*- acsection: general-init -*-
import pygame as pg

# ukljucivanje rada biblioteke PyGame
pg.init()

# postavljamo naslov prozora
pg.display.set_caption("Шаховска табла")

# otvaramo prozor dimenzije 400x400 piksela
(sirina, visina) = (400, 400)
prozor = pg.display.set_mode((sirina, visina))
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
# prikazujemo sadrzaj prozora
pg.display.update()

# program radi sve dok ne nastupi dogadjaj pg.QUIT
while pg.event.wait().type != pg.QUIT:
    pass

# iskljucivanje rada biblioteke PyGame
pg.quit()
