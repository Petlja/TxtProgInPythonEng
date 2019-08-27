Израда сложенијих цртежа помоћу петљи
-------------------------------------

Правилност коју желимо да искористимо на цртежима може да буде и нешто сложенија. Ево неких примера:

.. image:: ../../_images/PyGame/repeat_alternating.png 
   :width: 800px
   :align: center 

У свим овим случајевима правилност и даље постоји и може да се искористи при писању програма. Осим тога, можемо да приметимо да примери са слике сви имају нешто заједничко, а то је да се наизменично појављјују два правила. На пример, на цртежу са циглама први ред почиње целом циглом, други половином цигле, трећи опет целом и тако даље. Слично томе, на цртежу зграде се наизименично појављују осветљени и затамњени прозори.

Због наизменичног појављивања два правила на цртежима, и програми који их цртају ће имати неких сличности. Погледајмо примере.

Пример - рајсфершлус
''''''''''''''''''''

Да бисмо нацртали овакав рајсфершлус, линије ћемо свакако цртати у петљи. Са цртежа се види да је свака следећа линија за исти број пиксела ниже од претходне, тако да не би требало да буде проблема са рачунањем :math:`y` координата. Нешто је тежа ситуација са :math:`x` координатама, јер се оне мењају по мало сложенијем правилу.

Овај проблем можемо да решимо помоћу *if* наредбе у петљи. Након цртања једне линије, проверавамо коју од две могуће вредности има :math:`x` координата почетка линије, па ако има прву вредност - додељујемо јој другу и обрнуто. Ево како то изгледа у програму:

.. activecode:: PyGame_zipper1
   :nocodelens:
   :enablecopy:
   :modaloutput:
   :includesrc: src\PyGame\1_Drawing\7c_Loops_alternating\Examples\zipper1_srp.py

Друга могућност да решимо проблем са :math:`x` координатама је да у једном проласку кроз петљу цртамо по две линије, на пример овако:

.. activecode:: PyGame_zipper2
   :nocodelens:
   :enablecopy:
   :modaloutput:
   :includesrc: src\PyGame\1_Drawing\7c_Loops_alternating\Examples\zipper2_srp.py


Пример - Цигле
''''''''''''''

Већ смо поменули да редови цигала наизменично почињу целом циглом и половином цигле. Зато при цртању цигала можемо да искористимо исте две идеје као и у претходном примеру. 

Нека је дужина цигле означена са :math:`a`, а њена висина са :math:`h`. Целу циглу на почетку реда добијамо тако што цртамо правоугаоник од тачке на датој висини, са :math:`x` координатом једнаком нули. Половину цигле на почетку реда можемо да добијемо тако што нацртамо целу циглу померену за :math:`a \over 2` улево, то јест тако што цртамо правоугаоник од тачке на истој висини, али са :math:`x` координатом једнаком :code:`-a // 2`. Тако постижемо да се види само десна половина цигле. Остаје да решимо када цртамо померену циглу а када не.

Једно решење је да место почетка реда цигала чувамо у променљивој, назовимо је *x_poc*. После сваког исцртаног реда, проверавамо да ли променљива *x_poc* има вредност нула или :code:`-a // 2`. Као и у претходном примеру, коју год од ове две вредности променљива имала, доделићемо јој ону другу вредност, да би у следећем реду цртање цигала почело другачије.

Довршите наредбе за додељивање вредности променљивој *x_poc*.

.. activecode:: PyGame_loops_bricks1
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask:
    :includexsrc: src\PyGame\1_Drawing\7c_Loops_alternating\Examples\bricks1_srp.py

    prozor.fill(pg.Color("red"))
    a_cigle, h_cigle = 80, 40
    x_poc = 0
    for y0 in range(0, visina, h_cigle): # Za svaki red cigala
        for x0 in range(x_poc, sirina, a_cigle): # Za svaku ciglu u redu
            pg.draw.rect(prozor, pg.Color("black"), (x0, y0, a_cigle, h_cigle), 1)
            
        if x_poc == ???: # dopunite
            x_poc = -a_cigle//2
        else:
            x_poc = ??? # dopunite

Друга идеја је да у сваком проласку кроз двоструку петљу цртрамо циглу коју смо цртали и у првом решењу, а осим ње и циглу испод и полу-лево од ње. Приметите да у том случају петља по *y0* има двоструко већи корак, јер унутрашња петља црта два реда цигала.

Довршите наредбе за цртање правоугаоника у овом програму.

.. activecode:: PyGame_loops_bricks2
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :includexsrc: src\PyGame\1_Drawing\7c_Loops_alternating\Examples\bricks2_srp.py

    prozor.fill(pg.Color("red"))
    a_cigle, h_cigle = 80, 40
    for y0 in range(0, visina, 2 * h_cigle):
        for x0 in range(0, sirina, a_cigle):
            #crtamo prvu ciglu
            pg.draw.rect(???) # dopunite kao malopre
            
            # druga cigla je u sledecem redu, pomerena za pola sirine ulevo
            x1, y1 = x0 - a_cigle//2, y0 + h_cigle 
            pg.draw.rect(???) # dopunite crtanje druge cigle


Задаци за вежбу
'''''''''''''''

.. questionnote::

    **Задатак - шаховска табла**

    Нацртати шаховску таблу преко целог прозора (поља табле треба да буду величине 50х50 пиксела). Доње лево поље треба да буде тамне боје.

.. activecode:: PyGame_loops_chessboard
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask:
    :includexsrc: src\PyGame\1_Drawing\7c_Loops_alternating\Tasks\chessboard1_srp.py
    
    # bojimo pozadinu prozora u sivo za svetla polja
    prozor.fill(pg.Color("gray"))   
    
    brojPolja = 8
    sirinaPolja = sirina / brojPolja
    visinaPolja = visina / brojPolja

    # prolazimo kroz sva polja
    for i in range(brojPolja):
        for j in range(brojPolja):
            # bojimo crna polja
            if (i + j) % 2 != 0:
            ... # dovrsite


.. questionnote::

    **Задатак - Зграда**

    Измените програм тако да се прозори цртају у двострукој петљи.

Део који треба изменити, након измене може да почиње овако:

.. code::

    for y in range(5):     # sprat
        for x in range(2): # strana zgrade (0 - leva, 1 - desna)
            if (x+y) % 2 == 0:
                boja = ...


.. activecode:: PyGame_loops_building_alternating
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask:
    :includexsrc: src\PyGame\1_Drawing\7c_Loops_alternating\Tasks\building_alternating_srp.py
    
    pg.draw.rect(prozor, pg.Color("darkgray"), (120, 50, 60, 140)) # zgrada

    # Ovaj deo izmeniti
    pg.draw.rect(prozor, pg.Color('yellow'), (130,  60, 15, 15))
    pg.draw.rect(prozor, pg.Color('black'), (155,  60, 15, 15))
    pg.draw.rect(prozor, pg.Color('black'), (130,  80, 15, 15))
    pg.draw.rect(prozor, pg.Color('yellow'), (155,  80, 15, 15))
    pg.draw.rect(prozor, pg.Color('yellow'), (130, 100, 15, 15))
    pg.draw.rect(prozor, pg.Color('black'), (155, 100, 15, 15))
    pg.draw.rect(prozor, pg.Color('black'), (130, 120, 15, 15))
    pg.draw.rect(prozor, pg.Color('yellow'), (155, 120, 15, 15))
    pg.draw.rect(prozor, pg.Color('yellow'), (130, 140, 15, 15))
    pg.draw.rect(prozor, pg.Color('black'), (155, 140, 15, 15))

    pg.draw.rect(prozor, pg.Color("black"),  (140, 160, 20, 30))   # kapija

~~~~

Ако са свим овим задацима нисте имали већих проблема, покушајте за крај да решите и један мало тежи задатак. 

.. questionnote::

    **Задатак - изазов: Паркет**

    Напишите програм који приказује паркет (слику паркета можете да видите када кликнете на дугме "Прикажи пример", а слика је иста као на почетку ове стране, десно). Циљ је, наравно, да се цртање дашчица паркета обавља у вишеструкој петљи. Димензије дашчице су 10х60, а боје су "goldenrod" и "brown".

Костур програма угрубо изгледа овако:

.. code::

    for red ...
        for kol ...
            if ...
                for dascica in range(6):
                    pg.draw.rect(...)
            else:
                for dascica in range(6):
                    pg.draw.rect(...)

.. activecode:: PyGame_loops_parquet
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask:
    :includexsrc: src\PyGame\1_Drawing\7c_Loops_alternating\Tasks\parquet_srp.py
