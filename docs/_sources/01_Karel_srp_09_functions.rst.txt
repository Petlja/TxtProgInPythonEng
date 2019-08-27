Направите пакет наредби
=======================

Подсетимо се задатка *Узми лоптицу на суседном пољу*. Задатак је био да Карел у сваком смеру покуша да оде на суседно поље и (ако успе да оде на суседно поље) да покуша да узме лоптицу тамо. Наравно, да би Карел могао да покуша у следећем смеру, било је потребно и да се после сваког покушаја врати на полазно поље.

Програм који решава задатак може да изгледа овако:

.. activecode:: Karel_functions__take_neighboring_ball_1
    :passivecode: true

    from karel import *
    for i in range(4):          # u svakom od 4 smera
        if moze_napred():       # potrazi polje u tom smeru
            napred()
            if ima_loptica_na_polju():
                uzmi()
            levo()              # vrati se na polazno polje
            levo()
            napred()
            levo()              # okreni se ka polju koje si probao
            levo()
        levo()                  # sledeci smer

Вероватно вам је део програма од седме до једанаесте линије мало тежи за праћење. У том делу можда замишљате Карела како извршава наредбу по наредбу да бисте сасвим разумели шта се ту дешава.

Коментари донекле помажу да се овај део програма лакше разуме. Поред коментара, још боље би било када би постојала функција *nazad()*, помоћу које би Карел направио корак уназад. Тада би програм био краћи и јаснији:

.. activecode:: Karel_functions__take_neighboring_ball_2
    :passivecode: true

    from karel import *
    for i in range(4):          # u svakom od 4 smera
        if moze_napred():       # potrazi polje u tom smeru
            napred()
            if ima_loptica_na_polju():
                uzmi()
            nazad()             # vrati se na polazno polje
        levo()                  # sledeci smer
        
Функција *nazad()* није део Карел библиотеке, али можемо врло једноставно да сами направимо ту функцију. Када је направимо, функцију *nazad()* моћи ћемо да је користимо равноправно са функцијама библиотеке *Карел* као што су *napred()*, *desno()* и остале.

Како се пишу функције
---------------------

За сада ћемо се упознати само са најједноставнијим начином писања функције у Пајтону, а остале, сложеније облике ћемо упознавати касније.

.. activecode:: Karel_functions__function_def
    :passivecode: true

    def ime_funkcije():
        naredba_1
        ...
        naredba_k

.. infonote::
      
   При писању било које функције на Пајтону, реч ``def`` на почетку, заграде ``()`` и двотачка ``:`` на крају првог реда су обвавезни. Као *ime_funkcije* може се појавити било које правилно написано име које ми изаберемо. Наредбе које следе, пишу се увучено и чине тело функције (ако се пише више наредби у једном реду, онда се те наредбе раздвајају знаком тачка-зарез). Наредбе у телу функције ће се извршити сваки пут када се при извршавању програма наиђе на име функције, то јест када та функција буде позвана.

У складу са овим правилима, функцију *nazad()* можемо да напишемо овако:

.. activecode:: Karel_functions__backwards_def
    :passivecode: true

    def nazad():
        levo(); levo()
        napred()
        levo(); levo()

Тада би цео програм изгледао овако:
   
.. karel:: Karel_functions__take_neighboring_ball_final
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
                     "def nazad():",
                     "    levo(); levo()",
                     "    napred()",
                     "    levo(); levo()",
                     "",    
                     "for i in range(4):",
                     "    if moze_napred():",
                     "        napred()",
                     "        if ima_loptica_na_polju():",
                     "            uzmi()",
                     "        nazad()",
                     "    levo()  # sledeci smer",
                     ""];
                     
         return {robot:robot, world:world, code:code};
      },
      
      isSuccess: function(robot, world) {
         return robot.getBalls() > 0;
      }
   }

.. infonote::
    Када неку логичку целину издвојимо у функцију, можемо да пишемо програме који су краћи и јаснији, јер смо проблем разложили на делове који су мање сложени.
    
    Још једна предност од писања функција је да их лако можемо искористити у другим програмима (овде ћемо написане функције повремено копирати, али у реалном програмирању постоји бољи и једноставнији начин).


Излазак из функције или петље пре њеног краја
---------------------------------------------

У примеру тражења лоптице на суседном пољу, ради једноставности програма смо одлучили да Карел и кад нађе лоптицу, он наставља да је тражи у преосталим смеровима. Постоји начин да избегнемо ово непотребно извршавање преосталих наредби. 

.. infonote::
    **Када желимо да прекинемо извршавање петље**, пишемо специјалну наредбу ``break``. Ефекат наредбе *break* је да "искочимо" из петље и наставимо извршавање програма од прве наредбе после петље.
    
    Наредбом *break* ћемо искочити из најближе (најуже) *for* или *while* петље која садржи ову наредбу. Ако се *break* наредба налази у две или више угнежђених петљи, извршавање се наставља наредбом која следи после унутрашње (најуже) петље. 
    
Користећи наредбу *break*, могли бисмо главни део програма 

.. activecode:: Karel_functions__break_intro_1
    :passivecode: true

    for i in range(4):
        if moze_napred():
            napred()
            if ima_loptica_na_polju():
                uzmi()
            nazad()
        levo()  # sledeci smer

да преправимо у:

.. activecode:: Karel_functions__break_intro_2
    :passivecode: true

    for i in range(4):
        if moze_napred():
            napred()
            if ima_loptica_na_polju():
                uzmi()
                break
            nazad()
        levo()  # sledeci smer

На тај начин се из петље излази чим је лоптица пронађена и узета. Пошто после ове петље нема других наредби, у овом случају се извршавањем наредбе *break* завршава и рад програма.

~~~~

Врло слично изласку из петље, из функције такође можемо да изађемо пре него што се све њене наредбе изврше.

.. infonote::
    **Када желимо да прекинемо извршавање функције**, пишемо специјалну наредбу ``return``. Ефекат наредбе *return* је да "искочимо" из функције и наставимо извршавање програма од прве наредбе после места одакле је функција позвана.
    
    Наредбом *return* искачемо из функције без обзира на то колико петљи окружује наредбу *return*.

Од програма за узимање лоптице на суседном пољу можемо да направимо функцију. У том случају бисмо могли да пишемо:

.. activecode:: Karel_functions__return_intro
    :passivecode: true

    def uzmi_na_susednom_polju():
        for i in range(4):
            if moze_napred():
                napred()
                if ima_loptica_na_polju():
                    uzmi()
                    return # izlazak iz funkcije
                nazad()
            levo()  # sledeci smer
            
    uzmi_na_susednom_polju()
    
Задаци за вежбу
---------------

Остављај лоптице док има лоптица и поља
'''''''''''''''''''''''''''''''''''''''

.. questionnote::

    Карел на почетку има неколико лоптица и треба да их распореди дуж пута по једну на свако поље (почевши од поља на коме стоји) докле је могуће. Карел прекида са постављањем лоптица када наиђе на препреку или када остане без лоптица (шта год се пре догоди). При томе није важно да ли ће се Карел зауставити на последњем попуњеном, или на првом празном пољу.
    
Предлог: Ставите један од ова два услова у *while* петљу, тако да се петља заврши када услов не буде више испуњен. Користите *break* наредбу да изађете из петље ако други услов није испуњен.
    
.. karel:: Karel_functions__put_balls_until_wall_or_no_more_balls
   :blockly:

    {
        setup:function() {
            function random(n) {
                return Math.floor(n * Math.random());
            }
            var choice = random(3); // need initial world to get rid of 'choice'
            var N = [3, 4, 5];
            var world = new World(N[choice], 1);
            world.setRobotStartAvenue(1);
            world.setRobotStartStreet(1);
            world.setRobotStartDirection("E");
            
            var robot = new Robot();
            if (choice == 0) robot.setBalls(3);
            if (choice == 1) robot.setBalls(6);
            if (choice == 2) robot.setBalls(2);
           
            var code = ["from karel import *",
                        " # dopunite",
                        ""];
                        
            //var code = ["from karel import *",
            //            "while ima_loptica_kod_sebe():",
            //            "    ostavi()",
            //            "    if not moze_napred():",
            //            "        break",
            //            "    napred()",
            //            ""];
                        
            return {robot:robot, world:world, code:code};
        },
    
        isSuccess: function(robot, world) {
            var X = world.getAvenues();
            var zeroBallsFound = false;
            for (var x = 1; x <= X; x++) {
                var b = world.getBalls(x, 1);
                if (b > 1) return false;
                if (b == 1 && zeroBallsFound) return false;
                if (b == 0) zeroBallsFound = true;
            }
           
           if (robot.getBalls() > 0 && zeroBallsFound)
               return false;
                 
           return true;
        },
    }

Помери све лоптице уназад
'''''''''''''''''''''''''

.. questionnote::

    Испред Карела је прав пут непознате дужине. На почетном пољу нема лоптица. Карел треба да сваку лоптицу премести за једно поље ка левој страни екрана.
  
Овај задатак можете да решите тако што, док год има поља испред Карела, понављате следеће кораке:

- пређи на следеће поље
- узми све лоптице са тог поља
- иди корак назад (то јест, окрени се два пута и иди напред)
- остави све лоптице
- врати се на поље са којег си узео лоптице

При томе, за враћање на поље на које Карел премешта лоптице можете да користите раније написану функцију *nazad()*. Треба само да је ископирате или препишете у простор за решавање.

.. karel:: Karel_functions__all_balls_one_square_back
   :blockly:

    {
        setup:function() {
           function random(n) {
              return Math.floor(n * Math.random());
           }
           var choice = random(3); // need initial world to get rid of 'choice'
           var N = [3, 4, 5];
           var world = new World(N[choice], 1);
           world.setRobotStartAvenue(1);
           world.setRobotStartStreet(1);
           world.setRobotStartDirection("E");
           
           var B = 0;
           if (Math.random() > 0.8) B = random(3);
           if (choice == 0) {
              world.putBalls(2, 1, B);
              world.putBalls(3, 1, B + 2);
           }
           if (choice == 1) {
              world.putBalls(2, 1, B);
              world.putBalls(3, 1, B + 3);
              world.putBalls(4, 1, B + 1);
           }
           if (choice == 2) {
              world.putBalls(2, 1, B);
              world.putBalls(3, 1, B + 2);
              world.putBalls(4, 1, B + 1);
              world.putBalls(5, 1, B + 0);
           }

           var robot = new Robot();

           var code = ["from karel import *",
                       "",
                       "# kopirajte funkciju 'nazad'()",
                       "",
                       "while moze_napred():   # dok ima polja ispred Karela, ponavljaj",
                       "    napred();              # idi napred",
                       "    # dopunite             # pokupi sve loptice sa polja",
                       "    # dopunite             # idi jedno polje nazad",
                       "    # dopunite             # ostavi sve loptice",
                       "    # dopunite             # vrati se napred na ispraznjeno polje",
                       ""];
                       
           return {robot:robot, world:world, code:code};
        },
    
        isSuccess: function(robot, world) {
           var N = world.getAvenues();
           var B = world.getBalls(1, 1);
           if (N == 3) {
              if (world.getBalls(2, 1) != B + 2)
                return false;              
           }
           if (N == 4) {
              if (world.getBalls(2, 1) != B + 3)
                return false;
              if (world.getBalls(3, 1) != B + 1)
                return false;              
           }
           if (N == 5) {
              if (world.getBalls(2, 1) != B + 2)
                return false;
              if (world.getBalls(3, 1) != B + 1)
                return false;
              if (world.getBalls(4, 1) != B + 0)
                return false;
           }
           
           if (world.getBalls(N, 1) != 0) 
              return false;

           if (robot.getBalls() > 0)
                 return false;
                 
           return true;
        },
    }
   
.. reveal:: Karel_functions__all_balls_one_square_back_reveal
    :showtitle: Решење
    :hidetitle: Сакриј решење

    .. activecode:: Karel_functions__all_balls_one_square_back_solution
        :passivecode: true
      
        from karel import *
        def nazad():     # idi jedno polje nazad, ostani isto okrenut
            levo(); levo();
            napred(); 
            levo(); levo();

        while moze_napred():   # dok ima polja ispred Karela, ponavljaj
            napred();                     # idi na novo polje
            while ima_loptica_na_polju(): # uzmi sve loptice na polju
                uzmi()            
            nazad()                       # korak nazad
            while ima_loptica_kod_sebe(): # ostavi sve loptice
                ostavi()
            napred()                      # idi na polje koje si ispraznio


Прати лоптице
'''''''''''''

.. questionnote::

    На сваком пољу се налази по једна или ниједна лоптица. Поља са лоптицама формирају пут, који почиње на пољу поред Карела. Карел треба да прати тај пут и да покупи све лоптице.

Предлог: ради решавања овог задатка можете да напишете функцију *na_neprazno_susedno_polje()*, која треба само да премести Карела на суседно поље на коме постоји лоптица (при томе наредба *return* може да буде корисна). Функција *na_neprazno_susedno_polje* треба да се разликује од раније написане функције *uzmi_na_susednom_polju()* само по томе што не узима лоптицу.

Када Карел покупи све лоптице, следећи позив ове функције ће оставити Карела на неком празном пољу (то ће бити поље на коме је Карел узео последњу лоптицу). По томе што нема лоптице на пољу на коме се налази Карел, знаћемо да је Карел већ узео све лоптице.

.. karel:: Karel_functions__follow_the_balls
   :blockly:

    {
        setup:function() {
            function random(n) {
                return Math.floor(n * Math.random());
            }
         
            var ww = [
                [
                   '███████████',
                   '█0.0.1.1.0█',
                   '█.........█',
                   '█0.N.0.1.0█',
                   '█.........█',
                   '█0.1.1.1.0█',
                   '███████████'
                ],
                [
                   '███████████',
                   '█1.1.1.1.1█',
                   '█.........█',
                   '█1.0.0.0.1█',
                   '██........█',
                   '█S.1.1.1.1█',
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
                        "def nazad():",
                        "    levo(); levo()",
                        "    napred()",
                        "    levo(); levo()",
                        "",    
                        "def na_neprazno_susedno_polje():",
                        "    # napisite funkciju",
                        "",
                        "na_neprazno_susedno_polje()",
                        "while ??? # dodajte uslov",
                        "    uzmi()",
                        "    ??? # dopunite",
                        ""];
                     
            //var code = ["from karel import *",
            //            "def nazad():",
            //            "    levo(); levo()",
            //            "    napred()",
            //            "    levo(); levo()",
            //            "",
            //            "def na_neprazno_susedno_polje():",
            //            "    for i in range(4):",
            //            "        if moze_napred():",
            //            "            napred()",
            //            "            if ima_loptica_na_polju():",
            //            "                return",
            //            "            nazad()",
            //            "        levo()  # sledeci smer",
            //            "",
            //            "na_neprazno_susedno_polje()",
            //            "while ima_loptica_na_polju():",
            //            "    uzmi()",
            //            "    na_neprazno_susedno_polje()",
            //            ""];
            
            return {robot:robot, world:world, code:code};
        },
      
        isSuccess: function(robot, world) {
            var X = world.getAvenues();
            var Y = world.getStreets();
            for (var y = 1; y <= Y; y++)
                for (var x = 1; x <= X; x++)
                    if (world.getBalls(x, y) > 0)
                        return false;
               
            return true;
        },
    }



Узми све лоптице са целе табле
''''''''''''''''''''''''''''''

.. questionnote::

  Карел је на почетку окренут ка северу (горе), а налази се у доњем левом углу правоугаоне табле непознате величине, без унутрашњих зидова. На сваком пољу може бити било колико лоптица. Карел треба да узме све лоптице са свих поља табле.

Предлог: Напишите функцију *isprazni_red()*, помоћу које Карел:

- окреће се на лево (на истоку, тј. десној страни екрана, гледајући дуж реда на чијем је почетку)
- пролази цео ред табеле и успут узима све лоптице са сваког поља из тог реда, укључујући и прво поље у реду, са кога је кренуо
- окреће се ка почетку реда (ка западу, тј. ка десној страни екрана)
- враћа се на почетак реда и окреће се на северу (горе), као што је стајао пре позива функције

Програм који решава задатак помоћу ове функције није дугачак. Потребно је:

- испразнити први ред
- док има редова испред Карела, ићи на следећи ред и испразнити га

.. karel:: Karel_functions_take_all_balls_2D
   :blockly:

   {
      setup:function() {
         function random(n) {
            return Math.floor(n * Math.random());
         }

         var sizes = [1, 2, 3, 3, 4, 4, 4];
         var numBalls = [0, 0, 1, 1, 1, 3];
         var X = sizes[random(sizes.length)];
         var Y = sizes[random(sizes.length)];
         var world = new World(X, Y);
         world.setRobotStartAvenue(1);
         world.setRobotStartStreet(1);
         world.setRobotStartDirection("N");
         
         for (var col = 1; col <= X; col++) {
             for (var row = 1; row <= Y; row++) {
                 let B = numBalls[random(numBalls.length)];
                 world.putBalls(col, row, B);
             }
         }
      
         var robot = new Robot();
         
         var code = ["from karel import *",
                     "# dopunite",
                     ""];
        //var code = ["from karel import *
        //            "def isprazni_red():",
        //            "    desno()                            # okreni se ka kraju reda (ka istoku)",
        //            "    while ima_loptica_na_polju():      # isprazni prvo polje u redu",
        //            "        uzmi()",
        //            "    while moze_napred():               # dok ima jos polja u redu",
        //            "        napred()                           # predji na novo polje",
        //            "        while ima_loptica_na_polju():      # isprazni novo polje",
        //            "            uzmi()",
        //            "        ",
        //            "    desno(); desno()                   # okreni se ka pocetku reda (ka zapadu)",
        //            "    while moze_napred():               # vrati se na pocetak reda",
        //            "        napred()",
        //            "    desno()                            # okreni se ka sledecem redu (ka severu)",
        //            "",
        //            "isprazni_red()                 # pokupi loptice iz prvog reda",
        //            "while moze_napred():           # dok ima jos redova",
        //            "    napred(); isprazni_red()   #     predji u sledeci red i isprazni ga",
        //            ""];

         return {robot:robot, world:world, code:code};
        },

        isSuccess: function(robot, world) {
           var X = world.getAvenues();
           var Y = world.getStreets();
           for (var col = 1; col <= X; col++) {
              for (var row = 1; row <= Y; row++) {
                 if (world.getBalls(col, row) > 0)   
                    return false;
              }
           }
                 
           return true;
      },
   }
