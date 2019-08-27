Additional instructions to a function
=====================================

We mentioned that there are several ways to write functions in Python, and that the functions we have written and used so far have the simplest form. Such functions are, for example, *move()*, *turn_left()*, *turn_right()*, *pick_ball()* and *drop_ball()* from the Karel Library, as well as the functions *back()*, *take_at_neighboring_square()* and *go_to_neighboring_nonempty_square()*, which we wrote ourselves. All these functions perform a specific job, always in the same way.

Functions can be written so that in different executions they do not always do the exact same thing, but they perform a little more general task. When we call such functions, we tell them exactly how we want them to do their task. For example, a function that would move Karel for a certain number of squares forward or backward could often be very useful. For this function, we want to specify the request when calling it - how many squares Karel should move and on which side.

Functions with parameters
-------------------------

.. infonote::
    Additional information that we give to a function is written between the brackets after the function name in the first row of its definition. Between brackets we can specify one value, or multiple values separated by commas. These values are called **arguments** or **parameters** to a function. The words "arguments" and "parameters" are synonyms in programming and we will use them equally.
    
.. activecode:: Karel_functions__function_with_args_def
    :passivecode: true

    def function_name(parameter1, ... parameterN):
        statement_1
        ...
        statement_k

The function that moves Karel certain number of squares forward or backward, could be named *go* and it could have one integer parameter. If this parameter is positive, Karel would move that many squares forward, and if it is negative, Karel would go a corresponding (opposite) number of squares back. For example, the call *go(5)* would mean "go 5 squares forward", while *go(-2)* would mean "go 2 squares back". Here's how we can write such a function:

.. activecode:: Karel_functions__function_go_def
    :passivecode: true

    def go(n):
        if n > 0:
            for i in range(n):
                move()
        else:
            turn_left();turn_left()
            for i in range(-n):
                move()
            turn_left();turn_left()
 
This function can simplify many programs that are supposed to tell Karel to move several times along one path in both directions. Here is an example.

Perform specified displacements
'''''''''''''''''''''''''''''''

.. questionnote::

    Karel is located on the starting square of a path of a sufficient length, and should carry out the following displacements of balls:

    - 3 balls from the square 3 to the square 4
    - 4 balls from the square 5 to the square 1

In solving this task we will use the described function *go*. In order to further simplify the solution, we can also introduce the *displace* function, which displaces the specified number of balls for a specified number of squares forward or backward. This description shows that the *displace* function should have two arguments.

In order to make the purpose of each parameter clearer, we will give them names that describe their role:

.. activecode:: Karel_functions__function_displace_def
    :passivecode: true

    def displace(num_balls, num_squares):
        for i in range(num_balls):
            pick_ball()
        go(num_squares)
        for i in range(num_balls):
            drop_ball()

The *displace* function uses the previously written function *go*. Calling a function from another function like this can go in depth as far as we need. It is only important that each function is defined before it is called for execution.

Now that we have these two functions available, solving the starting task is very easy:

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
                     "# replace each word 'pass' with an appropriate function body",
                     "",
                     "def go(n):",
                     "    pass",
                     "",
                     "def displace(num_balls, num_squares):",
                     "    pass",
                     "",
                     "go(2) # to square 3",
                     "displace(3, 1) # displace 3 balls one square forward",
                     "go(1) # to the square 5",
                     "displace(4, -4) # displace 4 balls 4 squares back",
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

Tasks for exercise
------------------

Take a given number of balls
''''''''''''''''''''''''''''

.. questionnote::
    Write the function *take_up_to(n)*, which tells Karel to take the maximum of *n* balls from the square which he stands on. More precisely, if there are *n* or more balls at the square, Karel takes *n* of them, and if there are fewer balls, Karel takes as many as he can.
    
    Karel, who is on the first square, should take up to 4 balls from the second square, then up to 2 balls from the third square, and up to 3 balls from the fourth square, and then bring all the collected balls to the first square. Of course, the *take_up_to(n)* function, written in the first part of the task, should be used for this purpose.

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
                     "def take_up_to(n):",
                     "    pass # write the function",
                     "",
                     "move(); take_up_to(4)",
                     "# complete collecting the balls as specified",
                     "",
                     "turn_left(); turn_left() # come back",
                     "# complete Karel's return to the starting square and the dropping of the balls",
                     ""];
                     
            // from karel import *
            // def take_up_to(n):
            //     for i in range(n):
            //         if is_ball_on_square():
            //             pick_ball()
            // 
            // move(); take_up_to(4)
            // move(); take_up_to(2)
            // move(); take_up_to(3)
            //
            // turn_left(); turn_left()
            // move();move();move()
            // while any_balls_with_karel():
            //     drop_ball()
                     
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
    

Driving according to instructions
'''''''''''''''''''''''''''''''''

.. questionnote::
    The functions *face_left_at_intersection()* and *go_left(n)* are given.
    
    - Function *face_left_at_intersection()* positions Karel to face the first street he comes across on the left side. In the execution of this function, Karel goes forward until he encounters a square where he can go left, but he does not actually go left, he remains on the crossroad instead, turned to the left. If Karel can go left before the function call, he will not move from its square during the execution of this function, but will only turn to the left;
    - The function *go_left(n)* moves Karel one square to the *n*-th street on the left. If Karel is already in the crossroads, the street to the left of him is counted as the first;
        
    Write similar functions *face_left_at_intersection()* and *go_right(n)* using given functions as a model.
    
    Write a program that (using given and written functions) leads Karel to the third street to the left, then the second to the right, and at the end, the second to the left. Karel should reach the end of that street and take the only ball on the table.

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
                     "def face_left_at_intersection():",
                     "    turn_left()",
                     "    while not front_is_clear():",
                     "        turn_right()",
                     "        move()",
                     "        turn_left()",
                     "    ",
                     "def go_left(n):",
                     "    for i in range(n-1):",
                     "        face_left_at_intersection()",
                     "        turn_right()",
                     "        move()",
                     "    face_left_at_intersection()",
                     "    move()",
                     "",
                     "def face_right_at_intersection():",
                     "    # ...",
                     "    ",
                     "def go_right(n):",
                     "    # ...",
                     "",
                     
                     "go_left(3) # third street to the left",
                     "# second to the right",
                     "# second to the left",
                     "# go until end of the street",
                     "# take the ball",
                     ""];
                     
         //var code = ["from karel import *",
         //            "def face_left_at_intersection():",
         //            "    turn_left()",
         //            "    while not front_is_clear():",
         //            "        turn_right()",
         //            "        move()",
         //            "        turn_left()",
         //            "    ",
         //            "def go_left(n):",
         //            "    for i in range(n-1):",
         //            "        face_left_at_intersection()",
         //            "        turn_right()",
         //            "        move()",
         //            "    face_left_at_intersection()",
         //            "    move()",
         //            "",
         //            "def face_right_at_intersection():",
         //            "    turn_right()",
         //            "    while not front_is_clear():",
         //            "        turn_left()",
         //            "        move()",
         //            "        turn_right()",
         //            "    ",
         //            "def go_right(n):",
         //            "    for i in range(n-1):",
         //            "        face_right_at_intersection()",
         //            "        turn_left()",
         //            "        move()",
         //            "    face_right_at_intersection()",
         //            "    move()",
         //            "",
         //            
         //            "go_left(3)",
         //            "go_right(2)",
         //            "go_left(2)",
         //            "while front_is_clear():",
         //            "    move()",
         //            "if is_ball_on_square():",
         //            "    pick_ball()",
         //            ""];
                     
         return {robot:robot, world:world, code:code};
      },
      
      isSuccess: function(robot, world) {
         return robot.getBalls() > 0;
      }
   }
