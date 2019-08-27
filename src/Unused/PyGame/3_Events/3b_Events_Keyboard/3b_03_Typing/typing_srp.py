# -*- acsection: general-init -*-
import pygame as pg, time

pg.init() # uključujemo rad biblioteke PyGame
pg.display.set_caption("Куцање - пуцање")
(sirina, visina) = (600, 400)
prozor = pg.display.set_mode((sirina, visina))   # otvaramo prozor

# -*- acsection: main -*-

def crtanje():
    prozor.fill(pg.Color("black"))    # bojimo prozor u crno
    font = pg.font.SysFont("Arial", 40)
    tekst = font.render(otkucana_rec, True, pg.Color("green"))
    (sirina_teksta, visina_teksta) = (tekst.get_width(), tekst.get_height())
    (x, y) = ((sirina - sirina_teksta) // 2, (visina - visina_teksta) // 2)
    prozor.blit(tekst, (x, y))

def obradi_dogadjaj(dogadjaj):
    global treba_crtati, otkucana_rec, vreme_poslednjeg_kucanja
    if dogadjaj.type == pg.KEYDOWN: # pritisak tastera na tastaturi
        otkucano_slovo = dogadjaj.unicode
        if otkucano_slovo.upper() in 'АБВГДЂЕЖЗИЈКЛЉМНЊОПРСТЋУФХЦЋЏШ .,':
            vreme = time.time()
            # ako je od poslednjeg otkucanog slova proslo manje od pola sekunde
            if(vreme-vreme_poslednjeg_kucanja < 0.5):
                # dodaj slovo na otkucanu rec
                otkucana_rec = otkucana_rec + otkucano_slovo
            else:
                # inace pocni novi tekst
                otkucana_rec = otkucano_slovo
            vreme_poslednjeg_kucanja = vreme
            return True
    return False
            
otkucana_rec = ''
vreme_poslednjeg_kucanja = time.time()

# -*- acsection: after-main -*-

treba_crtati = True
kraj = False
while not(kraj):
    if treba_crtati:
        crtanje()
        pg.display.update()  # ažuriramo prikaz sadržaja ekrana
        treba_crtati = False # ne treba crtati do daljnjeg

    dogadjaj = pg.event.wait()      # čekamo naredni dogadjaj
    if dogadjaj.type == pg.QUIT:    # isključivanje prozora
        kraj = True
    else:
        treba_crtati = obradi_dogadjaj(dogadjaj)

pg.quit()  # isključivanje rada biblioteke PyGame
