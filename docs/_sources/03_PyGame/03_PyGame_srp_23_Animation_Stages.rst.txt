Анимација по фазама
-------------------

Семафор
'''''''

Један од најпознатијих примера уређаја који ради по фазама је семафор који регулише саобраћај. На примеру семафора ћемо објаснити рад по фазама и како можемо да анимирамо на рачунару догађања која се одвијају по фазама.

Постоји неколико стања у којима семафор може да се нађе. На пример, може да светли црвено, да светли трепћуће жуто, да буде искључен итд. Период у току којег семафор не мења стање зваћемо фаза. При нормалном раду семафора фазе се циклично смењују и свака фаза има своје трајање. Узмимо као пример семафор на коме се смењују следеће четири фазе: 1 - црвено светло, 2 - црвено и жуто светло, 3 - зелено светло, и 4 - жуто светло.

Да би анимација била једноставнија, трајање сваке фазе ћемо изразити бројем фрејмова (уместо секундама). Нека су трајања поменутих фаза :math:`n_1`, :math:`n_2`, :math:`n_3` и :math:`n_4` фрејмова редом. Тада цео циклус траје :math:`N = n_1 + n_2 + n_3 + n_4` фрејмова. Од тих :math:`N` фрејмова, првих :math:`n_1` припада првој фази, следећих :math:`n_2` другој итд.

Да бисмо знали којој фази припада текући фрејм, можемо да уведемо глобалну променљиву која броји фрејмове. Пошто цео циклус траје :math:`N` фрејмова, довољно је да бројимо по модулу :math:`N`. То значи да када бројач фрејмова достигне вредност :math:`N-1`, следећа вредност је нула (бројимо само у оквиру једног циклуса). При томе, за вредности од 0 до :math:`n_1 - 1`, фрејм припада првој фази, за вредности од :math:`n_1` до :math:`n_1 + n_2 - 1`, другој фази, за вредности од :math:`n_1 + n_2` до :math:`n_1 + n_2 + n_3 - 1` трећој, а за вредности од :math:`n_1 + n_2 + n_3` до :math:`N-1` четвртој.

Ево како може да изгледа програм написан на основу овог разматрања:

.. activecode:: PyGame__anim_stages_traffic_lights1_srp
    :nocodelens:
    :modaloutput:
    :includesrc: src/PyGame/2_Animation/2c_Anim_Stages/TrafficLights1_srp.py

Задаци
''''''

.. questionnote::

    **Пета фаза:** Копирајте претходни програм, па убаците фазу за трепћуће зелено светло после зеленог, а пре жутог светла (као у примеру - дугме "Прикажи пример").

.. activecode:: PyGame__anim_stages_traffic_lights1a_srp
    :nocodelens:
    :modaloutput:
    :playtask:
    :includehsrc: src/PyGame/2_Animation/2c_Anim_Stages/TrafficLights1a_srp.py

**Помоћ:** У петој фази нећемо имати један позив функције *crtaj_semafor*, него део кода који отприлике изгледа овако:

.. code::

        if i_frejm % 2 == 0:
            crtaj_semafor(...)
        else:
            crtaj_semafor(...)

.. questionnote::

    **Авион:** Напишите програм који ради као у примеру (дугме "Прикажи пример"). 
    
    Опис кретања: авион полази са средине леве ивице прозора. Креће се прво 20 фрејмова по 2 пиксела десно и горе, затим 20 фрејмова по 2 пиксела десно и доле. Када изађе кроз десну ивицу прозора, појављује се на истој висини са леве стране. Брзина приказивања је 50 фрејмова у секунди.

.. image:: ../../_images/airplane.png
   :width: 50px
.. image:: ../../_images/sun.png
   :width: 50px

.. activecode:: PyGame__anim_stages_plane_srp
    :nocodelens:
    :modaloutput:
    :playtask:
    :includehsrc: src/PyGame/2_Animation/2c_Anim_Stages/airplane_srp.py
    
    import pygame as pg, petljapg
    (sirina, visina) = (800, 350)
    prozor = petljapg.init(sirina, visina, "Авион")

    sunce_slika = pg.image.load("sun.png")      # slika sunca
    avion_slika = pg.image.load("airplane.png") # slika aviona
    avion_sirina = avion_slika.get_width()      # sirina slike aviona
    avion_visina = avion_slika.get_height()     # visina slike aviona
    # dovrsite


.. questionnote::

    **Кртица:** Напишите програм који ради као у примеру (дугме "Прикажи пример"). 
    
    Учитава се 10 слика на којима кртица редом све више вири из рупе. Циклус има четири фазе, које заједно трају 28 фрејмова. 
    
    - Прва фаза траје 10 фрејмова и током ње кртица излази из рупе (приказују се редом слике од прве до десете).
    - Друга фаза траје 5 фрејмова и током ње кртица је у највишем положају (приказује се десета слика).
    - Трећа фаза траје 10 фрејмова и током ње кртица улази у рупу (приказују се слике од десете до прве).
    - Четврта фаза траје 3 фрејма и током ње кртица је у рупи (приказује се прва слика).

.. image:: ../../_images/mole1.png
   :width: 50px
.. image:: ../../_images/mole2.png
   :width: 50px
.. image:: ../../_images/mole3.png
   :width: 50px
.. image:: ../../_images/mole4.png
   :width: 50px
.. image:: ../../_images/mole5.png
   :width: 50px
.. image:: ../../_images/mole6.png
   :width: 50px
.. image:: ../../_images/mole7.png
   :width: 50px
.. image:: ../../_images/mole8.png
   :width: 50px
.. image:: ../../_images/mole9.png
   :width: 50px
.. image:: ../../_images/mole10.png
   :width: 50px

.. activecode:: PyGame__anim_stages_mole_srp
    :nocodelens:
    :modaloutput:
    :playtask:
    :includehsrc: src/PyGame/2_Animation/2c_Anim_Stages/mole_srp.py

    import pygame as pg, petljapg
    (sirina, visina) = (150, 150)
    prozor = petljapg.init(sirina, visina, "Кртица")

    slike = []   # niz koji ce da sadrzi slike
    for i in range(1, 11): # učitavamo u listu slike mole1.png, ..., mole10.png
        naziv_slike = "mole" + str(i) + ".png"  # gradimo naziv slike od delova
        slike.append(pg.image.load(naziv_slike))

    braon = (60, 42, 3)
    Y_HORIZONT = 125
    ZEMLJA = (0, Y_HORIZONT, sirina, visina - Y_HORIZONT) # deo slike ispod horizonta
    i_frejm = 0 # redni broj frejma u sekvenci

    def nov_frejm():
        # dopunite - izracunajte koja slika se prikazuje u ovom frejmu

        prozor.fill(pg.Color("skyblue"))     # bojimo pozadinu prozora u nebo-plavo
        pg.draw.rect(prozor, braon, ZEMLJA)  # bojimo pravougaonik ZEMLJA u braon
        prozor.blit(slike[i_slika], (0, 0))  # prikazujemo sliku

    petljapg.run(10, nov_frejm)
