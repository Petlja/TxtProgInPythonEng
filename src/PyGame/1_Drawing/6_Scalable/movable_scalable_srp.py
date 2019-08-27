# -*- acsection: general-init -*-
import pygame as pg, petljapg
(sirina, visina) = (300, 300)
prozor = petljapg.open_window(sirina, visina, "Релативно цртање")
x = sirina // 2
y = visina // 2
a = 5
# -*- acsection: main -*-

def crtanje():
    prozor.fill(pg.Color("white"))
    pg.draw.circle(prozor, pg.Color("blue"), (x, y), 12*a)
    pg.draw.circle(prozor, pg.Color("yellow"), (x - 5*a, y - 5*a), 3*a)
    pg.draw.circle(prozor, pg.Color("black"), (x - 4*a, y - 4*a), a)
    pg.draw.circle(prozor, pg.Color("yellow"), (x + 5*a, y - 5*a), 3*a)
    pg.draw.circle(prozor, pg.Color("black"), (x + 4*a, y - 4*a), a)
    pg.draw.ellipse(prozor, pg.Color("red"), (x-5*a, y+2*a, 10*a, 2*a))
   
# Ideja je bila da deo koji sledi bude pridruzen korinickom programu, ali da ne bude vidljiv,
# a ovo zahteva dodatnu intervenciju na activecode komponenti.

# Korsnik treba da vidi onliko koliko vidi i u drugim primerima, 
# a ako napise funkciju crtanje kako mu je trazeno, da se slika "zalepi" za misa.
# Ne znam da je vredno realizacije, treba da se dogovorimo.
# Ako se dogovorimo program da ne udje ovakav kako je opisano, 
# moze da se svede na obican primer (kao sto su i ostali programi u toj lekciji).
    
def obradi_dogadjaj(dogadjaj):
    global x, y, a
    if dogadjaj.type == pg.MOUSEMOTION:
            (x, y) = dogadjaj.pos
            return True
    elif dogadjaj.type == pg.MOUSEBUTTONDOWN:
        if dogadjaj.button == 1:
            a += 1
            return True
        elif dogadjaj.button == 3:
            a -= 1
            return True
    return False

treba_crtati = True
kraj = False
while not(kraj):
    if treba_crtati:
        crtanje()
        pg.display.update()  # ažuriramo prikaz sadržaja ekrana
        treba_crtati = False # ne treba crtati do daljnjeg

    dogadjaj = pg.event.wait()      # čekamo naredni dogadjaj
    if dogadjaj.type == pg.QUIT:    # isključivanje prozora
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
