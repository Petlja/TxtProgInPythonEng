Додатна упутства функцији
=========================

Поменули смо да постоји неколико начина писања функција у Пајтону, а да су функције које смо до сада писали и користили најпростијег облика. Такве су на пример функције *napred()*, *levo()*, *desno()* , *uzmi()* и *ostavi()* из библиотеке Карел, као и функције *nazad()*, *uzmi_na_susednom_polju()* и *na_neprazno_susedno_polje()*, које смо сами писали. Све ове функције обављају неки конкретан посао, увек на исти начин. 

Функције могу да се пишу и тако да у различитим извршавањима не раде увек сасвим исту ствар, него да обављају мало општији задатак. За такве функције ми при њиховом позивању прецизније наводимо како тачно желимо да се задатак обави. На пример, често би могла да нам буде корисна функција која би померила Карела за неки број поља напред или назад. За ту функцију желимо да при њеном позивању прецизирамо захтев - за колико поља Карел треба да се помери и на коју страну.

Функције са параметрима
-----------------------

.. infonote::
    Додатне информације које дајемо функцији пишу се између заграда после имена функције, у првом реду њене дефиниције. Између заграда можемо да наведемо једну вредност, или више вредности раздвојених зарезима. Те вредности се називају **аргументи** функције, или **параметри** функције. Речи "аргументи" и "параметри" су у програмирању синоними и користићемо их равноправно.
    
.. activecode:: Karel_functions__function_with_args_def
    :passivecode: true

    def ime_funkcije(parametar1, ... parametarN):
        naredba_1
        ...
        naredba_k

Функција која помера Карела за задати број поља напред или назад, могла би да се зове *idi* и да има један параметар, чија вредност је цео број. Ако је тај параметар позитиван, Карел би се померио толико поља напред, а ако је негативан, Карел би ишао одговарајући (супротан) број поља назад. На пример, позив *idi(5)* би значио "иди 5 поља напред", док би *idi(-2)* значио "иди 2 поља назад". Ево како можемо да напишемо такву функцију:

.. activecode:: Karel_functions__function_go_def
    :passivecode: true

    def idi(n):
        if n > 0:
            for i in range(n):
                napred()
        else:
            levo();levo()
            for i in range(-n):
                napred()
            levo();levo()
 
Ова функција може да поједностави многе програме у којима Карел треба да више пута иде дуж једног ходника на једну и другу страну. Следи пример.


Обави задата премештања
'''''''''''''''''''''''

.. questionnote::

    Карел се налази на почетном пољу ходника довољне дужине, а треба да обави следећа премештања лоптица:

    - 3 лоптице са поља 3 на поље 4
    - 4 лоптице са поља 5 на поље 1

При решавању овог задатка користићемо описану функцију *idi*. Да бисмо додатно поједноставили програм, можемо да уведемо и функцију *premesti*, која премешта задати број лоптица за задати број поља напред или назад. Из овог описа се види да функција *premesti* треба да има два аргумента. 

Да би било јасније чему служи који аргумент, даћемо им имена која описују њихову улогу:

.. activecode:: Karel_functions__function_displace_def
    :passivecode: true

    def premesti(br_loptica, br_polja):
        for i in range(br_loptica):
            uzmi()
        idi(br_polja)
        for i in range(br_loptica):
            ostavi()
            
Функција *premesti* користи при свом извршавању раније написану функцију *idi*. Овакви позиви функције из друге функције могу ићи у дубину колико год нам је потребно. Важно је једино да да свака функција буде дефинисана пре него што је позовемо на извршење.

Сада, када имамо на располагању ове две функције, решавање полазног задатка је врло лако:

.. karel:: Karel_functions__displace_balls
    :blockly:

    {
        setup:function() {
            function random(n) {
                return Math.floor(n * Math.random());
        }
         
        var ww = [
            [
               '███████████',
               '█E.0.4.0.6█',
               '███████████'
            ],
            [
               '█████████████',
               '█E.1.3.0.4.0█',
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
                  world.setRobotStartDirection(c);
               }
               let d = w[wy].charCodeAt(wx);
               if (d >= 48 && d < 58) world.putBalls(x, y, d - 48);
            }
         }
         
            var robot = new Robot();
         
            var code = ["from karel import *",
                     "# umesto reci 'pass', kopirajte tela funkcija 'idi' i 'premesti'",
                     "",
                     "def idi(n):",
                     "    pass",
                     "",
                     "def premesti(br_loptica, br_polja):",
                     "    pass",
                     "",
                     "idi(2) # na polje 3",
                     "premesti(3, 1) # premesti 3 loptice jedno polje napred",
                     "idi(1) # na polje 5",
                     "premesti(4, -4) # premesti 4 loptice 4 polja nazad",
                     ""];
                     
            return {robot:robot, world:world, code:code};
        },
      
        isSuccess: function(robot, world) {
            var X = world.getAvenues();
            if (X == 5) {var tagret_layout = [4,0,1,3,2]}
            if (X == 6) {var tagret_layout = [4,1,0,3,0,0]}
           
            for (let x = 1; x <= X; x++)
                if (world.getBalls(x, 1) != tagret_layout[x-1]) return false;
           
            if (robot.getBalls() > 0)
                return false;
                 
            return true;
        }
    }

Задаци за вежбу
---------------

Узми задати број лоптица
''''''''''''''''''''''''

.. questionnote::
    Написати функцију *uzmi_do(n)*, којом Карел са поља на коме се налази узима највише *n* лоптица. Прецизније, ако је на пољу *n* или више лоптица, Карел их узима *n*, а ако има мање лоптица, Карел узима онолико лоптица колико их има.
    
    Потребно је да Карел, који се налази на првом пољу, узме са другог поља до 4 лоптице, са трећег до 2, а са четвртог до 3 лоптице, а затим да све прикупљене лоптице донесе на прво поље. Наравно, за то треба користити функцију *uzmi_do(n)*, написану у првом делу задатка.
    
.. karel:: Karel_functions__take_balls_up_to
    :blockly:

    {
        setup:function() {
            function random(n) {
                return Math.floor(n * Math.random());
        }
         
        var ww = [
            [
               '███████████',
               '█E.3.4.1.2█',
               '███████████'
            ],
            [
               '█████████',
               '█E.2.5.3█',
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
                  world.setRobotStartDirection(c);
               }
               let d = w[wy].charCodeAt(wx);
               if (d >= 48 && d < 58) world.putBalls(x, y, d - 48);
            }
         }
         
            var robot = new Robot();
         
            var code = ["from karel import *",
                     "def uzmi_do(n):",
                     "    pass # napisite funkciju",
                     "",
                     "napred(); uzmi_do(4)",
                     "# dovrsite uzimanje loptica",
                     "",
                     "levo(); levo() # vrati se",
                     "# dovrsite povratak i ostavljanje loptica",
                     ""];
                     
            // from karel import *
            // def uzmi_do(n):
            //     for i in range(n):
            //         if ima_loptica_na_polju():
            //             uzmi()
            // 
            // napred(); uzmi_do(4)
            // napred(); uzmi_do(2)
            // napred(); uzmi_do(3)
            //
            // levo(); levo()
            // napred();napred();napred()
            // while ima_loptica_kod_sebe():
            //     ostavi()
                     
            return {robot:robot, world:world, code:code};
        },
      
        isSuccess: function(robot, world) {
            var X = world.getAvenues();
            if (X == 5) {var tagret_layout = [6,0,2,0,2]} // = 0,3,4,1,2 - *,4,2,3
            if (X == 4) {var tagret_layout = [7,0,3,0]}   // = 0,2,5,3   - *,4,2,3
           
            for (let x = 1; x <= X; x++)
                if (world.getBalls(x, 1) != tagret_layout[x-1]) return false;
           
            if (robot.getBalls() > 0)
                return false;
                 
            return true;
        }
    }
    

Вожња по упутствима
'''''''''''''''''''

.. questionnote::
    Дате су функције *na_raskrsnici_nalevo()* и *skreni_levo(n)*. 
    
    - Функција *na_raskrsnici_nalevo()* поставља Карела да гледа у прву улицу са леве стране на коју наиђе. При извршавању ове функције, Карел иде напред док не дође до поља на коме може да иде лево, и остаје на том пољу окренут на лево. Ако пре позива функције са Карелове леве сране постоји поље, он се током рада ове функције неће ни померати са свог поља, него ће се само окренути на лево;
    - Функција *skreni_levo(n)* уводи Карела једно поље у *n*-ту улицу са леве стране. Ако је Карел већ у раскрсници, улица лево од њега се броји као прва;
    
    Написати функције *na_raskrsnici_nadesno()* и *skreni_desno(n)* по угледу на дате. 
    
    Написати програм који (помоћу датих и написаних функција) води Карела у трећу улицу лево, затим другу десно, и на крају другу лево. Карел треба да дође до краја те улице и да узме једину лоптицу на табели.

.. karel:: Karel_functions__travel_instructions_1
   :blockly:

   {
      setup:function() {
         function random(n) {
            return Math.floor(n * Math.random());
         }
         
         var ww = [
            [
               '█████████████',
               '█0.0.0█0█1█0█',
               '█████.█.█.█.█',
               '█0.0█0.0.0.0█',
               '███.█.███████',
               '█0█0█0.0.0.0█',
               '█.█.█.█████.█',
               '█E.0.0.0.0.0█',
               '█████████████'
            ],
            [
               '███████████████',
               '█0.0.0.0.0.0█1█',
               '███████.█████.█',
               '█0.0.0.0.0.0█0█',
               '███████.███.█.█',
               '█0.0█0.0.0.0.0█',
               '███.███.███████',
               '█0█0█0.0.0.0█0█',
               '█.█.███.█████.█',
               '█E.0.0.0.0.0.0█',
               '███████████████'
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
                     "def na_raskrsnici_nalevo():",
                     "    levo()",
                     "    while not moze_napred():",
                     "        desno()",
                     "        napred()",
                     "        levo()",
                     "    ",
                     "def skreni_levo(n):",
                     "    for i in range(n-1):",
                     "        na_raskrsnici_nalevo()",
                     "        desno()",
                     "        napred()",
                     "    na_raskrsnici_nalevo()",
                     "    napred()",
                     "",
                     "def na_raskrsnici_nadesno():",
                     "    # ...",
                     "    ",
                     "def skreni_desno(n):",
                     "    # ...",
                     "",
                     
                     "skreni_levo(3) # treca levo",
                     "# druga desno",
                     "# druga levo",
                     "# idi do kraja ulice",
                     "# uzmi lopticu",
                     ""];
                     
         //var code = ["from karel import *",
         //            "def na_raskrsnici_nalevo():",
         //            "    levo()",
         //            "    while not moze_napred():",
         //            "        desno()",
         //            "        napred()",
         //            "        levo()",
         //            "    ",
         //            "def skreni_levo(n):",
         //            "    for i in range(n-1):",
         //            "        na_raskrsnici_nalevo()",
         //            "        desno()",
         //            "        napred()",
         //            "    na_raskrsnici_nalevo()",
         //            "    napred()",
         //            "",
         //            "def na_raskrsnici_nadesno():",
         //            "    desno()",
         //            "    while not moze_napred():",
         //            "        levo()",
         //            "        napred()",
         //            "        desno()",
         //            "    ",
         //            "def skreni_desno(n):",
         //            "    for i in range(n-1):",
         //            "        na_raskrsnici_nadesno()",
         //            "        levo()",
         //            "        napred()",
         //            "    na_raskrsnici_nadesno()",
         //            "    napred()",
         //            "",
         //            
         //            "skreni_levo(3)",
         //            "skreni_desno(2)",
         //            "skreni_levo(2)",
         //            "while moze_napred():",
         //            "    napred()",
         //            "if ima_loptica_na_polju():",
         //            "    uzmi()",
         //            ""];
                     
         return {robot:robot, world:world, code:code};
      },
      
      isSuccess: function(robot, world) {
         return robot.getBalls() > 0;
      }
   }
