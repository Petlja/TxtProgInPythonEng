import random, pygame as pg, petljapg
(sirina, visina) = (500, 300)
prozor = petljapg.open_window(sirina, visina, "Лопте")
cx, cy = sirina // 2, visina // 2

# Zvezdu odredjuje polozaj (x, y) i velicina (r).
def nova_zvezda():
    r = random.randint(1, 3)
    x = random.randint(r, sirina - r)
    y = random.randint(r, visina - r)
    return (x, y, r)

# Napravimo listu zvezda.
br_zvezda = 40
zvezde = []
for _ in range(br_zvezda):
    zvezde.append(nova_zvezda())
    
def nov_frejm():
    global zvezde
    sledece_zvezde = [] # lista koja ce da sadrzi novo stanje
    for x, y, r in zvezde:
        x += 0.01 * (x-cx) # x se udaljava od centra prozora
        y += 0.01 * (y-cy) # y se udaljava od centra prozora
        r *= 1.01          # zvezdu vidimo kao vecu, jer se "priblizavamo"
        # ako je bar jos deo zvezde u prozoru, sacuvacemo je
        if (x+r > 0 and x-r < sirina and y+r > 0 and y-r < visina):
            sledece_zvezde.append((x, y, r))
            
    while len(sledece_zvezde) < br_zvezda:
        sledece_zvezde.append(nova_zvezda())

    zvezde = sledece_zvezde
    prozor.fill(pg.Color("black"))
    for x, y, r in zvezde:
        ix, iy, ir = int(x), int(y), int(r)
        pg.draw.circle(prozor, pg.Color('white'), (ix, iy), ir)

petljapg.frame_loop(60, nov_frejm)
