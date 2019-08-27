Решите више задатака одједном
=============================

Судећи према програмима које смо до сада видели, могло би се помислити да за сваки, макар мало другачији задатак, треба писати посебан програм. Када би то било тако, програмирање би било врло, врло заморан посао.

Да би програм који напишемо могао да се примени на групу сличних задатака, потребно нам је да се у различитим ситуацијама извршавају различите наредбе. То значи да нам је потребан начин да програм сазна тренутну ситуацију и да бира које ће наредбе извршити у зависности од стуације. Ситуација се може односити на број лоптица које се налазе на неком пољу или код Карела, на положај зидова око Карела и слично. Програм који би могао да добија одговоре на питања о Карелу и његовој околини, могао би и да решава више сличних задатака, односно један општији задатак. 

Питања о Карелу
---------------

На почетку уводног поглавља смо видели команде Карелу, помоћу којих му задајемо да извршава неке радње (иде напред, окреће се налево и надесно, узима и оставља лоптице). Тада смо поменули да постоји још пет функција у вези са Карелом. Ових пет функција су друкчије од претходних по томе што помоћу њих постављамо нека питања о Карелу или о пољу на коме се он налази и добијамо одговор. Ево тих функција:

- ``moze_napred()`` - питамо да ли Карел може да иде напред (није пред зидом). Добијамо одовор "да" или "не".
- ``broj_loptica_na_polju()`` - питамо колико има лоптица на пољу испод Карела. Добијамо број лоптица на пољу.
- ``ima_loptica_na_polju()`` - питамо да ли на пољу испод Карела има лоптица. Добијамо одовор "да" или "не".
- ``broj_loptica_kod_sebe()`` - питамо колико лоптица Карел тренутно има код себе. Добијамо број лоптица код Карела.
- ``ima_loptica_kod_sebe()`` - питамо да ли Карел има лоптица код себе. Добијамо одовор "да" или "не".

Функције које дају одговор не можемо да пишемо као засебне наредбе, као што смо то до сада радили. Уместо тога, ове функције пишемо као део неке наредбе језика Пајтон. 

Све док је потребно (наредба while)
-----------------------------------

Један начин да употребимо функције које дају одговор је да их пишемо у наредби ``while``. Наредба while постоји у скоро свим програмским језицима и њено писање у разним језицима је врло слично. На Пајтону то изгледа овако:

.. activecode:: while_syntax
   :passivecode: true

   while uslov:
       naredba_1
       ...
       naredba_k

.. infonote::

   Смисао ``while`` наредбе је: док год је испуњен ``uslov``, извршавај наредбу или наредбе које су написане испод увучено (while на енглеском значи "док" или "док је"). Овде је са ``uslov`` означено било шта што је исправно написано на Пајтону, а своди са на **да** или **не** (то "било шта" се у програмирању назива логички израз). 

   Правила писања while наредбе налажу да се након услова обавезно наведе двотачка (знак ``:``). Наредбе које се понављају док је тај услов испуњен (док је одговор на питање у услову **да**, односно **тачно**) чине тело while наредбе и пишу се у наредним редовима мало десно (увучено) у односу на while наредбу. То значи да се испред сваке од наредби које се понављају додаје се исти број размака.


Услов се проверава пре сваког извршавања наредби у телу while наредбе. Први пут када услов не буде испуњен, комплетна наредба while (заједно са наредбама у свом телу) се завршава и прелази се на наредбу која је наведена испод тела while наредбе. На пример, ако извршимо:

.. activecode:: while_example
   :passivecode: true

   while moze_napred():
       napred()
   uzmi()

Карел ће се померати напред док год може, то јест док на питање moze_napred() не добијемо одговор "не", што значи да је Карел наишао на зид. Кад заврши са померањем, Карел ће узети лоптицу. У случају да је Карел већ пред зидом, наредба napred() се неће извршити ни једном и Карел ће одмах узети лоптицу.

~~~~

У примерима и задацима који следе задатак ће бити уопштен. То значи да ће при различитим покретањима програма задатак изгледати слично, али мало другачије. Програм треба написати тако да решава сваки од тих сличних задатака.


Иди до краја и покупи лоптицу
'''''''''''''''''''''''''''''

.. questionnote::

   Испред Карела је једно или више поља, а на последњем пољу је једна лоптица. Напишите програм на основу којега ће Карел покупити лоптицу са последњег поља. 
   
   **Програм треба покренути више пута**, јер ће при различитим покретањима Карелов свет имати различит број поља. Ево неких примера како задатак може да изгледа:
   
   .. image:: ../_images/Karel/While_01.jpg
      :width: 600px   
      :align: center

Користићемо while наредбу за кретање Карела и на крају му рећи да покупи лоптицу.


.. karel:: Karel_while__many_squares_and_ball_at_the_end
   :blockly:

   {
      setup:function() {
         function random(n) {
            return Math.floor(n * Math.random());
         }

         var N = 2 + random(14);
         var world = new World(N, 1);
         world.setRobotStartAvenue(1);
         world.setRobotStartStreet(1);
         world.setRobotStartDirection("E");
         world.putBall(N, 1);
      
         var robot = new Robot();
      
         var code = ["from karel import *",
                     "while moze_napred():",
                     "    napred()",
                     "uzmi()"];
         return {robot:robot, world:world, code:code};
      },
      
      isSuccess: function(robot, world) {
         return robot.getBalls() === 1;
      }
   }

.. infonote::
    
    Може се догодити да неки програм често даје добар резултат, а повремено даје лош резултат или начини грешку при извршавању. **Такав програм треба сматрати неисправним**. Исправан програм треба увек да даје исправан резултат.

Задаци за вежбу
---------------

Иди једно поље напред и покупи све лоптице
''''''''''''''''''''''''''''''''''''''''''

.. questionnote::

  Испред Карела је тачно једно поље, а на њему било који број лоптица. Карел треба све да их покупи.
  
Пратећи овако написан програм, Карел ће покушати да заувек понавља наредбу ``uzmi()``, јер је услов у ``while`` наредби увек испуњен (``True`` значи "Тачно"). Међутим, када Карел узме све лоптице са тог поља, добићемо поруку о грешци, јер смо тражили да се узме лоптица са празног поља (слободно испробајте ово и видите како изгледа порука о грешци). Покушајте да поправите програм, тако да Карел узима лоптице само док их има.
  
.. karel:: Karel_while__one_square_many_balls
   :blockly:

   {
        setup:function() {
           function random(n) {
              return Math.floor(n * Math.random());
           }
           
           var world = new World(2, 1);
           world.setRobotStartAvenue(1);
           world.setRobotStartStreet(1);
           world.setRobotStartDirection("E");
           
           var N = random(14);
           world.putBalls(2, 1, N);

           var robot = new Robot();

           var code = ["from karel import *",
                       "napred()",
                       "while True: # umesto True koristite funkciju ima_loptica_na_polju",
                       "    uzmi()",
                       ""];
           return {robot:robot, world:world, code:code};
        },
    
        isSuccess: function(robot, world) {
           var N = world.getAvenues();
           for (var k = 1; k <= N; k++)
              if (world.getBalls(k, 1) > 0)
                 return false;
               
           return true;
        },
   }

.. commented out
   .. reveal:: Karel_while__one_square_many_balls_reveal
      :showtitle: Решење
      :hidetitle: Сакриј решење
   
      .. activecode:: Karel_while__one_square_many_balls_solution
         :passivecode: true
         
         from karel import *
         napred()
         while ima_loptica_na_polju():
             uzmi()

Иди до краја и покупи по једну лоптицу
''''''''''''''''''''''''''''''''''''''

.. questionnote::

   Испред Карела је једно или више поља, а на сваком пољу је по једна лоптица. Напишите програм на основу којега ће Карел покупити лоптице са свих поља. 
   
   **И овај програм треба покренути више пута** да бисмо се уверили да он решава задатак без обзира на дужину стазе којом иде Карел.

   
Треба користити једну while наредбу за кретање Карела и узимање лоптица.

.. karel:: Karel_while__many_squares_and_ball_at_each
   :blockly:

   {
      setup:function() {
         function random(n) {
            return Math.floor(n * Math.random());
         }

         var N = 2 + random(8);
         var world = new World(N, 1);
         world.setRobotStartAvenue(1);
         world.setRobotStartStreet(1);
         world.setRobotStartDirection("E");
         for (var k = 2; k <= N; k++)
             world.putBall(k, 1);

         var robot = new Robot();
      
         var code = ["from karel import *",
                     "# dopunite",
                     ];
         return {robot:robot, world:world, code:code};
      },
      
      isSuccess: function(robot, world) {
         return (robot.getBalls() == world.getAvenues() - 1);
      }
   }

Премести све лоптице са последњег на прво поље
''''''''''''''''''''''''''''''''''''''''''''''

.. questionnote::

   Испред Карела је једно или више поља, а на последњем пољу је неколико лоптица. Карел треба да узме све лоптице са последњег поља и остави их на прво поље. 
   
   (Задатак треба тестирати више пута).
   
У овом задатку су потребне четири петље једна за другом (не једна у другој):

- Првом петљом Карел стиже до последњег поља
- Другом петљом Карел узима лоптице
- Трећом петљом Карел се враћа на полазно поље
- Четвртом петљом Карел оставља све лоптице које има код себе

Наравно, после прве или друге петље, Карел треба да се окрене ка почетном пољу (два пута налево или два пута надесно).

.. karel:: Karel_while__bring_balls_to_front_square
    :blockly:

    {
        setup:function() {
            function random(n) {
                return Math.floor(n * Math.random());
            }

            var N = 2 + random(5);
            var world = new World(N, 1);
            world.setRobotStartAvenue(1);
            world.setRobotStartStreet(1);
            world.setRobotStartDirection("E");
            world.putBalls(N, 1, 2 + random(4));

            var robot = new Robot();
      
            var code = ["from karel import *",
                        "# idi do kraja",
                        "# uzmi sve loptice",
                        "desno()",
                        "desno()",
                        "# idi do kraja",
                        "# ostavi sve loptice",
                       ];
            return {robot:robot, world:world, code:code};
        },
      
        isSuccess: function(robot, world) {
            var N = world.getAvenues();
            for (var k = 2; k <= N; k++) {
                if (world.getBalls(k, 1) > 0)
                    return false;
            }
            if (robot.getBalls() > 0)
                return false;

            return true;
        }
    }
    
.. commented out
   .. reveal:: Karel_while__bring_balls_to_front_square_reveal
       :showtitle: Решење
       :hidetitle: Сакриј решење
   
       .. activecode:: Karel_while__bring_balls_to_front_square_solution
           :passivecode: true
         
           from karel import *
           while moze_napred():
               napred()
           while ima_loptica_na_polju():
               uzmi()
           desno()
           desno()
           while moze_napred():
               napred()
           while ima_loptica_kod_sebe():
               ostavi()

Пребаци лоптице у горњи ред
'''''''''''''''''''''''''''

.. questionnote::

  Карелов свет се овај пут састоји од два реда исте, али непознате дужине. Карел је у доњем левом углу, окренут ка истоку. Сва поља горњег реда су празна, а на сваком пољу првог реда се налази по једна лоптица, **укључујући и поље на коме је Карел**. Карелов задатак је да распореди по једну лоптицу на свако поље горњег реда.
  
  (Задатак треба тестирати више пута).
  
.. karel:: Karel_while__put_balls_in_upper_row
   :blockly:

   {
      setup:function() {
         function random(n) {
            return Math.floor(n * Math.random());
         }

         var N = 2 + random(4);
         var world = new World(N, 2);
         world.setRobotStartAvenue(1);
         world.setRobotStartStreet(1);
         world.setRobotStartDirection("E");
         for (var k = 1; k <= N; k++)
             world.putBall(k, 1);

         var robot = new Robot();
      
         var code = ["from karel import *",
                     "# dopunite",
                     ];
         return {robot:robot, world:world, code:code};
      },
      
      isSuccess: function(robot, world) {
          var N = world.getAvenues();
          for (var k = 1; k <= N; k++) {
              if (world.getBalls(k, 1) > 0)
                  return false;
              if (world.getBalls(k, 2) != 1)
                  return false;
          }
          if (robot.getBalls() > 0)
              return false;

          return true;
      }
   }

.. reveal:: Karel_while__put_balls_in_upper_row_reveal
    :showtitle: Помоћ
    :hidetitle: Сакриј помоћ
    
    Дајемо упутство које наликује програму:

    .. activecode:: Karel_while__put_balls_in_upper_row_solution
        :passivecode: true
      
        uzmi lopticu
        dok mozes napred:
            idi napred
            uzmi lopticu
        # okreni se ka gornjem redu
        # predji u gornji red
        # okreni se ka pocetku reda
        ostavi lopticu
        dok mozes napred:
            idi napred
            ostavi lopticu

.. commented out
    .. reveal:: Karel_while__put_balls_in_upper_row_reveal
        :showtitle: Решење
        :hidetitle: Сакриј решење

        .. activecode:: Karel_while__put_balls_in_upper_row_solution
            :passivecode: true
          
            from karel import *
            uzmi()
            while moze_napred():
                napred()
                uzmi()
            levo()
            napred()
            levo()
            ostavi()
            while moze_napred():
                napred()
                ostavi()
