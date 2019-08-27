import pygame as pg, petljapg
tekst = "ПАЈТОН"
(sirina, visina) = (400, 100)
prozor = petljapg.open_window(sirina, visina, "Реклама")

font = pg.font.SysFont("Arial", 80) # font kojim će biti prikazan tekst
slika_teksta = font.render(tekst, True, pg.Color("yellow"))
x = sirina
y = (visina - slika_teksta.get_height()) // 2


def nov_frejm():
    global x
    x = x - 2
    if x + slika_teksta.get_width() < 0:
        x = sirina
    prozor.fill(pg.Color("black")) # bojimo pozadinu prozora u crno
    prozor.blit(slika_teksta, (x, y))

petljapg.frame_loop(60, nov_frejm)
