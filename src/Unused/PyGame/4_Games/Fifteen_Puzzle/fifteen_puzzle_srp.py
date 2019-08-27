# -*- acsection: general-init -*-
import random
import pygame as pg

pg.init() # inicijalizujemo rad biblioteke PyGame
pg.display.set_caption("Клизна слагалица")  # otvaramo prozor
(sirina, visina) = (400, 400)
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

# pokušavamo da pomerimo rupu na polje_v, polje_k
def pomeri_rupu(polje_v, polje_k):
    global rupa_v, rupa_k, slagalica                                      # globalne promenljive koje ćemo modifikovati
    if 0 <= polje_v and polje_v < DIM and \
       0 <= polje_k and polje_k < DIM:                                    # polje mora biti unutar slagalice
        (dv, dk) = (abs(polje_v - rupa_v), abs(polje_k - rupa_k))         # polje mora biti susedno rupi
        if (dv == 1 and dk == 0) or (dv == 0 and dk == 1):
            (slagalica[rupa_v][rupa_k], slagalica[polje_v][polje_k]) = \
            (slagalica[polje_v][polje_k], slagalica[rupa_v][rupa_k])      # razmenjujemo broj na polju i broj na rupi
            (rupa_v, rupa_k) = (polje_v, polje_k)                         # pomeramo rupu
            return True                                                   # uspešno smo pomerili rupu
    return False                                                          # nismo uspeli da pomerimo rupu

# nasumično mešamo slagalicu
def promesaj_slagalicu():
    global rupa_v, rupa_k, slagalica                             # globalne promenljive koje ćemo modifikovati
    smerovi = [(-1, 0), (1, 0), (0, -1), (0, 1)]                 # četiri moguća smera pomeranja
    max_broj_pomeranja = 100                                     # mešamo tako što rupu pomerimo 100 puta
    broj_pomeranja = 0                                           # broj izvršenih pomeranja
    while broj_pomeranja < max_broj_pomeranja:                   # dok je broj izvršenih pomeranja manji od maksimalnog 
        (smer_v, smer_k) = smerovi[random.randint(0, 3)]         #    nasumično biramo smer u kojem se pomera rupa
        (polje_v, polje_k) = (rupa_v + smer_v, rupa_k + smer_k)  #    određujemo novu potencijalnu poziciju rupe
        if pomeri_rupu(polje_v, polje_k):                        #    pokušavamo da pomerimo rupu na novo polje
            broj_pomeranja += 1                                  #    ako smo uspeli, uvecavamo broj pomeranja

# provera da li je slagalica složena ispravno
def slagalica_slozena():
    # proveravamo da li postoji polje na kom se nalazi pogrešan broj
    for v in range(DIM):
        for k in range(DIM):
            if slagalica[v][k] != v*DIM+k+1:
                return False  # broj na polju[v][k] je pogrešan
    return True  # nismo naišli na pogrešan broj

DIM = 4                        # dimenzija slagalice je 4x4
SIRINA_KOLONE = sirina // DIM  # širina kolone u pikselima
VISINA_VRSTE = visina // DIM   # širina vrste u pikselima

slagalica = [[DIM*v + k + 1 for k in range(DIM)] for v in range(DIM)] # inicijalno slagalicu popunjavamo redom brojevima od 1 do n*n
(rupa_v, rupa_k) = (DIM-1, DIM-1)                                     # prazno polje je u donjem desnom uglu
promesaj_slagalicu()                                                  # pre početka igre mešamo slagalicu


def prikazi_slagalicu():
    prozor.fill(pg.Color("white"))        # bojimo pozadinu u belo
    font = pg.font.SysFont("Arial", 40)   # font kojim će biti ispisani brojevi
    # prolazimo redom kroz sva polja
    for v in range(DIM):
        for k in range(DIM):
            rect = (k*SIRINA_KOLONE, v*VISINA_VRSTE, SIRINA_KOLONE, VISINA_VRSTE)  # okružujući pravougaonik tekućeg polja
            if v == rupa_v and k == rupa_k:                                        # ako je na tekućem polju rupa
                pg.draw.rect(prozor, pg.Color("black"), rect)                      # iscrtavamo je pomoću potpuno crnog kvadrata
            else:
                pg.draw.rect(prozor, pg.Color("black"), rect, 1)                                # iscrtavamo okvir polja
                (xc, yc) = (k*SIRINA_KOLONE + SIRINA_KOLONE/2, v*VISINA_VRSTE + VISINA_VRSTE/2) # centar okvira polja
                tekst = font.render(str(slagalica[v][k]), True, pg.Color("black"))              # ispisujemo centriran tekst
                (sirina_teksta, visina_teksta) = (tekst.get_width(), tekst.get_height())
                prozor.blit(tekst, (xc - sirina_teksta/2, yc - visina_teksta/2))

def prikazi_cestitku():
    prozor.fill(pg.Color("white"))                                           # bojimo pozadinu prozora u belo
    font = pg.font.SysFont("Arial", 60)                                      # font kojim će biti prikazan tekst
    poruka = "Браво!"                                                        # poruka koja će se ispisivati
    tekst = font.render(poruka, True, pg.Color("black"))                     # sličica koja predstavlja tu poruku ispisanu crnom bojom
    (sirina_teksta, visina_teksta) = (tekst.get_width(), tekst.get_height()) # određujemo veličinu tog teksta
    (x, y) = ((sirina - sirina_teksta) / 2, (visina - visina_teksta) / 2)    # položaj određujemo tako da tekst bude centriran
    prozor.blit(tekst, (x, y))                                               # prikazujemo sličicu na odgovarajućem mestu na ekranu

def crtaj():
    if not slagalica_slozena(): # slagalica još nije složena, pa je prikazujemo
        prikazi_slagalicu()
    else:  # slagalica je složena uspešnо, pa čestitamo igraču            
        prikazi_cestitku()
                
def obradi_dogadjaj(dogadjaj):
    global v, k, slagalica
    if slagalica_slozena():  # ako je slagalica složena, ne obrađujemo više događaje
        return
    if dogadjaj.type == pg.MOUSEBUTTONDOWN:  # klik dugmeta miša
        (x, y) = dogadjaj.pos                # koordinate na koje je kliknuto
        v = y // VISINA_VRSTE                # vrsta na koju je kliknuto
        k = x // SIRINA_KOLONE               # kolona na koju je kliknuto
        if pomeri_rupu(v, k):                # ako uspemo da pomerimo rupu na to polje
            return True                      # treba ponovo da crtamo
    return False                             # ne treba ponovo da crtamo
                
# -*- acsection: after-main -*-

# glavna petlja
kraj = False
treba_crtati = True
while not kraj:
    if treba_crtati:
        crtaj()
        pg.display.update()         # ažuriramo prikaz sadržaja prozora
        treba_crtati = False
    dogadjaj = pg.event.wait()      # čekamo na naredni događaj
    if dogadjaj.type == pg.QUIT:    # događaj isključivanja prozora
        kraj = True
    else:
        treba_crtati = obradi_dogadjaj(dogadjaj)
pg.quit()  # isključujemo rad biblioteke Pygame
