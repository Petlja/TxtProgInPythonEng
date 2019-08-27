Наредба *for* - вежбање
=======================

У овом делу ћемо само увежбавати употребу *for* наредбе.

Задаци
------

Три пута горе-доле
''''''''''''''''''

.. questionnote::

  Карел се налази на правоугаоној табли од 5 редова и 7 колона и треба да стигне до доњег десног поља.


Карел треба три пута да понови једну сложену радњу, а то је: да пређе у следећу (десну) колону, оде до њеног врха, оде још једну колону десно, сиђе до првог реда и на крају да се окрене ка последњој колони да би се припремио за следеће понављање. 

Допуните програм, водећи рачуна да се бројач у *for* наредбама које додајете не зове ``i`` (то име је већ употребљено у спољној петљи).

.. karel:: Karel_for_up_col_down_col_constant
   :blockly:

   {
      setup:function() {

         var X2 = 3;
         var Y = 5;
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
                     "for i in range(3):              # tri puta ponovi sve sto sledi",
                     "    napred(); levo()             #    udji u sledecu kolonu i okreni se na sever",
                     "    # upotrebite for naredbu da kazete Karelu da ode do gornje ivice",
                     "    ",
                     "    desno(); napred(); desno()   #    predji u sledecu kolonu i okreni se na jug",
                     "    # upotrebite for naredbu da kazete Karelu da ode do donje ivice",
                     "    ",
                     "    levo()                       #    okreni se na istok",
                     ""];
    
         return {robot:robot, world:world, code:code};
      },
    
      isSuccess: function(robot, world) {
         return robot.getAvenue() == world.getAvenues() &&
            robot.getStreet() == 1;
      },
   }

.. reveal:: Karel_for_up_col_down_col_constant_reveal
   :showtitle: Решење
   :hidetitle: Сакриј решење

   .. activecode:: Karel_for_up_col_down_col_constant_solution
      :passivecode: true
      
      from karel import *
      for i_vodoravno in range(3):     # 3 puta ponovi sve sto sledi
          napred(); levo()             #     udji u sledecu kolonu i okreni se na sever
          for i_uspravno in range(4):  #     idi do gornje ivice
              napred()

          desno(); napred(); desno()   #     predji u sledecu kolonu i okreni se na jug
          for i_uspravno in range(4):  #     idi do donje ivice
              napred()

          levo()                       #     okreni se na istok


Донеси све са табле
'''''''''''''''''''

.. questionnote::

  Карел треба да донесе свих 12 лоптица на полазно поље.


Карел треба четири пута да пређе у следећу колону и испразни је, а на крају да дође на полазно поље и остави све лоптице. Карел ће испразнити колону ако три пута понови корак напред и узимање, а затим се врати на почетак колоне у исти положај.

Допуните програм.

.. karel:: Karel_for_fetch_from_matrix
   :blockly:

   {
      setup:function() {
         var X = 5;
         var Y = 4;
         var world = new World(X, Y);
         world.setRobotStartAvenue(1);
         world.setRobotStartStreet(1);
         world.setRobotStartDirection("E");

         world.addEWWall(1, 1, 1);
         world.addNSWall(1, 2, Y - 1);
         
         for (var col = 2; col <= X; col++) {
            for (var row = 2; row <= Y; row++) {
               world.putBall(col, row);
            }
         }
         
         var robot = new Robot();
         
         var code = ["from karel import *",
                     "for i_kolona in range(4):      # cetiri puta ponovi ciscenje kolone",
                     "    napred()                   #     udji u sledecu kolonu",
                     "    levo()                     #     okreni se na sever",
                     "    #for ...                   #     3 puta ponovi korak napred i uzimanje",
                     "",
                     "    desno(); desno()           #     okreni se na jug",
                     "    #for ...                   #     3 koraka napred do donje ivice",
                     "",
                     "    levo()                     #     okreni se na istok",
                     "    ",
                     "                               # sada smo prosli sva polja",
                     "levo()                         #     okreni se na zapad",
                     "levo()",
                     "#for ...                       # vrati se na pocetno polje",
                     "    ",
                     "for i_loptica in range(12):",
                     "    ostavi()",
                     ""];
    
         return {robot:robot, world:world, code:code};
      },
    
      isSuccess: function(robot, world) {
         return world.getBalls(1, 1) == 12 &&
            robot.getAvenue() == 1 &&
            robot.getStreet() == 1;
      },
   }

.. reveal:: Karel_for_fetch_from_matrix_reveal
   :showtitle: Решење
   :hidetitle: Сакриј решење

   .. activecode:: Karel_for_fetch_from_matrix_solution
      :passivecode: true
      
      from karel import *
      for i_kolona in range(4):     # cetiri puta ponovi ciscenje kolone
          napred()                  #     udji u sledecu kolonu
          levo()                    #     okreni se na sever
          for i_red in range(3):    #     idi do gornje ivice i usput pokupi
              napred()
              uzmi()

          desno(); desno()          #     okreni se na jug
          for i_red in range(3):    #     idi do donje ivice
              napred()

          levo()                    #     okreni se na istok
         
      levo()                        # okreni se na zapad
      levo()
      for i_kolona in range(4):     # vrati se na pocetno polje
          napred()
         
      for i_loptica in range(12):   # ostavi sve loptice
          ostavi()


Трострука петља
'''''''''''''''

.. questionnote::

  Сада се на сваком од 6 поља налази по 4 лоптице, слично претходном задатку. Карел треба да донесе све 24 лоптице на полазно поље.


Овај програм се од претходног разликује по томе што наредба *uzmi()* треба да стоји у додатној петљи, трећој у дубину. Такође, разликује се и број лоптица које Карел на крају програма оставља на полазно поље. Можете да ископирате претходни програм и преправите га.

.. karel:: Karel_for_fetch_60_from_matrix
   :blockly:

   {
      setup:function() {
         var X = 3;
         var Y = 4;
         var world = new World(X, Y);
         world.setRobotStartAvenue(1);
         world.setRobotStartStreet(1);
         world.setRobotStartDirection("E");

         world.addEWWall(1, 1, 1);
         world.addNSWall(1, 2, Y - 1);
         
         for (var col = 2; col <= X; col++) {
            for (var row = 2; row <= Y; row++) {
               world.putBalls(col, row, 4);
            }
         }
         
         var robot = new Robot();
         
         var code = ["from karel import *",
                     "# dopunite program",
                     ""];
    
         return {robot:robot, world:world, code:code};
      },
    
      isSuccess: function(robot, world) {
         return world.getBalls(1, 1) == 24 &&
            robot.getAvenue() == 1 &&
            robot.getStreet() == 1;
      },
   }

.. reveal:: Karel_for_fetch_24_from_matrix_reveal
   :showtitle: Решење
   :hidetitle: Сакриј решење

   .. activecode:: Karel_for_fetch_24_from_matrix_solution
      :passivecode: true
      
      from karel import *
      for i_kolona in range(2):         # cetiri puta ponovi ciscenje kolone
          napred()                      #     udji u sledecu kolonu
          levo()                        #     okreni se na sever
          for i_red in range(3):        #     idi do gornje ivice i usput pokupi
              napred()                   
              for i_loptica in range(4): 
                  uzmi()                  

          desno(); desno()              #     okreni se na jug
          for i_red in range(3):        #     idi do donje ivice
              napred()                   

          levo()                        #     okreni se na istok

      levo()                            #     okreni se na zapad
      levo()                           
      for i_kolona in range(2):         # vrati se na pocetno polje
          napred()

      for i_loptica in range(24):       # ostavi sve loptice
          ostavi()


Попни се па сиђи
''''''''''''''''

.. questionnote::

  Карел треба да се попне уз прве степенице, а затим да сиђе низ друге и заврши у доњем десном углу.

Сада нам требају само две петље једна за другом (не угнежђене). У првој петљи Карел треба да се попне уз прве, а у другој да сиђе низ друге степенице. У свакој петљи Карел треба да обави по 4 радње које представљају један корак уз или низ степенице.

.. karel:: Karel_for_stairs_constant
   :blockly:

   {
      setup:function() {

         var Y = 4;
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
                     "levo()                                 # ka severu",
                     "for i_stepenik in range(3):            # 3 puta ponovi",
                     "    # recite Karelu da se popne jedan stepenik ",
                     "",
                     "desno(); desno()                       # ka jugu",
                     "",
                     "# recite Karelu da sidje 3 stepenika",
                     ""];
    
         return {robot:robot, world:world, code:code};
      },
    
      isSuccess: function(robot, world) {
         return robot.getAvenue() == world.getAvenues() &&
            robot.getStreet() == 1;
      },
   }

.. reveal:: Karel_for_stairs_constant_reveal
   :showtitle: Решење
   :hidetitle: Сакриј решење

   .. activecode:: Karel_for_stairs_constant_solution
      :passivecode: true
      
      from karel import *
      levo()                                  # ka severu
      for i_stepenik in range(3):             # 3 puta ponovi
          napred(); desno(); napred(); levo() #     popni se jedan stepenik 

      desno(); desno()                        # ka jugu
      
      for i_stepenik in range(3):             # 3 puta ponovi
          napred(); levo(); napred(); desno() #     sidji jedan stepenik 



Сакупи лоптице на степеницама
'''''''''''''''''''''''''''''

.. questionnote::

  Карел поново треба да заврши у доњем десном углу, а успут треба да узме све лоптице.

Добар начин да се реши овај задатак је да се почне од решења претходног задатка. Препорука: ископирајте решење претходног задатка овде, а затим убаците петље за узимање лоптица.


.. karel:: Karel_for_stairs_and_balls_constant
   :blockly:

   {
      setup:function() {

         var Y = 4;
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
         
         // Balls
         for (let y = 2; y <= Y; y++) {
            world.putBalls(y - 1, y, 3);
            world.putBalls(y, y, 4);
         }
         for (let y = 1; y < Y; y++) {
            world.putBalls(X - y, y, 2);
            world.putBalls(X + 1 - y, y, 3);
         }

         var robot = new Robot();
         
         var code = ["from karel import *",
                     "# napisite program",
                     ""];
    
         return {robot:robot, world:world, code:code};
      },
    
      isSuccess: function(robot, world) {
         return robot.getBalls() == 36 &&
            robot.getAvenue() == world.getAvenues() &&
            robot.getStreet() == 1;
      },
   }

.. reveal:: Karel_for_stairs_and_balls_constant_reveal
   :showtitle: Решење
   :hidetitle: Сакриј решење

   .. activecode:: Karel_for_stairs_and_balls_constant_solution
      :passivecode: true
      
      from karel import *
      levo()                                 # ka severu
      for i_stepenik in range(3):            # 3 puta ponovi
          napred(); desno()
          for i_loptica in range(3):
              uzmi()
          napred(); levo() #    popni se jedan stepenik 
          for i_loptica in range(4):
              uzmi()
      
      desno(); desno()                       # ka jugu
      
      for i_stepenik in range(3):            # 3 puta ponovi
          napred(); levo()
          for i_loptica in range(2):
              uzmi()
          napred(); desno() #    sidji jedan stepenik 
          for i_loptica in range(3):
              uzmi()

