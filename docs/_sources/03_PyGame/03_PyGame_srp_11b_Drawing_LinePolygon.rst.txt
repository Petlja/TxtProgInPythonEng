Цртање правих линија и многоуглова
----------------------------------

Функције за цртање правих линија и многоуглова сличне су функцијама за цртање правоугаоника, елипси и кругова, које смо већ упознали. Параметри *prozor*, *boja* и *debljina* се и овде користе, и то са истим значењем као и раније. Нове параметре ћемо објаснити на месту појављивања.

Поновићемо и овде "празан" програм, који само рукује библиотеком ПајГејм и прозором за цртање (а сам не црта ништа), за случај да желите нешто да испробате.

.. activecode:: pygame__drawing_primirives_def_copy_srp
    :nocodelens:
    :modaloutput: 
    :enablecopy:

    # -*- acsection: general-init -*-
    import pygame as pg, petljapg
    prozor = petljapg.open_window(200, 200, "Pygame")
    prozor.fill(pg.Color("gray"))
    # -*- acsection: main -*-



    # -*- acsection: after-main -*-
    petljapg.wait_loop()
 

Цртање линије
'''''''''''''

За цртање линије се користи функција ``pg.draw.line``, са или без праметра који представља дебљину. 

.. code::

    pg.draw.line(prozor, boja, tacka1, tacka2, debljina)
    pg.draw.line(prozor, boja, tacka1, tacka2)


- Параметри *tacka1*, *tacka2* су тачке на екрану, које представљају крајеве дужи. Подсетимо се још једном, тачка се задаје као торка или листа дужине 2. Елементи ове торке или листе су координате тачке у прозору у коме цртамо.
- Код ове функције изостављање дебљине има другачије значење него у осталим функцијама, а то је да се користи подразумевана дебљина линије од 1 пиксел.
    
На пример, наредбом:

.. activecode:: pygame__drawing_line_def_srp
    :passivecode: true

    pg.draw.line(prozor, pg.Color("blue"), (20, 10), (40, 30), 2)
    
исцртавамо плаву линију дебљине 2 пиксела од тачке :math:`(20, 10)` до тачке :math:`(40, 30)`.

.. image:: ../../_images/PyGame/drawing_line.png
   :width: 200px   
   :align: center 

Цртање многоугла
''''''''''''''''

За цртање многоугла се користи функција ``pg.draw.polygon``, која такође има два облика:

.. code::

    pg.draw.polygon(prozor, boja, lista_tacaka, debljina)
    pg.draw.polygon(prozor, boja, lista_tacaka)

- Параметар *lista_tacaka* представља листу темена многоугла који цртамо. На пример [(50, 250), (150, 150), (250, 250)] представља листу од 3 тачке.
- Овде поново облик функције без праметра *debljina* користимо када желимо да многоугао буде цео обојен наведеном бојом (ако наведемо дебљину, црта се многугаона линија те дебљине). 

На пример, следећа наредба црта троугао обојен бојом :math:`(0, 100, 36)`. Темена троугла су :math:`(50, 100)`, :math:`(150, 150)` и :math:`(150, 50)`.

.. activecode:: pygame__drawing_polygon_def_srp
    :passivecode: true

    pg.draw.polygon(prozor, (0, 100, 36), [(50, 100), (150, 150), (150, 50)])

.. image:: ../../_images/PyGame/drawing_polygon.png
   :width: 200px   
   :align: center 

Поред ових набројаних и описаних функција, у модулу ``pg.draw`` постоје и друге функције за цртање, али се овде нећемо њима бавити. Уколико вас интересује више о тим функцијама, комплетније информације можете наћи на пример нa `<https://www.pygame.org/docs/ref/draw.html>`__

Функције за цртање - питања
'''''''''''''''''''''''''''

Проверите колико знате о функцијама за цртање:

.. parsonsprob:: pygame__drawing_quiz_arg_order_srp

   Којим редом се ови аргументи задају у позиву функције `pg.draw.line`
   -----
   прозор
   боја
   координате првог темена
   координате другог темена
   дебљина

.. mchoice:: pygame__drawing_quiz_polygon_args1_srp
   :answer_a: pg.draw.polygon(prozor, boja, [(0, 0), (50, 100), (100, 0)])
   :answer_b: pg.draw.polygon(prozor, boja, (0, 0), (50, 100), (100, 0))
   :answer_c: pg.draw.polygon(prozor, boja, (0, 0, 50, 100, 100, 0))
   :answer_d: pg.draw.polygon(prozor, boja, [0, 0, 50, 100, 100, 0])
   :correct: a
   :feedback_a: Тачно
   :feedback_b: Покушај поново
   :feedback_c: Покушај поново
   :feedback_d: Покушај поново

   Желимо да нацртамо троугао. У ком облику могу да се задају координате тачака?

.. mchoice:: pygame__drawing_quiz_polygon_args2_srp
   :multiple_answers:
   :answer_a: pg.draw.polygon(prozor, boja, [(0, 0), (50, 100), (100, 0)], 7)
   :answer_b: pg.draw.polygon(prozor, boja, [(0, 0), (0, 50), (50, 50), (50,  0)])
   :answer_c: pg.draw.polygon(prozor, boja, [(0, 0), (50, 100), (100, 0)])
   :answer_d: pg.draw.polygon(prozor, boja, [(0, 0), (0, 50), (50, 50), (50,  0)], 4)
   :correct: b, c
   :feedback_a: Тачно
   :feedback_b: Покушај поново
   :feedback_c: Покушај поново
   :feedback_d: Тачно

   Који од наредних полигона се не може нацртати помоћу више позива функције ``pg.draw.line``?
   
.. dragndrop:: pygame__drawing_quiz_function_names_srp
    :feedback: Покушај поново!
    :match_1: Дуж|||pg.draw.line
    :match_2: Многоугао|||pg.draw.polygon
    :match_3: Правоугаоник|||pg.draw.rect
    :match_4: Круг|||pg.draw.circle

    Упарите наредбе за цртање и облике који се њима цртају.
    
.. parsonsprob:: pygame__drawing_quiz_general_arg_order_srp

   Поређајте у складу са типичним редоследом аргумената у функцијама за цртање:
   -----
   prozor
   boja
   koordinate
   debljina

   
.. mchoice:: pygame__drawing_quiz_point_list_srp
   :answer_a: Круг
   :answer_b: Елипса
   :answer_c: Многоугао
   :answer_d: Дуж
   :answer_e: Квадрат
   :correct: c
   :feedback_a: Покушај поново
   :feedback_b: Покушај поново
   :feedback_c: Тачно
   :feedback_d: Покушај поново
   :feedback_e: Покушај поново

   Приликом цртања ког од наведених облика се координате задају у облику листе уређених парова?


Цртежи по упутствима
''''''''''''''''''''

.. questionnote::

    **Страшило:** Нацртајте страшило на белој позадини. Оно се састоји од следећих делова:
    
    - глава: црна кружна линија дебљине 6, са центром у тачки (150, 70), полупречника 50
    - тело: црна права линија дебљине 6, од тачке (150, 120) до тачке (150, 300)
    - руке: црна права линија дебљине 6, од тачке (80, 170) до тачке (220, 170)
    - лева нога: црна права линија дебљине 6, од тачке (150, 300) до тачке (90, 480)
    - десна нога: црна права линија дебљине 6, од тачке (150, 300) до тачке (210, 480)

.. activecode:: pygame__drawing_scarecrow_srp
   :nocodelens:
   :enablecopy:
   :modaloutput:
   :playtask:
   :includexsrc: src/PyGame/1_Drawing/1_BasicExamples/scarecrow_srp.py
   
.. questionnote::

    **Јелка:** Нацртајте јелку на белој позадини. Она се састоји од следећих делова:

    - стабло: правоугаоник попуњен бојом (97, 26, 9), величине 40 х 50, са горњим левим теменом у тачки (130, 250)
    - горњи део крошње: троугао попуњен бојом (0, 100, 36), са теменима (50, 250), (150, 150) и (250, 250)
    - средњи део крошње: троугао попуњен бојом (0, 100, 36), са теменима (75, 200), (150, 100) и (225, 200)
    - доњи део крошње: троугао попуњен бојом (0, 100, 36), са теменима (100, 150), (150, 50) и (200, 150)
    
.. activecode:: pygame__drawing_tree_srp
   :nocodelens:
   :enablecopy:
   :modaloutput:
   :playtask:
   :includexsrc: src/PyGame/1_Drawing/1_BasicExamples/tree_srp.py


Цртежи изненађења
'''''''''''''''''

Да бисте у задацима који следе видели цртеж, потребно је да напишете тражене наредбе и покренете свој програм.

.. questionnote::

    **изненађење 1 - спојите тачке:** Дата су темена многоугла. Нацртајте на позадини боје "darkgreen" тај многоугао, попуњен бојом "khaki".

.. activecode:: pygame__drawing_giraffe_srp
   :nocodelens:
   :enablecopy:
   :modaloutput:
   :includexsrc: src/PyGame/1_Drawing/2_ByInstructions/giraffe_srp.py

.. questionnote::

    **изненађење 2:** 
    
    Бојом "limegreen" исцртајте:
    
    - Пуну елипсу која је уписана у правоугаоник, чије је горње лево теме (75, 100), ширина му је 150, а висина 180;
    - Линију дебљине 6, од тачке (130, 110) до тачке (120, 20);
    - Још једну линију дебљине 6, од тачке (170, 110) до тачке (180, 20);
    - Попуњен круг полупречника 10 пиксела, са центром у тачки (120, 20);
    - Попуњен круг полупречника 10 пиксела, са центром у тачки (180, 20);
    
    Црном бојом исцртајте још две пуне елипсе, и то:

    - једну уписану у правоугаоник чије је горње лево теме (110, 140), ширина му је 30, а висина 50;
    - другу уписану у правоугаоник чије је горње лево теме (160, 140), ширина му је 30, а висина 50;


.. activecode:: pygame__drawing_ant_srp
   :nocodelens:
   :enablecopy:
   :modaloutput:
   :includexsrc: src/PyGame/1_Drawing/2_ByInstructions/insect_srp.py
   
