# -*- acsection: general-init -*-
import pygame as pg

pg.init()                          # uključivanje rada biblioteke PyGame
pg.display.set_caption("Дрвеће")   # podešavamo naslov prozora
(sirina, visina) = (300, 300)      # otvaramo prozor dimenzije 300x300
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-
prozor.fill(pg.Color("green")) # bojimo pozadinu ekrana u zeleno

pg.draw.rect(prozor, pg.Color("brown"), (40, 180, 20, 100))        # prvo stablo
pg.draw.ellipse(prozor, pg.Color("darkgreen"), (10, 50, 80, 150))  # prva krosnja
pg.draw.rect(prozor, pg.Color("brown"), (140, 180, 20, 100))       # drugo stablo
pg.draw.ellipse(prozor, pg.Color("darkgreen"), (110, 50, 80, 150)) # druga krosnja
pg.draw.rect(prozor, pg.Color("brown"), (240, 180, 20, 100))       # trece stablo
pg.draw.ellipse(prozor, pg.Color("darkgreen"), (210, 50, 80, 150)) # treca krosnja

# -*- acsection: after-main -*-
pg.display.update()   # prikazujemo nacrtano na ekranu

# petlja obrade događaja - čekamo dok korisnik ne isključi prozor
while pg.event.wait().type != pg.QUIT:
    pass

# isključivanje rada biblioteke PyGame
pg.quit()
