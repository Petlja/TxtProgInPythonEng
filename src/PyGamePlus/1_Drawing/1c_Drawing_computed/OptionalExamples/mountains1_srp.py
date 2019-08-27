# -*- acsection: general-init -*-
import pygame as pg, random

# ukljucivanje rada biblioteke PyGame
pg.init()

# podesavamo naslov prozora
pg.display.set_caption("Врхови планина")
# otvaramo prozor dimenzije 800x400 piksela
(sirina, visina) = (800, 400)
prozor = pg.display.set_mode((sirina, visina))
# -*- acsection: main -*-

# bojimo pozadinu prozora u belo
prozor.fill(pg.Color("white"))

# ukupan broj planina na slici
broj_planina = 5
# sirina jedne planine (sve planine su iste sirine)
sirina_planine = sirina / broj_planina
# crtamo jednu po jednu planinu
for i in range(broj_planina):
    # x koordinata pocetka tekuce planine
    pocetak_planine_x = i*sirina_planine
    # y koordinata vrha planine (obavezno iznad sredine prozora)
    vrh_planine_y = random.randint(0, visina / 2)
    # tri temena planine
    levo  = (pocetak_planine_x, visina)
    vrh   = (pocetak_planine_x + sirina_planine / 2, vrh_planine_y)
    desno = (pocetak_planine_x + sirina_planine, visina)
    # crtamo planinu pomocu dve duzi
    pg.draw.line(prozor, pg.Color("black"), levo, vrh, 3)
    pg.draw.line(prozor, pg.Color("black"), vrh, desno, 3)

# -*- acsection: after-main -*-
# osvezavamo prikaz sadrzaja prozora
pg.display.update()

# program radi sve dok ne nastupi dogadjaj pg.QUIT
while pg.event.wait().type != pg.QUIT:
    pass

# iskljucivanje rada biblioteke PyGame
pg.quit()
