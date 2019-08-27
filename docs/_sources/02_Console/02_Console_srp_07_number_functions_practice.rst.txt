Математичке функције - вежбање
==============================

Провежбајмо употребу математичких функција које смо научили.


.. questionnote::
    
    **Задатак - рекламни пакети:** 
    
    Јован дели рекламне пакете у којима се налази по један календар, привезак за кључеве и хемијска оловка. Написати програм који учитава колико Јован има календара, привезака и оловака, а затим исписује колико рекламних пакета може да направи.

Искористите једну од математичких функција које сте научили и довршите програм.

.. activecode:: console__mathfunc_promo_material_srp

    kalendara = int(input("Колико има календара?"))
    privezaka = int(input("Колико има привезака?"))
    olovaka = int(input("Колико има оловака?"))
    cega_je_najmanje = 0 # dopunite ovu naredbu
    print("Може да се направи", cega_je_najmanje, "пакета.")
            

.. questionnote::

    **Задатак - лимунада:** 
    
    Група људи полази на пут и Дара је направила лимунаду за све. Написати програм који учитава колико литара лимунаде је Дара направила (као реалан број), а затим исписује колико флашица од пола литра може да се напуни са толико лимунаде и колико је укупно флашица потребно за сву лимунаду (ова два броја могу да се разликују највише за један).
    
  
.. activecode:: console__mathfunc_lemonade_srp

.. reveal:: console__mathfunc_lemonade_reveal_srp
   :showtitle: Прикажи помоћ
   :hidetitle: Сакриј помоћ
   
   Да бисте довршили овај програм, користите неке од функција за заокруживање.
   
   .. activecode:: console__mathfunc_lemonade_solution_srp
   
        litara = float(input())
        punih_flasica = 0 # dopunite ovu naredbu
        ukupno_flasica = 0 # dopunite ovu naredbu
        print("Може да се напуни", punih_flasica, "флашица.")
        print("Потребно је укупно", ukupno_flasica, "флашица.")



.. questionnote::

    **Задатак - утакмица:** 
    
    Шест другара се договорило да се нађу на игралишту у одређено време и одиграју утакмицу. Написати програм који учитава време кашњења сваког од играча у минутима (као целе бројеве), а исписује са колико минута закашњења је утакмица могла да почне.
    
.. activecode:: console__mathfunc_late_game_srp

.. reveal:: console__mathfunc_late_game_reveal_srp
   :showtitle: Прикажи помоћ
   :hidetitle: Сакриј помоћ
   
   Једно од могућих решења је делимично написано у наставку. Покушајте да га довршите.
   
   .. activecode:: console__mathfunc_late_game_help_srp

        t1 = int(input("Колико минута је каснио први: "))
        # ucitajte ostale podatke na isti nacin
        kasnjenje_utakmice = 0 # dopunite ovu naredbu
        print("Утакмица је могла да почне са", kasnjenje_utakmice, "минута закашњења.")

.. commented out

   .. activecode:: console__mathfunc_late_game_solution_srp

        t1 = int(input("Колико минута је каснио први: "))
        t2 = int(input("Колико минута је каснио други: "))
        t3 = int(input("Колико минута је каснио трећи: "))
        t4 = int(input("Колико минута је каснио четврти: "))
        t5 = int(input("Колико минута је каснио пети: "))
        t6 = int(input("Колико минута је каснио шести: "))
        kasnjenje_utakmice = 0 # dopunite ovu naredbu
        print("Утакмица је могла да почне са", kasnjenje_utakmice, "минута закашњења.")


.. questionnote::

    **Задатак - два аутобуса:** 
    
    Марко и Горан путују истим аутопутем у два различита аутобуса и разговарају телефоном. Један од њих је управо приметио ознаку :math:`x` километраже пута, а други :math:`y`. Написати програм који учитава целе бројеве :math:`x` и :math:`y` и исписује колико километара су Марко и Горан удаљени један од другог.

.. activecode:: console__mathfunc_buses_srp

.. commented out
        
    .. reveal:: console__mathfunc_buses_reveal_srp
       :showtitle: Прикажи помоћ
       :hidetitle: Сакриј помоћ
       
       Да бисте довршили следећи програм, користите једну од математичких функција које сте научили.
       
       .. activecode:: console__mathfunc_buses_solution_srp

            x = int(input("Колико је x: "))
            y = int(input("Колико је y: "))
            rastojanje = 0 # dopunite ovu naredbu
            print("Растојање је", rastojanje)

    
.. questionnote::

    **Задатак - Видео лекције**

    Курс се састоји из неколико видео лекција које све једнако трају. Одлучили сте да том курсу посветитие сваког дана по 90 минута и интересује вас колико дана ће вам бити потребно за цео курс. Напишите програм који учитава редом број лекција и трајање једне лекције у минутима, а исписује потребан број дана, заокружен на најближи цео број.
    
.. activecode:: console__mathfunc_videolessons_srp
