import random, pygame as pg, petljapg

voda = pg.image.load('water.png')
(sirina, visina) = (voda.get_width(), voda.get_height())
prozor = petljapg.open_window(sirina, visina, "Капи")
MAX_BR_KAPI = 50
MARGINA = 30
BOJA_KISE = (46, 99, 113)
HORIZONT_Y = int(visina * 0.6)

kapi = []

# kap je kratka uspravna liija, koja se spusta u svakom frejmu.
# Odredjena je gornjom tackom (x,y), krajnjom tackom y_max i duzinom d.
# Kada kap stigne do y_max, ona nestaje.
def nov_frejm():
    global kapi
    nove_kapi = []
    for i in range(len(kapi)):
        x, y, y_max, d = kapi[i]
        if y + 20 <= y_max:
            nove_kapi.append((x, y + 20, y_max, d))
            
    br_dodatih_kapi = min(5, MAX_BR_KAPI - len(kapi))
    for _ in range(br_dodatih_kapi):
        x, y = random.randint(MARGINA, sirina - MARGINA), 0
        y_max = random.randint(HORIZONT_Y + MARGINA, visina - MARGINA)
        d = random.randint(5, 15)
        nove_kapi.append((x, y, y_max, d))
            
    kapi = nove_kapi
    prozor.blit(voda, (0, 0))
    pg.draw.rect(prozor, pg.Color("skyblue"), (0, 0, sirina, HORIZONT_Y)) # nebo
    for x, y, y_max, d in kapi:
        pg.draw.line(prozor, BOJA_KISE, (x, y), (x, y+d), 1)

petljapg.frame_loop(20, nov_frejm)
