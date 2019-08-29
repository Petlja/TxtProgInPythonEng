Combining loops
===============

We've seen that in the body of a *for* statement, we can place several different statements. Similarly to the *for* statement, in the ``while`` statement we can also (in addition to other commands) place a new loop statement, and it could be either a *while* or a *for* loop. That way, we can build different combinations of inserted loops.

When the two loops are inserted into one another, we call them a double loop, while three nested loops are called a triple loop. Similarly, we can nest any number of loops into one another, we just rarely need a large number of nested loops.

In this lesson we will practice writing combinations of the nested *while* and *for* loops.

Various double and multiple loops - tasks
-----------------------------------------

Take 4 balls at each square until the end of a row
''''''''''''''''''''''''''''''''''''''''''''''''''

.. questionnote::

  There are one or more squares in front of Karel, and on each of these squares there are four balls (there are no balls on the starting square). Karel needs to pick them all up.
  
Now, until he reaches the wall, Karel needs to repeat stepping forward and taking 4 balls. Try complementing the program.

Recall, as in the earlier examples of nesting loops, the statement in the body of the inner loop (here it will be the statement ``pick_ball()``) should be indented further.

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
                     "while front_is_clear():",
                     "    move()",
                     "    # add missing statements",
                     ""];
                     //from karel import *
                     //while front_is_clear():
                     //    move()
                     //    for i in range(4):
                     //        pick_ball()
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
       :showtitle: Solution
       :hidetitle: Hide solution
    
       .. activecode:: Karel_while__many_squares_two_bals_per_square_solution
          :passivecode: true
          
          from karel import *
          while front_is_clear():
              move()
              for i in range(4):
                  pick_ball()
   
   
Pick up all the balls
'''''''''''''''''''''

.. questionnote::

  There is at least one square in front of Karel, and there may be any number of them. On each of the squares **in front of** Karel there are zero or more balls (the starting square is empty). Karel needs to pick up all the balls.

This task is the generalization of the previous one, so the program that solves this task can be used in the previous one as well. The difference is that now the inner loop must be a *while* loop, while in the previous task it could have been a *for* loop as well.

Again, the statement ``pick_ball()`` should be indented further in. This way, it will repeat while the condition of the inner *while* statement holds, that is, while there is a ball on the square Karel is on at that moment. Taking all the balls, together with the ``move`` statement is repeated in the outer ``while`` loop as long as there are squares in front of Karel. The overall effect of nesting loops is that all the balls from each square will be taken.

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
                     "while front_is_clear():",
                     "    # go forward",
                     "    while ... # finish the program",
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

Bring all the balls
'''''''''''''''''''

.. questionnote::

  There is a path of unknown length in front of Karel. Karel should collect all the balls from all the squares and bring them to the starting square.

The program has been broken down to smaller pieces by the comments. Add missing statements.

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
                     "# use double loop to take all balls from all squares",
                     "",
                     "",
                     "turn_left(); turn_left()                # turn back",
                     "# tell Karel to go back to the starting square ",
                     "# (that is, to move forward while he can)",
                     "",
                     "while any_balls_with_karel():",
                     "    # drop one ball",
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
       :showtitle: Solution
       :hidetitle: Hide solution

       .. activecode:: Karel_while__bring_all_balls_solution
          :passivecode: true
          
          from karel import *
          while front_is_clear():          # bring all balls from all squares
              move()
              while is_ball_on_square():
                  pick_ball()
                
          turn_left(); turn_left()         # turn back
          
          while front_is_clear():          # go back to the starting square
              move()
              
          while any_balls_with_karel():    # drop all the balls
              drop_ball()


Up and down
'''''''''''

.. questionnote::

  Karel is on a rectangular board of unknown size (the number of columns is always odd), without any balls on the squares. The goal is for Karel to reach the bottom right square. In order to achieve this, Karel will have to move through the columns alternately up and down.
  
   These are some of the possible looks of the labyrinth:

   .. image:: ../../_images/Karel/While_UpDown.jpg
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
                     "# add the missing statements",
                     ""];
                     //from karel import *
                     //while front_is_clear():        # while you are not in the bottom right corner
                     //    move(); turn_left()            # enter the next column and turn north
                     //    while front_is_clear():        # go to the top edge
                     //        move()
                     //
                     //    turn_right(); move(); turn_right() # move to the next column and turn south
                     //    while front_is_clear():        # go to the bottom edge
                     //        move()
                     //
                     //    turn_left()                    # turn east
    
         return {robot:robot, world:world, code:code};
      },
    
      isSuccess: function(robot, world) {
         return robot.getAvenue() == world.getAvenues() &&
            robot.getStreet() == 1;
      },
   }

.. reveal:: Karel_while__up_col_down_col_reveal
   :showtitle: Hint
   :hidetitle: Hide hint

   .. activecode:: Karel_while__up_col_down_col_solution
      :passivecode: true
      
      from karel import *
      while front_is_clear(): # while you are not in the bottom right corner
          move(); turn_left()     # enter the next column and turn north
          ... # finish this part  # go to the top edge

          turn_right(); move()    # move to the next column
          turn_right()            # turn south
          ... # finish this part  # go to the bottom edge

          turn_left()             # turn east

Stairs
''''''

.. questionnote::

  Karel should climb up the first stairs, then go down the other ones and end up in the lower right corner. The table size is not known, but the number of columns will always be odd. The table might look like this:
  
   .. image:: ../../_images/Karel/While_Stairs.jpg
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
                     "# add missing statements",
                     ""];
                     //from karel import *
                     //turn_left()                       # northwards
                     //while front_is_clear():           # while there are stairs up
                     //    move(); turn_right(); move(); turn_left() #    climb up one stair
                     //
                     //turn_right(); turn_right()        # southwards
                     //
                     //while front_is_clear():           # while there are srairs down
                     //    move(); turn_left(); move(); turn_right() #    come down one stair 
    
         return {robot:robot, world:world, code:code};
      },
    
      isSuccess: function(robot, world) {
         return robot.getAvenue() == world.getAvenues() &&
            robot.getStreet() == 1;
      },
   }

.. reveal:: Karel_while__stairs_reveal
   :showtitle: Hint
   :hidetitle: Hide hint

   .. activecode:: Karel_while__stairs_solution
      :passivecode: true
      
      from karel import *
      turn_left()                        # northwards
      while front_is_clear():            # while there are stairs up
          move(); turn_right(); move(); turn_left() # climb up one stair

      turn_right(); turn_right()         # southwards
      
      while ... # add the condition      # while there are srairs down
          ... # add 4 statements             # come down one stair


Spiral to the left
''''''''''''''''''

.. questionnote::

  In all displayed cases, Karel should come to a square marked with a red circle (there are no balls in this task).
   
   .. image:: ../../_images/Karel/While_SpiralLeft.jpg
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
                  "# finish the incomplete statements",
                  "while front_is_clear():",
                  "    while ... ",
                  "        ... ",
                  "    turn_left()",
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
   :showtitle: Solution
   :hidetitle: Hide solution

   .. activecode:: Karel_while__spiral_left_solution
      :passivecode: true
      
      from karel import *
      while front_is_clear():
          while front_is_clear():
              move()
          turn_left()

