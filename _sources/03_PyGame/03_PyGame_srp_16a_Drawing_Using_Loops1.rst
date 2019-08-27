Израда цртежа помоћу петљи
--------------------------

Размотримо следећи задатак: нека је потребно нацртати 6 кругова, као на овој слици:

.. image:: ../../_images/PyGame/target.png
   :width: 300px
   :align: center 

Гледајући у слику можемо да претпоставимо (а могло је да буде и речено у поставци) да су кругови једнако размакнути. Ово значи да је разлика полупречника свака два суседна круга иста.

Величину кругова бирамо тако да буду што већи, али да могу да стану у дати простор за цртање од 300x300 пиксела. Пошто је ширина прозора 300 пиксела, полупречник највећег круга је 150. Као разлику полупречника два суседна круга можемо да узмемо :math:`{150 \over 6} = 25`. Тако добијамо полупречнике 25, 50, 75, 100, 125, 150.

На основу израчунатих вредности, могли бисмо да напишемо овакав програм:

.. activecode:: PyGame_loop__target_fixed
   :nocodelens:
   :enablecopy:
   :modaloutput:
   :includesrc: src\PyGame\1_Drawing\7a_UsingLoops\Examples\circles_target_fixed_srp.py

Замислимо да смо после овога добили нови задатак да направимо исти такав цртеж, али са 5 кругова. Ово је врло мала промена, зар не? Требало би да можемо да искористимо нешто од претходно решеног задатка.

Када започнемо рад на цртежу од 5 кругова, видимо да врло мало од претходног програма можемо да искористимо. У ствари, можемо да искористимо само идеју, а величине кругова треба да израчунамо испочетка.

Да смо програм писали другачије, прилагођавање би било много једноставније. Могли смо на пример да број кругова упишемо у променљиву, а затим да у свим потребним рачунањима користимо ту промељиву. Тај програм би изгледао овако:

.. activecode:: PyGame_loop__target_flexible
   :nocodelens:
   :enablecopy:
   :modaloutput:
   :includesrc: src\PyGame\1_Drawing\7a_UsingLoops\Examples\circles_target_flexible_srp.py

У овом програму је довољно да се измени само један број, па да он црта било који задати број кругова.

Код многих цртежа постоји нека правилност, као што је симетрија или неки део који се понавља (и многе друге, сложеније правилности). Ако схватимо правилност на таквим цртежима и изразимо је математички, моћи ћемо да је искористимо при писању програма за цртање таквих цртежа, као што смо урадили у претходном примеру. На тај начин добијамо програм који је много лакше изменити да би се добио неки други, сличан цртеж. Код цртежа са великим бројем понављања неког дела (истоветног или мало измењеног), програм који користи правилност ће бити и доста краћи.

.. infonote::

    Многи програми које користе милиони људи се стално усавршавају и дорађују. Стално се објављују нове верзије у којима је нешто урађено боље. Према томе, измене програма су нешто потпуно нормално и нешто што се стално дешава. Ситуација је слична и са програмима које сами пишемо. Када напишемо неки програм, лако може да се догоди да се касније сетимо нечега, због чега ћемо хтети да изменимо део програма који је већ написан.
    
    Зато, када пишемо програме, треба да имамо на уму могућност да ће неко (могуће и ми сами) хтети да направи неки сличан програм и да ће можда желети да употреби наш програм као почетну верзију.

Погледајмо још један пример како можемо да искористимо правилности на цртежу за писање флексибилнијег програма (програма који је лакше прилагодити мало другачијој намени).

Пример - антена
'''''''''''''''

Раније смо већ имали програм који црта овакву антену. Сада је програм написан тако да није сувише тешко изменити број попречних сегмената, размак између њих, разлику дужина узастопних сегмената и слично.

.. activecode:: PyGame_loop__antenna
   :nocodelens:
   :enablecopy:
   :modaloutput:
   :includesrc: src\PyGame\1_Drawing\7a_UsingLoops\Examples\antenna1_srp.py

Део програма који црта попречне сегменте антене је могао да буде написан и овако:

.. code::

    for i in range(6):
        pg.draw.line(prozor, pg.Color('darkgray'), (120 - 10 * i,  75 + 25 * i), (180 +  10 * i,  75 + 25 * i), 1 + i//2)

Овако написан програм би био нешто краћи, али први је јаснији, тако да сваки има своје предности. Истакнимо само да су оба ова програма боља од директног цртања 6 линија за попречне сегменте (као што смо то радили раије). Када би се овај део програма састојао од шест позива функције за цртање линије, било би теже изменити и прилагодити програм цртању другачије антене.

Правилно распоређени бројеви
''''''''''''''''''''''''''''

У оба претходна примера било је потребно да набројимо неки низ или низове правилно распоређених бројева. У задатку са круговима то су били бројеви 25, 50, 75, 100, 125, 150 (полупречници кругова), а у задатку са антеном биле су нам потребне чак четири серије бројева - *x* и *y* координате левих и десних крајева попречних сегмената антене. Конкретно, ти бројеви су:

- *x* координате левих крајева: 120, 110, 100, 90, 80, 70
- *y* координате левих крајева: 75, 100, 125, 150, 175, 200
- *x* координате десних крајева: 180, 190, 200, 210, 220, 230
- *y* координате десних крајева: 75, 100, 125, 150, 175, 200

Видели смо да постоје различити начини да добијемо потребне вредности. На пример, у задатку са концентричним круговима, вредности 25, 50, 75, 100, 125, 150 могли смо да добијемо на било који од следећих (једнако добрих) начина:

..  code::

    for r in range(25, 151, 25):
        pg.draw.circle(prozor, pg.Color("red"), centar, r, 2)

..  code::

    for i in range(br_krugova):
        pg.draw.circle(prozor, pg.Color("red"), centar, round(25 + i * 25), 2)

..  code::

    r = 25
    for _ in range(br_krugova):
        pg.draw.circle(prozor, pg.Color("red"), centar, r, 2)
        r += 25

У општем случају, ако треба добити серију вредности *a*, *a+d*, *a+2d*, ... *a+(n-1)d*, претходна три начина можемо да користимо овако:

..  code::

    for x in range(a, a + n*d, d):
        print(x)

..  code::

    for i in range(n):
        print(a+i*d)

..  code::

    x = a
    for _ in range(n):
        print(x)
        x += d


Видећемо да се велики број задатака са цртањем правилно распоређених облика може решити применом оваквих петљи.

Нагласимо још и да функција ``range`` са кораком (са три аргумента) прима обавезно целобројне аргументе, па у ситуацијама када корак није
целобројан њено коришћење није могуће.

Када нам је потребно (као у задатку са антеном) да направимо неколико серија у једној петљи, први начин је мање погодан, па треба бирати неки од осталих начина.

Следећа питања ће вам помоћи да утврдите знање о формирању серија правилно распоређених бројева.

.. dragndrop:: pygame__loop_quiz_match_series_srp
    :feedback: Покушај поново!
    :match_1: 100, 200, 300, 400, 500|||for i in range(100, 600, 100)
    :match_2: 100, 300, 500|||for i in range(100, 601, 200)
    :match_3: 100, 200, 300, 400, 500, 600|||for i in range(100, 601, 100)
    :match_4: 200, 300, 400, 500, 600|||for i in range(200, 601, 100)

    Упари низ бројева са петљом која га генерише.
     
.. dragndrop:: pygame__loop_quiz_match_series2_srp
    :feedback: Покушај поново!
    :match_1: 100, 150, 200, 250, 300|||x = 100 + i*50
    :match_2: 50, 150, 250, 350, 450|||x = 50 + i*100
    :match_3: 0, 100, 200, 300, 400|||x = i*100
    :match_4: 100, 200, 300, 400, 500|||x = 100+i*100

    Упари бројеве који се добијају са изразом у петљи "for i in range(5):" који их генерише.
     

.. mchoice:: pygame__loop_quiz_range01_srp
    :answer_a: x = 25 * i + 50
    :answer_b: x = (25 + i) * 50
    :answer_c: x = 25 * 2*i+1
    :answer_d: x = 25 + 50 * i
    :correct: d
    :feedback_a: Не.
    :feedback_b: Не.
    :feedback_c: Не.
    :feedback_d: Тачно!
    
    Који израз треба користити у петљи 
    
    .. code::
    
        for i in range(19):
            x = ???
            ...
            
    да би *x* имало исте вредности као у петљи

    .. code::
    
        for x in range(25, 500, 50):
            ...
            
Следе задаци за вежбу.

Мердевине
'''''''''

Измените програм тако да се пречаге мердевина цртају у петљи.

.. activecode:: PyGame_loop__ladder
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask:
    :includexsrc: src\PyGame\1_Drawing\7a_UsingLoops\Tasks\ladder_srp.py

    prozor.fill(pg.Color("green")) # bojimo pozadinu ekrana u zeleno

    pg.draw.line(prozor, pg.Color("brown"), (100, 10), (100, visina - 10), 10)    # leva strana
    pg.draw.line(prozor, pg.Color("brown"), (200, 10), (200, visina - 10), 10)    # desna strana

    # овај део преправити
    pg.draw.line(prozor, pg.Color("brown"), (100,  50), (200, 50), 10) # precaga
    pg.draw.line(prozor, pg.Color("brown"), (100, 100), (200, 100), 10) # precaga
    pg.draw.line(prozor, pg.Color("brown"), (100, 150), (200, 150), 10) # precaga
    pg.draw.line(prozor, pg.Color("brown"), (100, 200), (200, 200), 10) # precaga
    pg.draw.line(prozor, pg.Color("brown"), (100, 250), (200, 250), 10) # precaga

   
.. reveal:: PyGame_loop__ladder_reveal
    :showtitle: Помоћ
    :hidetitle: Сакриј помоћ

    Уместо 5 наредби за цртање линија, можете да употребите петљу следећег облика:
    
    .. code::
    
        for y in ???:
            pg.draw.line(prozor, pg.Color("brown"), (100, y), (200, y), 10)
            
    Да бисте на прави начин комплетирали петљу, треба да одговорите на следеће питање:
    
    .. mchoice:: pygame__loop_quiz_range1_srp
        :answer_a: range(0, 50, 250)
        :answer_b: range(250, 50)
        :answer_c: range(50, 251, 50)
        :answer_d: range(50, 250, 50)
        :correct: c
        :feedback_a: Не, за тај опсег први број није одговарајући.
        :feedback_b: Не, покушајте поново.
        :feedback_c: Тачно!
        :feedback_d: Не, за тај опсег последњи број није одговарајући.
        
        Који од понуђених опсега даје вредности 50, 100, 150, 200, 250?


.. commented out

    .. reveal:: PyGame_loop__ladder_reveal
        :showtitle: Прикажи решење
        :hidetitle: Сакриј решење
        
        Једно могуће решење је:
        
        .. activecode:: PyGame_loop__ladder_solution
            :nocodelens:
            :enablecopy:
            :modaloutput:
            :includesrc: src\PyGame\1_Drawing\7a_UsingLoops\Tasks\ladder_srp.py
          
Дрвеће
''''''

Измените програм тако да се у три проласка кроз петљу црта по једно дрво.

.. activecode:: PyGame_loop__trees
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask:
    :includexsrc: src\PyGame\1_Drawing\7a_UsingLoops\Tasks\trees_srp.py
   
    prozor.fill(pg.Color("green")) # bojimo pozadinu ekrana u zeleno

    pg.draw.rect(prozor, pg.Color("brown"), (40, 180, 20, 100))        # prvo stablo
    pg.draw.ellipse(prozor, pg.Color("darkgreen"), (10, 50, 80, 150))  # prva krosnja
    pg.draw.rect(prozor, pg.Color("brown"), (140, 180, 20, 100))       # drugo stablo
    pg.draw.ellipse(prozor, pg.Color("darkgreen"), (110, 50, 80, 150)) # druga krosnja
    pg.draw.rect(prozor, pg.Color("brown"), (240, 180, 20, 100))       # trece stablo
    pg.draw.ellipse(prozor, pg.Color("darkgreen"), (210, 50, 80, 150)) # treca krosnja

.. reveal:: PyGame_loop__trees_reveal
    :showtitle: Прикажи решење
    :hidetitle: Сакриј решење

    Програм може да изгледа овако:
    
    .. activecode:: PyGame_loop__trees_solution
        :nocodelens:
        :enablecopy:
        :modaloutput:
        :includexsrc: src\PyGame\1_Drawing\7a_UsingLoops\Tasks\trees_srp.py

        prozor.fill(pg.Color("green")) # bojimo pozadinu ekrana u zeleno


        for i in range(3):
            pg.draw.rect(prozor, pg.Color("brown"), (???, 180, 20, 100))        # stablo
            pg.draw.ellipse(prozor, pg.Color("darkgreen"), (???, 50, 80, 150))  # krosnja

    
    при чему уместо упитника треба ставити одговарајуће изразе за *x* координату. Када *i* узима редом вредности 0, 1, 2, потребно је да израз у првој наредби узима редом вредности 40, 140, 240, а у другој 10, 110, 210.
    
.. commented out::    

        pg.draw.rect(prozor, pg.Color("brown"), (40, 180, 20, 100))        # prvo stablo
        pg.draw.ellipse(prozor, pg.Color("darkgreen"), (10, 50, 80, 150))  # prva krosnja
        pg.draw.rect(prozor, pg.Color("brown"), (140, 180, 20, 100))       # drugo stablo
        pg.draw.ellipse(prozor, pg.Color("darkgreen"), (110, 50, 80, 150)) # druga krosnja
        pg.draw.rect(prozor, pg.Color("brown"), (240, 180, 20, 100))       # trece stablo
        pg.draw.ellipse(prozor, pg.Color("darkgreen"), (210, 50, 80, 150)) # treca krosnja
        
        
Решетка
'''''''

Измените програм тако да се у једној петљи исртавају усправне линије, а након тога у другој петљи водоравне линије.

.. activecode:: PyGame_loop__grid
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask:
    :includexsrc: src\PyGame\1_Drawing\7a_UsingLoops\Tasks\grid_srp.py
    
    pg.draw.line(prozor, pg.Color("black"), (10, 10), (10, visina - 10), 1)
    pg.draw.line(prozor, pg.Color("black"), (30, 10), (30, visina - 10), 1)
    pg.draw.line(prozor, pg.Color("black"), (50, 10), (50, visina - 10), 1)
    pg.draw.line(prozor, pg.Color("black"), (70, 10), (70, visina - 10), 1)
    pg.draw.line(prozor, pg.Color("black"), (90, 10), (90, visina - 10), 1)
    pg.draw.line(prozor, pg.Color("black"), (110, 10), (110, visina - 10), 1)
    pg.draw.line(prozor, pg.Color("black"), (130, 10), (130, visina - 10), 1)
    pg.draw.line(prozor, pg.Color("black"), (150, 10), (150, visina - 10), 1)
    pg.draw.line(prozor, pg.Color("black"), (170, 10), (170, visina - 10), 1)
    pg.draw.line(prozor, pg.Color("black"), (190, 10), (190, visina - 10), 1)
    pg.draw.line(prozor, pg.Color("black"), (210, 10), (210, visina - 10), 1)
    pg.draw.line(prozor, pg.Color("black"), (230, 10), (230, visina - 10), 1)
    pg.draw.line(prozor, pg.Color("black"), (250, 10), (250, visina - 10), 1)
    pg.draw.line(prozor, pg.Color("black"), (270, 10), (270, visina - 10), 1)
    pg.draw.line(prozor, pg.Color("black"), (290, 10), (290, visina - 10), 1)
    pg.draw.line(prozor, pg.Color("black"), (310, 10), (310, visina - 10), 1)
    pg.draw.line(prozor, pg.Color("black"), (330, 10), (330, visina - 10), 1)
    pg.draw.line(prozor, pg.Color("black"), (350, 10), (350, visina - 10), 1)
    pg.draw.line(prozor, pg.Color("black"), (370, 10), (370, visina - 10), 1)
    pg.draw.line(prozor, pg.Color("black"), (390, 10), (390, visina - 10), 1)
    pg.draw.line(prozor, pg.Color("black"), (410, 10), (410, visina - 10), 1)
    pg.draw.line(prozor, pg.Color("black"), (430, 10), (430, visina - 10), 1)
    pg.draw.line(prozor, pg.Color("black"), (450, 10), (450, visina - 10), 1)
    pg.draw.line(prozor, pg.Color("black"), (470, 10), (470, visina - 10), 1)
    pg.draw.line(prozor, pg.Color("black"), (490, 10), (490, visina - 10), 1)
    
    pg.draw.line(prozor, pg.Color("black"), (10, 10), (sirina - 10, 10), 1)
    pg.draw.line(prozor, pg.Color("black"), (10, 30), (sirina - 10, 30), 1)
    pg.draw.line(prozor, pg.Color("black"), (10, 50), (sirina - 10, 50), 1)
    pg.draw.line(prozor, pg.Color("black"), (10, 70), (sirina - 10, 70), 1)
    pg.draw.line(prozor, pg.Color("black"), (10, 90), (sirina - 10, 90), 1)
    pg.draw.line(prozor, pg.Color("black"), (10, 110), (sirina - 10, 110), 1)
    pg.draw.line(prozor, pg.Color("black"), (10, 130), (sirina - 10, 130), 1)
    pg.draw.line(prozor, pg.Color("black"), (10, 150), (sirina - 10, 150), 1)
    pg.draw.line(prozor, pg.Color("black"), (10, 170), (sirina - 10, 170), 1)
    pg.draw.line(prozor, pg.Color("black"), (10, 190), (sirina - 10, 190), 1)
    pg.draw.line(prozor, pg.Color("black"), (10, 210), (sirina - 10, 210), 1)
    pg.draw.line(prozor, pg.Color("black"), (10, 230), (sirina - 10, 230), 1)
    pg.draw.line(prozor, pg.Color("black"), (10, 250), (sirina - 10, 250), 1)
    pg.draw.line(prozor, pg.Color("black"), (10, 270), (sirina - 10, 270), 1)
    pg.draw.line(prozor, pg.Color("black"), (10, 290), (sirina - 10, 290), 1)

.. commented out::

    .. reveal:: PyGame_loop__grid_reveal
        :showtitle: Прикажи решење
        :hidetitle: Сакриј решење

        Једно могуће решење је:
       
        .. activecode:: PyGame_loop__grid_solution
            :nocodelens:
            :enablecopy:
            :modaloutput:
            :includesrc: src\PyGame\1_Drawing\7a_UsingLoops\Tasks\grid_srp.py
