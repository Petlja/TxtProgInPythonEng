import pygame as pg, petljapg

(sirina, visina) = (750, 150)
prozor = petljapg.open_window(sirina, visina, "Прича")

font = pg.font.SysFont("Century", 40)     # font kojim će biti prikazan tekst
uvod = "Ово је једна стара прича"
nastavak = " о једном човеку, који је желео да му неко исприча причу"
br_slova_za_prikaz = 33
vidljivi_tekst = (uvod + nastavak)[0 : br_slova_za_prikaz]
poz_sledeceg_slova = br_slova_za_prikaz - len(uvod)
fps = 5
i_frejm = 0

def nov_frejm():
    global vidljivi_tekst, poz_sledeceg_slova, i_frejm
    
    i_frejm += 1
    if i_frejm > 8:
        vidljivi_tekst = vidljivi_tekst[1:] + nastavak[poz_sledeceg_slova]
        poz_sledeceg_slova = (poz_sledeceg_slova + 1) % len(nastavak)

    prozor.fill(pg.Color("skyblue")) # bojimo pozadinu
    # gradimo sličicu од tekstа i prikazujemo je
    slika_teksta = font.render(vidljivi_tekst, True, pg.Color("black"))
    prozor.blit(slika_teksta, (50, 50))


petljapg.frame_loop(fps, nov_frejm)
