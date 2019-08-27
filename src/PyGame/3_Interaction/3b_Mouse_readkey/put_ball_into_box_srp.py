# -*- acsection: general-init -*-
import pygame as pg, petljapg
sirina, visina = 400, 400
prozor = petljapg.open_window(sirina, visina, "Убаци лоптицу")
font = pg.font.SysFont("Arial", 30) # font kojim će biti prikazan tekst

r = 10 # velicina loptice
(cilj_x, cilj_y) = (sirina//4, visina//4) # ciljna tacka
cilj_kutija = (cilj_x - 2*r, cilj_y - 2*r, 4*r, 4*r) # pravougaonik oko ciljne tacke

(x, y) = (sirina//2, visina//2) # loptica krece iz centra
pobedio, izgubio = False, False

def crtanje():
    prozor.fill(pg.Color("black")) # crna pozadina
    if pobedio or izgubio:
        # igra je zavrsena, ispisujemo poruku
        poruka = "Браво!" if pobedio else "Побеже..."
        slika_teksta = font.render(poruka, True, pg.Color("green"))
        tx = (sirina - slika_teksta.get_width()) // 2
        ty = (visina - slika_teksta.get_height()) // 2
        prozor.blit(slika_teksta, (tx, ty))
    else:
        # igra jos traje, crtamo kutiju i lopticu
        pg.draw.rect(prozor, pg.Color("red"), cilj_kutija, 3)
        pg.draw.circle(prozor, pg.Color("green"), (int(x), int(y)), 10)

# -*- acsection: main -*-
def nov_frejm():
    global x, y, pobedio, izgubio
    
    pritisnut_taster_misa = pg.mouse.get_pressed()
    if pritisnut_taster_misa[2]: # desni taster - nova igra
        (x, y) = (sirina//2, visina//2) # vracamo lopticu u centar
        pobedio, izgubio = False, False # igrac nije ni pobedio ni izgubio
        
    if pritisnut_taster_misa[0]: # levi taster - pomeri lopticu
        (xm, ym) = pg.mouse.get_pos() # koordinate pozicije misa
        # loptica se pomera od misa za jos pola tog rastojanja
        x = x - 0.5 * (xm - x)
        y = y - 0.5 * (ym - y)

    # ako je centar loptice blizu centra cilja - igrac je pobedio
    if abs(x - cilj_x) < r and abs(y - cilj_y) < r:
        pobedio = True
    # ako je centar loptice van prozora - igrac je izgubio
    if x < 0 or x > sirina or y < 0 or y > visina:
        izgubio = True
    crtanje()
# -*- acsection: after-main -*-

petljapg.frame_loop(50, nov_frejm)
