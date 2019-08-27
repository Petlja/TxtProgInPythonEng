Померање цртежа
---------------

У претходним примерима смо направили неколико цртежа састављених од основних облика. При томе је за сваки од тих облика било потребно одредити тачан положај да би се сви делови уклопили у целину. За неке цртеже је било могуће (а у појединим задацима и потребно) да се координате појединих тачака израчунају на основу познатих координата других тачака. То рачунање се могло обавити и ван програма, а затим у програм само унети израчунате координате. Боље је, међутим, да се таква рачунања обаве у самом програму, и то из више разлога:

- Можда нећемо из првог покушаја израчунавати координате на исправан начин. У таквој ситуацији је лакше изменити упутство за рачунање него рачунати све тачке ручно поново.
- Када сами креирамо цртеж, може се догодити да након прве верзије програма пожелимо да додамо још нешто, на пример са леве стране цртежа, али да немамо довољно места. У таквом случају потребно је цео цртеж померити удесно, тако што се *x* координате свих тачака повећају за исту вредност. Ако смо ручно рачунали координате тачака, потребно је израчунати их све поново. У добро организованом програму за померање цртежа удесно довољно је променити један број. Овај поступак ће можда бити потребно поновити неколико пута док не будемо задовољни положајем нацртаног дела, тако да је испробавање много лакше када рачуна програм а не ми.
- Ако пожелимо да нацртамо исти цртеж на више места у прозору, предности програмског рачунања поново долазе до изражаја.

Сада ћемо још мало систематизовати рачунање координата и употребити га за једноставније померање нацртаних објеката. Пре него што почнемо, било би добро да проверите потребно предзнање и одговорите на ова питања:

.. mchoice:: pygame_quiz_point_left_srp
   :answer_a: (50, 60)
   :answer_b: (50, 80)
   :answer_c: (40, 70)
   :answer_d: (60, 70)
   :answer_e: (40, 60)
   :correct: c
   :feedback_a: Покушај поново
   :feedback_b: Покушај поново
   :feedback_c: Тачно
   :feedback_d: Покушај поново
   :feedback_e: Покушај поново

    Kоје су координате тачке која се налази 10 пиксела лево од тачке (50, 70)?

.. mchoice:: pygame_quiz_point_down_srp
   :answer_a: (50, 60)
   :answer_b: (50, 80)
   :answer_c: (40, 70)
   :answer_d: (60, 70)
   :answer_e: (40, 60)
   :correct: b
   :feedback_a: Покушај поново
   :feedback_b: Тачно
   :feedback_c: Покушај поново
   :feedback_d: Покушај поново
   :feedback_e: Покушај поново

    Kоје су координате тачке која се налази 10 пиксела испод тачке (50, 70)?

.. mchoice:: pygame_quiz_rect_up_left_srp
   :answer_a: pg.draw.rect(prozor, boja, (70, 120, 50, 60))
   :answer_b: pg.draw.rect(prozor, boja, (100, 150, 110, 120))
   :answer_c: pg.draw.rect(prozor, boja, (100, 150, 50, 60))
   :answer_d: pg.draw.rect(prozor, boja, (70, 120, 80, 90))
   :answer_e: pg.draw.rect(prozor, boja, (70, 180, 80, 90))
   :correct: d
   :feedback_a: Покушај поново
   :feedback_b: Покушај поново
   :feedback_c: Покушај поново
   :feedback_d: Тачно
   :feedback_e: Покушај поново

   Правоугаоник је нацртан помоћу ``pg.draw.rect(prozor, boja, (100, 150, 80, 90))``. Како се може нацртати правоугаоник исте величине који се налази 30 пиксела лево и 30 пиксела изнад овог правоугаоника?
          
.. mchoice:: pygame_quiz_circle_above_srp
   :answer_a: pg.draw.circle(prozor, boja, (100, 120), 40)
   :answer_b: pg.draw.circle(prozor, boja, (100, 160), 40)
   :answer_c: pg.draw.circle(prozor, boja, (120, 100), 40)
   :answer_d: pg.draw.circle(prozor, boja, (160, 100), 40)
   :answer_e: pg.draw.circle(prozor, boja, (20, 120), 40)
   :correct: a
   :feedback_a: Тачно
   :feedback_b: Покушај поново
   :feedback_c: Покушај поново
   :feedback_d: Покушај поново
   :feedback_e: Покушај поново

   Круг је нацртан помоћу ``pg.draw.circle(prozor, boja, (100, 200), 40)``. Како се може нацртати круг исте величине који се налази изнад овог круга и додирује га?


Преправљање непомичног цртежа у помични
'''''''''''''''''''''''''''''''''''''''

Погледајмо како је нацртан облак у следећем примеру:

.. activecode:: PyGame_cloud_fixed
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :includesrc: src\PyGame\1_Drawing\5_Movable\cloud_fixed_srp.py

Облак смо представили помоћу три круга, једног већег у средини и два мања око њега:

.. code::

    pg.draw.circle(prozor, pg.Color("white"), (200, 200), 50)
    pg.draw.circle(prozor, pg.Color("white"), (150, 200), 30)
    pg.draw.circle(prozor, pg.Color("white"), (250, 200), 30)

Ако бисмо хтели да тај облак нацртамо на различитим висинама, могли бисмо да понављамо ове три наредбе, сваки пут са неком новом вредношћу за :math:`y` координату центара ова три круга уместо 200, колико је на почетку. На пример:

.. code::

    pg.draw.circle(prozor, pg.Color("white"), (200, 200), 50)
    pg.draw.circle(prozor, pg.Color("white"), (150, 200), 30)
    pg.draw.circle(prozor, pg.Color("white"), (250, 200), 30)

    pg.draw.circle(prozor, pg.Color("white"), (200, 80), 50)
    pg.draw.circle(prozor, pg.Color("white"), (150, 80), 30)
    pg.draw.circle(prozor, pg.Color("white"), (250, 80), 30)
    
    pg.draw.circle(prozor, pg.Color("white"), (200, 320), 50)
    pg.draw.circle(prozor, pg.Color("white"), (150, 320), 30)
    pg.draw.circle(prozor, pg.Color("white"), (250, 320), 30)

.. image:: ../../_images/PyGame/clouds.png
    :width: 400px
    :align: center

На овај начин, не само да програм расте брже него што мора, него и сваку промену треба да направимо на три места (на пример, ако уместо 320 желимо да пробамо 330, ту промену треба направити на три места). Три измене није много, али ако усвојимо такав начин рада, на сложенијим цртежима (и сложенијим програмима уопште) бисмо имали све више проблема. 

Уместо овога, боље је да направимо функцију и да :math:`y` координату центара прослеђујемо као параметар:

.. code::

    def oblak(yc):
        pg.draw.circle(prozor, pg.Color("white"), (200, yc), 50)
        pg.draw.circle(prozor, pg.Color("white"), (150, yc), 30)
        pg.draw.circle(prozor, pg.Color("white"), (250, yc), 30)

    oblak(200)
    oblak(80)
    oblak(320)

Нови програм је прегледнији и лакши за даље мењање и испробавање. За више облака, или сложеније облаке, предност оваквог приступа би била још већа.

А како би изгледало померање облака на лево или десно? Требало би :math:`x` координате 200, 150, 250 центара кругова све повећати или смањити за исту вредност. На пример, ако бисмо као :math:`x` координате уписали 260, 210, 310, цео облак би био померен за 60 пиксела десно. 

Било би добро да можемо да помоћу само једног броја задамо и водоравни положај облака. Да бисмо то постигли, приметимо да су центри мањих кругова удаљени по 50 пиксела од центра средњег круга на лево и десно. Ова рaстојања се не мењају при померању облака. То значи да ако са :math:`X_c` означимо :math:`x` координату центра средњег круга, онда центри мањих кругова имају :math:`x` координате :math:`X_c - 50` и :math:`X_c + 50`. Захваљујући овој сталној вези (која не зависи од положаја облака), сада можемо у функцију за цртање облака да уведемо и параметар :math:`x`:

.. code::

    def oblak(xc, yc):
        pg.draw.circle(prozor, pg.Color("white"), (xc, yc), 50)
        pg.draw.circle(prozor, pg.Color("white"), (xc - 50, yc), 30)
        pg.draw.circle(prozor, pg.Color("white"), (xc + 50, yc), 30)
        
    oblak(200, 200)
    oblak(200, 80)
    oblak(200, 320)

Било који од ова три облака бисмо сада лако могли да померимо на пример 60 пиксела на десно, тако што у позиву функције на месту :math:`x` координате (првог параметра) уместо 200 упишемо 260. Једнако лако је и направити цртеж са неколико облака. Боја, односно нијанса сиве, такође може да буде параметар функције. На тај начин неки облаци могу да буду тамнији, а неки светлији.

Када искористимо све поменуто, можемо да направмо програм који црта неколико облака разних нијанси, на пример:

.. activecode:: PyGame_cloud_movable_srp
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :includesrc: src\PyGame\1_Drawing\5_Movable\clouds_movable_srp.py

Резимирајмо, уз мала уопштења, шта је потребно да се уради да бисмо могли да прказујемо један цртеж на разним местима: 

- Треба да изаберемо једну тачку чије се координате задају директно. Ову изабрану тачку зваћемо **главна тачка**, (понекад се ова тачка назива и **сидро**, енгл. anchor). У примеру облака, главна тачка је центар средњег круга.
- Након избора главне тачке, координате свих осталих битних тачака одређујемо у односу на њу, тако што на координате главне тачке додајемо или одузимамо одређени померај. У примеру са облаком, да бисмо добили :math:`x` координату центра левог круга, од :math:`x` координате главне тачке тачке (центра средњег круга) одузимамо 50 пиксела, а за десни круг додајемо 50 пиксела. 

У општем случају, на цртежу може бити и других облика осим кругова. Тачке које одређују положаје тих облика су: 

- за дуж: њени крајеви 
- за многоугао: његова темена
- за круг: његов центар
- за правоугаоник: његово горње лево теме
- за елипсу: горње лево теме правоугаоника у који је уписана та елипса

Све ове тачке треба задати у односу на главну тачку, то јест изразити њихове координате као координате главне тачке увећане или умањене за неку вредност.

Проверите колико сте разумели претходна објашњења и одгоровите на питања.

.. mchoice:: pygame_quiz_anchor_introduction1_srp
   :answer_a: pg.draw.circle(prozor, pg.Color("red"), (x, y), 50, 1)
   :answer_b: pg.draw.circle(prozor, pg.Color("red"), (x+120, y+90), 50, 1)
   :answer_c: pg.draw.circle(prozor, pg.Color("red"), (x+20, y-10), 50, 1)
   :answer_d: pg.draw.circle(prozor, pg.Color("red"), (x-20, y+10), 50, 1)
   :correct: c
   :feedback_a: Покушај поново
   :feedback_b: Покушај поново
   :feedback_c: Тачно
   :feedback_d: Покушај поново

   Желимо да прилагодимо цртеж који се састоји од неколико облика, тако да се све црта у односу на сидро са координатама `x=100`, `y=100`. Једна од наредби које формирају цртеж је
                
   .. activecode:: pygame_quiz_anchor_introduction_code1_srp
      :passivecode: true
                    
      pg.draw.circle(prozor, pg.Color("red"), (120, 90), 50, 1)

   Која наредба треба да замени дату?
      
.. mchoice:: pygame_quiz_anchor_introduction2_srp
   :answer_a: pg.draw.line(prozor, pg.Color("red"), (x-50, y-50), (150, 150))
   :answer_b: pg.draw.line(prozor, pg.Color("red"), (x-50, y-50), (x+50, y+50))
   :answer_c: pg.draw.line(prozor, pg.Color("red"), (x-50, x+50), (y-50, y+50))
   :answer_d: pg.draw.line(prozor, pg.Color("red"), (x+50, y+50), (x+150, y+150))
   :correct: b
   :feedback_a: Покушај поново
   :feedback_b: Тачно
   :feedback_c: Покушај поново
   :feedback_d: Покушај поново

   Желимо да прилагодимо цртеж који се састоји од неколико облика, тако да се све црта у односу на сидро са координатама `x=100`, `y=100`. Једна од наредби које формирају цртеж је
                
   .. activecode:: pygame_quiz_anchor_introduction_code2_srp
      :passivecode: true
                    
      pg.draw.line(prozor, pg.Color("red"), (50, 50), (150, 150))

   Која наредба треба да замени дату?
      
.. mchoice:: pygame_quiz_anchor_introduction3_srp
   :answer_a: pg.draw.rect(prozor, pg.Color("red"), (x-50, y-50, x, y))
   :answer_b: pg.draw.rect(prozor, pg.Color("red"), (x, y, 100, 100))
   :answer_c: pg.draw.rect(prozor, pg.Color("red"), (x+50, y+50, 100, 100))
   :answer_d: pg.draw.rect(prozor, pg.Color("red"), (x-50, y-50, 100, 100))
   :correct: d
   :feedback_a: Покушај поново
   :feedback_b: Покушај поново
   :feedback_c: Покушај поново
   :feedback_d: Тачно

   Желимо да прилагодимо цртеж који се састоји од неколико облика, тако да се све црта у односу на сидро са координатама `x=100`, `y=100`. Једна од наредби које формирају цртеж је
                
   .. activecode:: pygame_quiz_anchor_introduction_code3_srp
      :passivecode: true
                    
      pg.draw.rect(prozor, pg.Color("red"), (50, 50, 100, 100))

   Која наредба треба да замени дату?
      
.. mchoice:: pygame_quiz_pomeranje_nadesno
   :multiple_answers:
   :answer_a: Уместо pg.draw.circle(prozor, boja, (x, y), r, d) позваћемо pg.draw.circle(prozor, boja, (x+100, y), r, d).
   :answer_b: Уместо pg.draw.circle(prozor, boja, (x, y), r, d) позваћемо pg.draw.circle(prozor, boja, (x-100, y-100), r, d).
   :answer_c: Уместо pg.draw.rect(prozor, boja, (x, y, w, h), d) позваћемо pg.draw.circle(prozor, boja, (x+100, y, w+100, h), d).
   :answer_d: Уместо pg.draw.rect(prozor, boja, (x, y, w, h), d) позваћемо pg.draw.rect(prozor, boja, (x+100, y, w, h), d).
   :answer_e: Уместо pg.draw.rect(prozor, boja, (x, y, w, h), d) позваћемо pg.draw.rect(prozor, boja, (x-100, y, w, h), d).
   :correct: a, d
   :feedback_a: Тачно
   :feedback_b: Покушај поново
   :feedback_c: Покушај поново
   :feedback_d: Тачно
   :feedback_e: Покушај поново

   Желимо да померимо цртеж који се састоји од неколико облика надесно за 100 пиксела. Означите тачна тврђења.

Следе још неки примери претварања фиксног цртежа у помични.

Меда - положај
''''''''''''''

Дат је следећи програм, који приказује главу медведића играчке:

.. activecode:: PyGame_bear_fixed
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :includesrc: src\PyGame\1_Drawing\5_Movable\teddy-bear_fixed_srp.py

У програму се седам пута позива функција *uokviren_krug*, која задати круг уоквирује црном бојом (мада је за три мала црна круга могла је да буде позвана и само функција *circle*). Да бисмо могли да мењамо положај цртежа, изаберимо главну тачку (сидро). Нека то буде центар великог круга, то јест главе медведића. Координате ове тачке су (250, 150). Сада је потребно да координате центара свих осталих кругова изразимо полазећи од главне тачке, померајући се за потребан број пиксела у смеру :math:`x` и :math:`y` осе. Узмимо као пример десно уво медведића.

:math:`x` координата центра десног увета је :math:`310 = 250 + 60`, док је :math:`y` координата :math:`80 = 150 - 70`. Одавде се види да координате центра десног увета можемо у програму да напишемо као :code:`(cx + 60,  cy - 70)`, где су :code:`(cx, cy)` координате главне тачке. Спроведите исти поступак за остале кругове и довршите функцију *crtaj_medu*.

.. activecode:: PyGame_bear_movable1
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask:
    :includexsrc: src\PyGame\1_Drawing\5_Movable\teddy-bear_movable1b_srp.py

   
    # bojimo pozadinu prozora u belo
    prozor.fill(pg.Color("white"))
    
    def uokviren_krug(prozor, boja, centar, poluprecnik):
        pg.draw.circle(prozor, boja, centar, poluprecnik)
        pg.draw.circle(prozor, pg.Color("black"), centar, poluprecnik, 1)
    
    def crtaj_medu(cx, cy):
        uokviren_krug(prozor, pg.Color("yellow"), (cx - 60,  cy - 70),  45) # levo uvo
        # dovrsite
        
    crtaj_medu(sirina // 2, visina // 2)

Овако написан програм нам омогућава да једноставно приказујемо медведиће на разним местима на екрану. На пример, можете да позив функције

.. code::

    crtaj_medu(sirina // 2, visina // 2)
    
која црта медведића са главном тачком у центру прозора (као што је и био), замените са следећа два:

.. code::

    crtaj_medu(sirina // 2 - 120, visina // 2)
    crtaj_medu(sirina // 2 + 120, visina // 2)

Испробајте ово! Било би знатно теже нацртати другог медеведића да нисмо почетни програм прилагодили за овакву употребу.

Кућа - положај
''''''''''''''

Рецимо да сте написали овај програм, а циљ вам је да преправите програм тако да кућица може једноставно да се премешта:

.. activecode:: PyGame_house_detailed_fixed
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :includesrc: src\PyGame\1_Drawing\5_Movable\house2D_detailed_fixed_srp.py

Нека је главна тачка :code:`(x, y) = (50, 150)`. Довршите започето преправљање програма у пољу испод, у коме се цртање обавља у функцији :code:`kuca(x, y, boja_zidova)`. Када се уверите да цртежи у два програма изгледају исто (осим што су прозори у којима се црта различите величине), замените позив :code:`kuca( 50, 150, pg.Color("khaki"))` са следећа 4, да бисте добили слику као кад се кликне на дугме "Прикажи пример":

.. code::

    kuca(150,  90, pg.Color(220, 220, 220))
    kuca(220, 130, pg.Color("white"))
    kuca(350, 160, (255,255,150))
    kuca( 50, 150, pg.Color("khaki"))

.. activecode:: PyGame_house_detailed_movable
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask: 
    :includexsrc: src\PyGame\1_Drawing\5_Movable\house2D_detailed_movable_srp.py
   
    prozor.fill(pg.Color("darkgreen")) # bojimo pozadinu ekrana u tamno zeleno

    def kuca(x, y, boja_zidova):
        pg.draw.polygon(prozor, pg.Color("red"), [(x, y), (x+???, y-???), (x+140, y)]) # krov
        pg.draw.rect(prozor, boja_zidova,       (x,       y,     140, 100))   # kuca
        pg.draw.rect(prozor, pg.Color("brown"), (x + ???, y + ???,  30,  30)) # levi prozor
        pg.draw.rect(prozor, pg.Color("brown"), (x + ???, y + ???, ???, ???)) # desni prozor
        pg.draw.rect(prozor, pg.Color("brown"), (x + ???, y + ???, ???, ???)) # vrata
        
    kuca( 50, 150, pg.Color("khaki"))

Задатак - цртеж који се стално помера
'''''''''''''''''''''''''''''''''''''

Следећа функција исцртава неки цртеж. 
   
.. activecode:: PyGame_movable_scalable_zadato

   def crtanje():
       prozor.fill(pg.Color("white"))
       pg.draw.circle(prozor, pg.Color("blue"), (100, 100), 60)
       pg.draw.circle(prozor, pg.Color("yellow"), (75, 75), 15)
       pg.draw.circle(prozor, pg.Color("black"), (80, 80), 5)
       pg.draw.circle(prozor, pg.Color("yellow"), (125, 75), 15)
       pg.draw.circle(prozor, pg.Color("black"), (120, 80), 5)
       pg.draw.ellipse(prozor, pg.Color("red"), (75, 110, 50, 10))

У програму који следи функција која црта је само започета. Довршите је тако да црта исти цртеж, али да при томе користи сидро :math:`(x, y)`, које се налази у центру плавог круга (у почетку је то тачка :math:`(100, 100)`). 

Када завршите функцију, проверите да ли ради исто као када кликнете на дугме "Прикажи пример".

.. activecode:: PyGame_movable
   :nocodelens:
   :enablecopy:
   :modaloutput:
   :playtask:
   :includexsrc: src\PyGame\1_Drawing\5_Movable\movable_scalable_srp.py
   
                 
   def crtanje():
       prozor.fill(pg.Color("white"))

.. commented out

    .. reveal:: PyGame_movable_reveal
       :showtitle: Прикажи решење
       :hidetitle: Сакриј решење

       .. activecode:: PyGame_movable_code
          :passivecode:

          def crtanje():
              prozor.fill(pg.Color("white"))
              pg.draw.circle(prozor, pg.Color("blue"), (x, y), 60)
              pg.draw.circle(prozor, pg.Color("yellow"), (x-25, y-25), 15)
              pg.draw.circle(prozor, pg.Color("black"), (x-20, y-20), 5)
              pg.draw.circle(prozor, pg.Color("yellow"), (x+25, y-25), 15)
              pg.draw.circle(prozor, pg.Color("black"), (x+20, y-20), 5)
              pg.draw.ellipse(prozor, pg.Color("red"), (x-25, y+10, 50, 10))
           

