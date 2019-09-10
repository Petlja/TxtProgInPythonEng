Managing Karel
==============

To see what programming looks like, we will introduce you to Karel. Karel is an animated robot that moves along a maze-like table by following our instructions in the form of a program. Through managing Karel, we will adopt a logic that is very important for writing any program, and we can also have some fun along the way.

.. infonote::

    The idea of learning programming through controlling a robot dates back to the 1970s, when Richard E. Pattis, as a graduate student at Stanford University, created the first such environment with a programming language specially designed for this purpose. The language, like the robot, was named Karel, after Karel Čapek, the Czech writer who first started using the word robot. Patis's book *Karel The Robot: A Gentle Introduction to the Art of Programming* was published in 1981 and quickly became the best-selling introductory book in programming courses.
    
To manage Karel we can use these functions:

- ``move()`` - move one square forward,
- ``turn_left()`` - turn 90 degrees to the left (counterclockwise),
- ``turn_right()`` - turn 90 degrees to the right (clockwise),
- ``pick_ball()`` - pick up a ball from the square you are located on,
- ``drop_ball()`` - drop a ball on the square you are located on.

By using these five functions, we state what we want Karel to do, so we will call them "commands for Karel", or "statements". Karel understands five more different functions, which we will see soon. In addition to these commands directly addressed to Karel, we can also use all the commands of the Python programming language, which we will learn during the course.

Let's look at the examples of how the above-mentioned commands can be used to guide Karel through his world:

Examples
--------

Move one square forward and take the ball
'''''''''''''''''''''''''''''''''''''''''

.. questionnote::

    Write a program to move Karel to the field (2, 1) and make him pick up the ball.

This program consists of only two commands. The first one tells Karel to move one field forward, and the other one to take the ball.
   
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
                    "move()",
                    "pick_ball()"];
            return {robot:robot, world:world, code:code};
        },
    
        isSuccess: function(robot, world) {
           return robot.getBalls() === 1;
        },
   }

**Including** *karel* **library**
'''''''''''''''''''''''''''''''''

.. infonote::

    The functions we use to manage Karel are defined in the library *karel*. Therefore, at the beginning of each program, we should tell the computer (more precisely, the program that executes our program) to first attach the definitions of these functions for managing Karel. This is achieved by the first line of the program: ``from karel import *``. Every program dealing with Karel that we write should start this way.
   
    Keep in mind that *karel* library can only be used in this environment for now. You can run your other programs in other ways, but we will remind you of that when the time is right.

There may be more than one ball on one square, and our task may be to tell Karel to take several, or all of them.

Move one square forward and take three balls
''''''''''''''''''''''''''''''''''''''''''''

.. questionnote::

    Write a program that tells Karel to move to the square (2, 1) and pick up three of the five balls that are there.
    
In this program, after the command ``move()``, the command ``pick_ball()`` should be written three times, since we need Karel to pick up three balls. Pay attention to the number that appears on the ball. It shows how many balls there are on that square. In addition to that, the number to the left of Karel's head (which you might have noticed in the previous example as well) tells how many balls Karel has with him.
   
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
                    "move()",
                    "pick_ball()",
                    "pick_ball()",
                    "pick_ball()"];
            return {robot:robot, world:world, code:code};
        },
    
        isSuccess: function(robot, world) {
           return robot.getBalls() === 3;
        },
   }
   

Next task is similar, but somewhat more difficult.
   
Get to the ball and take it
'''''''''''''''''''''''''''

.. questionnote::

   Write a program that tells Karel to come to the field (4, 1) and pick up the ball.

The task does not essentially differ from the previous one. It is still necessary to bring Karel to the target square and tell him to take the ball. The difference is that now the path to the target square is longer, and so is our program:

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
                    "move()       # go to (2, 1)",
                    "move()       # go to (3, 1)",
                    "turn_left()  # turn north (^)",
                    "move()       # go to (3, 2)",
                    "move()       # go to (3, 3)",
                    "turn_right() # turn east (>)",
                    "move()       # go to (4, 3)",
                    "move()       # go to (5, 3)",
                    "turn_right() # turn south (v)",
                    "move()       # go to (5, 2)",
                    "move()       # go to (5, 1)",
                    "turn_right() # turn west (<)",
                    "move()       # go to (4, 1)",
                    "pick_ball()  # take the ball at (4, 1)"];
            return {robot:robot, world:world, code:code};
        },
    
        isSuccess: function(robot, world) {
           return robot.getBalls() === 1;
        },
   }

Reading this program, it's becoming hard to follow which command brings Karel to which square. This is not the case just with beginners, it's difficult for anyone because every ``move()`` statement looks the same. To help both ourselves and yourself, after each command we have added the # sign and some text that helps us to follow where we have brought Karel.

**Comments**
''''''''''''

.. infonote::

    Part of any Python program from the ``#`` character to the end of the line is called a ``comment``. Comments do not affect the execution of the program, the program does the same thing with or without them. Comments are intended only for people who read and write programs, to help them better understand these programs and to handle them more easily.
    
    When thinking about writing comments in our programs, we should write them for both ourselves and other people who will read our programs. On the other hand, the comments that other people write in their programs will help us understand their programs.
    
    There are no precise rules for writing comments. In your comments, you should write down whatever you believe helps others (and yourself) better understand your program.
   
Pick up all the balls
'''''''''''''''''''''

In this example, the balls are on different squares and we need to bring Karel to each of these balls.

.. questionnote::

   Write a program to tell Karel to pick up all four balls.

We can choose the path for Karel in many ways, but the shorter the path we choose, the shorter (and faster) our program will be. So, for instance, we could first take the ball at square (5, 2), then the two balls at (5, 5) and finally the ball at (4, 4).

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
                    "move(); move(); turn_left()  # go to square (3, 1) and turn north",
                    "move(); move(); turn_right() # go to square (3, 3) and turn east",
                    "move(); move(); turn_right() # go to square (5, 3) and turn south",
                    "move(); pick_ball()          # come to square (5, 2) and take the ball",
                    "turn_left(); turn_left()     # turn north",
                    "move(); move(); move()       # come to square (5, 5)",
                    "pick_ball(); pick_ball()     # take two balls",
                    "turn_left(); move();         # go to square (4, 5)",
                    "turn_left(); move();         # go to square (4, 4)",
                    "pick_ball()                  # take the last ball at (4, 4)"];
            return {robot:robot, world:world, code:code};
        },
    
        isSuccess: function(robot, world) {
           return robot.getBalls() === 4;
        },
   }

**Grouping commands**
'''''''''''''''''''''

Since this program is even longer than the previous one, in order to make it easier to navigate in the program and track the Karel's position, we made groups of commands that make up one stage of the journey and put each group into one line of the program. At the end of each line, there is a comment that explains the group of commands in that line.

Note that, when writing a program this way, the ``;`` character must be written between the commands (after the last command in line, semicolon is not needed).

Commands can be grouped differently, for example by separating a group of commands (written one below the other) from the next group with an empty line. This way of grouping is used much more commonly, since commands are usually not as short as these for managing Karel. Here's how it would look:

.. code::

    from karel import *
    
    # go to square (3, 1) and turn north"
    move()
    move()
    turn_left()
    
    # go to square (3, 3) and turn east
    move()
    move()
    turn_right()
    
    # go to square (5, 3) and turn south
    move()
    move()
    turn_right()
    
    # come to square (5, 2) and take the ball
    move()
    pick_ball()
    
    # turn north
    turn_left()
    turn_left()
    
    # come to square (5, 5)
    move()
    move()
    move()
    
    # take two balls
    pick_ball()
    pick_ball()
    
    # go to square (4, 4)
    turn_left()
    move()
    turn_left()
    move()
    
    # take the last ball at (4, 4)
    pick_ball()
    
~~~~

Karel can also drop balls at squares. Here's how he does it.

Move the ball
'''''''''''''

.. questionnote::

   Write a program which makes Karel move the ball to the square (2, 2) (note that at the beginning Karel **is not** oriented properly).
   

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
                    "turn_left(); move(); pick_ball();  # take the ball at (2, 1)",
                    "turn_right(); turn_right(); move() # go back to (1, 1)",
                    "turn_right(); move()               # go to (1, 2)",
                    "turn_right(); move()               # go to (2, 2)",
                    "drop_ball()                        # place the ball at (2, 2)"];
            return {robot:robot, world:world, code:code};
        },
    
        isSuccess: function(robot, world) {
           return world.getBalls(2, 2) === 1;
        },
   }

**Errors in execution**
'''''''''''''''''''''''

.. infonote::

    Please note that **Karel can not execute any command at any time**. More specifically, Karel can not go forward if he is in front of a wall, he can not take a ball where there isn't one, and he can not drop a ball if he has no balls with him.
    
    Try deleting the first command ``turn_left()`` in the previous program, and then run the program to see what happens.
    
    When the program executing our program comes to a command that can not be executed, the execution of our program is interrupted and we receive an error message. Such messages are normal and we will see them whenever Karel is unable to do what we told him, or when our statement is unclear (more precisely, when it is not written properly). In such situations, we should try to understand what the problem is, to fix the program and restart it.
    
Below are some tasks for independent work. With each task, a solution is offered, which you can see by clicking on the "solution" button. You can copy the displayed solution to the area for your work and try it by running the program. Note that your solution may differ from ours and still be quite ok.

Tasks for exercise
------------------

Come to square (3, 3)
'''''''''''''''''''''

.. questionnote::

   In this task there are no balls, you only need to bring Karel to the square (3, 3).
   
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
                    "# Add missing commands"];
            return {robot:robot, world:world, code:code};
        },
    
        isSuccess: function(robot, world) {
           return robot.getStreet() === 3 &&
           robot.getAvenue() === 3;
        },
   }
   
.. reveal:: Karel_intro_task_go_to_3_3_reveal
   :showtitle: Solution
   :hidetitle: Hide solution

   .. activecode:: Karel_intro_task_go_to_3_3_solution
      :passivecode: true
      
      from karel import *
      move(); move()               # to square (1, 3)
      turn_right(); move()         # to square (2, 3)
      turn_right(); move(); move() # to square (2, 1)
      turn_left(); move()          # to square (3, 1)
      turn_left(); move(); move()  # to square (3, 3)

Pick up the balls
'''''''''''''''''

.. questionnote::

   Write a program based on which Karel will pick up the balls.
   
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
                    "# Add missing commands",
                    "pick_ball()"];
            return {robot:robot, world:world, code:code};
        },
    
        isSuccess: function(robot, world) {
           return robot.getBalls() === 3;
        },
   }
   
.. reveal:: Karel_intro_task_collect_balls_in_2x2_reveal
   :showtitle: Solution
   :hidetitle: Hide solution
  
   .. activecode:: Karel_intro_task_collect_balls_in_2x2_solution
      :passivecode: true
       
      from karel import *
      move(); pick_ball()                 # take the ball at square (2, 1)
      turn_right(); turn_right(); move()  # go back to square (1, 1)
      turn_right(); move(); pick_ball()   # pick the ball at square (1, 2)
      turn_right(); move(); pick_ball()   # pick the ball at square (2, 2)

Zig-zag
'''''''

.. questionnote::

  Karel should reach the square (5, 1).

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
                     "# Add missing commands ",
                     ""];
    
         return {robot:robot, world:world, code:code};
      },
    
      isSuccess: function(robot, world) {
         return robot.getAvenue() == world.getAvenues() &&
            robot.getStreet() == 1;
      },
   }

.. reveal:: Karel_intro_task_stairs_fixed_reveal
   :showtitle: Solution
   :hidetitle: Hide solution

   .. activecode:: Karel_intro_task_stairs_fixed_solution
      :passivecode: true
      
      from karel import *
      turn_left(); move()     # to (1, 2)
      turn_right(); move()    # to (2, 2)
      turn_left(); move()     # to (2, 3)
      turn_right(); move()    # to (3, 3)
      turn_right(); move()    # to (3, 2)
      turn_left(); move()     # to (4, 2)
      turn_right(); move()    # to (4, 1)
      turn_left(); move()     # to (5, 1)


Forward, then left, then again
''''''''''''''''''''''''''''''

.. questionnote::

  Karel should get to the square (2, 3).
   

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
                     "# Add missing commands",
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
   :showtitle: Solution
   :hidetitle: Hide solution

   .. activecode:: Karel_intro_task_spiral_left_fixed_solution
      :passivecode: true
      
      from karel import *
      move(); move(); move(); turn_left() # to (4, 1)
      move(); move(); move(); turn_left() # to (4, 4)
      move(); move(); move(); turn_left() # to (1, 4)
      move(); move(); turn_left()         # to (1, 2)
      move(); move(); turn_left()         # to (3, 2)
      move(); turn_left()                 # to (3, 3)
      move();                             # to (2, 3)
