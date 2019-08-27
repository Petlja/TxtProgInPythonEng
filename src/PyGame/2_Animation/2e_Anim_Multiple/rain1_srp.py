import random, pygame as pg, petljapg

voda = pg.image.load('water.png')
(sirina, visina) = (voda.get_width(), voda.get_height())
prozor = petljapg.open_window(sirina, visina, "Колутови")
MARGINA = 30
BOJA_KISE = (46, 99, 113)

# kolut je opisan uredjenom cetvorkom (x, y, r, r_max), gde je 
# (x, y) centar koluta, r je velicina koluta koja se povecava 
# u svakom frejmu, a kada r dostigne vrednost r_max, kolut nestaje.
def novi_kolut():
    x = random.randint(MARGINA, sirina - MARGINA)
    y = random.randint(MARGINA, visina - MARGINA)
    r0 = 10
    r_max = random.randint(2, 5) * 10
    return (x, y, r0, r_max)

kolutovi = []
for _ in range(20):
    kolutovi.append(novi_kolut())
    
def nov_frejm():
    global kolutovi
    for i in range(len(kolutovi)):
        x, y, r, r_max = kolutovi[i]
        if r > r_max:
            kolutovi[i] = novi_kolut()
        else:
            kolutovi[i] = (x, y, r + 10, r_max)
        
    prozor.blit(voda, (0, 0))
    for kolut in kolutovi:
        x, y, r, r_max = kolut
        ra, rb = r, r/3
        pg.draw.ellipse(prozor, BOJA_KISE, (x-ra, y-rb, 2*ra, 2*rb), 1)

petljapg.frame_loop(10, nov_frejm)
