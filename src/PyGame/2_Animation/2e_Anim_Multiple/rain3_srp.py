import random, pygame as pg, petljapg

voda = pg.image.load('water.png')
(sirina, visina) = (voda.get_width(), voda.get_height())
prozor = petljapg.open_window(sirina, visina, "Киша")
voda = pg.image.load('water.png')
MAX_BR_KAPI = 50
MARGINA = 30
BOJA_KISE = (46, 99, 113)
HORIZONT_Y = int(visina * 0.6)

kapi = []
kolutovi = []

def azuriraj_kapi_i_kolutove(kapi, kolutovi):
    nove_kapi = []
    novi_kolutovi = []

    # spusti kapi
    for i in range(len(kapi)):
        x, y, y_max, d = kapi[i]
        if y + 20 <= y_max:
            nove_kapi.append((x, y + 20, y_max, d))
        else:
            novi_kolutovi.append((x, y_max, 10, 4*d))
            
    # dodaj nove kapi
    br_dodatih_kapi = min(5, MAX_BR_KAPI - len(kapi))
    for _ in range(br_dodatih_kapi):
        x, y = random.randint(MARGINA, sirina - MARGINA), 0
        y_max = random.randint(HORIZONT_Y + MARGINA, visina - MARGINA)
        d = random.randint(5, 15)
        nove_kapi.append((x, y, y_max, d))

    # povecaj kolutove
    for i in range(len(kolutovi)):
        x, y, r, r_max = kolutovi[i]
        r += 5
        if r < r_max:
            novi_kolutovi.append((x, y, r, r_max))

    return nove_kapi, novi_kolutovi

def nov_frejm():
    global kapi, kolutovi
    kapi, kolutovi = azuriraj_kapi_i_kolutove(kapi, kolutovi)
    
    prozor.blit(voda, (0, 0))
    pg.draw.rect(prozor, pg.Color("skyblue"), (0, 0, sirina, HORIZONT_Y)) # nebo
    
    # nacrtaj kapi
    for x, y, y_max, d in kapi:
        pg.draw.line(prozor, BOJA_KISE, (x, y), (x, y+d), 1)

    # nacrtaj kolutove
    for x, y, r, r_max in kolutovi:
        ra, rb = r, r/3
        pg.draw.ellipse(prozor, BOJA_KISE, (x-ra, y-rb, 2*ra, 2*rb), 1)

petljapg.frame_loop(20, nov_frejm)
