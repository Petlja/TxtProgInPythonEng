import pygame as pg, petljapg
tekst = "ПАЈТОН"
(sirina, visina) = (len(tekst) * 70, 100)
prozor = petljapg.open_window(sirina, visina, "Реклама")

font = pg.font.SysFont("Arial", 80) # font kojim će biti prikazan tekst
slika_teksta = font.render(tekst, True, pg.Color("yellow"))
x = (sirina - slika_teksta.get_width()) // 2
y = (visina - slika_teksta.get_height()) // 2
svetli = True

def nov_frejm():
    global svetli    
    svetli = not svetli
    prozor.fill(pg.Color("black")) # bojimo pozadinu prozora u crno
    if svetli: 
        prozor.blit(slika_teksta, (x, y))

petljapg.frame_loop(3, nov_frejm)
