import pygame as pg, petljapg
(sirina, visina) = (800, 400)
prozor = petljapg.open_window(sirina, visina, "Билијар")

(cx, cy) = (sirina // 2, visina // 2) # polozaj centra loptice (na početku je u centru prozora)
(dx, dy) = (3, 2)  # promena polozaja loptice (na pocetku po 3 piksela nadesno i 2 nadole)
r = 15             # poluprečnik loptice


def nov_frejm():
    global cx, cy, dx, dy  # ove promenljive menjamo u funkciji
    # pomeramo куглu
    cx += dx
    cy += dy
    
    if cx - r < 0 or cx + r > sirina: # ako je куглa "probila" levu ili desnu ivicu prozora
        dx = -dx # menjamo joj smer po x osi (ako je isla nadesno, ici ce nalevo i obrnuto)
    if cy - r < 0 or cy + r > visina: # ako je куглa "probila" gornju ili donju ivicu prozora
        dy = -dy # menjamo joj smer po y osi (ako je isla nadole, ici ce nagore i obrnuto)

    prozor.fill(pg.Color("darkgreen"))
    pg.draw.circle(prozor, pg.Color("white"), (cx, cy), r)

petljapg.frame_loop(100, nov_frejm)
