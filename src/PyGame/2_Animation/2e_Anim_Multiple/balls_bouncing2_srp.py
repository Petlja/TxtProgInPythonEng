import random, pygame as pg, petljapg
(sirina, visina) = (500, 300)
prozor = petljapg.open_window(sirina, visina, "Лопте")

boje = (
    pg.Color("red"), pg.Color("yellow"), pg.Color("blue"),
    pg.Color("cyan"), pg.Color("green"), pg.Color("purple")
)

# Napravimo listu od 10 lopti. Loptu odredjuje
# polozaj (x, y), pomeraj (dx, dy), velicina (r) i boja.
x, y, dx, dy, r, boja = [], [], [], [], [], []
for _ in range(10):
    r.append(random.randint(10, 30))
    x.append(random.randint(r[-1], sirina - r[-1]))
    y.append(random.randint(r[-1], visina - r[-1]))
    boja.append(random.choice(boje))
    kdx, kdy = 0, 0
    while kdx == 0 and kdy == 0: # ne zelimo lopte koje stoje
        kdx = random.randint(-8, 8)
        kdy = random.randint(-8, 8)
    dx.append(kdx)
    dy.append(kdy)
    
def nov_frejm():
    global x, y, dx, dy, r, boja
    for i in range(10):
        x[i] = x[i] + dx[i]
        y[i] = y[i] + dy[i]
        if x[i] - r[i] < 0 or x[i] + r[i] > sirina: 
            dx[i] = -dx[i]
        if y[i] - r[i] < 0 or y[i] + r[i] > visina: 
            dy[i] = -dy[i]
        
    prozor.fill(pg.Color("darkgray"))
    for i in range(10):
        pg.draw.circle(prozor, boja[i], (x[i], y[i]), r[i])

petljapg.frame_loop(50, nov_frejm)
