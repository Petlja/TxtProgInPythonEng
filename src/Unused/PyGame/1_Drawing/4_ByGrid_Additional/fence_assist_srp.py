# -*- acsection: general-init -*-
import pygame as pg, random

pg.init()   # uključujemo rad biblioteke PyGame

pg.display.set_caption("Пример") 

# otvaramo prozor
(sirina, visina) = (300, 300)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-
def crtanje():
    prozor.blit(platno, (0, 0))  # crtanje onoga sto je zadato
    
    # ose
    pg.draw.line(prozor, pg.Color("black"), (mis_x, 0), (mis_x, visina), 1) # uspravna linija misa
    pg.draw.line(prozor, pg.Color("black"), (0, mis_y), (sirina, mis_y), 1) # vodoravna linija misa

    # ispis koordinata
    str_x, str_y = str(mis_x), str(mis_y)
    xt_y, yt_y = (5, mis_y - 25) if 2 * mis_y > visina else (visina - 25, mis_y + 5)
    xt_x, yt_x = (mis_x - 50, 5) if 2 * mis_x > sirina else (mis_x + 5, sirina - 50)
    sl_x = font.render(str_x, True, pg.Color("black"))
    sl_y = font.render(str_y, True, pg.Color("black"))
    if mis_x <= 60: # x ispisujemo samo za levu stranu ekrana
        prozor.blit(sl_x, (xt_x, xt_y))
    prozor.blit(sl_y, (yt_x, yt_y))

def obradi_dogadjaj(dogadjaj):
    global mis_x, mis_y
    if dogadjaj.type == pg.MOUSEMOTION:   # miš je pomeren
        mis_x, mis_y = dogadjaj.pos
        return True                         # ponovo iscrtavamo scenu
    return False                            # nema potrebe da iscrtavamo scenu

################# crtez
platno = pg.Surface((sirina, visina)) # platno na kome je slika nacrtana
platno.fill(pg.Color("skyblue")) # bojimo pozadinu ekrana u nebo-plavo
pg.draw.rect(platno, pg.Color("green"), (0, 200, 300, 100))  # trava

pg.draw.line(platno, pg.Color('brown'), ( 10, 100), (290, 100), 10)
pg.draw.line(platno, pg.Color('brown'), ( 10, 250), (290, 250), 10)
pg.draw.polygon(platno, pg.Color('brown'), [( 20, 80), ( 30,  70), ( 40, 80), ( 40, 270), ( 20, 270)])
pg.draw.polygon(platno, pg.Color('brown'), [( 60, 80), ( 70,  70), ( 80, 80), ( 80, 270), ( 60, 270)])
pg.draw.polygon(platno, pg.Color('brown'), [(100, 80), (110,  70), (120, 80), (120, 270), (100, 270)])
pg.draw.polygon(platno, pg.Color('brown'), [(140, 80), (150,  70), (160, 80), (160, 270), (140, 270)])
pg.draw.polygon(platno, pg.Color('brown'), [(180, 80), (190,  70), (200, 80), (200, 270), (180, 270)])
pg.draw.polygon(platno, pg.Color('brown'), [(220, 80), (230,  70), (240, 80), (240, 270), (220, 270)])
pg.draw.polygon(platno, pg.Color('brown'), [(260, 80), (270,  70), (280, 80), (280, 270), (260, 270)])
#################

font = pg.font.SysFont("Arial", 20)         # font kojim će biti prikazan tekst
font.set_bold(True)
mis_x, mis_y = 0, 0

treba_crtati = True
kraj = False
while not kraj:
    if treba_crtati:    # ako je potrebno nacrtati lopticu
        crtanje()
        pg.display.update()        # ažuriramo prikaz sadržaja prozora
        treba_crtati = False

    dogadjaj = pg.event.wait()     # čekamo naredni događaj
    if dogadjaj.type == pg.QUIT:   # isključivanje prozora
        kraj = True
    else:
        treba_crtati = obradi_dogadjaj(dogadjaj)

# Zavrsetak skrivenog progrma, koji radi kao primer
pg.quit()
import sys 
sys.exit()

# Zavrsetak korisnickog programa je posebnoj sekciji

# -*- acsection: after-main -*-
pg.display.update()   # prikazujemo nacrtano na ekranu

# petlja obrade događaja - čekamo dok korisnik ne isključi prozor
while pg.event.wait().type != pg.QUIT:
    pass

# isključivanje rada biblioteke PyGame
pg.quit()
