# -*- acsection: general-init -*-
import pygame as pg, math

pg.init()                      # uključivanje rada biblioteke PyGame
pg.display.set_caption("Цвет") # podešavamo naslov prozora
(sirina, visina) = (400, 400)  # uključujemo prozor dimenzije 400x400 piksela
prozor = pg.display.set_mode((sirina, visina))

# boje koje ćemo koristiti
BELA = (255, 255, 255)
ZUTA = (255, 255, 0)
ROZE = (255, 200, 200)

# -*- acsection: main -*-
prozor.fill(BELA)   # bojimo pozadinu u belo

(cx, cy) = (sirina // 2, visina // 2) # koordinate centra prozora

# prečnici krugova - dužina stranice pravilnog šestougla u čijim se
# temenima nalaze centri krugova
a = 100
# visina karakterističnog trougla šestougla
h = round(a * math.sqrt(3) / 2)

# sva temena šestougla dele ove koordinate
xF = cx - a
xAE = cx - a//2
xBD = cx + a//2
xC = cx + a
yAB = cy - h
yCF = cy
yDE = cy + h

# koordinate temena šestougla
O = (cx, cy)
A = (xAE, yAB)
B = (xBD, yAB)
C = (xC, yCF)
D = (xBD, yDE)
E = (xAE, yDE)
F = (xF, yCF)

# poluprečnik krugova
r = a // 2

# iscrtavamo krugove
pg.draw.circle(prozor, ZUTA, O, r)
pg.draw.circle(prozor, ROZE, A, r)
pg.draw.circle(prozor, ROZE, B, r)
pg.draw.circle(prozor, ROZE, C, r)
pg.draw.circle(prozor, ROZE, D, r)
pg.draw.circle(prozor, ROZE, E, r)
pg.draw.circle(prozor, ROZE, F, r)

# -*- acsection: after-main -*-
pg.display.update()  # osvežavamo sadržaj prozora

# petlja obrade događaja - čekamo dok korisnik ne isključi prozor
while pg.event.wait().type != pg.QUIT:
    pass

pg.quit()            # isključivanje rada biblioteke PyGame

