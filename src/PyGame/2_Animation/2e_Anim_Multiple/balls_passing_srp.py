import random, pygame as pg, petljapg
(sirina, visina) = (500, 300)
prozor = petljapg.open_window(sirina, visina, "Лопте")

boje = (
    pg.Color("red"), pg.Color("yellow"), pg.Color("blue"),
    pg.Color("cyan"), pg.Color("green"), pg.Color("purple")
)
 
# Loptu odredjuje polozaj (x, y), pomeraj (dx, dy), velicina (r) i boja.
def nova_lopta():
    r = random.randint(10, 30)
    x = random.randint(r, sirina - r)
    y = random.randint(r, visina - r)
    boja = random.choice(boje)
    dx, dy = 0, 0
    while dx == 0 and dy == 0: # ne zelimo lopte koje stoje
        dx = random.randint(-8, 8)
        dy = random.randint(-8, 8)
    return (x, y, dx, dy, r, boja)


# Napravimo listu od 10 lopti.
lopte = []
for _ in range(10):
    lopte.append(nova_lopta())
    
def nov_frejm():
    global lopte
    sledece_lopte = [] # lista koja ce da sadrzi sledeci polozaj lopti
    for x, y, dx, dy, r, boja in lopte:
        (x, y) = (x + dx, y + dy)
        if (x+r < 0 or x-r > sirina or y+r < 0 or y-r > visina):
            x, y, dx, dy, r, boja = nova_lopta()
            
        sledece_lopte.append((x, y, dx, dy, r, boja))
        
    lopte = sledece_lopte
    prozor.fill(pg.Color("darkgray"))
    for x, y, dx, dy, r, boja in lopte:
        pg.draw.circle(prozor, boja, (x, y), r)

petljapg.frame_loop(50, nov_frejm)
