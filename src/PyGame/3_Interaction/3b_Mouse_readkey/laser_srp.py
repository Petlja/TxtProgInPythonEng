import pygame as pg, petljapg
sirina, visina = 400, 400
prozor = petljapg.open_window(sirina, visina, "Ласер")

laser_ukljucen = False
energija = 25 # koliko je laser pun od 0 do 100 

def crtanje():
    prozor.fill(pg.Color("black")) # pozadina
    
    # indikator pokazuje koliko je laser pun
    pg.draw.rect(prozor, pg.Color("green"), (10, 10, 100, 10), 1)
    pg.draw.rect(prozor, pg.Color("green"), (10, 10, energija, 10))
    
    if laser_ukljucen:
        domet = (4 * energija, visina - 4 * energija)
        pg.draw.line(prozor, pg.Color("red"), (0, visina), domet, 5)

def nov_frejm():
    global energija, laser_ukljucen
    
    pritisnut_taster_misa = pg.mouse.get_pressed()
    laser_ukljucen = pritisnut_taster_misa[0] # levi taster 
    if laser_ukljucen:
        if energija > 0:  # ako se nije ispraznio
            energija -= 1 # laser se prazni
    else:
        # laser se puni, ali najvise do 100
        energija = min(energija + 2, 100)

    crtanje()

petljapg.frame_loop(15, nov_frejm)
