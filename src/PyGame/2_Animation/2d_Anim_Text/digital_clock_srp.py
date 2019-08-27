import pygame as pg, datetime, petljapg
(sirina, visina) = (200, 200)
prozor = petljapg.open_window(sirina, visina, "Дигитални сат")

font = pg.font.SysFont("Arial", 40)     # font kojim će biti prikazan tekst

def nov_frejm():
    vreme = datetime.datetime.now()           # određujemo trenutno vreme
    sati = str(vreme.hour).rjust(2, "0")      # broj sati kao string, po potrebi dopunjen sleva nulom
    minuta = str(vreme.minute).rjust(2, "0")  # isto za broj minuta
    sekundi = str(vreme.second).rjust(2, "0") # isto za broj sekundi
    
    # gradimo sličicu koja predstavlja tu poruku ispisanu crnom bojom
    sl_teksta = font.render(sati + ":" + minuta + ":" + sekundi, True, pg.Color("black"))

    # položaj određujemo tako da tekst bude centriran u prozoru
    (x, y) = ((sirina - sl_teksta.get_width()) // 2, (visina - sl_teksta.get_height()) // 2)
    
    prozor.fill(pg.Color("white")) # bojimo pozadinu u belo
    prozor.blit(sl_teksta, (x, y)) # prikazujemo sliku teksta

petljapg.frame_loop(1, nov_frejm)
