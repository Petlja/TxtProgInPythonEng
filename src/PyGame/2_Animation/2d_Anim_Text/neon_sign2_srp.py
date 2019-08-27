import pygame as pg, petljapg

tekst = "ПАЈТОН"
br_slova = len(tekst)
(sirina, visina) = (br_slova * 70, 100)
prozor = petljapg.open_window(sirina, visina, "Реклама")

# Imamo po jedan frejm za svako slovo, plus 
# jedan frejm za iskljucivanje i tri za ukljucivanje svih slova
br_frejmova = br_slova + 4

font = pg.font.SysFont("Arial", 80) # font kojim će biti prikazan tekst

# Svaki tekst se prikazuje na istoj poziciji, koju ovde izracunavamo
slika_teksta = font.render(tekst, True, pg.Color("yellow"))
x = (sirina - slika_teksta.get_width()) // 2
y = (visina - slika_teksta.get_height()) // 2
i_frejm  = 0

def nov_frejm():
    global i_frejm
    
    prozor.fill(pg.Color("black")) 
    if i_frejm < br_slova: # ako treba ukljuciti neki pocetni deo teksta
        slika_teksta = font.render(tekst[:i_frejm+1], True, pg.Color("yellow"))
        prozor.blit(slika_teksta, (x, y))
    elif i_frejm == br_slova:
        pass # ovo je frejm u kome se nista ne prikazuje
    else:
        # ovo je jedan od poslednja tri frejma, prikazuje se ceo tekst
        slika_teksta = font.render(tekst, True, pg.Color("yellow"))
        prozor.blit(slika_teksta, (x, y))
                
    # pripremamo se za sledeci frejm
    i_frejm = (i_frejm + 1) % br_frejmova

petljapg.frame_loop(2, nov_frejm)
