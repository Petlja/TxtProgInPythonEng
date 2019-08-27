Скратите писање програма
========================

У претходном поглављу је било задатака у којима би нам било згодно да имамо скраћени запис за неке акције које се понављају. На пример, било је потребно да Карел иде три корака напред. У случају само три корака није проблем да напишемо наредбу ``napred()`` три пута, међутим када Карел треба да направи дванаест корака напред, ако пишемо:

.. activecode:: Karel_for_12_steps_manual
   :passivecode: true
   
   napred(); napred(); napred(); napred(); napred()
   napred(); napred(); napred(); napred(); napred()
   napred(); napred()

у таквом начину писања лакше се погреши, а није ни довољно прегледно. Ако вам изгледа да ни дванаест није неки проблем, помислите да у свету програмирања није ретко да се нека наредба понавља и по милион пута.

Наредба for
-----------

Бољи начин задавања оваквог кретања би био да кажемо: "дванаест пута иди напред". Да бисмо неку наредбу (или групу наредби) поновили одређени број пута, користимо наредбу ``for``. Најчешће коришћени облик ове наредбе У Пајтону изгледа овако:

.. activecode:: Karel_for_syntax
   :passivecode: true
   
   for i in range(n):
       naredba_1
       ...
       naredba_k

Касније ћемо се упознати са још неким облицима наредбе ``for``. 

Наш пример са дванаест понављања једног корака напред се помоћу ``for`` наредбе може записати овако:
      
.. activecode:: Karel_for_12_steps_loop
   :passivecode: true
   
   for i in range(12):
       napred()


Овде дајемо и нешто детаљнији опис ``for`` наредбе. Не морате га потпуно разумети у овом тренутку, употреба и правила писања ће постати јаснији уз примере који следе. Када будете желели мало више детаља о наредби ``for``, можете се вратити на ово објашњење (мада оно не описује друге облике *for* наредбе).


.. infonote::

   Према правилима писања програма на Пајтону, речи ``for`` и ``in``, као и двотачка (знак ``:``) на крају реда, морају се појавити у запису ове наредбе. 
   
   - Слово ``i`` је овде име за место на коме бројимо докле смо стигли са понављањем, па уместо ``i`` може да стоји и неко друго име (вратићемо се на ово кад нам затреба). 
   - Запис ``range(n)`` представља опсег целих бројева почевши од 0, а ``n`` говори колико бројева садржи тај опсег. На пример ``range(3)`` је опсег који садржи бројеве :code:`0, 1, 2`, а ``range(7)`` је опсег са бројевима :code:`0, 1, 2, 3, 4, 5, 6`.
   - Наредбе у следећим редовима чине такозвано **тело for наредбе**. То могу бити било које наредбе на Пајтону, укључујући наредбе за кретање Карела, друге наредбе ``for``, или неке наредбе које још нисмо поменули. Може их бити једна или више. 
   
   Запис ``for i in range(3)`` би требало читати: "за ``i`` у опсегу [0, 1, 2]". То значи да ће се наредбе у телу for наредбе извршити по једанпут за i=0, i=1, i=2, дакле укупно три пута. Ми у телу for наредбе за сада нећемо користити вредност i, тако да нам је битно само колико опсег има вредности (број иза ``range`` у загради), јер ће се тело for наредбе толико пута извршити.
   
   Да би било јасно које наредбе чине тело for наредбе, те наредбе се пишу увучено (померено у десно), и то све за исти број размака. Можемо сами да одаберемо колико размака користимо за увлачење наредби у телу *for* наредбе. Било би добро да то увек буде исти број, јер ћемо тако навићи да одређени изглед програма и лакше га читати. Најчешће је то 4 размака, па ћемо и ми увлачити тело *for* наредбе за четири места.


Наредба ``for`` се често зове и наредба понављања. Такође је позната и као петља (енгл. loop), јер кретањем у програму по наредбама које извршавамо, кад наиђемо на наредбу ``for`` кружимо одређени број пута по наредбама у њеном телу, то јест правимо петљу. 
Изрази "петља" или "наредба понављања" су мање прецизни, јер као што ћемо ускоро видети, наредба for није једина петља, односно наредба понављања. Реч "петља" обично користимо када је јасно (или небитно) о којој наредби говоримо, јер лакше је рећи на пример "тело петље", него "тело for наредбе".

Задаци за вежбу
---------------

Помери се петнаест поља напред и узми лоптицу
'''''''''''''''''''''''''''''''''''''''''''''

.. questionnote::

   Напиши програм на основу којега ће се Карел померити на поље (16, 1) и покупити лоптицу.

У простору за решавање вас чека дужи (и ружнији) програм. Покушајте да га замените ``for`` наредбом. У случају да вам решење са ``for`` наредбом не проради (што се у почетку често дешава), решење можете да видите када кликнете на дугме "Решење" испод.

.. karel:: Karel_for_15_steps_and_take
   :blockly:

   {
      setup:function() {
          var world = new World(16, 1);
          world.setRobotStartAvenue(1);
          world.setRobotStartStreet(1);
          world.setRobotStartDirection("E");
          world.putBall(16, 1);
      
         var robot = new Robot();
      
         var code = ["from karel import *",
                  "napred(); napred(); napred(); napred(); napred()",
                  "napred(); napred(); napred(); napred(); napred()",
                  "napred(); napred(); napred(); napred(); napred()",
                  "uzmi()"];
                  
         return {robot:robot, world:world, code:code};
      },
      
      isSuccess: function(robot, world) {
         return robot.getBalls() === 1;
      }
   }

.. reveal:: Karel_for_15_steps_and_take_reveal
   :showtitle: Решење
   :hidetitle: Сакриј решење

   .. activecode:: Karel_for_15_steps_and_take_solution
      :passivecode: true
      
      from karel import *
      for i in range(15):
          napred()
      uzmi()

      
Иди једно поље напред и покупи 10 лоптица
'''''''''''''''''''''''''''''''''''''''''

.. questionnote::

  Испред Карела је тачно једно поље, а на њему 14 лоптица. Карел треба да их покупи тачно десет.
  
.. karel:: Karel_for_one_square_take_10_balls
   :blockly:

   {
        setup:function() {
           var world = new World(2, 1);
           world.setRobotStartAvenue(1);
           world.setRobotStartStreet(1);
           world.setRobotStartDirection("E");
           
           world.putBalls(2, 1, 14);

           var robot = new Robot();

           var code = ["from karel import *",
                       "napred()",
                       "# dovrsite program",
                       ""];
           return {robot:robot, world:world, code:code};
        },
    
        isSuccess: function(robot, world) {
           return robot.getBalls() == 10;
        },
   }
   
.. reveal:: Karel_for_one_square_take_10_balls_reveal
   :showtitle: Решење
   :hidetitle: Сакриј решење

   .. activecode:: Karel_for_one_square_take_10_balls_solution
      :passivecode: true
      
      from karel import *
      napred()
      for i in range(10):
          uzmi()


Узимај по једну лоптицу на наредних 8 поља
''''''''''''''''''''''''''''''''''''''''''

.. questionnote::

  Испред Карела је осам поља, а на сваком од њих по једна лоптица. Карел треба да покупи све лоптице.
  
Приметите да сада у for петљи треба урадити две ствари: коракнути напред и узети лоптицу.

.. karel:: Karel_for_EightSquaresOneBallEach_TakeAllBalls
   :blockly:

   {
        setup:function() {
           var numAvenues = 9;
           var world = new World(numAvenues, 1);
           world.setRobotStartAvenue(1);
           world.setRobotStartStreet(1);
           world.setRobotStartDirection("E");
           
         for (var k = 2; k <= numAvenues; k++)
            world.putBall(k, 1);

           var robot = new Robot();

           var code = ["from karel import *",
                       "# dovrsite program",
                       ""];
           return {robot:robot, world:world, code:code};
        },
    
        isSuccess: function(robot, world) {
           return robot.getBalls() == world.getAvenues() - 1;
        },
   }
   
.. reveal:: Karel_for_EightSquaresOneBallEach_TakeAllBalls_reveal
   :showtitle: Решење
   :hidetitle: Сакриј решење

   .. activecode:: Karel_for_EightSquaresOneBallEach_TakeAllBalls_solution
      :passivecode: true
      
      from karel import *
      for i in range(8):
          napred()
          uzmi()


Покупи по 5 лоптица са наредна три поља
'''''''''''''''''''''''''''''''''''''''

.. questionnote::

  Испред Карела су три поља, а на сваком од њих по пет лоптица. Карел треба да покупи све лоптице.

  
.. karel:: Karel_for_Take_5_5_5
   :blockly:

   {
        setup:function() {
           var world = new World(4, 1);
           world.setRobotStartAvenue(1);
           world.setRobotStartStreet(1);
           world.setRobotStartDirection("E");
           
           world.putBalls(2, 1, 5);
           world.putBalls(3, 1, 5);
           world.putBalls(4, 1, 5);
           
           var robot = new Robot();

           var code = ["from karel import *",
                       "# dovrsite program",
                       ""];
           return {robot:robot, world:world, code:code};
        },
    
        isSuccess: function(robot, world) {
           return robot.getBalls() == 15;
        },
   }
   
.. reveal:: Karel_for_Take_5_5_5_reveal
   :showtitle: Решење
   :hidetitle: Сакриј решење
   
   .. activecode:: Karel_for_Take_5_5_5_solution
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

