проблеми:

- Код регуларних израза у мечованом објекту не раде методи 'sub', 'start', #'MatchObject' object has no attribute 'start'

Стрингови
=========

.. questionnote::

    **Пример - Помешане реченице**

``random.sample, od ranije join, len, (ima i MATRICA stringova)``

.. activecode:: console__str_mixed_statements

    import random

    recenice = [
        ['Беба', 'поспано', 'лиже', 'умазане', 'прсте.'],
        ['Риба', 'збуњено', 'удара', 'стаклене', 'зидове.'],
        ['Деда', 'са уживањем', 'чита', 'јучерашње', 'новине.'],
        ['Ветар', 'шумећи', 'разноси', 'суве', 'листове.'],
        ['Тигар', 'халапљиво', 'кида', 'велике', 'комаде меса.'],
        ['Бака', 'с љбављу', 'пече', 'укусне', 'палачинке.'],
        ['Фудбалер', 'ужурбано', 'обува', 'жуте', 'копачке.']
    ]

    n = len(recenice)
    r = range(n)
    for i in range(20): # napravi 20 recenica
        s = random.sample(r, 5) # izaberi 5 razlicitih recenica
        # slozi pet delova recenice
        nova_recenica = ' '.join((recenice[s[deo]][deo] for deo in range(5))) 
        print(nova_recenica)

        
.. questionnote::

    **Пример - Банер**
        
.. activecode:: console__str_banner

    red1 = [' ███ ', '████ ', ' ███ ', '████ ', '█████', '█████', ' ███ ', '█   █', ' ███ ', '  ███', '█   █', '█    ', '█   █', '█   █', ' ███ ', '████ ', ' ███ ', '████ ', ' ████', '█████', '█   █', '█   █', '█   █', '█   █', '█   █', '█████']
    red2 = ['█   █', '█   █', '█   █', '█   █', '█    ', '█    ', '█   █', '█   █', '  █  ', '   █ ', '█  █ ', '█    ', '██ ██', '█   █', '█   █', '█   █', '█   █', '█   █', '█    ', '  █  ', '█   █', '█   █', '█   █', '█   █', '█   █', '    █'] 
    red3 = ['█   █', '█   █', '█    ', '█   █', '█    ', '█    ', '█    ', '█   █', '  █  ', '   █ ', '█ █  ', '█    ', '█ █ █', '██  █', '█   █', '█   █', '█   █', '█   █', '█    ', '  █  ', '█   █', '█   █', '█   █', ' █ █ ', ' █ █ ', '   █ '] 
    red4 = ['█████', '████ ', '█    ', '█   █', '████ ', '████ ', '█    ', '█████', '  █  ', '   █ ', '██   ', '█    ', '█ █ █', '█ █ █', '█   █', '████ ', '█   █', '████ ', ' ███ ', '  █  ', '█   █', '█   █', '█ █ █', '  █  ', '  █  ', '  █  '] 
    red5 = ['█   █', '█   █', '█    ', '█   █', '█    ', '█    ', '█  ██', '█   █', '  █  ', '   █ ', '█ █  ', '█    ', '█   █', '█  ██', '█   █', '█    ', '█ █ █', '█ █  ', '    █', '  █  ', '█   █', ' █ █ ', '█ █ █', ' █ █ ', '  █  ', ' █   '] 
    red6 = ['█   █', '█   █', '█   █', '█   █', '█    ', '█    ', '█   █', '█   █', '  █  ', '█  █ ', '█  █ ', '█    ', '█   █', '█   █', '█   █', '█    ', '█  █ ', '█  █ ', '    █', '  █  ', '█   █', ' █ █ ', '█ █ █', '█   █', '  █  ', '█    '] 
    red7 = ['█   █', '████ ', ' ███ ', '████ ', '█████', '█    ', ' ███ ', '█   █', ' ███ ', ' ██  ', '█   █', '█████', '█   █', '█   █', ' ███ ', '█    ', ' ██ █', '█   █', '████ ', '  █  ', ' ███ ', '  █  ', ' █ █ ', '█   █', '  █  ', '█████'] 

    redovi = [red1, red2, red3, red4, red5, red6, red7]

    tekst = input('Унесите текст (малим енглеским словима): ')
    for red in redovi:
        for slovo in tekst:
            if slovo == ' ':
                print('     ', end = ' ')
            elif 'a' <= slovo and slovo <='z':
                print(red[ord(slovo)-ord('a')], end = ' ')
            else:
                print('█████', end = ' ')
        print()

        
.. questionnote::

    **Пример - Уметање слогова**

.. activecode:: console__str_cripto1a

    tekst = input('унесите текст: ')
    tekst = tekst.replace('а', 'апа')
    tekst = tekst.replace('е', 'епе')
    tekst = tekst.replace('и', 'ипи')
    tekst = tekst.replace('о', 'опо')
    tekst = tekst.replace('у', 'упу')
    print(tekst)

.. activecode:: console__str_cripto1b

    tekst = input('унесите текст: ')
    for slovo in 'аеиоу':
        tekst = tekst.replace(slovo, slovo+'p'+slovo)
    print(tekst)

.. questionnote::

    **Задатак - брисање самогласника**
    
    Учитати текст а затим га исписати без самогласника. 
    
    На пример, ако је учитан текст 'Кад мало размислите, самогласници су сувишни.', онда треба исписати 'Кд мл рзмслт, смглснц с свшн.'

.. activecode:: console__str_removing_vowels1a
   
    tekst = input()
    bez_samogl = ''
    for slovo in tekst:
        if slovo not in 'аеиоу':
            bez_samogl += slovo
    print(bez_samogl)

``ово је ок за мале стрингове, за веома дугачак текст је непотребно врло скупо због имутабилности стрингова``
   
.. activecode:: console__str_removing_vowels1b
   
    tekst = input()
    bez_samogl = []
    for slovo in tekst:
        if slovo not in 'аеиоу':
            bez_samogl.append(slovo)
    print(''.join(bez_samogl))

.. activecode:: console__str_removing_vowels2
   
    tekst = input()
    for slovo in 'аеиоу':
        tekst = tekst.replace(slovo, '')
    print(tekst)

.. activecode:: console__str_removing_vowels3
   
    tekst = input()
    tekst = [slovo for slovo in tekst if slovo not in 'аеиоу']
    print(''.join(tekst))

.. activecode:: console__str_removing_vowels4
   
    s = map(lambda sl : '' if sl in 'аеиоу' else sl, input())
    print(''.join(s))

.. questionnote::

    **Пример - Преметање слогова**

.. activecode:: console__str_cripto2a

    import re
    def premetni(rec):
        n = len(rec)
        i = 0
        while i < n and rec[i] not in 'аеиоу':
            i += 1
        if i < n:
            i += 1
            rec = rec[i:] + rec[:i]
        return rec
                
    tekst = [
        'брате пази мало како идеш',
        'који си ти глупи глупан',
        'ниџо дођи вамо да ти нешто кажем',
        'зоки што пљујеш немој да си простак',
    ]
    
    for recenica in tekst:
        print('%35s' % recenica, end = ' -> ')
        for rec in recenica.split():
            print(premetni(rec), end = ' ')
        print()
        
``Основно о регуларним изразима``

.. activecode:: console__str_cripto2b

    import re
    def premetni(rec):
        m = re.search("([^аеиоу]*[аеиоу])(.*)", rec)
        if m:
            rec = m.group(2)+m.group(1)
        return rec
                
    tekst = [
        'брате пази мало како идеш',
        'који си ти глупи глупан',
        'ниџо дођи вамо да ти нешто кажем',
        'зоки што пљујеш немој да си простак',
    ]
    
    for recenica in tekst:
        print('%35s' % recenica, end = ' -> ')
        print(*tuple(map(premetni, recenica.split())), sep=' ')

.. questionnote::

    **Пример - Вешала**

- LISTE I STRINGOVI - mutabilnost, konverzija
- zip, (c = a1 if b else a2), continue, 
- postepeno dorađivanje programa - primer: 
    da ne skida ponovo za isti promašaj, da prikaže promašaje, da ponavlja input dok je odgovor prazan
        
.. activecode:: console__str_hangman
    
    ukupno_pokusaja = 6
    promasaji = ['.'] * ukupno_pokusaja
    pojam = input('Погађач нека не гледа, задавач нека унесе текст: ')
    pojam = pojam.upper()             # prebaci sve u velika slova
    polupogodjen_pojam = [(' ' if slovo == ' ' else '_') for slovo in pojam]    
    pogodjeno = False
    preostalo_pokusaja = ukupno_pokusaja
    
    while not pogodjeno and preostalo_pokusaja > 0:
        pokusaj = input('Промашаји: ' + ''.join(promasaji) +\
        '    Појам: ' + ''.join(polupogodjen_pojam) +\
        '    Погађај слово: ')
        if pokusaj == '': continue
        slovo = pokusaj[0].upper()
        if slovo in promasaji: continue
        polupogodjen_pojam = [(slovo if slovo == p else pp) 
            for p, pp in zip(pojam, polupogodjen_pojam)]
        if slovo not in pojam: # ako slovo nije nadjeno
            promasaji[ukupno_pokusaja - preostalo_pokusaja] = slovo
            preostalo_pokusaja -= 1 # pogadjac gubi jedan zivot
        pogodjeno = (''.join(polupogodjen_pojam) == pojam)        
    
    print('Реч је била', pojam)
    print('Браво!' if pogodjeno else 'Биће боље следећи пут.')

        
