Наредба *if* - вежбање
======================

У овом делу ћемо само увежбавати употребу *if* наредбе и њено комбиновање са петљама.

Задаци за вежбу
---------------

Иди до краја и узми само једну
''''''''''''''''''''''''''''''

.. questionnote::

   Карел треба да стигне до краја ходника, а да успут узме само прву лоптицу на коју наиђе. Поље са кога Карел полази никад нема лоптицу, а и Карел је на почетку без лоптица.
   
.. karel:: Karel_if__take_first_ball_only
   :blockly:

   {
      setup:function() {
         function random(n) {
            return Math.floor(n * Math.random());
         }
         
         var ww = [
            [
               '█████████████',
               '█E.0.1.0.3.0█',
               '█████████████'
            ],
            [
               '█████████',
               '█E.0.2.2█',
               '█████████'
            ],
            [
               '███████',
               '█E.1.0█',
               '███████'
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
         return robot.getBalls() > 0;
      }
   }

.. reveal:: Karel_if__take_first_ball_only_reveal
    :showtitle: Помоћ
    :hidetitle: Сакриј помоћ
    
    Овде је започето једно решење, потребно је допунити *if* наредбе одговарајућим условима.
    
    Карел треба да узме лоптицу само ако су испуњена два услова:
    
    - један је услов који проверавамо при сваком узимању лоптице (без тог услова програм би могао да се прекине због неизводљиве операције).
    - други услов је наметнут захтевима овог задатка, а то је да Карел узима лоптицу само ако пре тога није већ узео неку лоптицу.
    
    Редослед испитивања ова два услова није битан, свакако оба треба да буду испуњена да би Карел узео лоптицу.
    
    .. activecode:: Karel_if__take_first_ball_only_solution
        :passivecode: true
      
        from karel import *
        while moze_napred():  # dok ima polja ispred Karela
            napred()                    
            if ???
                if ???
                    uzmi()

Узми лоптицу на суседном пољу
'''''''''''''''''''''''''''''

.. questionnote::

   На табли се налази само једна лоптица. Карел и лоптица се налазе на два суседна поља, између којих нема зида (Карела од лоптице дели само један корак, ако се пре тога окрене ка лоптици). Између осталих поља може а не мора бити зидова. Карел треба да узме лоптицу и при томе није битно на којем пољу ће да остане када се програм заврши.
   
   Као и обично, покрените програм више пута да бисте га тестирали на различитим примерима.   

Једна од идеја је да у сваком од 4 смера покушамо Карелом корак напред и узимање лоптице. При сваком од 4 покушаја могу да наступе разни случајеви:

- могуће је да у том смеру нема поља напред
- могуће је да постоји поље испред Карела, али да на њему нема лоптице
- могуће је да постоји поље и да је на њему лоптица

При покушају у следећем смеру нам је много једноставније ако не морамо да водимо рачуна о томе да ли је Карел у претходном смеру нашао поље без лоптице, или није нашао ни поље. Ради тога је потребно да Карел, када заврши покушај у једном смеру, стане на исти начин када је био на празном пољу, као и када поља није ни било. Када поља у датом смеру нема, Карел ће остати на почетном пољу, окренут у том смеру. Најједноставније за наставак трагања је да Карела оставимо на истом пољу и у истом положају и када се врати са празног суседног поља. У ствари, неће сметати ако то урадимо и када Карел узме лоптицу (може да догодити да Карел непотребно настави да тражи, али неће доћи до грешке). 

Захваљујући овом довођењу Карела на исто стање (позиција и оријентација) после било ког од три горе набројана случаја, за сваки следећи покушај тачно знамо од ког Кареловог стања почињемо. Остаје да након сваког покушаја окренемо Карела ка следећем смеру у којем ћемо покушати да дођемо до лоптице (на лево или на десно).

.. karel:: Karel_if__take_neighboring_ball
   :blockly:

   {
      setup:function() {
         function random(n) {
            return Math.floor(n * Math.random());
         }
         
         var ww = [
            [
               '█████',
               '█0.0█',
               '███.█',
               '█1.N█',
               '███.█',
               '█0.0█',
               '█████'
            ],
            [
               '█████',
               '█1.0█',
               '█...█',
               '█E.0█',
               '█████'
            ],
            [
               '███████',
               '█0█0█0█',
               '█.█.█.█',
               '█0.W.0█',
               '█.█.█.█',
               '█0█1█0█',
               '███████'
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
                     "for i in range(4):",
                     "    if moze_napred():",
                     "        napred()",
                     "        # recite Karelu da pokusa da uzme lopticu",
                     "        # recite Karelu da se vrati na pocetno polje",
                     "        # i okrene se ka polju na kome je upravo pokusao",
                     "        # (kao da nije ni isao na to polje)",
                     "    # recite Karelu da se pripremi za sledeci pokusaj",
                     ""];
                     
         return {robot:robot, world:world, code:code};
      },
      
      isSuccess: function(robot, world) {
         return robot.getBalls() > 0;
      }
   }

.. commented out
   .. reveal:: Karel_if__take_neighboring_ball_reveal
       :showtitle: Решење
       :hidetitle: Сакриј решење
       
       Решење може да изгледа овако:
       
       .. activecode:: Karel_if__take_neighboring_ball_solution
           :passivecode: true
         
           from karel import *
           for i in range(4):          # u svakom od 4 smera
               if moze_napred():       # potrazi polje u tom smeru
                   napred()                    
                   if ima_loptica_na_polju():
                       uzmi()
                   levo()              # idi na polazno polje
                   levo()
                   napred()
                   levo()              # okreni se ka polju koje si probao
                   levo()
               levo()                  # sledeci smer

Прати пут
'''''''''

.. questionnote::

  Постоји само једна лоптица и Карел треба да је узме. Пут до лоптице је кривудав, али нема раскрсница (увек постоји само један наставак пута, чак и са полазног поља).


.. karel:: Karel_if__take_ball_no_branches
   :blockly:

   {
      setup:function() {
         function random(n) {
            return Math.floor(n * Math.random());
         }
         
         var ww = [
            [
               '███████████',
               '█N█0.0.0.0█',
               '█.█.█████.█',
               '█0█0█0.1█0█',
               '█.█.█.███.█',
               '█0.0█0.0.0█',
               '███████████'
            ],
            [
               '█████████',
               '█0.0.0.0█',
               '█.█████.█',
               '█0█0.0.0█',
               '█.█.█████',
               '█0█E█0.0█',
               '█.███.█.█',
               '█0.0.0█1█',
               '█████████'
            ],
            [
               '█████████████',
               '█W.0.0█0.0.0█',
               '█████.█.███.█',
               '█0.0.0█0█0.0█',
               '█.█████.█.███',
               '█0.0.0.0█0.1█',
               '█████████████'
            ],
            [
               '███████████',
               '█0.0█0.0█S█',
               '█.█.█.█.█.█',
               '█0█0.0█0.0█',
               '█.█████████',
               '█0█0.0█0.0█',
               '█.█.█.█.█.█',
               '█0.0█0.0█1█',
               '███████████'
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
                     "... # dopunite",
                     ""];
                     
         return {robot:robot, world:world, code:code};
      },
      
      isSuccess: function(robot, world) {
         return robot.getBalls() > 0;
      }
   }

.. reveal:: Karel_if__take_ball_no_branches_reveal
    :showtitle: Помоћ
    :hidetitle: Сакриј помоћ
    
    Упутства за једно могуће решење:

    .. activecode:: Karel_if__take_ball_no_branches_solution
        :passivecode: true
      
        # prvo se okreni ka (jedinom) praznom polju
        dok ne mozes napred: 
            okreni se na levo
            
        dok mozes napred:
            idi napred            
            ako ispred tebe nije prazno polje: # ako ne mozes pravo
                okreni se na levo
                ako ispred tebe nije prazno polje: # ako ne mozes ni levo
                    okreni se dva puta na desno
        
        uzmi lopticu

.. commented out
   .. reveal:: Karel_if__take_ball_no_branches_reveal
       :showtitle: Решење
       :hidetitle: Сакриј решење
       
       Једно могуће решење је:
   
       .. activecode:: Karel_if__take_ball_no_branches_solution
           :passivecode: true
         
           from karel import *
           while not moze_napred(): # okreni se ka (jedinom) praznom polju
               levo()
               
           while moze_napred():
               napred()
               
               # okreni se ka sledecem praznom polju
               if not moze_napred(): # ako ne moze pravo,
                   levo()                # probaj levo
               if not moze_napred(): # ako ne moze ni levo
                   desno(); desno()      # probaj desno
           
           if ima_loptica_na_polju():
               uzmi()

Скрећи
''''''

.. questionnote::

  Постоји само једна лоптица и Карел треба да је узме. Да би стигао до лоптице, Карел треба да иде право само кад не може да скрене ни лево ни десно (неће се појавити раскрснице на којима се може скренути и лево и десно). 


.. karel:: Karel_if__p1_left_p2_right_p3_forward
   :blockly:

   {
      setup:function() {
         function random(n) {
            return Math.floor(n * Math.random());
         }
         
         var ww = [
            [
               '███████████',
               '█1.0█0.0.0█',
               '███.█.█████',
               '█0.0.0█0.0█',
               '█████.███.█',
               '█S.0.0.0.0█',
               '███████████'
            ],
            [
               '███████████',
               '█0.0.0█0.0█',
               '█████.█.███',
               '█0.0.0█0.0█',
               '█.█.█.█.█.█',
               '█0█0█E█0█1█',
               '█.█.███.███',
               '█0█0.0.0.0█',
               '███████████'
            ],
            [
               '█████████████',
               '█E.0.0█0.0.0█',
               '███.█.█.█████',
               '█0.0█0█0.0.0█',
               '█.█.███.███.█',
               '█0█0█0.0.0█0█',
               '█.███.█████.█',
               '█0.0.0.0.0█1█',
               '█████████████'
            ],
            [
               '█████████',
               '█0.0.0█S█',
               '█.█████.█',
               '█0.0.0.0█',
               '███.███.█',
               '█0█0.0█0█',
               '█.█.█.███',
               '█0.0█0.1█',
               '█████████'
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
                     "... # dopunite",
                     ""];
                     
         return {robot:robot, world:world, code:code};
      },
      
      isSuccess: function(robot, world) {
         return robot.getBalls() > 0;
      }
   }
   
.. reveal:: Karel_if__p1_left_p2_right_p3_forward_reveal
    :showtitle: Помоћ
    :hidetitle: Сакриј помоћ

    Упутства за једно могуће решење:
    
    .. activecode:: Karel_if__p1_left_p2_right_p3_forward_solution
        :passivecode: true
      
        # okreni se ka (jedinom) praznom polju
        
        dok mozes da ides napred:
            idi napred
            # probaj da skrenes levo (okreni se na levo i probaj napred)
            # ako ne mozes levo
                # probaj da skrenes desno
                # ako ne mozes ni desno
                    # probaj pravo u sledecoj iteraciji
        
        uzmi lopticu

.. commented out
    .. reveal:: Karel_if__p1_left_p2_right_p3_forward_reveal
        :showtitle: Решење
        :hidetitle: Сакриј решење

        .. activecode:: Karel_if__p1_left_p2_right_p3_forward_solution
            :passivecode: true
          
            from karel import *
            for i in range(3):        # okreni se ka (jedinom) praznom polju
                if not moze_napred():
                    levo()
            
            while moze_napred():
                napred()
                levo()                # probaj da skrenes levo
                if not moze_napred(): # ako ne mozes levo
                    desno(); desno()     # probaj da skrenes desno
                if not moze_napred(): # ako ne mozes ni desno
                    levo()               # probaj pravo u sledecoj iteraciji
            
            uzmi()

Лево кад год може
'''''''''''''''''

.. questionnote::

  Постоји само једна лоптица и Карел треба да је узме. Карел ће до лоптице увек стићи тако што скрене лево кад год може, а иначе иде право (кад не може ни лево ни право, значи да је стигао). Карел је на почетку окренут како треба и први корак му је увек право.


.. karel:: Karel_if_p1_left_p2_forward
   :blockly:

   {
      setup:function() {
         function random(n) {
            return Math.floor(n * Math.random());
         }
         
         var ww = [
            [
               '█████████████',
               '█0.0.0.0.0.0█',
               '█.███████.█.█',
               '█0.0.0.1█0█0█',
               '█████.███...█',
               '█0.0.0.0█0.0█',
               '█████████.███',
               '█E.0.0.0.0.0█',
               '█████████████'
            ],
            [
               '█████████████',
               '█0.0.0.0.0█0█',
               '█..██████.█.█',
               '█0.0█0.0.0█0█',
               '█████..██.█.█',
               '█0.0.0.1█0█0█',
               '█████████..██',
               '█E.0.0.0.0.0█',
               '█████████████'
            ],
            [
               '█████████████',
               '█0.0.0.0.0█0█',
               '█.█.........█',
               '█0█0.0.0.0.0█',
               '█.█.███████.█',
               '█0█0.0.1█0█0█',
               '█.█.█████.█.█',
               '█0.0.0.0.0█N█',
               '█████████████'
            ],
            [
               '█████████████',
               '█S█0.0.0.0█0█',
               '█.███.███...█',
               '█0█0.1█0█..0█',
               '█.███████.█.█',
               '█0.0.0.0.0█0█',
               '█.███████████',
               '█0.0.0.0.0.0█',
               '█████████████'
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
                     "... # dopunite",
                     ""];
                     
         return {robot:robot, world:world, code:code};
      },
      
      isSuccess: function(robot, world) {
         return robot.getBalls() > 0;
      }
   }

.. reveal:: Karel_if_p1_left_p2_forward_reveal
    :showtitle: Помоћ
    :hidetitle: Сакриј помоћ

    Упутства за једно могуће решење:
    
    .. activecode:: Karel_if_p1_left_p2_forward_solution
        :passivecode: true
      
        dok mozes da ides napred:
            idi napred
            # ako ne postoji put na levo
                # ostani okrenut pravo

        uzmi lopticu

.. commented out
    .. reveal:: Karel_if_p1_left_p2_forward_reveal
        :showtitle: Решење
        :hidetitle: Сакриј решење

        .. activecode:: Karel_if_p1_left_p2_forward_solution
            :passivecode: true
          
            from karel import *
            while moze_napred():
                napred()
                levo()
                if not moze_napred():
                    desno()

            if ima_loptica_na_polju():
                uzmi()
