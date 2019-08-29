*For* statement - practicing
============================

In this section we will only practice the use of *for* statement.

Tasks for exercise
------------------

Three times up and down
'''''''''''''''''''''''

.. questionnote::

  Karel is on a rectangular board of 5 rows and 7 columns and needs to reach the right bottom square.


Karel should repeat one complex action three times, that is, to go to the next column to the right, go to the top of the column, go to another column to the right, go down to the first row, and finally turn towards the last column to prepare for the next iteration.

Complete the program, taking into consideration that the counter in *for* statements you write should not be named ``i`` (this name is already used in the outer loop).

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
                     "for i in range(3):   # repeat everything that follows 3 times",
                     "    move(); turn_left()  # Enter the next column and turn north",
                     "    # use the for statement to tell Karel to go to the top edge",
                     "    ",
                     "    turn_right(); move() # go to the next column",
                     "    turn_right()             # turn south",
                     "    # use the for statement to tell Karel to go to the bottom edge",
                     "    ",
                     "    turn_left()          #    turn east",
                     ""];
    
         return {robot:robot, world:world, code:code};
      },
    
      isSuccess: function(robot, world) {
         return robot.getAvenue() == world.getAvenues() &&
            robot.getStreet() == 1;
      },
   }

.. reveal:: Karel_for_up_col_down_col_constant_reveal
   :showtitle: Solution
   :hidetitle: Hide solution

   .. activecode:: Karel_for_up_col_down_col_constant_solution
      :passivecode: true
      
      from karel import *
      for i in range(3):       # repeat everything that follows 3 times
          move(); turn_left()      # go to the next column and turn north
          for i_up in range(4):    # go to the top edge
              move()

          turn_right(); move()     # go to the next column
          turn_right()             # turn south
          for i_down in range(4):  # go to the bottom edge
              move()

          turn_left()              # turn east

Bring all the balls from all the squares
''''''''''''''''''''''''''''''''''''''''

.. questionnote::

  Karel should bring all 12 balls to the starting square.

Karеl needs to repeat "step into the next column and empty it" four times and eventually come back to the starting square and drop all the balls. Karel can empty each column by repeating "move one step forward and take the ball" three times, and then returning to the bottom of the column, facing the next column.

Complete the program.

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
                     "for i_column in range(4):      # repeat four times emptying one column",
                     "    move()                     # enter the next column",
                     "    turn_left()                # turn north",
                     "    #for ...                       # repeat 'move forward and take the ball' 3 times",
                     "",
                     "    turn_right(); turn_right() # turn south",
                     "    #for ...                   # go 3 steps forward to the bottom edge",
                     "",
                     "    turn_left()                # turn east",
                     "    ",
                     "# (Karel went through all the squares)",
                     "turn_left()                    # turn west",
                     "turn_left()",
                     "#for ...                       # come back to the starting square",
                     "    ",
                     "for i_ball in range(12):       # drop all the balls",
                     "    drop_ball()",
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
   :showtitle: Solution
   :hidetitle: Hide solution

   .. activecode:: Karel_for_fetch_from_matrix_solution
      :passivecode: true
      
      from karel import *
      for i_column in range(4):    # repeat emptying one column four times
          move()                       # enter the next column
          turn_left()                  # turn north
          for i_row in range(3):       # go to the top edge, picking the balls along
              move()
              pick_ball()

          turn_right(); turn_right()   # turn south
          for i_row in range(3):       # go to the bottom edge
              move()

          turn_left()                  # turn east (to the next column)
         
      turn_left()                  # turn west
      turn_left()
      for i_column in range(4):    # come back to the starting square
          move()
         
      for i_ball in range(12):     # drop all the balls
          drop_ball()


Triple loop
'''''''''''

.. questionnote::

  Now, there are 4 balls on each of the 6 squares, similar to the the previous task. Karel should bring all 24 balls to the starting square.

The only difference (compared to the previous task) is that now *pick_ball()* statement should be in an additional loop, the third in depth. Also, the number of balls that Karel drops on the starting square (at the end of the program) is different. Therefore, a bit easier way to solve the task is to copy the previous program and modify it.

.. karel:: Karel_for_fetch_24_from_matrix
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
                     "# Complete the program",
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
   :showtitle: Solution
   :hidetitle: Hide solution

   .. activecode:: Karel_for_fetch_24_from_matrix_solution
      :passivecode: true
      
      from karel import *
      for i_column in range(2):   # repeat emptying one column four times
          move()                      # enter the next column
          turn_left()                 # turn north
          for i_row in range(3):      # go to the top edge, picking the balls along
              move()                   
              for i_ball in range(4): 
                  pick_ball()                  

          turn_right(); turn_right()  # turn south
          for i_row in range(3):      # go to the bottom edge
              move()                   

          turn_left()                 # turn east

      turn_left()                 # turn west
      turn_left()                           
      for i_column in range(2):   # come back to the starting square
          move()

      for i_ball in range(24):    # drop all the balls
          drop_ball()


Ascend and descend
''''''''''''''''''

.. questionnote::

  Karel should climb up the first set of stairs, then go down the other ones, and end up in the lower right corner.

Now we need two loops one after the other (not nested). In the first loop, Karel should climb to the first staircase, and come down the second staircase in the second loop. In each loop, Karel has to perform 4 actions that represent one step up or down the stairs.

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
                     "turn_left()                  # northwards",
                     "for i_stair in range(3):         # repeat 3 times",
                     "    # tell Karel to climb up one stair",
                     "",
                     "turn_right(); turn_right()   # southwards",
                     "",
                     "# tell Karel to go down the stairs",
                     ""];
    
         return {robot:robot, world:world, code:code};
      },
    
      isSuccess: function(robot, world) {
         return robot.getAvenue() == world.getAvenues() &&
            robot.getStreet() == 1;
      },
   }

.. reveal:: Karel_for_stairs_constant_reveal
   :showtitle: Solution
   :hidetitle: Hide solution

   .. activecode:: Karel_for_stairs_constant_solution
      :passivecode: true
      
      from karel import *
      turn_left()                # northwards
      for i_stair in range(3):   # repeat 3 times
          move(); turn_right()       # climb up one stair
          move(); turn_left() 

      turn_right(); turn_right() # southwards
      
      for i_stair in range(3):   # repeat 3 times
          move(); turn_left()        # go one stair down
          move(); turn_right() 

Collect the balls on the stairs
'''''''''''''''''''''''''''''''

.. questionnote::

  Karel should finish again in the lower right corner, and along the way he should take all the balls.

A good way to solve this task is to start from the solution of the previous task. Hint: copy the solution of the previous task here, and then insert the loops for taking the balls.

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
                     "# write a program",
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
   :showtitle: Solution
   :hidetitle: Hide solution

   .. activecode:: Karel_for_stairs_and_balls_constant_solution
      :passivecode: true
      
      from karel import *
      turn_left()                     # northwards
      for i_stair in range(3):        # repeat 3 times
          move(); turn_right()            # climb up one stair
          for i_ball in range(3):
              pick_ball()
          move(); turn_left() 
          for i_ball in range(4):
              pick_ball()

      turn_right(); turn_right()      # southwards
      
      for i_stair in range(3):        # repeat 3 times
          move(); turn_left()             # go one stair down
          for i_ball in range(2):
              pick_ball()
          move(); turn_right() 
          for i_ball in range(3):
              pick_ball()
