# -*- acsection: general-init -*-
import pygame as pg

pg.init()  # inicijalizujemo biblioteku pygame
pg.display.set_caption("Семафор")

# otvaramo prozor
(sirina, visina) = (100, 300)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

trajanje_faze_u_sekundama = (2.5, 1, 2.5, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 1)
svetla_faze = (
    (1, 0, 0), # faza crveno
    (1, 1, 0), # faza crveno_zuto
    (0, 0, 1), # faza zeleno
    (0, 0, 0), # faza ni jedna
    (0, 0, 1), # faza zeleno
    (0, 0, 0), # faza ni jedna
    (0, 0, 1), # faza zeleno
    (0, 0, 0), # faza ni jedna
    (0, 0, 1), # faza zeleno
    (0, 1, 0), # faza zuto
)

svetla_boje = (
#    za iskljucena   za ukljucena
    ((128,   0, 0), (255,   0, 0)), # crvena
    ((128, 128, 0), (255, 255, 0)), # zuta
    ((  0, 128, 0), (  0, 255, 0))  # zelena
)
svetla_pozicije = ((50, 50), (50, 150), (50, 250))
i_faza = 0
br_frejmova_do_promene = 0
fps = 5

def novi_frejm():
    global i_faza, br_frejmova_do_promene # ove vrednosti izracunavamo
    nova_faza = False
    if br_frejmova_do_promene == 0:
        i_faza = (i_faza + 1) % len(svetla_faze)
        br_frejmova_do_promene = round(trajanje_faze_u_sekundama[i_faza] * fps)
        nova_faza = True
    br_frejmova_do_promene -= 1
    return nova_faza
    
def crtaj():
    prozor.fill(pg.Color("darkgray"))  # bojimo pozadinu prozora u sivo
    ukljuceno = svetla_faze[i_faza]
    for i_svetlo in range(3):
        (x, y) = svetla_pozicije[i_svetlo]
        stanje = ukljuceno[i_svetlo] # 0 za iskljuceno, a 1 za ukljuceno
        pg.draw.circle(prozor, svetla_boje[i_svetlo][stanje], (x, y), 40)
        
# -*- acsection: after-main -*-

kraj = False
sat = pg.time.Clock()  # sat koji određuje broj frejmova u sekundi

while not kraj:
    treba_crtati = novi_frejm()
    if treba_crtati:
        crtaj()
        pg.display.update()
    
    # proveravamo da li je korisnik isključio prozor
    for dogadjaj in pg.event.get():
        if dogadjaj.type == pg.QUIT:
            kraj = True
            
    # pauziramo do sledeceg frejma
    sat.tick(fps)
pg.quit() # isključujemo rad biblioteke PyGame
