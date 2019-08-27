import pygame as pg, petljapg
(sirina, visina) = (800, 500)
prozor = petljapg.open_window(sirina, visina, "Прекидачи")

shema_slike = (pg.image.load('Shema3_Off.png'), pg.image.load('Shema3_On.png'))
prekidac_slike = (pg.image.load('SwitchOff.png'), pg.image.load('SwitchOn.png'))
sijalica_slike = (pg.image.load('BulbOff.png'), pg.image.load('BulbOn.png'))

ukljucen_prekidac = [False, False, False]
prekidac_poz = [(100, 200), (300, 150), (300, 250)]
sijalica_poz = (500, 100)

def nov_frejm():
    svetli = ukljucen_prekidac[0] and (ukljucen_prekidac[1] or ukljucen_prekidac[2])
    prozor.blit(shema_slike[svetli], (0, 0))
    for i in range(3):
        prozor.blit(prekidac_slike[ukljucen_prekidac[i]], prekidac_poz[i])
    prozor.blit(sijalica_slike[svetli], sijalica_poz)
    
def tacka_u_pravougaoniku(tacka, gornje_levo_teme, sirina, visina):
    x, y = tacka
    x0, y0 = gornje_levo_teme
    return x0 <= x and x <= x0 + sirina and y0 <= y and y <= y0 + visina
    
def obradi_dogadjaj(dogadjaj):
    global ukljucen_prekidac
    if dogadjaj.type == pg.MOUSEBUTTONDOWN:   # pritisnuto je dugme miša
        mis_tacka = dogadjaj.pos
        for i in range(3):
            if tacka_u_pravougaoniku(mis_tacka, prekidac_poz[i], 80, 80):
                ukljucen_prekidac[i] = not ukljucen_prekidac[i]

petljapg.frame_loop(10, nov_frejm, obradi_dogadjaj)
