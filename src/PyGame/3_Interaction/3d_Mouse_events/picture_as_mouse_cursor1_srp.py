import pygame as pg, petljapg
(sirina, visina) = (400, 400)
prozor = petljapg.open_window(sirina, visina, "Слика као курсор миша")

mis_slika = (pg.image.load("HammerUp.png"), pg.image.load("HammerDown.png"))
i_slika = 0
(mis_x, mis_y) = (sirina // 2, visina // 2)
pg.mouse.set_pos((mis_x, mis_y))
pg.mouse.set_visible(False)

def nov_frejm():
    prozor.fill(pg.Color("skyblue")) # bojimo prozor u nebo-plavo
    # crtamo sliku tako da je mis na sredini slike
    slika_sirina = mis_slika[i_slika].get_width()
    slika_visina = mis_slika[i_slika].get_height()
    gore_levo = (mis_x - slika_sirina // 2, mis_y - slika_visina // 2)
    prozor.blit(mis_slika[i_slika], gore_levo)

def obradi_dogadjaj(dogadjaj):
    global mis_x, mis_y, i_slika
    if dogadjaj.type == pg.MOUSEBUTTONDOWN:
        i_slika = 1
    elif dogadjaj.type == pg.MOUSEBUTTONUP:
        i_slika = 0
    elif dogadjaj.type == pg.MOUSEMOTION:
        mis_x, mis_y = dogadjaj.pos

petljapg.frame_loop(30, nov_frejm, obradi_dogadjaj)
