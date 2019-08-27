Очитавање тастатуре
-------------------

Добијање информације о притиснутим тастерима на тастатури је врло слично као за тастере миша. Функција ``pg.key.get_pressed()`` враћа торку чији се елементи користе као логичке вредности, а показују за сваки тастер на тастатури да ли је он тренутно притиснут или не.

Пошто тастатура има много више тастера него миш, коришћење индекса 0, 1, 2 итд. за поједине тастере би било непрактично. Да не бисмо морали да знамо који индекс у торци одговара којем тастеру, ПајГејм библиотека садржи именоване константе које користимо као индексе. На пример, константе ``pg.K_LEFT``, ``pg.K_RIGHT``, ``pg.K_UP``, ``pg.K_DOWN`` одговарају тастерима са стрелицама, који се често очитавају. Тастеру за размак одговара константа ``pg.K_SPACE``, док тастерима слова на пример *a*, *b*, *c* одговарају константе ``pg.K_a``, ``pg.K_b``, ``pg.K_c`` итд. комплетан списак ових константи можете да видите `овде <https://www.pygame.org/docs/ref/key.html>`__ .
 
Примери и задаци
''''''''''''''''

.. questionnote::

    **Пример - Свемирски брод:** У овом примеру имамо сличицу свемирског брода, коју померамо лево - десно у складу са притиснутим стрелицама. Осим тога, из брода може да се пуца притиском на размак. 
    
Најпре обратите пажњу на истакнути део програма са светлијом позадином (линије 23-37). То је део који је овде нов, и он је нешто детаљније прокоментарисан и у самом коду.

Остали део програма само ради анимацију више објеката, а то је техника позната од раније.

.. activecode:: PyGame__interact_spaceship_arrow_keys_srp
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :includesrc: src/PyGame/3_Interaction/3c_Keyboard_read/spaceship_arrow_keys_srp.py

Дакле, након што очитамо стање свих тастера и сместимо га у торку *pritisnut*, у *if* наредби једноставно проверавамо стање тастера који нас интересују.


.. questionnote::

    **Задатак - навигација:**  Допуните следећи програм, тако да се помоћу 4 стрелице управља жутим кругом, као у примеру. Круг треба да се не помера ако није притиснута ни једна стрелица, а да се креће за по један пиксел у смеру стрелица које су притиснуте (притиснуте супротне стрелице се међусобно поништавају).
    

.. activecode:: PyGame__interact_navigtate1_srp
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask:
    :includexsrc: src/PyGame/3_Interaction/3c_Keyboard_read/navigtate1_srp.py

        pritisnut = pg.key.get_pressed()
        if pritisnut[pg.K_LEFT] and (x > 0):
            x -= 1
            
        # DOVRSITE



.. questionnote::

    **Задатак - змија:**  Допуните следећи програм, тако да помоћу стрелица може да се управља 'змијом' која се састоји од неколико квадратића, као у примеру.
    
    Променљиве *d_red* и *d_kol* означавају смер кретања змије. Док ни једна стрелица није притиснута, ове променљиве не мењају вредност и змија наставља да се креће у истом смеру. Ваш задатак је да додате наредбе за очитавање стања тастатуре и израчунавање нових вреднсти за *(d_red, d_kol)* на основу притиснутих стрелица, тако да се кретање настави у изабраном смеру.

**Помоћ:** ако се глава змије налазила на пољу *(red, kol)*, у новом фрејму ће се налазити на пољу *(red + d_red, kol + d_kol)*. Проверите да ли разумете како треба доделити вредности променљивама *d_red*, *d_kol* за сваки од смерова:

.. mchoice:: pygame__interact_quiz_direction_srp
   :answer_a: Горе
   :answer_b: Доле
   :answer_c: Лево
   :answer_d: Десно
   :correct: c
   :feedback_a: Не, вредности за горе су (d_red, d_kol) = (-1, 0)
   :feedback_b: Не, вредности за доле су (d_red, d_kol) = (1, 0)
   :feedback_c: Тачно
   :feedback_d: Не, вредности за десно су (d_red, d_kol) = (0, 1)

   Ако се променљивама (d_red, d_kol) доделе вредности (0, -1), у ком смеру се наставља кретање?

.. activecode:: PyGame__interact_snake_srp
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask:
    :includexsrc: src/PyGame/3_Interaction/3c_Keyboard_read/snake_srp.py
    
        # OVDE IZRACUNAJTE POMERAJ (d_red, d_kol)
        # NA OSNOVU PRITISNUTIH TASTERA

.. commented out
    
    import pygame as pg, petljapg, random
    (sirina, visina) = (400, 400)
    prozor = petljapg.open_window(sirina, visina, "Змија")

    boja_zmije = (255, 0, 0)            # boja zmije
    a = 10                              # velicina jednog polja
    (br_redova, br_kolona) = (visina // a, sirina // a) # velicina table
    (d_red, d_kol) = (0, 1) # inicijalno po jednu kolonu udesno
    centar = (br_redova // 2, br_kolona // 2) # koordinate centra table
    zmija = [centar] * 10 # na pocetku je zmija sklupcana u centru
    i_glava = 0 # indeks kvadratica u listi koji predstavlja glavu zmije
    kraj = False

    def crtanje():
        prozor.fill(pg.Color("gray")) # bojimo prozor u sivo
        if kraj:
            # ispisujemo poruku da je kraj
            font = pg.font.SysFont("Arial", 60)
            sl_tekst = font.render("Крај!", True, pg.Color("black"))
            x = (sirina - sl_tekst.get_width()) // 2
            y = (visina - sl_tekst.get_height()) // 2
            prozor.blit(sl_tekst, (x, y))
        else:
            # crtamo zmiju
            for red, kol in zmija:
                pg.draw.rect(prozor, boja_zmije, (kol*a, red*a, a, a))


    def nov_frejm():
        global zmija, i_glava, d_red, d_kol, kraj
        
        # OVDE IZRACUNAJTE POMERAJ (d_red, d_kol)
        # NA OSNOVU PRITISNUTIH TASTERA
        
        # izracunavamo nov polozaj glave zmije
        red, kol = zmija[i_glava]
        i_glava = (i_glava + 1) % len(zmija)
        zmija[i_glava] = (red + d_red, kol + d_kol)
        if kol < 0 or kol >= br_kolona or red < 0 or red >= br_redova:
            kraj = True  # zmija je izasla iz table
        
        crtanje()


    petljapg.frame_loop(10, nov_frejm)


Питања
''''''

Док одговарате на питања, враћајте се по потреби на програм "змија" и погледајте део који вам је потребан за одговор.

.. fillintheblank:: pygame_quiz_interact_snake_tablesize_srp

    Колико редова има табла?

    - :40: Тачно!
      :[0-9]+: Погледајте почетак програма пажљивије.
      :.*: Одговор треба да буде записан цифрама.

.. mchoice:: pygame_quiz_interact_snake_rowcol_to_xy_srp
   :answer_a: x = red*a + a, y = kol*a + a
   :answer_b: x = kol*a + a, y = red*a + a
   :answer_c: x = red*a, y = kol*a
   :answer_d: x = kol*a, y = red*a
   :correct: d
   :feedback_a: Покушај поново
   :feedback_b: Покушај поново
   :feedback_c: Покушај поново
   :feedback_d: Тачно

   Које су координате горњег левог угла квадратића на месту *(red, kol)*?

.. mchoice:: pygame_quiz_interact_snake_head_srp
   :multiple_answers:
   :answer_a: Листа zmija се у сваком фрејму продужава за нови елемент који представља нови положај главе змије.
   :answer_b: Листа zmija током рада програма стално има исти број елемената.
   :answer_c: Из листе zmija се у сваком фрејму избацује један елемент, који представља крај репа змије.
   :correct: b
   :feedback_a: Не постоји таква наредба у програму
   :feedback_b: Тачно
   :feedback_c: Не постоји таква наредба у програму.

   Које реченице су тачне?
    

.. commented out

    chase_and_avoid_srp.py