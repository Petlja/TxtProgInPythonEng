# -*- acsection: general-init -*-
import pygame as pg

pg.init()  # inicijalizujemo biblioteku pygame

pg.display.set_caption("Шетање")  # otvaramo prozor
(sirina, visina) = (800, 600)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

# učitavamo u listu pozadina_slike walk_background1.png, walk_background2.png, walk_background3.png
pozadina_slike = []
for i in range(1, 4):
    naziv_slike = "walk_background" + str(i) + ".png"  # gradimo naziv slike od delova
    pozadina_slike.append(pg.image.load(naziv_slike))  # učitavamo sliku i dodajemo je na kraj niza

# učitavamo u listu decak_slike walk1.png, walk2.png, ..., walk5.png
decak_slike = []   # niz u koji dodajemo slike
for i in range(1, 6):
    naziv_slike = "walk" + str(i) + ".png"           # gradimo naziv slike od delova
    decak_slike.append(pg.image.load(naziv_slike))   # učitavamo sliku i dodajemo je na kraj niza

x_offset_stope = 40 # stope su 40 piksela desno od leve ivice
y_offset_stope = 170 # stope su 170 piksela ispod od gornje ivice
i_decak = 0  # indeks tekuće slike decaka
i_pozadina = 0

(x, y) =  (0, visina // 2)

def crtaj():
    prozor.blit(pozadina_slike[i_pozadina], (0, 0))
    prozor.blit(decak_slike[i_decak], (x - x_offset_stope, y - y_offset_stope))
    
def novi_frejm():
    global x, y, i_decak, i_pozadina
    i_decak = (i_decak + 1) % len(decak_slike)  # prelazimo na sledeću sliku
    
    x += 10
    if x >= sirina:
        i_pozadina = (i_pozadina + 1) % len(pozadina_slike)
        x -= sirina
    
    pxarray = pg.surfarray.pixels3d(pozadina_slike[i_pozadina])
    while pxarray[x, y][0] < 50: # trava
        y -= 1
    while pxarray[x, y][0] > 50: # nebo
        y += 1
    
# -*- acsection: after-main -*-

kraj = False
sat = pg.time.Clock()  # sat koji određuje broj frejmova u sekundi
while not kraj:
    novi_frejm()
    # crtamo i ažuriramo sadržaj prozora
    crtaj()
    pg.display.update()

    # proveravamo da li je korisnik isključio prozor
    for dogadjaj in pg.event.get():
        if dogadjaj.type == pg.QUIT:
            kraj = True

    # pauziramo do sledeceg frejma
    sat.tick(5)

pg.quit() # isključujemo rad biblioteke PyGame
