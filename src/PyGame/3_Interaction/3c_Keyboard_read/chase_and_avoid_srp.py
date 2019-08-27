import pygame as pg, petljapg, random
br_redova, br_kolona = 15, 15
a = 30 # velicina polja
(sirina, visina) = (a* br_kolona, a * br_redova)
prozor = petljapg.open_window(sirina, visina, "Пакмен")
font = pg.font.SysFont("Arial", 30) # font kojim će biti prikazan tekst

(igrac_red, igrac_kol) = (br_redova // 2, br_kolona // 2)

br_botova = 8
botovi = []
for _ in range(br_botova):
    bot_poz = (random.randint(0,br_redova-1), random.randint(0,br_redova-1))
    botovi.append(bot_poz)

(cilj_red, cilj_kol) = (random.randint(0,br_redova-1), random.randint(0,br_redova-1))
kraj, pobeda = False, False

def nov_frejm():
    global igrac_red, igrac_kol, botovi, kraj, pobeda

    # pomeri igraca
    pritisnut = pg.key.get_pressed()
    if pritisnut[pg.K_LEFT] and (igrac_kol > 0):            igrac_kol -= 1
    if pritisnut[pg.K_RIGHT] and (igrac_kol < br_kolona-1): igrac_kol += 1
    if pritisnut[pg.K_UP] and (igrac_red > 0):              igrac_red -= 1
    if pritisnut[pg.K_DOWN] and (igrac_red < br_redova-1):  igrac_red += 1
    
    # pomeri botove
    for i in range(br_botova):
        dred, dkol = 0, 0
        if random.randint(1,5) == 1:
            dred, dkol = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        bot_red, bot_kol = botovi[i]
        bot_red += dred
        bot_kol += dkol
        if (bot_kol >= 0 and bot_kol < br_kolona and
            bot_red >= 0 and bot_red < br_redova):
            botovi[i] = bot_red, bot_kol 

    # ima li sudara?
    for bot_red, bot_kol in botovi:
        if bot_red == igrac_red and bot_kol == igrac_kol:
            kraj, pobeda = True, False
    if cilj_red == igrac_red and cilj_kol == igrac_kol:
        kraj, pobeda = True, True

    prozor.fill(pg.Color("gray"))   # bojimo prozor u sivo

    if kraj:
        if pobeda: 
            sl = font.render('Браво!', True, pg.Color("red"))
        else:
            sl = font.render('Штета!', True, pg.Color("blue"))
        prozor.blit(sl, (0, 0))
    else:
        # crtamo 'igraca'
        (x, y) = (igrac_kol * a + a//2, igrac_red * a + a//2)
        pg.draw.circle(prozor, pg.Color('yellow'), (x, y), a // 3)
        
        (x, y) = (cilj_kol * a + a//2, cilj_red * a + a//2)
        pg.draw.circle(prozor, pg.Color('white'), (x, y), a // 5)
        
        # crtamo botove
        for bot_red, bot_kol in botovi:
            (x, y) = (bot_kol * a + a//2, bot_red * a + a//2)
            pg.draw.circle(prozor, pg.Color('black'), (x, y), a // 5)
    
petljapg.frame_loop(15, nov_frejm)
