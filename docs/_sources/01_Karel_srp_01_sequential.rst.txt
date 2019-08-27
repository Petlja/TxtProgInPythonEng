Одмакни

~~~~

Управљање Карелом
=================

Да бисте видели како програмирање изгледа, упознаћемо вас са Карелом. Карел је анимирани робот, који се креће по табели налик лавиринту тако што прати наша упутства у облику програма. Кроз управљање Карелом усвојићемо логику која је веома битна за писање било каквих програма, а можемо се успут и забавити.

За управљање Карелом можемо користити ове функције:

- ``napred()`` - помери се једно поље напред,
- ``levo()`` - окрени се 90 степени налево (у смеру супротном казаљки на сату),
- ``desno()`` - окрени се 90 степени надесно (у смеру казаљке на сату),
- ``uzmi()`` - покупи лоптицу са поља на којем се налазиш,
- ``ostavi()`` - спусти лоптицу на поље на којем се налазиш.

Ових пет функција користимо као команде упућене Карелу. Карел разуме још пет нешто друкчијих функција, које ћемо видети ускоро. Поред ових команди упућених директно Карелу, можемо да користимо и све наредбе програмског језика Пајтон, који ћемо успут упознавати. 

Погледајмо кроз примере како горе наведене наредбе можемо да користимо да бисмо водили Карела кроз његов свет:

Примери
-------

Помери се једно поље напред и узми лоптицу
''''''''''''''''''''''''''''''''''''''''''

.. questionnote::

   Напишите програм на основу којега ће се Карел померити на поље (2, 1) и покупити лоптицу.

Овај програм се састоји од само две наредбе. Прва каже Карелу да се помери једно поље напред, а друга да узме лоптицу.
   
.. karel:: Karel_intro_two_squares_one_ball
   :blockly:

   {
        setup:function() {
            var world = new World(2, 1);
            world.setRobotStartAvenue(1);
            world.setRobotStartStreet(1);
            world.setRobotStartDirection("E");
            world.putBall(2, 1);

        var robot = new Robot();

        var code = ["from karel import *",
                    "napred()",
                    "uzmi()"];
            return {robot:robot, world:world, code:code};
        },
    
        isSuccess: function(robot, world) {
           return robot.getBalls() === 1;
        },
   }

**Прикључивање библиотеке** *karel*
'''''''''''''''''''''''''''''''''''

.. infonote::

    Наредбе помоћу којих управљамо Карелом налазе се у библиотеци *karel*. Зато на почетку програма треба да кажемо рачунару (тачније програму који извршава наш програм) да прво прикључи дефиниције команди за управљање Карелом. То се постиже првом линијом програма: ``from karel import *``. Сваки наш програм који се бави Карелом, треба да почне овако.
   
    Имајте на уму да библиотека *karel* за сада може да се користи само у овом окружењу. Остале програме које будете писали можете покретати и на друге начине, али на то ћемо вас подсетити када за то буде време.

На једном пољу може бити и више лоптица, а наш задатак може бити да кажемо Карелу да их узме неколико или све.

Помери се једно поље напред и узми три лоптице
''''''''''''''''''''''''''''''''''''''''''''''

.. questionnote::

   Напишите програм на основу којега ће се Карел померити на поље (2, 1) и покупити три од пет лоптица које се тамо налазе.

У овом програму након наредбе ``napred()``, наредбу ``uzmi()`` треба навести три пута, јер треба покупити три лоптице. Обратите пажњу на број који се појављује на лоптици. Он показује колико лоптица има на том пољу. Осим тога, број лево од Карелове главе (који сте можда приметили и у претходном примеру), говори колико лоптица Карел има код себе.
   
.. karel:: Karel_intro_two_squares_five_balls
   :blockly:

   {
        setup:function() {
            var world = new World(2, 1);
            world.setRobotStartAvenue(1);
            world.setRobotStartStreet(1);
            world.setRobotStartDirection("E");
            world.putBalls(2, 1, 5);

        var robot = new Robot();

        var code = ["from karel import *",
                    "napred()",
                    "uzmi()",
                    "uzmi()",
                    "uzmi()"];
            return {robot:robot, world:world, code:code};
        },
    
        isSuccess: function(robot, world) {
           return robot.getBalls() === 3;
        },
   }
   

Следи сличан, али нешто тежи задатак.
   
Дођи до лоптице и узми је 
'''''''''''''''''''''''''

.. questionnote::

   Напишите програм на основу којега ће Карел доћи на поље (4, 1) и покупити лоптицу.

Задатак се суштински не разликује од претходног. И сада је потребно навести Карела до циљног поља и рећи му да узме лоптицу. Разлика је у томе што је сада путања до циљног поља дужа, а тиме и наш програм:
   
.. karel:: Karel_intro_take_ball_on_square_4_1
   :blockly:

   {
        setup:function() {
            var world = new World(5,5);
            world.setRobotStartAvenue(1);
            world.setRobotStartStreet(1);
            world.setRobotStartDirection("E");
            world.putBall(4, 1);
            world.addEWWall(1, 1, 2);
            world.addNSWall(2, 2, 2);
            world.addEWWall(2, 3, 3);
            world.addNSWall(3, 1, 2);
            world.addNSWall(3, 4, 1);
            world.addNSWall(1, 5, 1);
            world.addEWWall(4, 1, 1);
            
        var robot = new Robot();

        var code = ["from karel import *",
                    "napred()      # idi na (2, 1)",
                    "napred()      # idi na (3, 1)",
                    "levo()        # okreni se na sever (^)",
                    "napred()      # idi na (3, 2)",
                    "napred()      # idi na (3, 3)",
                    "desno()       # okreni se na istok (>)",
                    "napred()      # idi na (4, 3)",
                    "napred()      # idi na (5, 3)",
                    "desno()       # okreni se na jug   (v)",
                    "napred()      # idi na (5, 2)",
                    "napred()      # idi na (5, 1)",
                    "desno()       # okreni se na zapad (<)",
                    "napred()      # idi na (4, 1)",
                    "uzmi()        # uzmi lopticu na (4, 1)"];
            return {robot:robot, world:world, code:code};
        },
    
        isSuccess: function(robot, world) {
           return robot.getBalls() === 1;
        },
   }

Читајући овај програм, постаје тешко да се прати која наредба докле доводи Карела. То није тако само са почетницима, то је стварно тешко, јер свака наредба napred() изгледа исто. Да бисмо помогли себи (и вама), иза сваке наредбе смо додали знак # и неки текст који нам помаже да пратимо "докле смо стигли". 

**Коментари**
'''''''''''''

.. infonote::

    Део било ког Пајтон програма од знака ``#`` до краја реда се зове ``коментар``. Коментари не утичу на извршавање програма, програм ради исто са или без њих. Коментари су намењени само људима који читају и пишу програме, да би боље разумели те програме и лакше се у њима сналазили.
    
    Када размишљамо о писању коментара у програму, треба да их пишемо и због себе и због других људи који ће читати наш програм. Исто тако, коментари које други људи напишу у својим програмима помоћи ће нама да разумемо њихове програме.
    
    За писање коментара не постоје прецизна правила. Пишите у коментаре оно што сматрате да би помогло разумевању вашег програма.

   
Покупи све лоптице 
''''''''''''''''''

У овом примеру, лоптице се налазе на разним пољима и потребно је да доведемо Карела до сваке од тих лоптица.

.. questionnote::

   Напишите програм на основу којега ће Карел покупити све четири лоптице.

Путању можемо бирати на више начина, али што краћу путању изаберемо, краћи ће бити и програм. Можемо на пример прво да узмемо лоптицу на пољу (5, 2), затим две лоптице на пољу (5, 5) и на крају лоптицу на пољу (4, 4).

.. karel:: Karel_intro_collect_three_balls
   :blockly:

   {
        setup:function() {
            var world = new World(5,5);
            world.setRobotStartAvenue(1);
            world.setRobotStartStreet(1);
            world.setRobotStartDirection("E");
            world.putBall(5, 2);
            world.putBalls(5, 5, 2);
            world.putBall(4, 4);
            world.addEWWall(1, 1, 2);
            world.addNSWall(2, 2, 2);
            world.addEWWall(2, 3, 3);
            world.addNSWall(3, 1, 2);
            world.addNSWall(3, 4, 1);
            world.addNSWall(1, 5, 1);
            world.addEWWall(4, 1, 1);
            
        var robot = new Robot();

        var code = ["from karel import *",
                    "napred(); napred(); levo()         # idi do polja (3, 1) i okreni se na sever",
                    "napred(); napred(); desno()        # idi do polja (3, 3) i okreni se na istok",
                    "napred(); napred(); desno()        # idi do polja (5, 3) i okreni se na jug",
                    "napred(); uzmi()                   # dodji na polje (5, 2) i uzmi lopticu",
                    "levo(); levo()                     # okreni se na sever",
                    "napred(); napred(); napred()       # dodji na polje (5, 5)",
                    "uzmi(); uzmi()                     # uzmi dve loptice",
                    "levo(); napred(); levo(); napred() # idi na polje (4, 4)",
                    "uzmi()                             # uzmi poslednju lopticu na polju (4, 4)"];
            return {robot:robot, world:world, code:code};
        },
    
        isSuccess: function(robot, world) {
           return robot.getBalls() === 4;
        },
   }

**Груписање наредби**
'''''''''''''''''''''

Пошто је овај програм још дужи од претходног, да бисмо се лакше оријентисали у програму и пратили докле смо довели Карела, груписали смо по неколико наредби које чине једну етапу путовања у један ред програма. На крају сваког реда је коментар који објашњава групу наредби у том реду.

Приметите да је при оваквом писању програма потребно између наредби писати знак ``;`` (иза последње наредбе у реду, овај знак се не пише).

Наредбе могу да се групишу и другачије, на пример тако што се група наредби (написаних једна испод друге) раздвоји празним редом од следеће групе. Овакав начин груписања је много чешће у употреби, јер наредбе обично нису тако тако кратке као ове за управљање Карелом. Ево како би то изгледало: 

.. code::

    from karel import *
    
    # idi do polja (3, 1) i okreni se na sever"
    napred()
    napred()
    levo()
    
    # idi do polja (3, 3) i okreni se na istok
    napred()
    napred()
    desno()
    
    # idi do polja (5, 3) i okreni se na jug
    napred()
    napred()
    desno()
    
    # dodji na polje (5, 2) i uzmi lopticu
    napred()
    uzmi()
    
    # okreni se na sever
    levo()
    levo()
    
    # dodji na polje (5, 5)
    napred()
    napred()
    napred()
    
    # uzmi dve loptice
    uzmi()
    uzmi()
    
    # idi na polje (4, 4)
    levo()
    napred()
    levo()
    napred()
    
    # uzmi poslednju lopticu na polju (4, 4)
    uzmi()
    
~~~~

Карел може и да оставља лоптице на поједина поља. Ево како он то може да уради.

Премести лоптицу
''''''''''''''''

.. questionnote::

   Напишите програм на основу којега ће се Карел преместити лоптицу на поље (2, 2) (приметите да Карел на почетку **није** окренут како треба).
   

.. karel:: Karel_intro_move_ball_in_2x2
   :blockly:

   {
        setup:function() {
            var world = new World(2, 2);
            world.setRobotStartAvenue(1);
            world.setRobotStartStreet(1);
            world.setRobotStartDirection("S");
            world.putBall(2, 1);
            world.addEWWall(2, 1, 1);

        var robot = new Robot();

        var code = ["from karel import *",
                    "levo(); napred(); uzmi();  # uzmi lopticu na (2, 1)",
                    "desno(); desno(); napred() # vrati se na (1, 1)",
                    "desno(); napred()          # idi na (1, 2)",
                    "desno(); napred()          # idi na (2, 2)",
                    "ostavi()                   # ostavi lopticu na (2, 2)"];
            return {robot:robot, world:world, code:code};
        },
    
        isSuccess: function(robot, world) {
           return world.getBalls(2, 2) === 1;
        },
   }

**Грешке при извршавању**
'''''''''''''''''''''''''

.. infonote::

    Имајте на уму да **Карел не може у сваком тренутку да изврши сваку наредбу коју му задамо**. Конкретније, Карел не може да иде напред ако је испред њега зид, не може да узме лоптицу тамо где је нема, и не може да је остави ако нема лоптица код себе.

    Пробајте да обришете прву наредбу ``levo()`` у претходном програму, па покрените програм и видите шта се дешава. 
    
    Када програм који извршава наш програм дође до наредбе коју није могуће извршити, извршавање нашег програма се прекида и добијамо поруку о грешци при извршавању. Такве поруке су нормална ствар и виђаћемо их када год Карел није у могућности "да нас послуша", или када је нека наредба нејасна (тачније, када није написана како треба). У таквим ситуацијама треба да се потрудимо да разумемо у чему је проблем, па да поправимо програм и поново га покренемо.


У наставку је дато неколико задатка за самосталан рад. Уз сваки задатак понуђено је решење, које можете да видите када кликнете на дугме "решење". Приказано решење можте да ископирате у простор за решавање и испробате га покретањем програма. Ваше решење може да буде сасвим добро иако је друкчије од нашег.

Задаци за вежбу
---------------

Дођи до поља (3, 3)
'''''''''''''''''''

.. questionnote::

   У овом задатку нема лоптица, потребно је само да доведете Карела до поља (3, 3).
   
.. karel:: Karel_intro_task_go_to_3_3
   :blockly:

   {
        setup:function() {
            var world = new World(3, 3);
            world.setRobotStartAvenue(1);
            world.setRobotStartStreet(1);
            world.setRobotStartDirection("N");
            world.addNSWall(1, 1, 2);
            world.addNSWall(2, 2, 2);

        var robot = new Robot();

        var code = ["from karel import *",
                    "# dodajte naredbe koje nedostaju"];
            return {robot:robot, world:world, code:code};
        },
    
        isSuccess: function(robot, world) {
           return robot.getStreet() === 3 &&
           robot.getAvenue() === 3;
        },
   }
   
.. reveal:: Karel_intro_task_go_to_3_3_reveal
   :showtitle: Решење
   :hidetitle: Сакриј решење

   .. activecode:: Karel_intro_task_go_to_3_3_solution
      :passivecode: true
      
      from karel import *
      napred(); napred()          # do polja (1, 3)
      desno(); napred()           # do polja (2, 3)
      desno(); napred(); napred() # do polja (2, 1)
      levo(); napred()            # do polja (3, 1)
      levo(); napred(); napred()  # do polja (3, 3)

Покупи лоптице
''''''''''''''

.. questionnote::

   Напишите програм на основу којега ће се Карел покупити лоптице.
   
.. karel:: Karel_intro_task_collect_balls_in_2x2
   :blockly:

   {
        setup:function() {
            var world = new World(2, 2);
            world.setRobotStartAvenue(1);
            world.setRobotStartStreet(1);
            world.setRobotStartDirection("E");
            world.putBall(2, 1);
            world.putBall(2, 2);
            world.putBall(1, 2);
            world.addEWWall(2, 1, 1);

        var robot = new Robot();

        var code = ["from karel import *",
                    "# dodajte naredbe koje nedostaju",
                    "uzmi()"];
            return {robot:robot, world:world, code:code};
        },
    
        isSuccess: function(robot, world) {
           return robot.getBalls() === 3;
        },
   }
   
.. reveal:: Karel_intro_task_collect_balls_in_2x2_reveal
   :showtitle: Решење
   :hidetitle: Сакриј решење
  
   .. activecode:: Karel_intro_task_collect_balls_in_2x2_solution
      :passivecode: true
       
      from karel import *
      napred(); uzmi()            # uzmi na polju (2, 1)
      desno(); desno(); napred()  # vrati se na polje (1, 1)
      desno(); napred(); uzmi()   # uzmi na polju (1, 2)
      desno(); napred(); uzmi()   # uzmi na polju (2, 2)

Кривудање
'''''''''

.. questionnote::

  Карел треба да стигне до поља (5, 1).

.. karel:: Karel_intro_task_stairs_fixed
   :blockly:

   {
      setup:function() {

         var Y = 3;
         var X = 2 * Y - 1;
         var world = new World(X, Y);
         world.setRobotStartAvenue(1);
         world.setRobotStartStreet(1);
         world.setRobotStartDirection("E");

         // Vertical walls
         for (let y = 1; y < Y; y++) world.addNSWall(y, y, 1); // low left
         for (let y = 1; y < Y; y++) world.addNSWall(X - 1 - y, y, 1); // low right
         for (let y = 3; y <= Y; y++) world.addNSWall(y - 2, y, 1); // high left
         for (let y = 2; y <= Y; y++) world.addNSWall(X + 1 - y, y, 1); // high right
         
         // Horizontal walls
         for (let y = 1; y < Y - 1; y++) world.addEWWall(y + 1, y, 1); // low left
         for (let y = 2; y < Y; y++) world.addEWWall(y - 1, y, 1); // high left
         for (let y = 1; y < Y - 1; y++) world.addEWWall(X - 1 - y, y, 1); // low right
         for (let y = 1; y < Y; y++) world.addEWWall(X + 1 - y, y, 1); // high right

         var robot = new Robot();
         
         var code = ["from karel import *",
                     "# dodajte naredbe ",
                     ""];
    
         return {robot:robot, world:world, code:code};
      },
    
      isSuccess: function(robot, world) {
         return robot.getAvenue() == world.getAvenues() &&
            robot.getStreet() == 1;
      },
   }

.. reveal:: Karel_intro_task_stairs_fixed_reveal
   :showtitle: Решење
   :hidetitle: Сакриј решење

   .. activecode:: Karel_intro_task_stairs_fixed_solution
      :passivecode: true
      
      from karel import *
      levo(); napred()     # na (1, 2)
      desno(); napred()    # na (2, 2)
      levo(); napred()     # na (2, 3)
      desno(); napred()    # na (3, 3)
      desno(); napred()    # na (3, 2)
      levo(); napred()     # na (4, 2)
      desno(); napred()    # na (4, 1)
      levo(); napred()     # na (5, 1)


Право па лево, па опет
''''''''''''''''''''''

.. questionnote::

  Карел треба да стигне до поља (2, 3).
   
.. karel:: Karel_intro_task_spiral_left_fixed
   :blockly:

   {
      setup:function() {

         var N = 4;
         var world = new World(N, N);
         world.setRobotStartAvenue(1);
         world.setRobotStartStreet(1);
         world.setRobotStartDirection("E");
         
         var i = 1;
         for (let d = N - 1; d > 0; d -= 2) { world.addEWWall(i, i, d); i++; }
         i = 2;
         for (let d = N - 2; d > 0; d -= 2) { world.addEWWall(i, N+1-i, d); i++; }
         i = 2;
         for (let d = N - 2; d > 0; d -= 2) { world.addNSWall(N+1-i, i, d); i++; }
         i = 1;
         for (let d = N - 3; d > 0; d -= 2) { world.addNSWall(i, i+2, d); i++; }
   
         var robot = new Robot();
      
         var code = ["from karel import *",
                     "# dodajte naredbe ",
                     ""];
      
         return {robot:robot, world:world, code:code};
      },
 
      isSuccess: function(robot, world) {
         var N = world.getAvenues();
         return robot.getStreet() === Math.floor((N+2)/2) &&
           robot.getAvenue() === Math.floor((N+1)/2);
     },
   }

.. reveal:: Karel_intro_task_spiral_left_fixed_reveal
   :showtitle: Решење
   :hidetitle: Сакриј решење

   .. activecode:: Karel_intro_task_spiral_left_fixed_solution
      :passivecode: true
      
      from karel import *
      napred(); napred(); napred(); levo() # do (4, 1)
      napred(); napred(); napred(); levo() # do (4, 4)
      napred(); napred(); napred(); levo() # do (1, 4)
      napred(); napred(); levo()           # do (1, 2)
      napred(); napred(); levo()           # do (3, 2)
      napred(); levo()                     # do (3, 3)
      napred();                            # do (2, 3)

