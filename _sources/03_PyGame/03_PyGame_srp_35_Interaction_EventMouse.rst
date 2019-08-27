Догађаји миша
-------------

У примеру "прекидач" смо показали како можемо да реагујемо у програму када корисник притисне тастер миша. Иако корисник посматра клик као једну акцију, видели смо да је за рачунар то низ догађаја који почиње догађајем типа *pg.MOUSEBUTTONDOWN*.

У наредним примерима и задацима ћемо користити укупно три типа догађаја који настају употребом миша:

- Спуштање било ког тастера миша (као у примеру са прекидачем), када *dogadjaj.type* има вредност *pg.MOUSEBUTTONDOWN*
- Подизање тастера миша, када *dogadjaj.type* има вредност *pg.MOUSEBUTTONUP*
- Покрет миша, када *dogadjaj.type* има вредност *pg.MOUSEMOTION*. Заправо, током померања миша генерише се више оваквих догађаја (сваки од њих описује неко мало померање миша у неком веома кратком временском интервалу, тако да сваки такав догађај обично описује померање тек за неколико пиксела). 

Објекти - догађаји чији је тип *pg.MOUSEBUTTONDOWN* садрже и неке додатне податке, као што су:

- *dogadjaj.pos* - позиција миша у тренутку регистровања догађаја (коришћено у примеру са прекидачем)
- *dogadjaj.button* - број од 1 до 5, који означава које дугме миша је притиснуто (1 - лево, 2 - средње, 3 - десно, 4 - скрол на горе, 5 - скрол на доле)

Неки од додатних података о догађају, које садрже објекти - догађаји типа *pg.MOUSEMOTION* су:

- dogadjaj.pos - позиција миша након догађаја померања миша
- dogadjaj.rel - уређени пар који описује колико се променила позиција миша од претходног догађаја померања миша
- dogadjaj.buttons - трочлана листа логичких вредности, које за свако од три дугмета миша (0 - лево, 1 - средње, 2 - десно) одређују да ли је било притиснуто током померања миша.

Обрада клика - вежбање
''''''''''''''''''''''

Можда нисте приметили да у програму "прекидач" из претходне лекције светло може да се укључи и искључи било којим тастером миша. То је тако јер се догађај истог типа генерише за сваки тастер миша, а ми нисмо проверавали који тастер је био притиснут приликом наступања догађаја.

.. questionnote::

    **Задатак - леви тастер као прекидач:** Ископирајте овде програм "прекидач", а затим га дорадите тако да се укључивање и искључивање сијалице може обавити само левим тастером миша.

**Помоћ:** Користите податак *dogadjaj.button*.

.. activecode:: PyGame__interact_switch_left_button_srp
    :nocodelens:
    :enablecopy:
    :playtask:
    :modaloutput:
    :includehsrc: src/PyGame/3_Interaction/3d_Mouse_events/Switch_left_button_srp.py




.. questionnote::

    **Задатак - три прекидача:** Искористите делове програма "прекидач" и направите програм који симулра рад три прекидача, као у примеру.

.. image:: ../../_images/Shema3_Off.png
   :width: 50px
.. image:: ../../_images/Shema3_On.png
   :width: 50px
.. image:: ../../_images/SwitchOff.png
   :width: 50px
.. image:: ../../_images/SwitchOn.png
   :width: 50px
.. image:: ../../_images/BulbOff.png
   :width: 50px
.. image:: ../../_images/BulbOn.png
   :width: 50px

.. activecode:: PyGame__interact_switches_srp
    :nocodelens:
    :enablecopy:
    :playtask:
    :modaloutput:
    :includehsrc: src/PyGame/3_Interaction/3d_Mouse_events/Switches_srp.py

    import pygame as pg, petljapg
    (sirina, visina) = (800, 500)
    prozor = petljapg.open_window(sirina, visina, "Прекидачи")

    shema_slike = (pg.image.load('Shema3_Off.png'), pg.image.load('Shema3_On.png'))
    prekidac_slike = (pg.image.load('SwitchOff.png'), pg.image.load('SwitchOn.png'))
    sijalica_slike = (pg.image.load('BulbOff.png'), pg.image.load('BulbOn.png'))
    
    ukljucen_prekidac = [False, False, False]
    prekidac_poz = [(100, 200), (300, 150), (300, 250)]
    sijalica_poz = (500, 100)
    
    # dovrsite program

Остали догађаји миша
''''''''''''''''''''

Као што је на почетку ове лекције речено, у програму се може реаговати и на догађаје отпуштања тастера миша и померања миша. Ради тога је потребно упоредити вредност *dogadjaj.type* са константама *pg.MOUSEBUTTONUP* и *pg.MOUSEMOTION*. Следе задаци у којима можете ово и да испробате.

.. questionnote::

    **Задатак - цртање линија:** Довршите програм тако да се помоћу њега могу цртати праве линије, као у примеру.

.. activecode:: PyGame__interact_mouse_lines1_srp
    :nocodelens:
    :enablecopy:
    :playtask:
    :modaloutput:
    :includehsrc: src/PyGame/3_Interaction/3d_Mouse_events/mouse_lines1_srp.py

    import pygame as pg, petljapg
    (sirina, visina) = (400, 400)
    prozor = petljapg.open_window(400, 400, "Линије мишем")

    mis_poz = (0, 0)
    pocetak_linije = mis_poz
    crta_se_linija = False
    ranije_linije = []

    def nov_frejm():
        prozor.fill(pg.Color("white")) # bojimo prozor u belo
        if crta_se_linija:
            pg.draw.line(prozor, pg.Color('black'), pocetak_linije, mis_poz)
        for a, b in ranije_linije:
            pg.draw.line(prozor, pg.Color('black'), a, b)

    def obradi_dogadjaj(dogadjaj):
        global crta_se_linija, pocetak_linije, mis_poz
        
        # ovde dodajte naredbe koje rade sledece:
        
        # ako je tip dogadjaja "spustanje tastera misa":
        #     rezim crtanja linije se ukljucuje
        #     pocetak linije postavljamo na trenutnu poziciju misa
        # inace, ako je tip dogadjaja "podizanje tastera misa":
        #     rezim crtanja linije se iskljucuje
        #     nova linija je od zapamcenog pocetka linije do trenutne pozicije misa
        #     u listu prethodnih linija dodajo novu liniju 
        # inace, ako je tip dogadjaja "pomeranje misa":
        #     u promenljivoj mis_poz zapamti trenutnu poziciju misa

    petljapg.frame_loop(30, nov_frejm, obradi_dogadjaj)





.. questionnote::

    **Задатак - цртање линија са брисањем:** Ископирајте доле програм за цртање линија, а затим додајте могућност да се све линије обришу кликом на десни тастер миша.

**Помоћ:** Да бисмо у програму разликовали леви и десни тастер миша, поново треба користити податак *dogadjaj.button*. Код у функцији *obradi_dogadjaj* сада треба да изгледа отприлике овако:

.. activecode:: PyGame__interact_mouse_lines2_part_srp
    :passivecode: true

        ako je tip dogadjaja  pg.MOUSEBUTTONDOWN:
            ako je pritisnuto dugme 1 (levi taster) 
                rezim crtanja linije se ukljucuje
                nova linija je od zapamcenog pocetka linije do trenutne pozicije misa
            ako je pritisnuto dugme 3 (desni taster)
                isprazni listu prethodnih linija 
        inace, ako je tip dogadjaja "podizanje tastera misa":
            ako je pritisnuto dugme 1 (levi taster)
                rezim crtanja linije se iskljucuje
                nova linija je od zapamcenog pocetka linije do trenutne pozicije misa
                u listu prethodnih linija dodajo novu liniju 
        inace, ako je tip dogadjaja "pomeranje misa":
            u promenljivoj mis_poz zapamti trenutnu poziciju misa


.. activecode:: PyGame__interact_mouse_lines2_srp
    :nocodelens:
    :enablecopy:
    :playtask:
    :modaloutput:
    :includehsrc: src/PyGame/3_Interaction/3d_Mouse_events/mouse_lines2_srp.py




.. questionnote::

    **Задатак - превлачење:** Следећи програм показује како да кориснику нашег програма омогућимо превлачење објеката.
    
    Испробајте програм (превуците јабуке у корпу) и потрудите се да га разумете, а затим одговорите на питања испод.

.. image:: ../../_images/apple.png
   :width: 50px
.. image:: ../../_images/basket.png
   :width: 50px
.. image:: ../../_images/drag_scene.png
   :width: 50px

.. activecode:: PyGame__interact_drag_srp
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :includesrc: src/PyGame/3_Interaction/3d_Mouse_events/drag_srp.py

.. mchoice:: pygame__interact_quiz_drag1_srp
   :answer_a: редни број јабуке коју цртамо
   :answer_b: редни број јабуке коју превлачимо
   :answer_c: укупан број јабука
   :answer_d: број преосталих јабука на дрвету
   :correct: b
   :feedback_a: Покушај поново
   :feedback_b: Тачно
   :feedback_c: Покушај поново
   :feedback_d: Покушај поново

   Шта представља променљива *i_jabuka* у програму? 

.. dragndrop:: pygame__interact_quiz_drag2_srp
    :feedback: Покушај поново!
    :match_1: if mis_je_na_slici(dogadjaj.pos, korpa_poz, korpa_slika):|||да ли јабуку треба обрисати
    :match_2: if mis_je_na_slici(dogadjaj.pos, pozicije_jabuka[i]|||да ли је корисник "узео" јабуку
    :match_3: if len(pozicije_jabuka) == 0:|||да ли је игра завршена
    :match_4: if i_jabuka >= 0:|||да ли је у току превлачење

    Упари провере у програму са њиховим значењем.

.. mchoice:: pygame__interact_quiz_drag3_srp
   :answer_a: очитавамо да ли је тастер миша доле током померања
   :answer_b: превлачење је посебан тип догађаја
   :answer_c: при обичном померању миша редни број "јабуке коју превлачимо" је -1
   :correct: c
   :feedback_a: То није згодан начин, јер тастер може бити притиснут на празном месту (корисник није "узео" предмет који треба да превлачи)
   :feedback_b: Не, не постоји такав тип догађаја
   :feedback_c: Тачно

   Како у програму разликујемо превлачење од обичног померања миша? 

.. commented out

    PICTURE_AS_MOUSE_CURSOR x2 - ovaj vervatno ispada jer sa novom shemom nije jasna prednost dogadjaja (svakako se crta na tik)
            
            
