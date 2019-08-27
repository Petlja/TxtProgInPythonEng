problemi:

- nema numpy #ImportError: No module named numpy on line 1
- nema locale #NotImplementedError: locale is not yet implemented in Skulpt on line 1

Серије података
===============

.. code::

    Овде иде уводна прича - једно име а много вредности (обично истородне али не мора).
    Баратање групом вредности помоћу функција које раде са итераблама (па и листама)
    Касније поменути индексе и приступ појединачним елементима листе


.. questionnote::

    **Задатак - Најјефтинији за динар**
    
    У продавници је распродаја - ако купите три производа, најјефтинији плаћате само један динар. Ви сте одабрали три ствари које желите да купите. Колико ће вас оне коштати?

.. activecode:: console_calc_cheapest_for_cent1

    cena1, cena2, cena3 = map(int, input('Unesite 3 cene: ').split())
    if cena1 <= cena2 and cena1 <= cena3:
        print(1 + cena2 + cena3)
    elif cena2 <= cena1 and cena2 <= cena3:
        print(cena1 + 1 + cena3)
    else:
        print(cena1 + cena2 + 1)

Овај програм је већ мало компликованији него што је неопходно, а додатно би се компликовао када би требало купити више од три ствари ради добијања попуста. Зато је бољи начин да се израчуна и искористи цена најјефтинијег производа.

Функција *min()* може да има било који број параметара, а као вредност враћа најмањи од њих.

.. activecode:: console_calc_cheapest_for_cent2

    cena1, cena2, cena3 = map(int, input('Unesite 3 cene: ').split())
    puna_cena = cena1 + cena2 + cena3
    najniza_cena = min(cena1, cena2, cena3)
    snizena_cena = puna_cena - najniza_cena + 1
    print(snizena_cena)

Програм постаје још мало једнставнији ако употребимо листу уместо појединачних вредности *cena1*, *cena2*, *cena3*.

- Функција *min()* може да као параметар прихвати и итераблу (па и листу, као једну врсту итерабле), а да врати најмању од вредности задатих том итераблом. 
- Функција *sum()*, слично функцији *min()*, прихвата итераблу као параметар, а враћа збир вредности задатих итераблом.

.. activecode:: console_calc_cheapest_for_cent3

    cene = map(int, input('Unesite 3 cene: ').split())
    puna_cena = sum(cene)
    najniza_cena = min(cene)
    snizena_cena = puna_cena - najniza_cena + 1
    print(snizena_cena)

Задатак је могао да гласи да се најјефтинији производ добија за динар при *n* купљених производа, при чему би *n* уместо 3, могао да буде 2 или 4, или било који други број. У последњој верзији програма при промени *n* не бисмо морали да мењамо ништа у програму. То нам је такође омогућила употреба функције *map()*.

          
.. questionnote::
    
    ``у овом задатку нема листи - преместити``
    
    **Пример - GdeJeNajjeftinije**
    
    Гледали сте цене неког производа на Интернету у више продавница, па вам се све измешало. 
    
    Напишите програм који вас прво пита за колико продавница сте гледали цену, затим за сваку продавницу тражи назив продавнице и цену производа у њој, а на крају исписује назив продавнице у којој је производ најјефтинији, као и ту најнижу цену.
    
.. activecode:: console_calc_cheapest_store

    najniza_cena = float("inf")  # beskonacno, svaka cena ce biti niza od ove
    najjeftinija_prodavnica = ''
    n = int(input("Колико продавница сте проверили: "))
    for i in range(n):
        prodavnica = input("Наведите назив продавнице: ")
        cena = float(input("Наведите цену: "))
        if najniza_cena > cena:
            najniza_cena = cena
            najjeftinija_prodavnica = prodavnica
            
    print(najjeftinija_prodavnica, najniza_cena)


.. questionnote::
    
    **Пример - време такмичара**
    
    Према пропозицијама такмичења, сваки такмичар *n* пута покушава што брже да обави задатак. Најкраће и најдуже време се затим одбацују, а од преосталих времена се узима аритметичка средина. 
    
    Дат је број *n* и *n* времена једног такмичара у секундама. Израчунати званично време овог такмичара. 

.. activecode:: console_tuplelist_mid_time1

    vremena = input('Unesite vremena u jednom redu: ')
    vremena = vremena.split()
    n = len(vremena)
    zbir_vremena = 0
    najmanje_vreme = float("inf") # plus beskonacno
    najvece_vreme =  - float("inf") # minus beskonacno
    for vreme in vremena:
        vreme = float(vreme)
        zbir_vremena += vreme
        if najmanje_vreme > vreme:
            najmanje_vreme = vreme
        if najvece_vreme < vreme:
            najvece_vreme = vreme
        
    print((zbir_vremena - najmanje_vreme - najvece_vreme) / (n - 2))

.. activecode:: console_tuplelist_mid_time2

    vremena = [float(i) for i in input('Unesite vremena u jednom redu: ').split()]
    print((sum(vremena) - max(vremena) - min(vremena)) / (len(vremena) - 2))

.. activecode:: console_tuplelist_mid_time3

    vremena = list(map(float, input('Unesite vremena u jednom redu: ').split()))
    print((sum(vremena) - max(vremena) - min(vremena)) / (len(vremena) - 2))

.. activecode:: console_tuplelist_mid_time4

    vremena = map(float, input('Unesite vremena u jednom redu: ').split())
    print((sum(vremena) - max(vremena) - min(vremena)) / (len(vremena) - 2))

.. questionnote::
    
    **Пример - уређивање пет бројева**
    
    Учитати пет целих бројева и исписати их поређане по величини.
    
``индексирање - приступ појединим елементима серије помоћу редног броја``

``распакивање листе: print(\*p, sep='\n')``

.. activecode:: console_tuplelist_sort_five1

    p = [ int(input()), int(input()), int(input()), int(input()), int(input()) ]
    p = sorted(p)
    print(p[0], p[1], p[2], p[3], p[4], sep='\n')

.. activecode:: console_tuplelist_sort_five2

    p = [ int(input()) for i in range(5) ]
    p = sorted(p)
    print(*p, sep='\n')

``торка, индексирање торке``

.. activecode:: console_tuplelist_indexing1

    print('Деца Воле')
    for reci in (
        ('чудне', 'оџачари', 'кочничари'),
        ('слатке', 'сутлијаши', 'грилијаши'),
        ('смешне', 'пападаћи', 'сумарени')):
        print()
        print('Деца воле %s ствари' % reci[0])
        print('као сто су %s,' % reci[1])
        print('као што су %s,' % reci[2])
        print('као што су, као што су...')

``још једно распакивање листе при испису``

.. activecode:: console_tuplelist_indexing2

    print('Деца Воле', end = '\n\n') # naslov
    strofa = '''
    Деца воле %s ствари
    као сто су %s,
    као што су %s,
    као што су, као што су...
    '''
    for nove_reci in (
        ('чудне', 'оџачари', 'кочничари'),
        ('слатке', 'сутлијаши', 'грилијаши'),
        ('смешне', 'пападаћи', 'сумарени')):
        print(strofa % nove_reci)

.. questionnote::
    
    **Пример - даљина за бронзу**
    
    Познате су нам дужине скокова у сантиметрима за свих *n* досадашњих такмичара. Колико треба да скочи следећи (последњи) такмичар, да би за бар један сантиметар надмашио тренутно трећепласираног и освојио бронзану медаљу?

.. activecode:: console_tuplelist_bronze1    
    
    x = [float(i) for i in input().split()]
    sx = sorted(x, reverse = True)
    print(1 + sx[2])

.. activecode:: console_tuplelist_bronze2

    print(1 + sorted(map(float, input().split()))[-3])
    
.. questionnote::
    
    **Пример - приказ календара**
    
    Написати програм који приказује календар за текући месец

``коментар - шта постоји у Пајтон библиотеци. Свеједно, урадити пешке за вежбу и забаву``

.. code::

    import datetime, calendar, locale

    locale.setlocale(locale.LC_ALL, 'sr_Cyrl_RS')
    sada = datetime.datetime.now()
    print('Календар за текући месец:\n')
    print(calendar.month(sada.year, sada.month))
    
.. activecode:: console_tuplelist_calendar

    import datetime

    def prestupna(godina):
        return (godina % 4 == 0 and godina % 100 != 0) or godina % 400 == 0

    def broj_dana_u_mesecu(mesec, godina):
        broj_dana_po_mesecima = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
        return 29 if mesec == 2 and prestupna(godina) else broj_dana_po_mesecima[mesec]

    def ispisi_kalendar(broj_dana, prvi_dan_u_mesecu, sirina_kolone):
        dani = ('Пон', 'Уто', 'Сре', 'Чет', 'Пет', 'Суб', 'Нед')
        opis = ('%' + str(sirina_kolone) + 's') * 7 # '%4s%4s%4s%4s%4s%4s%4s'
        print(opis % dani) 
        print('-' * 7 * sirina_kolone)
        kolona = prvi_dan_u_mesecu
        opis_broja = '%' + str(sirina_kolone) + 'd' # '%4d'
        print(' ' * (kolona - 1) * sirina_kolone, end = '')
        for i in range(1, broj_dana + 1):
            print(opis_broja % i, end = '')
            if kolona == 7:
                print()
                kolona = 1
            else:
                kolona += 1
        
    sada = datetime.datetime.now()
    dan_u_nedelji = int(sada.strftime("%w"))
    prvi_dan_u_mesecu = (dan_u_nedelji - sada.day + 1) % 7
    broj_dana = broj_dana_u_mesecu(sada.month, sada.year)
    sirina_kolone = 4
    meseci = ('Јануар', 'Фебруар', 'Март', 'Април', 'Мај', 'Јун', 
        'Јул', 'Август', 'Септембар', 'Октобар', 'Новембар', 'Децембар')
    print('Календар за текући месец (%s %d):' % (meseci[sada.month-1], sada.year))
    ispisi_kalendar(broj_dana, prvi_dan_u_mesecu, sirina_kolone)


**Издвајање делова листе, торке, или стринга**

``s[a:b:c] са комбинацијама изостављања неких од параметара a, b, c. У примеру је стринг, али све исто важи за листу и торку.``

Означимо са *n* број знакова у стрингу. Тада:

- s[a:b:c] значи почни од места *a*, иди до *b* не укључујући га, а са кораком *c*
- Ако се за *a* или *b* наведе негативан број, подразумева се за *n* већи (бројање с краја)
- Ако *c* није наведен, подразумева се 1
- Ако је *c* позитиван, подразумева се да је *a=0*, а *b=n*
- Ако је *c* негативан, подразумева се да је *a=n-1*, а *b* је "пре нуле" (-1, али не *n-1*)

.. activecode:: console__intro_slicing

    s = '0123456789'
    n = len(s)
    print('s[a:b:c] значи почни од места a, иди до b не укључујући га, а са кораком c')
    print('s          = s[0:n:1] = ', s)            # све
    print('s[3:7:1]   = s[3:7:1] = ', s[3:7:1])     # од 3 до 7 без 7
    print('s[3:7:2]   = s[3:7:2] = ', s[3:7:2])     # од 3 до 7 без 7

    print('Ако c није наведен, подразумева се 1')
    print('s[3:7]     = s[3:7:1] = ', s[3:7])       # од 3 до 7 без 7

    print('Када је c позитиван, ако се изостави a, подразумева се вредност 0')
    print('а ако се изостави b, подразумева се вредност n')
    print('s[:]       = s[0:n:1] = ', s[:])         # све
    print('s[::]      = s[0:n:1] = ', s[::])        # све
    print('s[:3]      = s[0:3:1] = ', s[:3])        # прва 3
    print('s[3:]      = s[3:n:1] = ', s[3:])        # од трећег до краја

    print('Ако се за a или b наведе негативан број, подразумева се индекс за n већи.')
    print('Према томе, индекс :code:`-k` можемо да читамо као к-ти елемент с краја')
    print('s[-2:]     = s[n-2:n:1]   = ', s[-2:])   # последња 2 (од другог скраја до краја) 
    print('s[:-2]     = s[0:n-2:1]   = ', s[:-2])   # све осим последња два
    print('s[3:-2]    = s[3:n-2:1]   = ', s[3:-2])  # од трећег до другог скраја
    print('s[-6:-2]   = s[n-6:n-2:1] = ', s[-6:-2]) # од шестог скраја до другог скраја

    print('Ако је c негативан, подразумева се ако је a или b изостављен,')
    print('да је a=n-1, а b је "до почетка" (не може се експлицитно навести)')
    print('s[::-1]    = s[n-1::-1] = ', s[::-1])    # све уназад
    print('s[3::-1]   = s[3::-1]   = ', s[3::-1] )  # од 3 до почетка (уназад)
    print('s[-2::-1]  = s[-2::-1]  = ', s[-2::-1])  # од n-2 до почeтка (уназад)
    print('s[7:3:-1]  = s[7:3:-1]  = ', s[7:3:-1])  # од 7 до 3 уназад
    print('s[7:3:-2]  = s[7:3:-2]  = ', s[7:3:-2])  # од 7 до 3 уназад, сваки други

    print('Ако су границе у нескладу, резултат је празан стринг')
    print('s[5:3:]    = s[5:3:1]   = ', s[5:3:]  )
    print('s[5:7:-1]  = s[5:7:-1]  = ', s[5:7:-1])
    

.. questionnote::
    
    **Пример - сумо рвачи**
    
    Четири сумо рвача су у приземљу зграде. Познате су њихове масе и носивост лифта. Колико вожњи лифтом је укупно потребно да би се сваки од њих превезао на спрат који жели?

.. activecode:: console_tuplelist_sumo

    prompt = 'unesite tezine 4 rvaca i nosivost lifta (razdvojene razmakom): '
    podaci = input(prompt).split()
    rvaci = map(int, podaci[0:4])
    L = int(podaci[4])
    a, b, c, d = sorted(rvaci, reverse=True) # prvo najtezi

    # izracunavamo broj voznji
    if a + b + c + d <= L:
        brojVoznji = 1
    elif (a + d <= L and b + c <= L or
         b + c + d <= L):
        brojVoznji = 2;
    elif c + d <= L:
        brojVoznji = 3;
    else:
        brojVoznji = 4;

    print('Potreban broj voznji je', brojVoznji)

.. questionnote::
    
    **Пример - полуфинале**

    Две хиљаде седамнаесте године, У полуфинале светског првенства у атлетици трке на 100 метара за мушкарце, пласирала су се 24 учесника. Они су подељени у три полуфиналне групе по осам такмичара. За финале се квалификују по најбржа два спринтера из сваке групе, као и два најбржа од преосталих.
    
    За сваког од 24 такмичара позната је његова полуфинална група, стаза у којој је трчао, његово име и време које је постигао. Исписаати имена и времена атлетичара који су се пласирали у финале.
    
    (Подаци преузети са https://en.wikipedia.org/wiki/2017_World_Championships_in_Athletics_%E2%80%93_Men%27s_100_metres)
    
``формат, slice, lambda``

.. activecode:: console_tuplelist_semifinals

    GRUPA, STAZA, IME, VREME = 0, 1, 2, 3
    takmicari = (
        (1, 2, "Akani Simbine", 10.05),
        (1, 3, "Asuka Cambridge", 10.25),
        (1, 4, "James Dasaolu", 10.22),
        (1, 5, "Julian Forte", 10.13),
        (1, 6, "Justin Gatlin", 10.09),
        (1, 7, "Ben Youssef Meïté", 10.12),
        (1, 8, "Kim Kuk-young", 10.4),
        (1, 9, "Xie Zhenye", 10.28),
        (2, 2, "Emmanuel Matadi", 10.2),
        (2, 3, "Alex Wilson", 10.3),
        (2, 4, "Yohan Blake", 10.04),
        (2, 5, "Abdul Hakim Sani Brown", 10.28),
        (2, 6, "Su Bingtian", 10.1),
        (2, 7, "Jak Ali Harvey", 10.16),
        (2, 8, "Christopher Belcher", 10.2),
        (2, 9, "Reece Prescod", 10.05),
        (3, 2, "Shuhei Tada", 10.26),
        (3, 3, "Emre Zafer Barnes", 10.27),
        (3, 4, "Christian Coleman", 9.97),
        (3, 5, "Andrew Fisher", 10.36),
        (3, 6, "Usain Bolt", 9.98),
        (3, 7, "Chijindu Ujah", 10.12),
        (3, 8, "Jimmy Vicaut", 10.09),
        (3, 9, "Cejhae Greene", 10.64)
    )

    prva_grupa = sorted(takmicari[0:8], key=lambda trkac: trkac[VREME])
    druga_grupa = sorted(takmicari[8:16], key=lambda trkac: trkac[VREME])
    treca_grupa = sorted(takmicari[16:24], key=lambda trkac: trkac[VREME])
    direktno = prva_grupa[0:2] + druga_grupa[0:2] + treca_grupa[0:2]
    ostali = prva_grupa[2:] + druga_grupa[2:] + treca_grupa[2:]
    po_vremenu = sorted(ostali, key=lambda trkac: trkac[VREME])[0:2]
    finale = sorted(direktno + po_vremenu, key=lambda trkac: trkac[VREME])

    for (grupa, staza, ime, vreme) in finale:
        print('%20s %10.2f' %(ime, vreme))