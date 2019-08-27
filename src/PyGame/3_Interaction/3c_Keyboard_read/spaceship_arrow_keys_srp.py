# -*- acsection: general-init -*-
import pygame as pg, petljapg
(sirina, visina) = (400, 400)
prozor = petljapg.open_window(sirina, visina, "Свемирски брод - лево, десно, пуцање")

brod = pg.image.load('spaceship.png')  # učitavamo sliku svemirskog broda
(brod_sirina, brod_visina) = (brod.get_width(), brod.get_height())

(x_brod, y_brod) = (sirina // 2, visina - brod_visina // 2) # sredina donje ivice
DX = 10 # pomeraj broda levo-desno
DY = 10 # pomeraj metka na gore
meci = []

def nov_frejm():
    global x_brod, y_brod, meci
    
    # pomeri sve metke na gore
    novi_meci = []
    for x, y in meci:
        if y > DY: 
            novi_meci.append((x, y - DY))
    meci = novi_meci
    
# -*- acsection: main -*-
    # proveri pritiske na tastere levo, desno, razmak
    
    # ocitavamo stanje svih tastera
    pritisnut = pg.key.get_pressed()
    
    # ako je pritisnuta strelica levo i brod moze da ide levo
    if pritisnut[pg.K_LEFT] and (x_brod > DX): 
        x_brod -= DX # pomeri brod na levo
        
    # ako je pritisnuta strelica desno i brod moze da ide desno
    if pritisnut[pg.K_RIGHT] and (x_brod < sirina - brod_sirina - DX):
        x_brod += DX # pomeri brod na desno
    
    if pritisnut[pg.K_SPACE]:               # ako je pritisnut razmak
        meci.append((x_brod, round(0.8 * visina))) # dodaj metak u listu
# -*- acsection: after-main -*-

    # crtanje
    prozor.fill(pg.Color("black"))    
    prozor.blit(brod, (x_brod - brod_sirina // 2, y_brod - brod_visina // 2))
    for metak in meci:
        pg.draw.circle(prozor, pg.Color('white'), metak, 3)

petljapg.frame_loop(30, nov_frejm)
