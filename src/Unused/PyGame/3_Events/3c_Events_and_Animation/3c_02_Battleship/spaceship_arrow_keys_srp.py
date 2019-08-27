# -*- acsection: general-init -*-
import pygame as pg

pg.init() # uključujemo rad biblioteke PyGame
pg.display.set_caption("Свемирски брод - лево, десно, пуцање")
(sirina, visina) = (400, 400)
prozor = pg.display.set_mode((sirina, visina))   # otvaramo prozor

# podešavamo događaje tastaturom - prvi događaj se generiše nakon
# 50ms, a svaki naredni nakon 25ms
pg.key.set_repeat(50, 25)

# -*- acsection: main -*-

brod = pg.image.load('spaceship.png')  # učitavamo sliku svemirskog broda
brod_sirina = brod.get_width()         # očitavamo dimenzije slike
brod_visina = brod.get_height()

(x, y) = (sirina // 2, visina - brod_visina // 2) # koordinate svemirskog broda
(DX, DY) = (10, 10)                               # pomeraji po x i y koordinati
meci = []

def crtanje():
    prozor.fill(pg.Color("black"))    # bojimo prozor u crno
    prozor.blit(brod, (x - brod_sirina // 2, y - brod_visina // 2)) # crtamo brod
    for metak in meci:
        pg.draw.circle(prozor, pg.Color('white'), metak, 3)


def novi_frejm():
    global meci
    novi_meci = []
    for metak in meci:
        x, y = metak
        if y > DY: 
            novi_meci.append((x, y - DY))

    meci = novi_meci

def obradi_dogadjaj(dogadjaj):
    global x, y, meci
    # pomeraji koji odgovaraju strelicama
    pomeraj = {pg.K_LEFT: -DX, pg.K_RIGHT: DX}
    if dogadjaj.type == pg.KEYDOWN:       # pritisak tastera na tastaturi
        x += pomeraj.get(dogadjaj.key, 0) # pomeramo centar broda za odgovarajući pomeraj
        if dogadjaj.key == pg.K_SPACE:
            meci.append((x, round(0.8 * visina)))

# -*- acsection: after-main -*-

kraj = False
sat = pg.time.Clock()    # sat koji određuje broj frejmova u sekundi
while not kraj:
    crtanje()
    pg.display.update()      # ažuriramo prikaz sadržaja prozora

    for dogadjaj in pg.event.get():
        if dogadjaj.type == pg.QUIT:    # isključivanje prozora
            kraj = True
        else:
            obradi_dogadjaj(dogadjaj)
        
    sat.tick(30)
    novi_frejm()

pg.quit()  # isključujemo rad biblioteke PyGame
