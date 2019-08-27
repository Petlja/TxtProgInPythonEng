# -*- acsection: general-init -*-
import pygame as pg, math

# uključivanje rada biblioteke PyGame
pg.init()

# podešavamo naslov prozora
pg.display.set_caption("Три круга")
# uključujemo prozor dimenzije 200x200 piksela
(sirina, visina) = (200, 200)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

prozor.fill(pg.Color("white")) # bojimo pozadinu u belo
(cx, cy) = (sirina // 2, visina // 2) # centar krugova je u sredni ekrana
pg.draw.circle(prozor, pg.Color("red"), (cx, cy), 100)   # crveni krug
pg.draw.circle(prozor, pg.Color("blue"), (cx, cy), 75)   # plavi krug
pg.draw.circle(prozor, pg.Color("green"), (cx, cy), 50)  # zeleni krug

# -*- acsection: after-main -*-

# osvežavamo sadržaj prozora
pg.display.update()

# petlja obrade događaja - čekamo dok korisnik ne isključi prozor
while pg.event.wait().type != pg.QUIT:
    pass

# isključivanje rada biblioteke PyGame
pg.quit()
