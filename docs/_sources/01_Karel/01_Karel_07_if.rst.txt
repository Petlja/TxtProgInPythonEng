Check out and decide
====================

The *while* statement proved very useful, because by using it we were able to solve more diversified tasks. However, the following example shows that there are simple tasks that we can not solve with what we have learned so far.

Let's say that in some situation you need to move Karel only for one square if possible (if not possible, Karel should remain where he is).

- If we only write the *move()* command, we are risking an error message in case that Karel is in front of the wall.
- If we place the *move()* command below the *while front_is_clear():* statement, we risk Karel going further than we wanted.
- If we do not use the command *move()*, we risk not moving even if it is possible (and necessary).

Obviously, we need a new statement, which will tell Karel "if you can go forward, move one place".

*If* statement
--------------

The statement we need in the described case is the ``if`` statement, which also exists in almost all programming languages. In Python, it (in its simpler form) is written like this:

.. activecode:: Karel_if__syntax
   :passivecode: true

   if condition:
       statement_1
       ...
       statement_k


.. infonote::

   We see that writing the ``if`` statement is very similar to writing a *while* statement. Under the ``if`` statement we can also place one or more other statements, which constitute the **body of the if statement**. Same rules apply for writing a colon ``:`` after the condition and for indenting statements that are executed if the condition is met. The difference is that the statements in the body of an *if* statement will not be repeated - if the condition is fulfilled, they will only be done once.

   The ``if`` statement is sometimes called the *branching statement* because the program execution flow branches at this stement: the next statement to be executed depends on the answer to the question from the condition.

In the above example, we should write:

.. activecode:: Karel_if__example
   :passivecode: true

   if front_is_clear():
       move()


Let's see some tasks in which (besides already known statements) the ``if`` statement is used.

Take one ball, if there are any
'''''''''''''''''''''''''''''''

.. questionnote::

   There is one square in front of Karel, with zero or more balls. Write a program that tells Karel to move onto that square, and then take exactly one ball if there is at least one ball in the field.
   
   Run the program several times to test it on different examples.

In our case, the condition will be ``is_ball_on_square()``, and the command that is conditionally executed is ``pick_ball()``.

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
                  "move()",
                  "if ...         # complete the statement",
                  "    pick_ball()",
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
       :showtitle: Solution
       :hidetitle: Hide solution
       
       Solution:
   
       .. activecode:: Karel_if__take_one_if_any_solution
           :passivecode: true
         
           from karel import *
           move()
           if is_ball_on_square():
               pick_ball()


Go to the end of path and pick one ball where possible
''''''''''''''''''''''''''''''''''''''''''''''''''''''

.. questionnote::

  There is at least one square in front of Karel, and there can be any number of them. Each square has zero or more balls. Karel should pick up exactly one ball from each square on which there is a ball.
  
  Run the program several times to test it on different examples.

Here it is necessary to use *while* statement for advancing forward, and in the body of the *while* loop, after every step forward, an *if* statement should be used to check whether Karel stands on a square with a ball on it or not.

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
                     "while front_is_clear():",
                     "    move()",
                     "    if ... # add the condition",
                     "       ... # add the conditional statement",
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
       :showtitle: Solution
       :hidetitle: Hide solution
       
       Solution:
   
       .. activecode:: Karel_if__many_squares_take_one_if_any_solution
           :passivecode: true
         
           from karel import *
           while front_is_clear():
               move()
               if is_ball_on_square():
                   pick_ball()


If you don't do that, do this (if-else)
---------------------------------------

In some tasks, one thing needs to be done if a certain condition is met, and some other thing if it is not met. In such case, we can use the extended form of an *if* statement, which looks like this:

.. activecode:: Karel_if__else_syntax
    :passivecode: true

    if condition:
        statement_a1
        ...
        statement_ak
    else:
        statement_b1
        ...
        statement_bm


.. infonote::

   In the extended form of the ``if`` statement, the first part (up to the word `else`) has the same look and meaning as before. Below that part, the word ``else`` is written, equally indented as the word `if``, followed by a colon ``:``. In the following lines we write one or more other statements, which constitute the **body of else branch**. This second group of statements is indented one level deaper than the word *else* above, and is executed if the condition specified in the `` if`` statement is not met.

Example - taking and dropping balls
'''''''''''''''''''''''''''''''''''

.. questionnote::

   There are 3 squares in front of Karel, and on each of them there can be either one ball or no balls. Karel should take balls from the squares that have balls on them and place one ball on each square that was initially empty. Karel has enough balls with him at start.

Using the new, expanded form of the ``if`` statement, we can tell Karel: "If there is a ball on the square, then take that ball, otherwise drop one ball", so that the task can be easily solved:

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
        "    move()",
        "    if is_ball_on_square():",
        "        pick_ball()",
        "    else:",
        "        drop_ball()"
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


Pick up the balls that you can reach
''''''''''''''''''''''''''''''''''''


.. questionnote::

   A labyrinth consists of two rows. Karel is in the upper row, which is completely empty and passable. In the lower row there may be obstacles, or squares with one ball. Karel's task is to pick up all the balls.
   
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
            "while front_is_clear():",
            "    move() # next square in upper row",
            "",
            "    # check the lower row",
            "    turn_right()           # southwards",
            "    if front_is_clear():   # if there is a square in the lower row",
            "        # tell Karel to go get the ball, ",
            "        # to come back to the upper row and turn east",
            "    # tell Karel, if he could not go to the lower row,",
            "    # to turn back to east, to be able to continue properly",
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
       :showtitle: Show solution
       :hidetitle: Hide solution
   
       One possible solution (not the only one) is the following:
   
       .. activecode:: Karel_if__take_all_from_lower_row_solution
           :passivecode: true
                       
           from karel import *
           while front_is_clear():
               move() # next square
               
               # check the lower row
               turn_right()  # southwards
               if front_is_clear(): # if there is a square in the lower row
                   move(); pick_ball() # go get the ball
                   
                   # go back to the upper row, and turn east
                   turn_left(); turn_left()
                   move(); turn_right() 
               else:
                   turn_left() # just turn back east


Act only when something is not met
----------------------------------

Let's say that Karel needs to turn left if he **can not** go forward (if he can go forward, he should not do anything).

According to the rules of writing an *if* statement, after the condition (in the body of the first branch) there must be at least one statement, and according to the logic of the task, we do not need any statements at that place. In such situations we can write:

.. activecode:: Karel_if__else_only
    :passivecode: true

    if front_is_clear():
        pass
    else:
        turn_left()

or

.. activecode:: Karel_if__not
    :passivecode: true

    if not front_is_clear():
        turn_left()

In the first case, we use special ``pass`` statement that does nothing. By doing so, we both satisfy the syntax (writing rules), and we get a program that works the way we want.

In the second case, by using the word ``not``, we make the opposite condition, which means that the condition of the *if* statement is satisfied when Karel can not go forward. In this case, branches change roles, so the *else* branch becomes the one that is no longer needed.

In the few upcoming tasks, there is something to be done only when the condition is not met.

Turn to an empty field
'''''''''''''''''''''''


.. questionnote::

   Initially, Karel can face either side, but he can start moving only in one direction. Karel needs to turn to the free square and make one step.
   
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
                     "# write the program",
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
    :showtitle: Solution
    :hidetitle: Hide solution

    We offer you two short solutions:
   
    .. activecode:: Karel_if__turn_to_free_square_solution1
        :passivecode: true
      
        from karel import *
        while not front_is_clear():
            turn_left()
        move()

    .. activecode:: Karel_if__turn_to_free_square_solution2
        :passivecode: true
      
        from karel import *
        for i in range(3):
            if not front_is_clear():
                turn_left()
        move()
                
Where there are no balls, add them
''''''''''''''''''''''''''''''''''

.. questionnote::

   There is an unknown number of squares in front of Karel, and, each of them can contain one ball or no balls. Karel has enough balls with him, and he needs to put one ball on an each emtpy sqare.
   
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
                        "# write the program"
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
