Очитавање тастера миша
----------------------

Информацију о тренутно притиснутим тастерима миша даје нам функција ``pg.mouse.get_pressed()``. Ова функција враћа торку од три елемента (уређену тројку), који се користе као логичке вредности. Елементи торке редом одговарају левом, средњем и десном тастеру миша. Вредност *True* означава да је тастер притиснут, а *False* да није.

Пример наведен ниже показује како се очитава који тастери миша су притиснути. Овако изгледа део програма у коме се то дешава:

.. activecode:: PyGame__interact_put_ball_into_box_part_srp
    :passivecode: true

    pritisnut_taster_misa = pg.mouse.get_pressed()
    
    if pritisnut_taster_misa[2]: # desni taster - nova igra
        (x, y) = (sirina//2, visina//2) # vracamo lopticu u centar
        pobedio, izgubio = False, False # igrac nije ni pobedio ni izgubio
        
    if pritisnut_taster_misa[0]: # levi taster - pomeri lopticu
        (xm, ym) = pg.mouse.get_pos() # koordinate pozicije misa
        # loptica se pomera od misa za jos pola tog rastojanja
        x = x - 0.5 * (xm - x)
        y = y - 0.5 * (ym - y)

Торка *pritisnut_taster_misa* добија три вредности које је вратила функција *pg.mouse.get_pressed()*. Те вредности касније типично користимо у *if* наредбама. На пример, *if pritisnut_taster_misa[2]* значи "ако је притиснут десни тастер" (0 за леви, 1 за средњи, а 2 за десни).

Примери и задаци
''''''''''''''''

.. questionnote::

    **Пример - убаци лоптицу:** Док је леви тастер миша притиснут, лоптица се удаљава од миша. Циљ је померањем миша и притискањем левог тастера постићи да лоптица буде у црвеном оквиру. Притиском на десни тастер игра се враћа на почетак.
    
Најпре пажљиво погледајте функцију *nov_frejm()*, а затим и остале делове програма. Испробајте програм и проверите да ли он ради онако како сте очекивали на основу читања.
    
.. activecode:: PyGame__interact_put_ball_into_box_srp
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :includesrc: src/PyGame/3_Interaction/3b_Mouse_readkey/put_ball_into_box_srp.py    



.. questionnote::

    **Задатак - ка и од миша:** Довршите програм, тако да ради као у примеру (дугме "Прикажи пример").
    
    - Када је леви тастер миша притиснут, лоптица треба да се удаљава од миша, као у примеру "убаци лоптицу" датом изнад, али не за по пола растојања, него само за по десети део растојања до миша. 
    - Када леви тастер миша није притиснут, лоптица треба да се пиближава за по десети део растојања до миша (као у задатку "према мишу" из претходне лекције).
    
.. activecode:: PyGame__interact_to_and_from_mouse_srp
    :nocodelens:
    :modaloutput:
    :playtask:
    :includehsrc: src/PyGame/3_Interaction/3b_Mouse_readkey/to_and_from_mouse_srp.py
    
    import pygame as pg, petljapg
    (sirina, visina) = (400, 400)
    prozor = petljapg.open_window(sirina, visina, "Ка и од миша")

    (x, y) = (sirina // 2, visina // 2) # loptica krece iz centra

    def nov_frejm():
        global x, y
        
        # DODAJTE DEO KOJI NEDOSTAJE
        
        # crtamo zelenu lopticu na beloj pozadini
        prozor.fill(pg.Color("white")) 
        pg.draw.circle(prozor, pg.Color("green"), (int(x), int(y)), 10)

    petljapg.frame_loop(50, nov_frejm)


.. questionnote::

    **Задатак - ласер:** Довршите програм тако да ради као у примеру (дугме "Прикажи пример").
    
    Док је леви тастер миша притиснут, "ласер" је укључен, иначе је искључен. Док је ласер укључен, енергија му се смањује за по 1 (али не испод 0), а кад је искључен енергија се повећава за по 2 (али не преко 100).
    

.. activecode:: PyGame__interact_laser_srp
    :nocodelens:
    :modaloutput:
    :playtask:
    :includehsrc: src/PyGame/3_Interaction/3b_Mouse_readkey/laser_srp.py

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
        
        # OCITAJTE STANJE LEVOG TASTERA MISA I POSTAVITE VREDNOSTI 
        # GLOBALNIH PROMENLJIVIH energija, laser_ukljucen

        crtanje()

    petljapg.frame_loop(15, nov_frejm)


.. commented out

    .. questionnote::

        **Задатак - боја позадине:** Овај једноставан пример само илуструје очитавање стања тастера миша. Док је притиснут леви тастер позадина постаје светлија, а док је притиснут десни тастер позадина постаје тамнија.
        

    .. activecode:: PyGame__interact_bg_color_srp
        :nocodelens:
        :modaloutput:
        :includesrc: src/PyGame/3_Interaction/3b_Mouse_readkey/bg_color_srp.py




