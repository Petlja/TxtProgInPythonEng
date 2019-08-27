Догађаји тастатуре
------------------

Од догађаја који настају употребом тастатуре најважнији је догађај спуштања тастера, па ћемо се њиме највише и бавити. Приликом спуштања тастера на тастатури, у објекту *dogadjaj* који представља догађај у нашим програмима, вредност *dogadjaj.type* ће бити ``pg.KEYDOWN``.

Када констатујемо да је неки тастер на тастатури притиснут, скоро увек нас интересује који је то тастер. Ово можемо сазнати испитивањем вредности ``dogadjaj.key``. У лекцији о очитавању стања тастатуре већ смо поменули да за сваки тастер постоји именована константа која одговара том тастеру. Подсетимо се имена ових константи за неке често провераване тастере (комплетан списак ових константи можете да видите `овде <https://www.pygame.org/docs/ref/key.html>`__ ):

============ ==============
константа    тастер
============ ==============
pg.K_LEFT    стрелица лево
pg.K_RIGHT   стрелица десно
pg.K_UP      стрелица горе
pg.K_DOWN    стрелица доле
pg.K_SPACE   размак
pg.K_a       тастер *a*
pg.K_b       тастер *b*
pg.K_c       тастер *c*
============ ==============

Вредност поља *dogadjaj.key* говори о ком се физичком тастеру ради и та вредност је погодна за тастере попут стрелица, *Ctrl*, *Shift*, *Alt*, *Home*, *End* и сличних. Када се ради о тексту, може да буде згодније да користимо вредност поља ``dogadjaj.unicode``, која садржи управо откуцани знак (као стринг од једног карактера).

Следећи пример илуструје како може да се испитује притисак на тастер, односно догађај типа *pg.KEYDOWN*.

.. questionnote::

    **Пример - укрштеница** 
    
    У овом примеру корисник може помоћу стрелица на тастатури да премешта оквир и да уноси слова у квадратиће. 
    
Обратите пажњу на функцију  *obradi_dogadjaj* у којој се дешава провера типа догађаја, а затим, ако се ради о притиску на тастер, проверавају се додатне информације о догађају, записане у пољима *dogadjaj.key* и *dogadjaj.unicode*.

Успут можете да покушате да саставите неке занимљиве укрштене речи.

.. activecode:: PyGame__interact_crossword_srp
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :includesrc: src/PyGame/3_Interaction/3e_Keyboard_events/crossword_srp.py
    
Упоредимо овај програм са програмом "Навигација" из лекције о очитавању стања тастатуре:

=========================================================== =============================================================
У програму "Навигација"                                     У програму "Укрштеница"
=========================================================== =============================================================
жути круг се кретао за по један пиксел - клизио је          оквир се креће за по једно поље - скаче
нисмо имали прецизну контролу где ће се круг зауставити     прецизно контролишемо где ће се оквир зауставити
није нам ни било важно где ће се тачно круг зауставити      важно нам је где ће се тачно оквир зауставити
очитавали смо стање тастера на тастатури (доле или горе)    користимо догађај (спуштање тастера)
=========================================================== =============================================================


.. questionnote::

    **Задатак - навигација по пољима** 
    
    Напишите програм који ради као у примеру (дугме "Прикажи пример"). 
    
    Корисник помоћу стрелица на тастатури може да води лика представљеног жутим кругом. Лик се креће по пољима на којима се налазе беле тачке.
    

.. activecode:: PyGame__interact_pacman1_srp
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask:
    :includehsrc: src/PyGame/3_Interaction/3e_Keyboard_events/pacman1_srp.py
    
    import pygame as pg, petljapg
    br_redova, br_kolona = 10, 10
    a = 50 # velicina polja
    (sirina, visina) = (a* br_kolona, a * br_redova)
    prozor = petljapg.open_window(sirina, visina, "Пакмен")

    (lik_red, lik_kol) = (br_redova // 2, br_kolona // 2)

    def nov_frejm():
        prozor.fill(pg.Color("black"))   # bojimo prozor u crno

        # bele kuglice
        for x in range(a // 2, sirina, a):
            for y in range(a // 2, visina, a):
                pg.draw.circle(prozor, pg.Color("white"), (x, y), 3)
       
        # OVDE DODAJTE NAREDBE ZA CRTANJE ZUTOG KRUGA
        
    def obradi_dogadjaj(dogadjaj):
        global lik_red, lik_kol
        # OVDE DODAJTE NAREDBE ZA OBRADU DOGADJAJA
        
    petljapg.frame_loop(30, nov_frejm, obradi_dogadjaj)





.. questionnote::

    **Задатак - прављење лавиринта** 
    
    Напишите програм који прави лавитинт. Црвени оквир треба да се помера помоћу стрелица, а притиском на размак да се мења боја поља (из црне у белу и обрнуто).
    
Када решите задатак, испробајте следеће:

- кликните на дугме "Прикажи пример" (овај пут програм из примера ради више од онога што је био ваш задатак)
- направите лавиринт какав желите
- притисните (латинично) *S* за старт и посматрајте
- притисните (латинично) *P* за паузу, тј. заустављање или наставак трагања
    
.. commented out

    Овде би било идеално да ученици не могу да пробају претрагу пре него што реше задатак

.. activecode:: PyGame__interact_labyrinth_srp
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :includehsrc: src/PyGame/3_Interaction/3e_Keyboard_events/labyrinth_edit_and_search_srp.py
    
    import pygame as pg, petljapg, random
    a = 50 # velicina polja
    br_redova = 12
    br_kolona = 20
    (sirina, visina) = (br_kolona * a, br_redova * a)
    prozor = petljapg.open_window(sirina, visina, "Лавиринт")

    def nov_frejm():
        prozor.fill(pg.Color('white')) # bela pozadina
        for red in range(br_redova):
            for kol in range(br_kolona):
                if tabla[red][kol] == 1: # zid
                    pg.draw.rect(prozor, pg.Color('black'), (kol * a, red * a, a, a))

        # okvir
        pg.draw.rect(prozor, pg.Color('red'), (okvir_kol * a, okvir_red * a, a, a), 3)
        
    def obradi_dogadjaj(dogadjaj):
        global tabla, okvir_red, okvir_kol
        
        # OVDE DODAJTE NAREDBE ZA OBRADU PRITISAKA NA RAZMAK I STRELICE

    tabla = []
    for j in range(br_redova):
        tabla.append([])
        for i in range(br_kolona):
            tabla[-1].append(random.randint(0, 1))
            
    (okvir_red, okvir_kol) = (0, 0)
    petljapg.frame_loop(10, nov_frejm, obradi_dogadjaj)


Бонус - програм за вежбање куцања
'''''''''''''''''''''''''''''''''

Програм који следи, служи за вежбање куцања. Програм јесте дугачак, али требало би да можете да разумете његов велики део. 

Можда ћете желети (без обавезе) да прилагодите програм својим потребама, нарочито у почетку коришћења. На пример:

- да успорите (или касније да убрзате) падање слова
- да не губите поене кад погрешите
- када добро увежбате слова која прва падају, да их избаците из листе слова за вежбу
- да знаци који падају буду само цифре и знаци операција (ако желите да вежбате куцање само на нумеричкој тастатури десно)
- да притисак на размак брише најниже слово (уз неко смањивање поена) 

или било шта друго чега се сетите.
    
Када будете имали времена, свакако покушајте и да направите што бољи резултат (без варања).

.. activecode:: PyGame__interact_typing_tutor_srp
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :includesrc: src/PyGame/3_Interaction/3e_Keyboard_events/typing_tutor_srp.py
