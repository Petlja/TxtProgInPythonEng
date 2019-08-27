Проверите па одлучите
=====================

Наредба while се показала као врло корисна, јер смо употребљавајући је могли да решавамо много разноврсније задатке. Ипак, следећи пример показује да постоје једноставни задаци које са овим што до сада знамо и даље не можемо да решимо. 

Рецимо да вам је у некој ситуацији потребно да померите Карела само за једно поље ако је могуће (ако није могуће, Карел треба да остане тамо где је). 

- Ако напишемо само наредбу *napred()*, ризикујемо поруку о грешци у случају да је Карел пред зидом.
- Ако наредбу *napred()* сместимо испод *while moze_napred():*, ризикујемо да одемо даље него што смо желели.
- Ако не користимо наредбу *napred()*, ризкујемо да се не померимо ни онда када је то могуће (и потребно).

Очигледно, потребна нам је нека нова наредба, која ће Карелу рећи "ако можеш напред, помери се за једно место". 

Наредба if
----------

Наредба која нам је потребна у описаном случају је наредба ``if``, која такође постоји у скоро свим програмским језицима. На пајтону се она (у свом једноставнијем облику) пише овако:

.. activecode:: Karel_if__syntax
   :passivecode: true

   if uslov:
       naredba_1
       ...
       naredba_k


.. infonote::

   Видимо да је писање ``if`` наредбе веома слично писању *while* наредбе. Под ``if`` наредбом се такође може наћи једна или више других наредби, које чине ``тело if наредбе``. При томе важе иста правила за писање двотачке после услова и увлачење наредби које се извршавају ако је услов испуњен. Разлика је у томе што се наредбе у телу *if* наредбе неће понављати - ако је услов испуњен оне ће се извршити само једанпут.

   Наредба ``if`` се зове и *наредба гранања* зато што се ток извршавања програма код ове наредбе грана: следећа наредба која ће се извршити зависи од одговора на питање из услова.


У поменутом примеру, требало би писати:


.. activecode:: Karel_if__example
   :passivecode: true

   if moze_napred():
       napred()


Следе задаци у којима се (поред раније упознатих) користи ``if`` наредба.


Узми једну лоптицу ако их има
'''''''''''''''''''''''''''''

.. questionnote::

   Испред Карела је једно поље, на коме се налази нула или више лоптица. Напишите програм на основу кога ће Карел прећи на то поље, а затим узети тачно једну лоптицу ако на пољу има бар једна лоптица.
   
   Покрените програм више пута да бисте га тестирали на различитим примерима.
   

У нашем случају, услов ће бити ``ima_loptica_na_polju()``, а наредба која се условно извршава је ``uzmi()``.

.. karel:: Karel_if__take_one_if_any
   :blockly:

   {
      setup:function() {
          var world = new World(2, 1);
          world.setRobotStartAvenue(1);
          world.setRobotStartStreet(1);
          world.setRobotStartDirection("E");
          if (Math.random() > 0.5)
             world.putBalls(2, 1, 1 + Math.floor(7 *  Math.random()));
      
      var robot = new Robot();
      
      var code = ["from karel import *",
                  "napred()",
                  "if ...         # dopunite",
                  "    uzmi()",
                  ""];
          return {robot:robot, world:world, code:code};
      },
      
      isSuccess: function(robot, world) {
         return world.getBalls(1, 1) === 0 &&
            (robot.getBalls() === 1 ||
            (robot.getBalls() === 0 && world.getBalls(2, 1) === 0));
      }
   }

.. commented out
   .. reveal:: Karel_if__take_one_if_any_reveal
       :showtitle: Решење
       :hidetitle: Сакриј решење
       
       Решење:
   
       .. activecode:: Karel_if__take_one_if_any_solution
           :passivecode: true
         
           from karel import *
           napred()
           if ima_loptica_na_polju():
               uzmi()


Иди до краја и покупи по једну лоптицу где их има
'''''''''''''''''''''''''''''''''''''''''''''''''

.. questionnote::

  Испред Карела је бар једно поље, а може их бити било колико. На сваком пољу има нула или више лоптица. Карел треба да покупи по тачно једну лоптицу са сваког поља на коме има лоптица.
  
  Покрените програм више пута да бисте га тестирали на различитим примерима.

Овде је потребно користити while наредбу за напредовање, а после сваког напредовања у телу while петље треба користити if наредбу за проверу да ли Карел стоји на пољу са лоптицом.
  
.. karel:: Karel_if__many_squares_take_one_if_any
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
             if (Math.random() > 0.5)
                world.putBalls(k, 1, 2 + random(3)); // need initial world to replace '2'->'1'
      
         var robot = new Robot();
      
         var code = ["from karel import *",
                     "while moze_napred():",
                     "    napred()",
                     "    if ... # dopunite",
                     "       ... # dopunite",
                     ""];
                     
         return {robot:robot, world:world, code:code};
      },
      
      isSuccess: function(robot, world) {
         var N = world.getAvenues();
         var nonEmpty = 0;
         for (var k = 1; k <= N; k++)
            if (world.getBalls(k, 1) > 0)
               nonEmpty++;
               
         return robot.getBalls() === nonEmpty;
      }
   }

.. commented out
   .. reveal:: Karel_if__many_squares_take_one_if_any_reveal
       :showtitle: Решење
       :hidetitle: Сакриј решење
       
       Решење:
   
       .. activecode:: Karel_if__many_squares_take_one_if_any_solution
           :passivecode: true
         
           from karel import *
           while moze_napred():
               napred()
               if ima_loptica_na_polju():
                   uzmi()


Ако не радиш то, уради ово (if-else)
------------------------------------

У неким задацима треба урадити једну ствар ако је неки услов испуњен, а неку другу ствар ако није испуњен. У том случају можемо да користимо проширени облик  *if* наредбе, који изгледа овако:

.. activecode:: Karel_if__else_syntax
    :passivecode: true

    if uslov:
        naredba_a1
        ...
        naredba_ak
    else:
        naredba_b1
        ...
        naredba_bm


.. infonote::

   У проширеном облику ``if`` наредбе први део (до речи ``else``) има исти изглед и значење као и до сада. У наставку се пише реч ``else`` једнако увучена као и реч ``if``, затим се пише двотачка, а испод следи једна или више других наредби, које чине ``тело else гране``. Ова друга група наредби се пише увучено у односу на реч ``else``, а извршава се ако услов наведен у ``if`` наредби није испуњен.

    
Пример - узимање и остављање лоптица
''''''''''''''''''''''''''''''''''''

.. questionnote::

   Испред Карела су 3 поља, а на сваком од њих може да буде по једна или ниједна лоптица. Карел треба да узме лоптице са оних поља на којима се налазе и да их постави на она поља на којима се не налазе. Карел на почетку има довољно лоптица код себе.

Помоћу новог, проширеног облика ``if`` наредбе, Карелу можемо да кажемо: "Ако је на пољу лоптица, онда узми ту лоптицу, иначе остави једну лоптицу", тако да се задатак лако решава:

.. karel:: Karel_if__take_else_put
    :blockly:
   
    {
      setup: function() {
       var world = new World(4, 1);
           world.setRobotStartAvenue(1);
           world.setRobotStartStreet(1);
           world.setRobotStartDirection("E");
       world.balls = [];
       for (var k = 2; k <= world.getAvenues(); k++) {
          var ball = Math.random() > 0.5;
          world.balls.push(ball);
          if (ball)
                  world.putBall(k, 1);
           }
           var robot = new Robot();
       robot.setInfiniteBalls(true);
       var code = ["from karel import *",
        "for i in range(3):",
        "    napred()",
        "    if ima_loptica_na_polju():",
        "        uzmi()",
        "    else:",
        "        ostavi()"
       ]
       return {world: world, robot: robot, code: code};
      },

      isSuccess: function(robot, world) {
       for (var k = 2; k <= world.getAvenues(); k++)
              if (world.getBalls(k, 1) == world.balls[k-2])
             return false;
       return true;
      }
    }


Покупи лоптице до којих можеш да дођеш
''''''''''''''''''''''''''''''''''''''


.. questionnote::

   Лавиринт се састоји од два реда. Карел се налази у горњем реду, који је проходан до краја. У доњем реду могу да се налазе препреке или поља са по једном лоптицом. Карелов задатак је да покупи све лоптице.
   
.. karel:: Karel_if__take_all_from_lower_row
    :blockly:
   
    {
      setup: function() {

         function random(n) {
             return Math.floor(n * Math.random());
         }

         var world = new World(4 + random(4), 2);
         world.setRobotStartAvenue(1);
         world.setRobotStartStreet(2);
         world.setRobotStartDirection("E");

         world.addEWWall(1, 1, 1);
         var balls = 0;
         var prevBall = false;
         for (var i = 2; i <= world.getAvenues(); i++) {
             if (random(2) == 0 || (balls == 0 && i == world.getAvenues() - 1)) {
                 balls++;
                 if (!prevBall)
                    world.addNSWall(i-1, 1, 1);
                 world.putBall(i, 1);
                 prevBall = true;
             } else {
                 if (prevBall)
                    world.addNSWall(i-1, 1, 1);
                 world.addEWWall(i, 1, 1);
                 prevBall = false;
             }
         }

         var robot = new Robot();
         var code = ["from karel import *",
            "while moze_napred():",
            "    napred() # sledece polje",
            "",
            "    # proveri donji red",
            "    desno()             # okreni se prema jugu",
            "    if moze_napred():   # ako postoji polje u donjem redu",
            "        # recite Karelu da ode po lopticu  uzme je, ",
            "        # da se vrati na sadasnje polje i okrene se ka istoku",
            "    # recite Karelu, ako nije mogao da predje na donji red,",
            "    # da se ponovo okrene ka istoku radi nastavka",
         ]
         return {world: world, robot: robot, code: code};
      },

      isSuccess: function(robot, world) {
           for (var i = 1; i <= world.getAvenues(); i++)
              for (var j = 1; j <= world.getStreets(); j++)
                 if (world.getBalls(i, j) != 0)
                    return false;
          return true;
      }
    }
   
.. commented out
   .. reveal:: Karel_if__take_all_from_lower_row_reveal
       :showtitle: Прикажи решење
       :hidetitle: Сакриј решење
   
       Једно могуће решење (не и једино) је следеће.               
   
       .. activecode:: Karel_if__take_all_from_lower_row_solution
           :passivecode: true
                       
           from karel import *
           while moze_napred():
               napred() # sledece polje
               
               # proveri donji red
               desno()  # okreni se prema jugu
               if moze_napred(): # ako postoji polje u donjem redu
                   napred(); uzmi() # idi po lopticu i uzmi je
                   levo(); levo(); napred(); desno() # u gornji red, ka istoku
               else:
                   levo() # ka istoku


Ради само кад нешто није
------------------------

Нека је потребно да се Карел окрене лево ако **не може** да иде напред (ако може да иде напред, не треба да ради ништа).

Према правилима писања *if* наредбе, после услова (у телу прве гране) мора да постоји бар једна наредба, а према логици задатка нам није потребна ни једна наредба на том месту. У таквим ситуацијама можемо да пишемо:

.. activecode:: Karel_if__else_only
    :passivecode: true

    if moze_napred():
        pass
    else:
        levo()

или 

.. activecode:: Karel_if__not
    :passivecode: true

    if not moze_napred():
        levo()

У првом случају користимо специјалну наредбу ``pass`` која не ради ништа. Тиме је задовољена и синтакса (правила писања), а добили смо и програм који ради како желимо.

У другом случају, помоћу речи ``not`` правимо супротан услов, што значи да је услов *if* наредбе испуњен када Карел не може да иде напред. У овом случају гране мењају улоге и онда нам *else* грана више није потребна.

Следи пар сличних задатака, у којима такође треба нешто урадити само када услов није испуњен.

Окрени се ка празном пољу
'''''''''''''''''''''''''


.. questionnote::

   Карел може да буде окренут на било коју страну, али само у једном смеру може да започне кретање. Потребно је да се Карел окрене ка слободном пољу и да направи један корак.
   
.. karel:: Karel_if__turn_to_free_square
   :blockly:

   {
      setup:function() {
         function random(n) {
            return Math.floor(n * Math.random());
         }
         
         var ww = [
            [
               '█████',
               '█N.0█',
               '█████'
            ],
            [
               '█████',
               '█S.0█',
               '█████'
            ],
            [
               '█████',
               '█E.0█',
               '█████'
            ],
            [
               '█████',
               '█W.0█',
               '█████'
            ],
            [
               '███',
               '█0█',
               '█.█',
               '█E█',
               '███'
            ],
            [
               '███',
               '█0█',
               '█.█',
               '█W█',
               '███'
            ],
            [
               '███',
               '█0█',
               '█.█',
               '█S█',
               '███'
            ],
            [
               '███',
               '█0█',
               '█.█',
               '█N█',
               '███'
            ],
            [
               '███████',
               '█0.0.N█',
               '███████'
            ],
            [
               '███████',
               '█0.0.S█',
               '███████'
            ],
            [
               '███████',
               '█0.0.W█',
               '███████'
            ],
            [
               '███████',
               '█0.0.E█',
               '███████'
            ],
            [
               '█████',
               '█0█N█',
               '█.█.█',
               '█0.0█',
               '█████'
            ],
            [
               '█████',
               '█0█S█',
               '█.█.█',
               '█0.0█',
               '█████'
            ],
            [
               '█████',
               '█0█W█',
               '█.█.█',
               '█0.0█',
               '█████'
            ],
            [
               '█████',
               '█0█E█',
               '█.█.█',
               '█0.0█',
               '█████'
            ]
         ];
         let choice = random(ww.length);
         var w = ww[choice];
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
                     "# dopunite",
                     ""];
                     
         return {robot:robot, world:world, code:code};
      },
      
      isSuccess: function(robot, world) {
         var X = world.getAvenues();
         var Y = world.getStreets();
         if (X == 2 && Y == 1) return robot.getAvenue() == 2 && robot.getStreet() == 1 && robot.getDirection() == "E";
         if (X == 1 && Y == 2) return robot.getAvenue() == 1 && robot.getStreet() == 2 && robot.getDirection() == "N";
         if (X == 3 && Y == 1) return robot.getAvenue() == 2 && robot.getStreet() == 1 && robot.getDirection() == "W";
         if (X == 2 && Y == 2) return robot.getAvenue() == 2 && robot.getStreet() == 1 && robot.getDirection() == "S";
         return false;
      }
   }

.. reveal:: Karel_if__turn_to_free_square_reveal
    :showtitle: Решење
    :hidetitle: Сакриј решење

    Нудимо вам два кратка решења:
   
    .. activecode:: Karel_if__turn_to_free_square_solution1
        :passivecode: true
      
        from karel import *
        while not moze_napred():
            levo()
        napred()

    .. activecode:: Karel_if__turn_to_free_square_solution2
        :passivecode: true
      
        from karel import *
        for i in range(3):
            if not moze_napred():
                levo()
        napred()
                
Додај лоптице где их нема
'''''''''''''''''''''''''

.. questionnote::

   Испред Карела је непознат број поља, а на сваком од њих може да буде по једна или ни једна лоптица. Карел има довољно лоптица код себе, а треба да стави по једну лоптицу на свако поље на коме нема лоптице.

.. karel:: Karel_if__fill_the_empty_squares
    :blockly:
   
    {
        setup: function() {
            function random(n) {
                return Math.floor(n * Math.random());
            }
            var N = 2 + random(5);
            var world = new World(N, 1);
            world.setRobotStartAvenue(1);
            world.setRobotStartStreet(1);
            world.setRobotStartDirection("E");
            world.balls = [];
            world.putBall(1, 1);
            for (var k = 2; k <= world.getAvenues(); k++) {
                var ball = Math.random() > 0.5;
                world.balls.push(ball);
                if (ball)
                    world.putBall(k, 1);
            }
            var robot = new Robot();
            robot.setInfiniteBalls(true);
            var code = ["from karel import *",
                        "# dopunite"
                        ]
            return {world: world, robot: robot, code: code};
        },

        isSuccess: function(robot, world) {
            for (var k = 1; k <= world.getAvenues(); k++)
                if (world.getBalls(k, 1) != 1)
                    return false;
            return true;
        }
    }
