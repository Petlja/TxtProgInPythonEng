import pygame as pg, petljapg
(sirina, visina) = (100, 300)
prozor = petljapg.open_window(sirina, visina, "Семафор")

BR_FAZA = 4   #  crveno   crveno_zuto  zeleno     zuto
svetla_faze   = ((1, 0, 0), (1, 1, 0), (0, 0, 1), (0, 1, 0) )
trajanje_faze = ( 2.5,       1,         2.5,       1 ) # u sekundama

BR_SVETALA = 3
boja_svetla = (
#    za iskljucena   za ukljucena
    ((128,   0, 0), (255,   0, 0)), # crvena
    ((128, 128, 0), (255, 255, 0)), # zuta
    ((  0, 128, 0), (  0, 255, 0))  # zelena
)
pozicija_svetla = ((50, 50), (50, 150), (50, 250))
i_faza = 3
br_frejmova_do_promene = 0
fps = 5

def nov_frejm():
    global i_faza, br_frejmova_do_promene # ove vrednosti izracunavamo
    if br_frejmova_do_promene == 0:
        i_faza = (i_faza + 1) % BR_FAZA
        br_frejmova_do_promene = round(trajanje_faze[i_faza] * fps)
    
    br_frejmova_do_promene -= 1
    
    prozor.fill(pg.Color("darkgray"))  # bojimo pozadinu prozora u sivo
    ukljuceno = svetla_faze[i_faza]
    for i_svetlo in range(BR_SVETALA):
        (x, y) = pozicija_svetla[i_svetlo]
        stanje = ukljuceno[i_svetlo] # 0 za iskljuceno, a 1 za ukljuceno
        pg.draw.circle(prozor, boja_svetla[i_svetlo][stanje], (x, y), 40)
        
petljapg.frame_loop(fps, nov_frejm)
