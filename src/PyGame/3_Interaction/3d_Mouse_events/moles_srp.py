import pygame as pg, petljapg, random

br_redova, br_kolona = 2, 4
krtice = []
pogodjena = []
for red in range(br_redova):
    krtice.append([0] * br_kolona)
    pogodjena.append([False] * br_kolona)

# učitavamo u listu slike krtica
slike_krtica = []   # niz koji ce da sadrzi slike
for i in range(1, 11): # učitavamo u listu slike mole1.png, ..., mole10.png
    naziv_slike = "mole" + str(i) + ".png"  # gradimo naziv slike od delova
    slike_krtica.append(pg.image.load(naziv_slike))
    
a = slike_krtica[0].get_width() # velicina slike (slike su oblika kvadrata)
(sirina, visina) = (br_kolona * a, br_redova * a)
prozor = petljapg.open_window(sirina, visina, "Кртице")
BRAON = (60, 42, 3)
broj_vidljivih_nepogodjenih = 0
broj_nepogodjenih = br_redova * br_kolona

def tekst_centar(x, y, tekst, velicina):
    font = pg.font.SysFont("Arial", velicina)
    sl = font.render(tekst, True, pg.Color("black"))
    (x, y) = (x - sl.get_width() / 2, y - sl.get_height() / 2)
    prozor.blit(sl, (x, y))

def crtaj():
    if broj_nepogodjenih == 0:
        prozor.fill(pg.Color('white'))
        tekst_centar(sirina / 2, visina / 2, "Браво", 100)
    else:
        prozor.fill(BRAON)
        for red in range(br_redova):
            for kol in range(br_kolona):
                x, y = kol * a, red * a
                prozor.blit(slike_krtica[abs(krtice[red][kol])], (x, y))

def nov_frejm():
    global broj_vidljivih_nepogodjenih
    if broj_vidljivih_nepogodjenih == 0:
        verovatnoca = 20
    else:
        verovatnoca = 100
    for red in range(br_redova):
        for kol in range(br_kolona):
            if krtice[red][kol] == 0:
                if random.randint(1, verovatnoca) == 1:
                    krtice[red][kol] = 1
                    broj_vidljivih_nepogodjenih += 1
            elif krtice[red][kol] == 9 and not pogodjena[red][kol]:
                if random.randint(1, 20) == 1:
                    krtice[red][kol] = -9
            elif krtice[red][kol] < 9:
                krtice[red][kol] += 1
            elif krtice[red][kol] < 0 and not pogodjena[red][kol]:
                krtice[red][kol] += 1
                if krtice[red][kol] == 0:
                    broj_vidljivih_nepogodjenih -= 1
    crtaj()
    
def obradi_dogadjaj(dogadjaj):
    global pogodjena, broj_nepogodjenih, broj_vidljivih_nepogodjenih
    if dogadjaj.type == pg.MOUSEBUTTONDOWN:
        for red in range(br_redova):
            for kol in range(br_kolona):
                if abs(krtice[red][kol]) >= 5:
                    (x, y) = (kol * a, red * a)
                    (xm, ym) = dogadjaj.pos
                    if x <= xm and xm <= x + a and y <= ym and ym <= y + a:
                        pogodjena[red][kol] = True
                        broj_nepogodjenih -= 1
                        broj_vidljivih_nepogodjenih -= 1
    
petljapg.frame_loop(10, nov_frejm, obradi_dogadjaj)