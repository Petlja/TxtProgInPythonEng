# http://paulbourke.net/fractals/lsys/ odlican, mnogo primera, prosirenje sintakse
# http://www.sidefx.com/docs/houdini/nodes/sop/lsystem.html lepo objasnjava
# opsti slucaj ima vise od jednog pravila, a ovde je jedino pravilo "X -> generator" (to je ok)
# dodati tepih Sjerpinskog i jos biljaka iz starog i sa prvog linka, 
# dodati random u posebnoj verziji
import pygame as pg
import math

def napred(d, crtaj = True):
    global cp, smer, jed_ugao
    np = (cp[0] + d * math.cos(smer*jed_ugao), cp[1] - d * math.sin(smer*jed_ugao))
    if crtaj:
        pg.draw.line(prozor, pg.Color("darkgreen"), cp, np )
    cp = np

def  f(n, a, pupoljak):
    global cp, smer, stanje, skala, generator
    for c in pupoljak:
        if c == 'F': napred(a)
        if c == 'f': napred(a, crtaj = False)
        elif c == '+': smer += 1
        elif c == '-': smer -= 1
        elif c == '[': stanje.append((cp,smer))
        elif c == ']': cp, smer = stanje.pop()
        elif c == 'X': 
            if n > 1:
                f(n-1, a * skala, generator) 
            else:
                napred(a)

pg.init()
(sirina, visina) = (800, 600)
prozor = pg.display.set_mode((sirina,visina))
clock = pg.time.Clock()

N, L, Q, X0, Y0, POC_SMER, JED_UGAO_ST, INIT, GEN = range(9) # nazivi parametara
opisi_linija = (
    (5, 500, 1/3, 0.1, 0.6, 0,   60, 'X',           'XfX'),                   # kantorov skup
    (7, 400, 0.5, 0.5, 0.9, 3,   30, 'X',           'F[-X][+X]'),             # drvce
    (7, 400, 0.5, 0.5, 0.9, 4, 22.5, 'X',           'F[-X][+X][--X][++X]'),   # razgranatije drvce
    (5, 300, 0.3, 0.5, 0.5, 0,   60, 'X+X+X+X+X+X', '[F[+X][-X]F[X]]'),       # kohova pahuljica varijanta
    (5,  50, 0.5, 0.2, 0.4, 0,   60, 'X++X++X',     'X-X++X-X'),              # kohova kriva manja
    (5,  25, 0.5, 0.5, 0.6, 0,   60, 'X+X+X+X+X+X', 'X-X++X-X'),              # kohova kriva veca
    (7, 300, 0.5, 0.2, 0.6, 0,   60, 'X',           '[X]FF++[X]FF++[X]FF++'), # trougao Sjerpinskog
    (6, 200, 0.5, 0.5, 0.9, 3,   25, 'X',           'F+[[X]-X]-F[-FX]+X'),    # fraktalna biljka
) 

stanje = []
kraj = False
i_opis = 0
while not kraj:
    opis = opisi_linija[i_opis]
    i_opis = (i_opis + 1) % len(opisi_linija)
    
    jed_ugao = opis[JED_UGAO_ST] * math.pi / 180
    cp = (opis[X0] * sirina, opis[Y0] * visina)
    smer = opis[POC_SMER]
    skala = opis[Q]
    generator = opis[GEN]

    prozor.fill(pg.Color("skyblue"))    
    f(opis[N], opis[L], opis[INIT])
    pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            kraj = True
            
    clock.tick(0.5) # FPS

pg.quit()
quit()
