# -*- acsection: general-init -*-
import pygame as pg, petljapg
prozor = petljapg.open_window(300, 300, "Чича Глиша")

# -*- acsection: main -*-
(sirina, visina) = (300, 300)
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
    if mis_x <= 150 or mis_y <= 175:
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
platno.fill(pg.Color("white")) # bojimo pozadinu ekrana u belo
pg.draw.circle(platno, pg.Color("black"), (150, 70), 20, 2)      # glava

pg.draw.line(platno, pg.Color("blue"), (120, 50), (180,50), 3)   # obod šešira
pg.draw.rect(platno, pg.Color("blue"), (130, 10, 40, 40))        # šešir

pg.draw.circle(platno, pg.Color("black"), (145, 60), 2, 2)       # levo oko
pg.draw.circle(platno, pg.Color("black"), (155, 60), 2, 2)       # desno oko

pg.draw.ellipse(platno, pg.Color("red"), (145, 70, 10, 7))       # usta

pg.draw.line(platno, pg.Color("black"), (150, 90), (150,170), 3) # telo

pg.draw.line(platno, pg.Color("black"), (150, 110), (100, 120), 3) # leva ruka
pg.draw.line(platno, pg.Color("black"), (100, 120), (80, 100), 3)

pg.draw.line(platno, pg.Color("black"), (150, 110), (200, 150), 3) # desna ruka
pg.draw.line(platno, pg.Color("black"), (200, 150), (210, 170), 3)

pg.draw.line(platno, pg.Color("black"), (150, 170), (130, 200), 3) # leva noga
pg.draw.line(platno, pg.Color("black"), (130, 200), (140, 250), 3)

pg.draw.line(platno, pg.Color("black"), (150, 170), (170, 200), 3) # desna noga
pg.draw.line(platno, pg.Color("black"), (170, 200), (160, 250), 3)
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

# Zavrsetak skrivenog programa, koji radi kao primer
pg.quit()
import sys 
sys.exit()

# Zavrsetak korisnickog programa je posebnoj sekciji

# -*- acsection: after-main -*-
petljapg.wait_loop()
