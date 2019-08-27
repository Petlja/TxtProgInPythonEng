Речници
=======

Замислите да вам је потребно да често преводите неке речи са српског на енглески и желите да за то искористите неки програм. Било би згодно да можемо да организујемо податке тако да свакој речи на српском придружимо реч на енглеском, то јест да направимо речник тих речи које често користимо. Скоро сви модерни програмски језици имају такву структуру података. Наравно, има је и Пајтон. Како бисте желели да назовете такву структуру? У пајтону (и још неким језицима) се она баш и зове речник.

Речник у Пајтону можемо да схватимо као уопштење листе. За разлику од листе у којој су индекси узастопни цели бројеви почев од 0, у речнику за индексирање можемо да користимо било какве целе или реалне бројеве. Можемо да користимо чак и стрингове или торке. У ствари, можемо да користимо било какве неизменљиве објекте. Пошто се за приступање подацима из речника могу користити тако разноврсни објекти, нећемо их звати индекси него кључеви. Тако се речник састоји од парова (кључ, вредност). Ако имамо речник :math:`r` у који желимо да за кључ :math:`k` упишемо вредност :math:`v`, пишемо :math:`r[k]=v`. Ту вредност можемо касније да користимо као :math:`r[k].`

``Показати на што ммањем уводном примеру још r = {k1:v1, k2:v2, k3:v3}, print(r[k1]), r[k4] = v4, r.get(k5, default_v), r.keys(), r.values(), r.items()``

У следећем примеру показујемо најједноставнију употребу речника, који је задат на почетку програма и касније се из њега само очитавају вредности за дате кључеве.

.. questionnote::

    **Пример - превод текста**
    
    У речнику *srpsko_engleski* на почетку следећг програма, налазе се преводи појединачних речи са српског на енглески језик (то значи да су речи на српском у овом речнику кључеви, а речи на енглеском вредности). Да се речник не би непотребно повећавао, све речи и преводи у речнику су писане малим словима. 
    
    У торци *kratki_tekstovi* дата су и два кратка текста, које треба превести **реч по реч**. Речи којих нема у речнику оставити непромењене. Речи које су писане великим словима или великим почетним словом, написати тако и у преводу. Пренети знакове интерпункције без измене у превод, претпостављајући да се они (тамо где их има) јављају само по један на крају речи.

Како се у речнику налазе само речи писане малим словима без интерпункције, пре тражења речи у речнику са краја речи треба уклонити евентуалну интерпункцију и заменити велика слова малим помоћу методе  *lower()*. Након превођења треба вратити интерпункцију на крај речи, ако је постојала. На крају проверавамо да ли је дата реч изворно била написана великим словима или великим почетним словом, па ако јесте, онда и у преводу поставимо одговарајућа велика слова. 

.. activecode:: dict__word_translation

    srpsko_engleski = {
        'велики':'big', 'мали':'little', 'велика':'big', 'мала':'little',
        'шета':'walks', 'иде':'goes', 'лаје':'barks', 'је':'is',
        'и':'and',
        'дечак':'boy', 'девојчица':'girl', 'пас':'dog', 'пса':'dog', 'кућа':'home', 'кући':'home'
    }
        
    kratki_tekstovi = (
        'Велика девојчица Ана шета пса. Пас Боби је мали и лаје.', 
        'Мали дечак ИДЕ кући. Кућа је велика.'
    )

    def prevod_reci(rec):
        interpunkcija = '.,:;?!"-_~/' + "'"
        poslednji_znak = ''
        if rec[-1] in interpunkcija:
            poslednji_znak = rec[-1]
            rec = rec[:-1]
        prevod = srpsko_engleski.get(rec.lower(), rec) + poslednji_znak
        if rec == rec.upper(): return prevod.upper()
        if rec == rec.capitalize(): return prevod.capitalize()
        return prevod
        
    def prevod_teksta(tekst):
        prevod = map(prevod_reci, tekst.split())
        return ' '.join(prevod)

    for tekst in kratki_tekstovi:
        print('текст:', tekst)
        print('превод:', prevod_teksta(tekst))
        print()

``Провери појављивања map, join``

Кад смо код употребе речника ради превођења, на сличан начин се могу превести римски бројеви у арапске.

.. questionnote::

    **Задатак - превод римских бројева у арапске**
    
    у записима римских бројева појављују се слова I, V, X, L, C, D, M, и та слова представљају редом вредности 1, 5, 10, 50, 100, 500, 1000. Када се цифра мање вредности нађе испред цифре веће вредности, цифра мање вредности се не додаје него одузима. Тако на пример запис III представља 3, а запис VI представља 5+1=6, али IV представља 5-1=4.
    
    У следећем програму исправити функцију *pretvori_u_broj*, која за дати римски запис враћа његову бројчану вредност. Испод функције је дат програм помоћу којег можете да тестирате функцију.
    
.. activecode:: dict__roman_to_arabic_1

    vrednost_rimske_cifre = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    def pretvori_u_broj(rimski_zapis):
        s = 0
        prethodna_vrednost = 0
        for slovo in rimski_zapis:
            vrednost = 0 # ispravite
            s += vrednost
            if prethodna_vrednost < vrednost:
                # vec smo dodali, a trebalo je oduzeti
                # zato sad oduzimamo dva puta (da nadoknadimo)
                s -= 2*prethodna_vrednost
            prethodna_vrednost = 0 # ispravite
        return s
        
    rimski_zapisi = ('I', 'III', 'IV', 'VI', 'XCVIII', 'MDCCCLXXXIV', 'MMXIX')
    tacne_vrednosti = (1, 3, 4, 6, 98, 1884, 2019)
    for rimski_zapis, tacna_vrednost in zip(rimski_zapisi, tacne_vrednosti):
        print('%12s: izracunato je %6d, ispravno je %6d.' % 
            (rimski_zapis, pretvori_u_broj(rimski_zapis), tacna_vrednost))

``Провери појављивања zip, форматирани испис``
        
.. reveal:: dict__roman_to_arabic_1_reveal
   :showtitle: Решење
   :hidetitle: Сакриј решење
   
   Ево исправљене функције:
   
   .. activecode:: dict__roman_to_arabic_1_solution
        :passivecode: true
   
        def pretvori_u_broj(rimski_zapis):
            s = 0
            prethodna_vrednost = 0
            for slovo in rimski_zapis:
                vrednost = vrednost_rimske_cifre[slovo]
                s += vrednost
                if prethodna_vrednost < vrednost:
                    # vec smo dodali, a trebalo je oduzeti
                    # zato sad oduzimamo dva puta (da nadoknadimo)
                    s -= 2*prethodna_vrednost
                prethodna_vrednost = vrednost
            return s

Начин на који смо написали фунцкију је сличан ономе како би та функција била написана у већини програмских језика. Пајтон, међутим, има и своје специфичне начине, на пример:

``Ова фукција ради у локалу, а не ради кроз ранстоун!``

.. activecode:: dict__roman_to_arabic_2
       :passivecode: true

        def pretvori_u_broj(rimski_zapis):
            n = len(rimski_zapis)
            arapski = list(map(lambda x : vrednost_rimske_cifre[x], list(rimski_zapis)))
            negativni = [a for i, a in enumerate(arapski) if i < n-1 and a < arapski[i+1]]
            return sum(arapski) - 2*sum(negativni)

``Провери појављивања map, lambda, enumerate``


Вредности у речнику (као и у листи) могу да буду и сложенији објекти од стрингова и бројева. На пример, у следећем примеру као кључеве користимо стрингове, а као вредности - листе стрингова. 

.. questionnote::

    **Пример - Погађајте животињу (уз помагање рачунара)**

    Речник *asocijacije_na_zivotinje* свакој од набројаних животиња придружује листу неких асоцијација на ту животињу. Овај речник ће нам послужити за играње игре погађања. У сваком кругу игре, рачунар прво изабере једну животињу на случајан начин а затим и њене особине из листе распореди на случајан начин. Након ове припреме, рачунар исписује једну по једну особину док не погодимо о којој животињи се ради или док се не дође до краја листе.

.. activecode:: dict__animals_hints

    import random
    asocijacije_na_zivotinje = {
        'лав': ['савана', 'грива', 'рика', 'мачка', 'хороскоп'],
        'тигар': ['џунгла', 'крзно', 'пруге', 'мачка', 'тајга'],
        'медвед': ['крзно', 'шапе', 'снажан', 'зимски сан', 'Златокоса'],
        'сова': ['птица', 'велике очи', 'једе мишеве', 'ноћ', 'ху'],
        'жаба': ['бара', 'једе муве', 'дуг језик', 'водоземац', 'зелене боје'],
        'мајмун': ['дрвеће', 'једе воће', 'дуг реп', 'љуља се', 'човеколик'],
        'зебра': ['пруге', 'савана', 'сафари', 'грива', 'црно - бела', 'копита'],
        'петао': ['птица', 'борба', 'село', 'буђење', 'лупа крилима', 'креста'],
        'крокодил': ['зелене боје', 'месождер', 'гмизавац', 'Нил', 'сузе'],
        'ајкула': ['црно - бела', 'риба', 'океан', 'вири пераје', 'мирис крви']
    }

    igrac_zeli_jos = 'д'
    while igrac_zeli_jos == 'д':
        zivotinja, osobine = random.choice(list(asocijacije_na_zivotinje.items()))
        osobine = random.sample(osobine, len(osobine)) # ispremestaj osobine
        pogodjena = False
        for osobina in osobine:
            prompt = 'Погоди животињу коју сам замислио.' + '\n'
            prompt += 'Ево ти помоћ: ' + osobina + '\n'
            prompt += 'Шта мислиш, која је то животиња? '
            if zivotinja == input(prompt).lower():
                pogodjena = True
                break

        if pogodjena:
            prompt = 'Браво' + '\n'
        else:
            prompt = 'Животиња је била' + zivotinja + '\n'
            
        igrac_zeli_jos = input(prompt + 'Желите ли још једну игру (д/н)? ').lower()

Речник може да се употреби и за програмско пребројавање појављивања неких објеката или догађаја. Кључеви представљају објекте или догађаје које бројимо, а вредности број појављивања. У оваквом случају вредности у речнику зовемо бројачима.

.. questionnote::

    **Задатак - провера у игри састављања речи**
    
    Написати програм који, за понуђена слова и једну реч, проверава да ли је та реч могла бити састављена од датих слова.

Можемо да употребимо речник у коме су кључеви слова, а вредност за дато слово је број неупотребљених примерака тог слова. Прво ћемо пребројати појављивања датих слова повећавањем одговарајућих вредности у речнику. Након тога, за свако употребљено слово смањујемо његов бројач.

Ако при пребројавању бар један од бројача постане негативан, реч није могла да буде састављена и можемо да прекинемо даље проверавање.

Покушајте да довршите програм:

.. activecode:: dict__letter_counting_1

    zadata_slova = input("Која слова су задата: ")
    rec = input("Коју реч сте саставили: ")

    broj_raspolozivih_slova = {}
    moze = True
    # pomocu recnika prebroj pojavljivanja svakog slova medju zadatim slovima
    for slovo in zadata_slova: 
        broj_raspolozivih_slova[slovo] = 0 # ispravite

    # za svako uportebljeno slovo, smanji broj pojavljivanja
    for slovo in rec: 
        # dopunite - smanjite brojac
        # ako je slovo vise puta upotrebljeno nego sto ga ima
        if broj_raspolozivih_slova[slovo] < 0:
            # dopunite
            break
            
    if moze:
        print("Реч '" + rec + "' може да се састави")
    else:
        print("Реч '" + rec + "' не може да се састави")

.. reveal:: dict__letter_counting_1_reveal
   :showtitle: Решење
   :hidetitle: Сакриј решење
   
    .. activecode:: dict__letter_counting_1_solution

        zadata_slova = input("Која слова су задата: ")
        rec = input("Коју реч сте саставили: ")

        broj_raspolozivih_slova = {}
        moze = True
        # pomocu recnika prebroj pojavljivanja svakog slova medju zadatim slovima
        for slovo in zadata_slova: 
            broj_raspolozivih_slova[slovo] = broj_raspolozivih_slova.get(slovo, 0) + 1

        # za svako uportebljeno slovo, smanji broj pojavljivanja
        for slovo in rec: 
            broj_raspolozivih_slova[slovo] = broj_raspolozivih_slova.get(slovo, 0) - 1
            # ako je slovo vise puta upotrebljeno nego sto ga ima
            if broj_raspolozivih_slova[slovo] < 0:
                moze = False # sastavljanje reci nije moguce
                break
                
        if moze:
            print("Реч '" + rec + "' може да се састави")
        else:
            print("Реч '" + rec + "' не може да се састави")

Ако желите да се опробате у састављању речи, било би вам згодније да рачунар сам предложи 12 слова, уместо да их ви задајете. Ради тога можете да измените програм, да почиње овако:

.. activecode:: dict__letter_counting_2
    :passivecode: true

    import random

    slova = 'АБВГДЂЕЖЗИЈКЛЉМНЊОПРСТЋУФХЦЧЏШ'
    zadata_slova = [random.choice(slova) for i in range(12)]

    poruka = 'Извучена су слова: ' + str(zadata_slova) + '\n'
    rec = input(poruka + 'Коју реч сте саставили: ').upper()

    broj_raspolozivih_slova = {}
    # program je nadalje isti kao i ranije
    
Приметићете да су понуђена слова често незгодна за састављање дужих речи. На пример, можете добити слова 'Ћ', 'К', 'З', 'Б', 'Р', 'Т', 'Ш', 'Ј', 'Џ', 'К', 'Д', 'Ј'. Било би занимљивије играти се ако би се свако од понуђених слова појављивало онолико често колико се често појављује и у текстовима. Ради тога можемо да пронађемо на интернету учесталости појављивања слова у српском језику у процентима. Када пронађемо учесталости, можемо да свако слово поновимо у списку свих слова у складу са његвоом учесталошћу. На пример, ако је учесталост појављивања слова 'А' око 11%, ставићемо слово 'А' 11 пута у списак. На тај начин наредбу 

.. code::

    slova = 'АБВГДЂЕЖЗИЈКЛЉМНЊОПРСТЋУФХЦЧЏШ'

можемо да заменимо наредбом:

.. code::

    slova = 'АААААААААААБВВВВГГДДДЂЕЕЕЕЕЕЕЕЕЖЗЗИИИИИИИИИЈЈЈКККЛЛЛЉММММННННННЊООООООООООПППРРРРРССССССТТТТТЋУУУУФХЦЧЏШ'

Ово игру већ чини занимљивијом, на пример добијаћемо слова попут 'Ј', 'Д', 'О', 'А', 'Е', 'Ф', 'О', 'П', 'А', 'И', 'Е', 'П'].

Боље?

``Овде недостаје завршетак приче и објашњење кода``

Следи комплетан програм са бирањем слова у складу са њиховим стварним учесталостима. Уживајте!

.. activecode:: dict__letter_counting_3

    import random

    ucestalost_slova = {
        'А': 0.114, 'Б': 0.011, 'В': 0.037, 'Г': 0.015, 'Д': 0.034,  'Ђ': 0.002,
        'Е': 0.086, 'Ж': 0.007, 'З': 0.017, 'И': 0.095, 'Ј': 0.027,  'К': 0.034,
        'Л': 0.027, 'Љ': 0.006, 'М': 0.036, 'Н': 0.059, 'Њ': 0.011,  'О': 0.101,
        'П': 0.030, 'Р': 0.048, 'С': 0.056, 'Т': 0.052, 'Ћ': 0.005,  'У': 0.044,
        'Ф': 0.003, 'Х': 0.007, 'Ц': 0.007, 'Ч': 0.011, 'Џ': 0.0001, 'Ш': 0.009
    }
    slova = list(ucestalost_slova.keys())
    zbir_ucestalosti = sum(ucestalost_slova.values())

    def izvuci_slovo():
        r = random.uniform(0, zbir_ucestalosti)
        # Za svako slovo proveri da li je bas ono izvuceno
        for slovo in slova:
            r -= ucestalost_slova[slovo]
            if r <= 0:
                return slovo

    zadata_slova = [izvuci_slovo() for i in range(12)]

    poruka = 'Извучена су слова: ' + str(zadata_slova) + '\n'
    rec = input(poruka + 'Коју реч сте саставили: ').upper()
    # npr ['А', 'У', 'К', 'И', 'Д', 'У', 'Е', 'А', 'Н', 'У', 'М', 'Е']

    broj_raspolozivih_slova = {}
    moze = True
    # pomocu recnika prebroj pojavljivanja svakog slova medju zadatim slovima
    for slovo in zadata_slova: 
        broj_raspolozivih_slova[slovo] = broj_raspolozivih_slova.get(slovo, 0) + 1

    # za svako uportebljeno slovo, smanji broj pojavljivanja
    for slovo in rec: 
        broj_raspolozivih_slova[slovo] = broj_raspolozivih_slova.get(slovo, 0) - 1
        # ako je slovo vise puta upotrebljeno nego sto ga ima...
        if broj_raspolozivih_slova[slovo] < 0:
            moze = False # sastavljanje nije moguce
            break
            
    if moze:
        print("Реч '" + rec + "' може да се састави")
    else:
        print("Реч '" + rec + "' не може да се састави")

~~~~

Следи још један задатак у коме се речник мења током рада програма. Овога пута промене се дешавају на захтев корисника.
        
.. questionnote::

    **Задатак - стање магацина**
    
    Написати прорам који помоћу речника прати стање магацина на основу команди корисника. Корисник може да зада следеће 4 врсте команди:
    
    - **стави ставка n**, где је **ставка** било која реч, а **n** је цео број. По добијању ове команде треба у евиденцију стања додати **n** комада ставке *ставка* и приказати промену.
    - **узми ставка n**, где је **ставка** било која реч, а **n** је цео број. На ову команду са евиденције стања скинути **n** комада ставке *ставка* и приказати промену. Овде су дозвољена и негативна стања.
    - **стање**. У овом случају, кориснику треба приказати тренутно стање целог магацина.
    - **крај**. На ову команду програм треба да заврши са радом.

    Комуникација би на пример могла да изгледа овако:
    
    ================== ================================
    команде корисника  рачунар исписује
    ================== ================================
    стави брашно 300   брашно: 0 => 300
    стави јабуке 100   јабуке: 0 => 100
    узми брашно 30     брашно: 300 => 270
    стање              {'брашно': 270, 'јабуке': 100}
    крај
    ================== ================================
    
У програму који је већим делом написан, преостало је да се допуни неколико команди на крају.

.. activecode:: dict__warehouse_state

    stanje = {}
    kraj = False
    odgovor = ''
    while True:
        komanda = input(odgovor + 'Задајте команду: ')
        if komanda == 'крај': 
            break
            
        if komanda == 'стање': 
            odgovor = str(stanje) + '\n'
            continue
            
        komanda = komanda.split()
        if len(komanda) != 3:
            odgovor = 'Не разумем ту команду' + '\n'
            continue
            
        postupak, sta, koliko = komanda
        if postupak != 'узми' and postupak != 'стави':
            odgovor = 'Не разумем ту команду' + '\n'
            continue
        
        bilo_je = 0 # ispravite
        koliko = int(koliko)
        sada_ima = 0 if postupak == 'узми' else 0 # ispravite
        stanje[sta] = # ispravite
        odgovor = '%s: %d -> %d' % (sta, bilo_je, sada_ima) + '\n'


.. reveal:: dict__warehouse_state_reveal
   :showtitle: Решење
   :hidetitle: Сакриј решење
   
    .. activecode:: dict__warehouse_state_solution

        stanje = {}
        kraj = False
        odgovor = ''
        while True:
            komanda = input(odgovor + 'Задајте команду: ')
            if komanda == 'крај': 
                break
                
            if komanda == 'стање': 
                odgovor = str(stanje) + '\n'
                continue
                
            komanda = komanda.split()
            if len(komanda) != 3:
                odgovor = 'Не разумем ту команду' + '\n'
                continue
                
            postupak, sta, koliko = komanda
            if postupak != 'узми' and postupak != 'стави':
                odgovor = 'Не разумем ту команду' + '\n'
                continue
            
            bilo_je = stanje.get(sta, 0)
            koliko = int(koliko)
            sada_ima = bilo_je - koliko if postupak == 'узми' else bilo_je + koliko
            stanje[sta] = sada_ima
            odgovor = '%s: %d -> %d' % (sta, bilo_je, sada_ima) + '\n'

            


На крају поглавља о речницима, још једна игра. Овога пута ви замишљате животињу, а рачунар погађа.

``довршити опис игре и програма.``

.. activecode:: dict__animals_tree

    def prihvati_da_ili_ne(pitanje):
        odg = ''
        while odg != 'д' and odg != 'н': odg = input(pitanje + ' (д/н)? ')
        return DA if odg == 'д' else NE
            
    DA, NE = 0, 1
    prvo_pitanje = 'Хоћете ли још да играте? '
    hoce_jos = DA
    nastavak = {prvo_pitanje : ['коњ', None]}
    while hoce_jos == DA:
        postavljeno_pitanje = prvo_pitanje
        poslednji_odg = DA
        novo_pitanje = nastavak[prvo_pitanje][DA]
        while novo_pitanje:
            prethodno_pitanje = postavljeno_pitanje
            postavljeno_pitanje = novo_pitanje
            prethodni_odg = poslednji_odg
            poslednji_odg = prihvati_da_ili_ne(novo_pitanje)
            novo_pitanje = nastavak.get(novo_pitanje, [None, None])[poslednji_odg]
            
        if poslednji_odg == DA:
            komentar = 'Погодио сам. '
        else:
            stara_zivotinja = postavljeno_pitanje
            nova_zivotinja = input('Предајем се. Коју животињу сте замислили? ')
            novo_pitanje = input('Како да разликујем %s од %s? ' % (nova_zivotinja, stara_zivotinja))
            nastavak[novo_pitanje] = [nova_zivotinja, stara_zivotinja]
            nastavak[prethodno_pitanje][prethodni_odg] = novo_pitanje
            komentar = 'Хвала на разјашњењу, запамтићу. '
            
        hoce_jos = prihvati_da_ili_ne(komentar + 'Хоћете ли још да играте')
    print('Довиђења')

