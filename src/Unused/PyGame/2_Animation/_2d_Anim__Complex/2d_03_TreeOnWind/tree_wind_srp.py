# -*- acsection: general-init -*-
import pygame as pg, random, math

pg.init() # inicijalizujemo biblioteku PyGame
pg.display.set_caption("Дрво на ветру")

# otvaramo prozor
(sirina, visina) = (640, 360)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

def grana(h, ugao, nivo, poc_grane):
    if h > min_duzina_grane:
        debljina = max(1, 15 - 3*nivo)
        ugao += popravka_zbog_vetra(ugao, nivo)
        kraj_grane = (poc_grane[0] + h * math.cos(ugao), poc_grane[1] - h * math.sin(ugao))
        boja = pg.Color('brown4') if h > 12 else pg.Color('green')
        pg.draw.line(prozor, boja, poc_grane, kraj_grane, debljina)
        grana(h * umanjenje, ugao+ugao_grananja, nivo+1, kraj_grane)
        grana(h * umanjenje, ugao-ugao_grananja, nivo+1, kraj_grane)

def popravka_zbog_vetra(ugao, nivo):
    n = int(math.floor(ugao / math.pi))
    smer = 1 if n % 2 else -1
    koef = 0.1 + random.uniform(0, 0.05) # u radijanima
    return smer * nivo * vetar * koef

def crtanje():
    prozor.fill(pg.Color("black")) # bojimo prozor u crno
    grana(pocetna_duzina_grane, 0.5 * math.pi, 0, (sirina // 2, visina))

def novi_frejm():
    global ugao_grananja, vetar
    (mis_x, mis_y) = pg.mouse.get_pos()     # koordinate pozicije miša
    ugao_grananja = math.pi * (0.2*(mis_y / visina) + 0.1)
    vetar = 2 * (mis_x / sirina) - 1

pocetna_duzina_grane = 120
umanjenje = 0.66
min_duzina_grane = 4

# -*- acsection: after-main -*-

kraj = False
sat = pg.time.Clock()    # sat koji određuje broj frejmova u sekundi
while not(kraj):
    novi_frejm()
    crtanje()
    pg.display.update()  # ažuriramo prikaz sadržaja ekrana

    # proveravamo da li je korisnik isključio prozor
    for dogadjaj in pg.event.get():
        if dogadjaj.type == pg.QUIT: # isključivanje prozora
            kraj = True

    sat.tick(5) # pauziramo do sledeceg frejma

pg.quit()  # isključivanje rada biblioteke PyGame
