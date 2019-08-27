Комбиновање петљи
=================

Видели смо да у телу *for* наредбе може да се нађе више различитих наредби. Слично као са *for* наредбом, и у телу ``while`` наредбе може (поред осталих наредби) да се нађе и нова петља, било *while* или *for*. Тако можемо да градимо различите комбинације уметнутих (угнежђених) петљи.

Када су две петље уметнуте једна у другу, зовемо их и двострука петља, док три угнежђене петље зовемо трострука петља. На сличан начин можемо угнездити било који број петљи једну у другу, али за великим бројем угнежђених петљи врло ретко имамо потребу.

У овој лекцији ћемо вежбати писање комбинација угнежђених *while* и *for* петљи.

Разне двоструке и вишеструке петље - задаци
-------------------------------------------

Узимај по четири лоптице до краја
'''''''''''''''''''''''''''''''''

.. questionnote::

  Испред Карела је једно или више поља, а на сваком од поља испред Карела су по четири лоптице (на почетном пољу нема лоптица). Карел треба све да их покупи.
  
Сада Карел, све док не дође до зида, треба да понавља корак напред и узимање 4 лоптице. Покушајте да допуните програм.

Подсетимо се, као и у ранијим примерима угнежђених петљи, наредба у телу унутрашње петље (овде ће то бити наредба ``uzmi()``) треба да буде додатно увучена. 
  
.. karel:: Karel_while__many_squares_four_bals_per_square
   :blockly:

   {
      setup:function() {
         function random(n) {
            return Math.floor(n * Math.random());
         }

         var N = 2 + random(9);
         var world = new World(N, 1);
         world.setRobotStartAvenue(1);
         world.setRobotStartStreet(1);
         world.setRobotStartDirection("E");
         for (var k = 2; k <= N; k++)
             world.putBalls(k, 1, 4);
      
         var robot = new Robot();
      
         var code = ["from karel import *",
                     "while moze_napred():",
                     "    napred()",
                     "    # dodajte naredbe koje nedostaju",
                     ""];
                     //from karel import *
                     //while moze_napred():
                     //    napred()
                     //    for i in range(4):
                     //        uzmi()
         return {robot:robot, world:world, code:code};
      },
      
      isSuccess: function(robot, world) {
         var N = world.getAvenues();
         for (var k = 1; k <= N; k++)
            if (world.getBalls(k, 1) > 0)
               return false;
               
         return true;
      }
   }
   
..  commented out
    .. reveal:: Karel_while__many_squares_four_bals_per_square_reveal
       :showtitle: Решење
       :hidetitle: Сакриј решење
    
       .. activecode:: Karel_while__many_squares_two_bals_per_square_solution
          :passivecode: true
          
          from karel import *
          while moze_napred():
              napred()
              for i in range(4):
                  uzmi()
   
   
Покупи све лоптице
''''''''''''''''''

.. questionnote::

  Испред Карела је бар једно поље, а може их бити било колико. На сваком од поља **испред** Карела има нула или више лоптица (почтено поље је празно). Карел треба да покупи све лоптице.

Овај задатак је уопштење претходног, па програм који решава овај задатак, може да се искористи и у претходном. Разлика је у томе што сада унутрашња петља мора да буде *while*, док је у претходном задатку могла да буде и *for*. 

И у овом програму наредба ``uzmi()`` треба да буде додатно увучена. На тај начин ће се она понављати док је услов унутрашње ``while`` наредбе испуњен, то јест док има лоптица на пољу на коме је Карел у том тренутку, а узимање свих лоптица се заједно са наредбом ``napred`` понавља у спољашњој ``while`` наредби док има поља испред Карела. Укупни ефекат угнежђених петљи је да ће бити узете све лоптице са сваког поља.


.. karel:: Karel_while__many_squares_many_balls
   :blockly:

   {
      setup:function() {
         function random(n) {
            return Math.floor(n * Math.random());
         }

         var N = 2 + random(9);
         var world = new World(N, 1);
         world.setRobotStartAvenue(1);
         world.setRobotStartStreet(1);
         world.setRobotStartDirection("E");
         
         for (var k = 2; k <= N; k++) {
            let B = random(7);
            world.putBalls(k, 1, B);
         }
      
         var robot = new Robot();
      
         var code = ["from karel import *",
                     "while moze_napred():",
                     "    # pomeri se napred",
                     "    while ... # dovrsite",
                     ""];
         return {robot:robot, world:world, code:code};
      },
      
      isSuccess: function(robot, world) {
         var N = world.getAvenues();
         for (var k = 1; k <= N; k++)
            if (world.getBalls(k, 1) > 0)
               return false;
               
         return true;
      }
   }

Донеси све лоптице
''''''''''''''''''

.. questionnote::

  Испред Карела је прав пут непознате дужине. Карел треба да прикупи све лоптице са свих поља и донесе их на почетно поље.

Програм је коментарима разложен на ситније целине. Додајте делове који недостају.

.. karel:: Karel_while__bring_all_balls
   :blockly:

   {
      setup:function() {
         function random(n) {
            return Math.floor(n * Math.random());
         }

         var N = 2 + random(9);
         var world = new World(N, 1);
         world.setRobotStartAvenue(1);
         world.setRobotStartStreet(1);
         world.setRobotStartDirection("E");
         
         for (var k = 1; k <= N; k++) {
            let B = random(7);
            world.putBalls(k, 1, B);
         }
      
         var robot = new Robot();
         
         var code = ["from karel import *",
                     "# koristite dvostruku while petlju za uzimanje svih loptica sa svih polja",
                     "",
                     "",
                     "levo(); levo()                # okreni se nazad",
                     "# kazite Karelu da se vrati na pocetno polje (to jest, da ide napred dok moze)",
                     "",
                     "while ima_loptica_kod_sebe(): # ostavi sve loptice",
                     "    # ostavi jednu lopticu",
                     ""];

           return {robot:robot, world:world, code:code};
        },
    
        isSuccess: function(robot, world) {
           var N = world.getAvenues();
           for (var k = 2; k <= N; k++)
              if (world.getBalls(k, 1) > 0)
                 return false;
               
           if (robot.getBalls() > 0)
                 return false;
                 
           return true;
        },
   }

..  commented out
    .. reveal:: Karel_while__bring_all_balls_reveal
       :showtitle: Решење
       :hidetitle: Сакриј решење

       .. activecode:: Karel_while__bring_all_balls_solution
          :passivecode: true
          
          from karel import *
          while moze_napred():          # pokupi sve loptice sa svih polja
              napred()
              while ima_loptica_na_polju():
                  uzmi()
                
          levo(); levo()                # okreni se nazad
          
          while moze_napred():          # vrati se na pocetno polje
              napred()
              
          while ima_loptica_kod_sebe(): # ostavi sve loptice           
              ostavi()


Горе-доле
'''''''''

.. questionnote::

  Карел се налази на правоугаоној табли непознате величине (број колона је увек непаран), без лоптица. Циљ је да Карел стигне до доњег десног поља, а да би то постигао, мораће да се креће кроз колоне наизменично горе-доле.
  
  Ово су неки од могућих изгледа лавиринта:

   .. image:: ../_images/Karel/While_UpDown.jpg
      :width: 600px   
      :align: center

.. karel:: Karel_while__up_col_down_col
   :blockly:

   {
      setup:function() {
         function random(n) {
            return Math.floor(n * Math.random());
         }

         var X2 = 1 + random(4);
         var Y = 2 + random(5);
         var world = new World(2*X2+1, Y);
         world.setRobotStartAvenue(1);
         world.setRobotStartStreet(1);
         world.setRobotStartDirection("E");
            
         world.addEWWall(1, 1, 1);
         for (let x = 0; x < X2; x++) { 
            world.addNSWall(2*x + 1, 2, Y - 1);
            world.addNSWall(2*x + 2, 1, Y - 1);
         }
         
         var robot = new Robot();
         
         var code = ["from karel import *",
                     "# dodajte naredbe ",
                     ""];
                     //from karel import *
                     //while moze_napred():           # dok nismo u donjem desnom uglu
                     //    napred(); levo()           #     udji u sledecu kolonu i okreni se na sever
                     //    while moze_napred():       #     idi do gornje ivice
                     //        napred()
                     //
                     //    desno(); napred(); desno() #     predji u sledecu kolonu i okreni se na jug
                     //    while moze_napred():       #     idi do donje ivice
                     //        napred()
                     //
                     //    levo()                     #     okreni se na istok
    
         return {robot:robot, world:world, code:code};
      },
    
      isSuccess: function(robot, world) {
         return robot.getAvenue() == world.getAvenues() &&
            robot.getStreet() == 1;
      },
   }

.. reveal:: Karel_while__up_col_down_col_reveal
   :showtitle: Помоћ
   :hidetitle: Сакриј помоћ

   .. activecode:: Karel_while__up_col_down_col_solution
      :passivecode: true
      
      from karel import *
      while moze_napred():           # dok nismo u donjem desnom uglu
          napred(); levo()           #     udji u sledecu kolonu i okreni se na sever
          ... # dovrsite             #     idi do gornje ivice

          desno(); napred(); desno() #     predji u sledecu kolonu i okreni se na jug
          ... # dovrsite             #     idi do donje ivice

          levo()                     #     okreni se na istok

Степенице
'''''''''

.. questionnote::

  Карел треба да се попне уз прве степенице, а затим да сиђе низ друге и заврши у доњем десном углу. Величина табле није позната, али број колона ће увек бити непаран. Табла може да изгледа на пример овако:
  

   .. image:: ../_images/Karel/While_Stairs.jpg
      :width: 600px   
      :align: center

.. karel:: Karel_while__stairs
   :blockly:

   {
      setup:function() {
         function random(n) {
            return Math.floor(n * Math.random());
         }

         var Y = 2 + random(6);
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
                     //from karel import *
                     //levo()                                  # ka severu
                     //while moze_napred():                    # dok ima uzbrdo
                     //    napred(); desno(); napred(); levo() #    popni se jedan stepenik 
                     //
                     //desno(); desno()                        # ka jugu
                     //
                     //while moze_napred():                    # dok ima nizbrdo
                     //    napred(); levo(); napred(); desno() #    sidji jedan stepenik 
    
         return {robot:robot, world:world, code:code};
      },
    
      isSuccess: function(robot, world) {
         return robot.getAvenue() == world.getAvenues() &&
            robot.getStreet() == 1;
      },
   }

.. reveal:: Karel_while__stairs_reveal
   :showtitle: Помоћ
   :hidetitle: Сакриј помоћ

   .. activecode:: Karel_while__stairs_solution
      :passivecode: true
      
      from karel import *
      levo()                                  # ka severu
      while moze_napred():                    # dok ima stepenika uzbrdo
          napred(); desno(); napred(); levo() #    popni se jedan stepenik 

      desno(); desno()                        # ka jugu
      
      while ... # dovrsite uslov              # dok ima stepenika nizbrdo
          ... # dodajte jos 4 naredbe         #    sidji jedan stepenik 


Спирала улево
'''''''''''''

.. questionnote::

  Карел у свим приказаним случајевима треба да дође до поља означеног црвеним кругом (ни у овом задатку нема лоптица).
   
   .. image:: ../_images/Karel/While_SpiralLeft.jpg
      :width: 600px   
      :align: center


.. karel:: Karel_while__spiral_left
   :blockly:

   {
      setup:function() {
         function random(n) {
            return Math.floor(n * Math.random());
         }

      var N = 1 + random(7);
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
                  "# dopunite naredbe koje nisu kompletne",
                  "while moze_napred():",
                  "    while ... ",
                  "        ... ",
                  "    levo()",
                  ""];

        return {robot:robot, world:world, code:code};
     },
 
     isSuccess: function(robot, world) {
        var N = world.getAvenues();
        return robot.getStreet() === Math.floor((N+2)/2) &&
           robot.getAvenue() === Math.floor((N+1)/2);
     },
   }

.. reveal:: Karel_while__spiral_left_reveal
   :showtitle: Решење
   :hidetitle: Сакриј решење

   .. activecode:: Karel_while__spiral_left_solution
      :passivecode: true
      
      from karel import *
      while moze_napred():
          while moze_napred():
              napred()
          levo()

