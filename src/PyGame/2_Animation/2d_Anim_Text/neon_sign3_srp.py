import pygame as pg, petljapg

tekst = "ПАЈТОН"
br_slova = len(tekst)
# po jedan frejm za svako slovo, plus 3 puta po dva frejma za treperenje
# (treperenje sadrzi jedan frejm sa svim slovima i jedan bez slova)
br_frejmova = br_slova + 6

(sirina, visina) = (br_slova * 70, 100)
prozor = petljapg.open_window(sirina, visina, "Реклама")

x = [0]                   # x koordinata prvog slova
for i in range(1, br_slova):
    x.append(x[-1] + 70)  # svako sledece slovo je 70 piksela desno
y = 0 # y koordinate svih slova
font = pg.font.SysFont("Arial", 80) # font kojim će biti prikazan tekst

i_frejm  = 0

def nov_frejm():
    global i_frejm
    
    prozor.fill(pg.Color("black")) # bojimo pozadinu prozora u crno
    if i_frejm < br_slova: # ako treba ukljuciti jedno slovo
        slika_teksta = font.render(tekst[i_frejm], True, pg.Color("yellow"))
        prozor.blit(slika_teksta, (x[i_frejm], y))
    else:
        # ovo je jedan od frejmova za treperenje, 
        # a u svakom drugom od njih treba da svetle sva slova
        if i_frejm % 2 == 0: # ako treba ukljuciti sva slova
            for i_slovo in range(br_slova):
                slika_teksta = font.render(tekst[i_slovo], True, pg.Color("yellow"))
                prozor.blit(slika_teksta, (x[i_slovo], y))
                
    # pripremamo se za sledeci frejm
    i_frejm = (i_frejm + 1) % br_frejmova

petljapg.frame_loop(3, nov_frejm)
