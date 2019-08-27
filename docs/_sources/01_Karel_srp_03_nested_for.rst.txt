Још краћи програми
==================

Подсетимо се последњег програма претходне лекције. Требало је да Карел узме по пет лоптица са сваког од три наредна поља. 

.. image:: ../_images/Karel/nested_for_3x5.png
    :width: 300px
    :align: center

Програм који решава задатак могао је да изгледа овако:

.. activecode:: Karel_nested_for__intro_1
   :passivecode: true

    from karel import *
    napred()
    for i in range(5):
        uzmi()
    napred()
    for i in range(5):
        uzmi()
    napred()
    for i in range(5):
        uzmi()
        
Видимо да се у овом програму следећа група наредби понавља три пута:

.. activecode:: Karel_nested_for__intro_2
   :passivecode: true

    napred()
    for i in range(5):
        uzmi()

То нам омогућава да додатно скратимо програм. При објашњавању *for* наредбе смо поменули да у телу петље могу да се нађу друге петље. Сада имамо прилику да то искористимо.
 
Угнежђене for наредбе
---------------------

Када се у телу једне петље налази друга петља, онда прву петљу зовемо спољна петља, а другу унутрашња. Заједно их зовемо угнежђене или уметнуте петље. У следећем примеру ћемо видети како се пишу угнежђене *for* наредбе.

Покупи три пута по 5 лоптица
''''''''''''''''''''''''''''

.. questionnote::

  Испред Карела су три поља, а на њима по 5 лоптица. Карел треба да покупи све лоптице.

Задатак је поновљен, али сада ћемо га решити на другачији начин. 

.. infonote::
   Раније смо поменули да је са ``i`` у досадашњим примерима *for* наредбе именовано место на коме бројимо докле смо стигли са понављањем. Сада први пут треба да у току бројања једне ствари (поља) пребројимо другу ствар (лоптице). То значи да ће на пример бити потребно да знамо када смо на трећем пољу при другој лоптици. Због тога не можемо да користимо исто име за оба бројача, па смо уместо досадашњег ``i`` увели нова имена за бројаче. У програму који следи бројач поља смо назвали ``i_polje``, а за бројач лоптица ``i_loptica``. 
   
.. karel:: Karel_for_TakeMxN
   :blockly:

   {
        setup:function() {
           var numAvenues = 4;
           var numBalls = 5;
           var world = new World(numAvenues, 1);
           world.setRobotStartAvenue(1);
           world.setRobotStartStreet(1);
           world.setRobotStartDirection("E");
           
           for (var k = 2; k <= numAvenues; k++)
              world.putBalls(k, 1, numBalls);
           
           var robot = new Robot();

           var code = ["from karel import *",
                       "for i_polje in range(3):",
                       "    napred()",
                       "    for i_loptica in range(5):",
                       "        uzmi()",
                       ""];
           return {robot:robot, world:world, code:code};
        },
    
        isSuccess: function(robot, world) {
           return robot.getBalls() == 15; // 3 x 5 balls
        },
   }

У датом решењу наредба *uzmi()* је додатно увучена, јер се она извршава по једном за свако ``i_loptica`` из опсега [0, 1, 2, 3, 4]. Осим тога, цела наредба ``for i_loptica in range(5):`` се (уз наредбу *napred()*, заједно са својим телом) понавља 3 пута, по једном за свако ``i_polje`` из опсега [0, 1, 2]. То значи да се наредба *uzmi()* извршава укупно 3 x 5 = 15 пута (на сваком од три поља по пет пута).
   
.. infonote::
   Код уметнутих петљи је потребно додатно пазити на правилно увлачење наредби, јер оно постаје нешто мало компликованије. Погрешно увлачење појединих наредби може да доведе до погрешног резултата, или до програма који уопште не ради.
  
Задаци за вежбу
---------------

Прескок
'''''''

.. questionnote::

  Испред Карела је на сваком трећем пољу по једна лоптица, а он треба да их обе покупи.
  
Карел треба да понови 2 пута групу наредби: "три пута иди напред, а затим узми лоптицу".

.. karel:: Karel_for_every_nth_square
    :blockly:

    {
        setup:function() {
            var everyNth = 3;
            var numRepetitions = 2;
            var numBalls = 1;
            var numAvenues = 1 + numRepetitions * everyNth;
            var world = new World(numAvenues, 1);
            world.setRobotStartAvenue(1);
            world.setRobotStartStreet(1);
            world.setRobotStartDirection("E");
           
            for (var k = 1; k <= numRepetitions; k++)
                world.putBalls(1+k*everyNth, 1, numBalls);
            
            var robot = new Robot();
         
            var code = ["from karel import *",
                        "for i_pon in range(2):      # dva puta ponovi sve sto sledi",
                        "    # upotrebite for naredbu da kazete Karelu da ode 3 polja napred",
                        "    uzmi()              #    uzmi lopticu",
                        ""];
    
            return {robot:robot, world:world, code:code};
        },
    
        isSuccess: function(robot, world) {
            return robot.getBalls() == 2; // number of repetitions
        },
    }

.. commented out
   .. reveal:: Karel_for_every_nth_square_reveal
       :showtitle: Решење
       :hidetitle: Сакриј решење
   
       .. activecode:: Karel_for_every_nth_square_solution
           :passivecode: true
         
           from karel import *
           for i_pon in range(2):     # dva puta ponovi sve sto sledi
               for i_polje in range(3):   # idi 3 polja napred
                   napred()
               uzmi()                     # uzmi lopticu

На сваком трећем по 5
'''''''''''''''''''''

.. questionnote::

  Испред Карела је на сваком трећем пољу по пет лоптица, а он треба да их све покупи.
  
Задатак је сличан претходном, треба само понављати узимање лоптице. Пазите да петља за узимање лоптица буде испод петље за кретање напред, а не у њој.

.. karel:: Karel_for_every_nth_square_5
    :blockly:

    {
        setup:function() {
            var everyNth = 3;
            var numRepetitions = 2;
            var numBalls = 5;
            var numAvenues = 1 + numRepetitions * everyNth;
            var world = new World(numAvenues, 1);
            world.setRobotStartAvenue(1);
            world.setRobotStartStreet(1);
            world.setRobotStartDirection("E");
           
            for (var k = 1; k <= numRepetitions; k++)
                world.putBalls(1+k*everyNth, 1, numBalls);
            
            var robot = new Robot();
         
            var code = ["from karel import *",
                        "for i_pon in range(2):      # dva puta ponovi sve sto sledi",
                        "    # upotrebite for naredbu da kazete Karelu da ode 3 polja napred",
                        "    # upotrebite novu for naredbu da kazete Karelu da uzme 5 loptica",
                        ""];
    
            return {robot:robot, world:world, code:code};
        },
    
        isSuccess: function(robot, world) {
            return robot.getBalls() == 10; // numRepetitions x numBalls
        },
    }

.. commented out
   .. reveal:: Karel_for_every_nth_square_5_reveal
       :showtitle: Решење
       :hidetitle: Сакриј решење
   
       .. activecode:: Karel_for_every_nth_square_5_solution
           :passivecode: true
         
           from karel import *
           for i_pon in range(2):     # dva puta ponovi sve sto sledi
               for i_polje in range(3):   # idi 3 polja napred
                   napred()
               for i_loptica in range(5): # uzmi 5 loptica
                   uzmi()


У круг
''''''

.. questionnote::

  Карел поново треба да покупи све лоптице.
  
Спољна петља треба да се изврши 3 пута, а у њој Карел треба да уради следеће:

- Два пута понови кораке: "иди напред" и "узми лоптицу"
- Окрени се лево

.. karel:: Karel_for_ring
    :blockly:

    {
        setup:function() {
            var w = [
               '███████',
               '█1.1.1█',
               '█.███.█',
               '█0.0█1█',
               '█████.█',
               '█E.1.1█',
               '███████'
            ];

            var ny = Math.floor(w.length / 2);
            var nx = Math.floor(w[0].length / 2);
            var world = new World(nx, ny);

            for (let y = 1; y <= ny; y++) {
                let wy = 2*(ny-y) + 1;
                for (let x = 1; x <= nx; x++) {
                    let wx = 2*x - 1;
                    if (y < ny && w[wy - 1].charAt(wx) == "█") world.addEWWall(x, y, 1);
                    if (x < nx && w[wy].charAt(wx + 1) == "█") world.addNSWall(x, y, 1);
                    let c = w[wy].charAt(wx);
                    let pos = "SWEN".indexOf(c);
                    if (pos > -1) {
                        world.setRobotStartAvenue(x);
                        world.setRobotStartStreet(y);
                        world.setRobotStartDirection("SWEN".charAt(pos));
                    }
                    let d = w[wy].charCodeAt(wx);
                    if (d >= 48 && d < 58) world.putBalls(x, y, d - 48);
                }
            }

            var robot = new Robot();
         
            var code = ["from karel import *",
                        "... # dopunite",
                        ""];
                     
            return {robot:robot, world:world, code:code};
        },
      
        isSuccess: function(robot, world) {
           return robot.getBalls() == 6;
        }
    }

.. reveal:: Karel_for_ring_reveal_1
    :showtitle: Помоћ
    :hidetitle: Сакриј помоћ

    Упутство смо још мало приближили програму, пробајте да га претворите у наредбе. Ако ипак желите да видите програм, кликните на дугме "Решење".
    
    .. activecode:: Karel_for_ring_solution_1
        :passivecode: true
      
        za svaku od 3 strane:
            za svako od 2 polja:
                idi napred
                uzmi lopticu
            okreni se na levo

    .. reveal:: Karel_for_ring_reveal_2
       :showtitle: Решење
       :hidetitle: Сакриј решење
   
       .. activecode:: Karel_for_ring_solution_2
           :passivecode: true
         
           from karel import *
           for i_strana in range(3):     # tri puta ponovi sve sto sledi
               for i_polje in range(2):     # dva puta idi napred i uzmi
                   napred()
                   uzmi()
               levo()                       # okreni se duz sledece strane



У круг по 3 лоптице
'''''''''''''''''''

.. questionnote::

  Напишите програм помоћу кога ће Карел да покупи свих 18 лоптица.
  
Разлика у односу на претходни задатак је у томе што сада узимање лоптица треба да буде у додатној петљи. То значи да ћемо имати три угнежђене петље: једну која броји стране лавиринта, другу која броји поља дуж једне стране, и трећу која броји лоптице на пољу.

.. karel:: Karel_for_ring_3
    :blockly:

    {
        setup:function() {
            var w = [
               '███████',
               '█3.3.3█',
               '█.███.█',
               '█0.0█3█',
               '█████.█',
               '█E.3.3█',
               '███████'
            ];

            var ny = Math.floor(w.length / 2);
            var nx = Math.floor(w[0].length / 2);
            var world = new World(nx, ny);

            for (let y = 1; y <= ny; y++) {
                let wy = 2*(ny-y) + 1;
                for (let x = 1; x <= nx; x++) {
                    let wx = 2*x - 1;
                    if (y < ny && w[wy - 1].charAt(wx) == "█") world.addEWWall(x, y, 1);
                    if (x < nx && w[wy].charAt(wx + 1) == "█") world.addNSWall(x, y, 1);
                    let c = w[wy].charAt(wx);
                    let pos = "SWEN".indexOf(c);
                    if (pos > -1) {
                        world.setRobotStartAvenue(x);
                        world.setRobotStartStreet(y);
                        world.setRobotStartDirection("SWEN".charAt(pos));
                    }
                    let d = w[wy].charCodeAt(wx);
                    if (d >= 48 && d < 58) world.putBalls(x, y, d - 48);
                }
            }

            var robot = new Robot();
         
            var code = ["from karel import *",
                        "... # dopunite",
                        ""];
                     
            return {robot:robot, world:world, code:code};
        },
      
        isSuccess: function(robot, world) {
           return robot.getBalls() == 18;
        }
    }

.. reveal:: Karel_for_ring_3_reveal
    :showtitle: Помоћ
    :hidetitle: Сакриј помоћ

    Поново дајемо упутство које мало више личи на програм (овај пут без решења).
    
    .. activecode:: Karel_for_ring_3_solution
        :passivecode: true
      
        za svaku od 3 strane:
            za svako od 2 polja:
                idi napred
                za svaku od 3 loptice:
                    uzmi lopticu
            okreni se na levo

.. commented out
   .. reveal:: Karel_for_ring_3_reveal
       :showtitle: Решење
       :hidetitle: Сакриј решење
   
       .. activecode:: Karel_for_ring_3_solution
           :passivecode: true
         
           from karel import *
           for i_strana in range(3):     # tri puta ponovi sve sto sledi
               for i_polje in range(2):     # dva puta idi napred i uzmi 3 loptice
                   napred()
                   for i_loptica in range(3):
                       uzmi()
               levo()                       # okreni se duz sledece strane


