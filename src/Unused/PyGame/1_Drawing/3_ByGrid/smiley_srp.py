# -*- acsection: general-init -*-
import pygame as pg

pg.init()                          # uključivanje rada biblioteke PyGame
pg.display.set_caption("Емотикон") # podešavamo naslov prozora
(sirina, visina) = (300, 300)      # otvaramo prozor dimenzije 300x300
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-
prozor.fill(pg.Color("white")) # bojimo pozadinu ekrana u belo

pg.draw.circle(prozor, pg.Color("yellow"), (150, 150), 100) # glava
pg.draw.ellipse(prozor, pg.Color("black"), (100, 90, 30, 60)) # levo oko
pg.draw.ellipse(prozor, pg.Color("black"), (170, 90, 30, 60)) # desno oko
pg.draw.ellipse(prozor, pg.Color("white"), (100, 190, 100, 20)) # unutrasnjost usta
pg.draw.ellipse(prozor, pg.Color("black"), (100, 190, 100, 20), 2) # ivica usta

# -*- acsection: after-main -*-
pg.display.update()   # prikazujemo nacrtano na ekranu

# petlja obrade događaja - čekamo dok korisnik ne isključi prozor
while pg.event.wait().type != pg.QUIT:
    pass

# isključivanje rada biblioteke PyGame
pg.quit()
