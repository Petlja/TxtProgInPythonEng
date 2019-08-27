Create a batch of statements
============================

Let's recall the task *Take the ball on the neighboring square*. The task was that in every direction, Karel needed to try to go to the neighboring square and (if he could go to the neighboring square) to try and get the ball there. In order to make trying the next direction easier, we chose to return Karel to the starting square after each attempt.

One program that solves that task is:

.. activecode:: Karel_functions__take_neighboring_ball_1
    :passivecode: true

    from karel import *
    for i in range(4):   # in each of the 4 directions
        if front_is_clear(): # search the square in that direction
            move()
            if is_ball_on_square():
                pick_ball()
            turn_left()          # come back to the starting square
            turn_left()
            move()
            turn_left()          # turn towards the square you just tried
            turn_left()
        turn_left()          # next direction

The part of the program from the seventh to the eleventh line seems a little tougher to follow. In that part, you might need to imagine Karel executing statements to fully understand what is happening there.

Comments somewhat help making this part of the program easier to understand. In addition to the comments, it would be even better if there was a function *back()*, which would move Karel a step back. Then the program would be shorter and more intelligible:

.. activecode:: Karel_functions__take_neighboring_ball_2
    :passivecode: true

    from karel import *
    for i in range(4):          # in each of the 4 directions
        if front_is_clear():       # seek a free square in that direction
            move()
            if is_ball_on_square():
                pick_ball()
            back()                     # come back to starting square
        turn_left()                # next direction
        
The function *back()* is not a part of the Karel library, but we can very easily write this function ourselves. When done, we will be able to use the function *back()* equally with the other functions of the *Karel* library, such as *move()* or *turn_right()*.

How to write functions
----------------------

For now, we will only learn the simplest way of writing a function in Python, and we will see other, more complex forms later.

.. activecode:: Karel_functions__function_def
    :passivecode: true

    def function_name():
        statement_1
        ...
        statement_k

.. infonote::
      
   When writing any function in Python, the word ``def`` at the beginning, brackets ``()`` and a colon  character ``:`` at the end of the first row are mandatory. For *function_name* we can use any correctly written name that we choose. The following statements are written indented, and they form the body of the function (if more than one command is written in a row, then these commands are separated by a semicolon ``;``). The statements in the function body will be executed each time the function name is encountered when running the program, that is, when this function is called.

In accordance to these rules, the function *back()* can be written as follows:

.. activecode:: Karel_functions__backwards_def
    :passivecode: true

    def back():
        turn_left(); turn_left()
        move()
        turn_left(); turn_left()

Then the whole program would look like this:
   
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
                     "def back():",
                     "    turn_left(); turn_left()",
                     "    move()",
                     "    turn_left(); turn_left()",
                     "",    
                     "for i in range(4):",
                     "    if front_is_clear():",
                     "        move()",
                     "        if is_ball_on_square():",
                     "            pick_ball()",
                     "        back()",
                     "    turn_left()  # next direction",
                     ""];
                     
         return {robot:robot, world:world, code:code};
      },
      
      isSuccess: function(robot, world) {
         return robot.getBalls() > 0;
      }
   }

.. infonote::
    When we extract some statements (that have a meaning as a group) into a function, we can write programs that are shorter and clearer, because we have broken down the problem into less complex parts.
    
    Another advantage of writing functions is that we can easily use them in other programs (here, we will occasionally copy previously written functions, but, in real programming, there is a better and simpler way to reuse once written functions).


Exiting the function or loop before its end
-------------------------------------------

In the task of searching for the ball on a neighboring square, for the sake of the simplicity of the program, we decided that even when Karel finds a ball, he continues to search in the remaining directions. There is a way to avoid this unnecessary execution of the remaining statements.

.. infonote::
    **When we want to interrupt a loop execution**, we write a special ``break`` statement. The effect of the *break* statement is to jump out of the loop and continue the execution of the program from the first statement after the loop.
    
    By using a *break* statement, we will jump out of the nearest (narrowest) *for* or *while* loop containing the *break* statement. If a *break* statement is located inside two or more nested loops, the execution continues with the statement that follows the innermost (narrowest) loop.
    
Using the *break* statement, we could modify the main part of the program:

.. activecode:: Karel_functions__break_intro_1
    :passivecode: true

    for i in range(4):
        if front_is_clear():
            move()
            if is_ball_on_square():
                pick_ball()
            back()
        turn_left()  # next direction

into:

.. activecode:: Karel_functions__break_intro_2
    :passivecode: true

    for i in range(4):
        if front_is_clear():
            move()
            if is_ball_on_square():
                pick_ball()
                break
            back()
        turn_left()  # next direction

This way, the loop ends as soon as the ball is found and taken. Since there are no other statements after this loop, in this case, by executing the *break* statement, the operation of the program finishes.

~~~~

Similarly to exiting the loop, we can also exit the function before all its statements are executed.

.. infonote::
    **When we want to interrupt the execution of a function**, we write a special ``return`` statement. The effect of the *return* statement is to jump out of the function and continue executing the program from the first statement after the place the function was called from.
    
    With a *return* statement we jump out of the function no matter how many loops there are around the *return* statement inside the function.

We can turn the program for taking the ball on a neighboring field into a function. In that case, we could write:

.. activecode:: Karel_functions__return_intro
    :passivecode: true

    def take_at_neighboring_square():
        for i in range(4):
            if front_is_clear():
                move()
                if is_ball_on_square():
                    pick_ball()
                    return # exit the function
                back()
            turn_left()  # next direction
            
    take_at_neighboring_square()
    
Tasks for exercise
------------------

Drop the balls while there are both balls and squares
'''''''''''''''''''''''''''''''''''''''''''''''''''''

.. questionnote::

    Initially, Karel has several balls and should arrange them along the path one at every square (starting from the square where he stands) as far as possible. Karel stops placing balls when he hits an obstacle or when he runs out of balls (whatever happens first). It does not matter if Karel will stop at the last filled square, or at the first empty square.
        
Hint: Put one of these two conditions into a *while* loop, so that the loop ends when the condition is no longer met. Additionally, use the *break* statement to exit the loop if the other condition is not met.
   
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
                        " # write the program",
                        ""];
                        
            //var code = ["from karel import *",
            //            "while any_balls_with_karel():",
            //            "    drop_ball()",
            //            "    if not front_is_clear():",
            //            "        break",
            //            "    move()",
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

Move all the balls one square backwards
'''''''''''''''''''''''''''''''''''''''

.. questionnote::

    There is a path of unknown lenght in front of Karel. There are no balls in the starting square. Karel should shift each ball one square to the west.
  
You can solve this task by repeating the following steps as long as there are squares in front of Karel:

- go to the next square
- Take all the balls from that square
- go a step back (that is, turn around and go one step ahead)
- drop all the balls
- go back to the square from which you took the balls

In doing so, you can use the previously written function *back()* to return to the square to which Karel moves the balls. You just need to copy it (or re-type it) to the area for your solution.

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
                       "# copy the function 'back()'",
                       "",
                       "while front_is_clear():  # while there are squares in fornt of Karel, repeat",
                       "    move();                  # go forward",
                       "    # complete the line      # pick up all the balls from this square",
                       "    # complete the line      # go one step back",
                       "    # complete the line      # drop all the balls",
                       "    # complete the line      # go forward once more to the emptied square",
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
    :showtitle: Solution
    :hidetitle: Hide solution

    .. activecode:: Karel_functions__all_balls_one_square_back_solution
        :passivecode: true
      
        from karel import *
        def back():      # go one step back, and maintain the same orientation
            turn_left(); turn_left();
            move(); 
            turn_left(); turn_left();

        while front_is_clear():       # while there are squares in fornt of Karel, repeat
            move();                       # go to a new square
            while is_ball_on_square():    # take all the balls from this square
                pick_ball()            
            back()                        # step back
            while any_balls_with_karel(): # drop all the balls
                drop_ball()
            move()                        # go to the emptied square


Follow the balls
''''''''''''''''

.. questionnote::

    Each square contains one ball or none. Squares with the balls on them form a path, which begins on the square next to Karel. Karel should follow this path and pick up all the balls.

Hint: To solve this task, you can write the function *go_to_neighboring_nonempty_square()*, which only needs to move Karell to the neighboring square which has a ball on it (the *return* statement can be useful there). The function *go_to_neighboring_nonempty_square()* should differ from the previously written function *take_at_neighboring_square()* only in the sense that it does not take the ball.

When Karel collects all the balls, the next call of this function will place him on an empty square (by the way, this will be the square where Karel took the last ball). When there is no ball on the square which Karel is on, this will mean that Karel has already taken all the balls.

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
                        "def back():",
                        "    turn_left(); turn_left()",
                        "    move()",
                        "    turn_left(); turn_left()",
                        "",    
                        "def go_to_neighboring_nonempty_square():", 
                        "    # write the function",
                        "",
                        "go_to_neighboring_nonempty_square()",
                        "while ??? # add the condition",
                        "    pick_ball()",
                        "    ??? # complete the program",
                        ""];
                     
            //var code = ["from karel import *",
            //            "def back():",
            //            "    turn_left(); turn_left()",
            //            "    move()",
            //            "    turn_left(); turn_left()",
            //            "",
            //            "def go_to_neighboring_nonempty_square():",
            //            "    for i in range(4):",
            //            "        if front_is_clear():",
            //            "            move()",
            //            "            if is_ball_on_square():",
            //            "                return",
            //            "            back()",
            //            "        turn_left()  # next direction",
            //            "",
            //            "go_to_neighboring_nonempty_square()",
            //            "while is_ball_on_square():",
            //            "    pick_ball()",
            //            "    go_to_neighboring_nonempty_square()",
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

Take all the balls from the whole table
'''''''''''''''''''''''''''''''''''''''

.. questionnote::

  Karel is initially facing north (up), and he is located in the lower left corner of a rectangular table of unknown size, with no interior walls. There can be any number of balls on each square. Karel should take all the balls from all the squares on the board.
  
Hint: Write a function *empty_one_row()*, which makes Karel:

- turn left (to the east), looking along the row he is in
- pass through the entire row and take all the balls from each square in that row, **including the square he started on**
- turn to the beginning of the row (i.e. to the west)
- return to the beginning of the row and turn north (up), as he stood before the function call

The program that solves the task using this function is not long. It needs to do the following:

- empty the first row
- while there are rows in front of Karel, go to the next one and empty it

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
                     "# write the program",
                     ""];
        //var code = ["from karel import *
        //            "def empty_one_row():",
        //            "    turn_right()                # turn towards end of the row (eastwards)",
        //            "    while is_ball_on_square():  # empty first square in the row",
        //            "        pick_ball()",
        //            "    while front_is_clear():     # while there are unvisited squares",
        //            "        move()                      # go to a new square",
        //            "        while is_ball_on_square():  # emtpy the new square",
        //            "            pick_ball()",
        //            "        ",
        //            "    turn_right(); turn_right()  # turn towards beginning of the row (westwards)",
        //            "    while front_is_clear():     # come back to the first square in that row",
        //            "        move()",
        //            "    turn_right()                # turn towards next row (northwards)",
        //            "",
        //            "empty_one_row()             # pick up the balls from the first row",
        //            "while front_is_clear():     # while there are new rows",
        //            "    move(); empty_one_row()     # go to the next row and empty it",
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
