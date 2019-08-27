import random, pygame as pg, petljapg
(sirina, visina) = (800, 400)
prozor = petljapg.open_window(sirina, visina, "Пахуљице")

pahulja_slika = pg.image.load("snowflake.png")  # slika pahuljice
visina_slike_pahulje = pahulja_slika.get_height()
broj_pahulja = 10                               # ukupan broj pahuljica

# nasumično generišemo pozicije pahuljica
pahulje = []
for i in range(broj_pahulja):
    x, y = random.randint(0, sirina), random.randint(0, visina)
    pahulje.append((x, y))

def nov_frejm():
    global pahulje

    # pahulje koje još nisu pale pomeramo na dole i prebacujemo u novu listu
    nove_pahulje = []
    for x, y in pahulje:
        if y + visina_slike_pahulje < visina:
            nove_pahulje.append((x, y+1))
            
    # dopunjavamo listu novim pahuljama, koje pocinju da padaju sa vrha prozora
    while len(nove_pahulje) < broj_pahulja:
        x, y = random.randint(0, sirina), random.randint(-visina_slike_pahulje, 0)
        nove_pahulje.append((x, y))
        
    pahulje = nove_pahulje
    prozor.fill(pg.Color("white"))    # bojimo pozadinu u belo
    for (x, y) in pahulje:            # crtamo sve pahulje
        prozor.blit(pahulja_slika, (x, y))

petljapg.frame_loop(50, nov_frejm)
