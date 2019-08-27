import pygame as pg, petljapg
(sirina, visina) = (400, 400)
prozor = petljapg.open_window(400, 400, "Линије мишем")

mis_poz = (0, 0)
pocetak_linije = mis_poz
crta_se_linija = False
ranije_linije = []

def nov_frejm():
    prozor.fill(pg.Color("white")) # bojimo prozor u belo
    if crta_se_linija:
        pg.draw.line(prozor, pg.Color('black'), pocetak_linije, mis_poz)
    for a, b in ranije_linije:
        pg.draw.line(prozor, pg.Color('black'), a, b)

def obradi_dogadjaj(dogadjaj):
    global crta_se_linija, pocetak_linije, mis_poz
    if dogadjaj.type == pg.MOUSEBUTTONDOWN:
        crta_se_linija = True
        pocetak_linije = dogadjaj.pos
    elif dogadjaj.type == pg.MOUSEBUTTONUP:
        crta_se_linija = False
        krajevi_linije = (pocetak_linije, dogadjaj.pos)
        ranije_linije.append(krajevi_linije)
    elif dogadjaj.type == pg.MOUSEMOTION:
        mis_poz = dogadjaj.pos

petljapg.frame_loop(30, nov_frejm, obradi_dogadjaj)
