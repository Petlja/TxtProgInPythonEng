Приказивање готових слика - задаци
----------------------------------

Научили смо како да прикажемо готову слику тако да њен горњи леви угао буде на задатој позицији на екрану. У неким ситуацијама позиција горњег левог угла слике неће нам бити позната, него ће бити потребно да је израчунамо. У таквим случајевима може да буде потребно да знамо и ширину и висину слике. У Пајтоновој библиотеци ПајГејм за слику ``sl``, ширину и висину те слике добијамо редом као  ``sl.get_width()`` и ``sl.get_height()``.

Корпе
'''''

Довршите следећи програм, тако да се добија слика као у примеру. Позиције дрвећа су дате, а поред сваког дрвета треба нацртати корпу тако да се доњи десни углови слике корпе и слике дрвета поклапају.

Да бисте могли да довршите овај задатак, потребно је да за сваку нацртану корпу израчунате позицију њеног горњег левог угла, што може да се уради полазећи од координата горњег левог угла дрвета, користећи ширине и висине обе слике.

.. activecode:: PyGame_baskets1_srp
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask:
    :includexsrc: src\PyGame\1_Drawing\9_UsingImages\trees_baskets_srp.py

    drvo_slika = pg.image.load("tree.png")  # slika drveta
    korpa_slika = pg.image.load("basket.png")  # slika korpe
    drvece_poz = ((200, 70), (120, 150), (240, 290), (550, 170), (400, 200))


Брање јабука
''''''''''''

Довршите следећи програм, тако да се добија слика као у примеру. Решење овог задатка се добија допуњавањем претходног програма, тако да се додају јабуке на дрвеће и у корпе.

.. activecode:: PyGame_baskets_apples_srp
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask:
    :includexsrc: src\PyGame\1_Drawing\9_UsingImages\trees_apples_baskets_srp.py

    drvo_slika = pg.image.load("tree.png")  # slika drveta
    korpa_slika = pg.image.load("basket.png")  # slika korpe
    jabuka_slika = pg.image.load("apple_small.png")  # slika jabuke
    drvece_poz = ((200, 70), (120, 150), (240, 290), (550, 170), (400, 200))
    jabuke_na_drvetu_poz = ((43,191), (61, 158), (124, 145), (134, 175), (160, 180))
    jabuke_u_korpi_poz = ((15, 38), (60, 41), (22, 43), (49, 45), (34, 48))


Сандуци
'''''''

Напишите програме који користе слику једног сандука приказану испод,

.. image:: ../../_images/PyGame/box.png
   :width: 200px
   :align: center 

и формирају слике као у примерима (користите дугме "Прикажи пример" у сваком од задатака).
      
Координате слике, то јест њеног горњег левог угла за крајњи леви сандук су (60, 400), а за највиши сандук су (420, 115). 

Из датих података и слике могу да се одреде серије *x* и *y* координата слике сваког сандука у сваком од примера. Овде додатно треба водити рачуна и о редоследу исцртавања слика кутија. 

Да бисте боље разумели како иста серија бројева (на пример 10, 15, 20, 25, 30) може да се добије у различитим редоследима и на шта при томе треба обратити пажњу, одговорите на помоћно питање.

.. dragndrop:: console__pictures_quiz_series_negative_step_srp
    :feedback: Покушај поново!
    :match_1: 10, 15, 20, 25, 30 ||| for x in range(10, 35, 5)
    :match_2: 30, 25, 20, 15, 10 ||| for x in range(30, 5, -5)
    :match_3: празна серија ||| for x in range(30, 10, 5)
    :match_4: 5, 15, 25 ||| for x in range(5, 35, 10)

    Упарите серије бројева са наредбама које их генеришу.

.. activecode:: PyGame_boxes1_srp
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask:
    :includexsrc: src\PyGame\1_Drawing\9_UsingImages\boxes1_srp.py

.. activecode:: PyGame_boxes2_srp
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask:
    :includexsrc: src\PyGame\1_Drawing\9_UsingImages\boxes2_srp.py

.. activecode:: PyGame_boxes3_srp
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask:
    :includexsrc: src\PyGame\1_Drawing\9_UsingImages\boxes3_srp.py

