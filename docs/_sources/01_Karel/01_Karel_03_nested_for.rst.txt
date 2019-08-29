Even shorter programs
=====================

Let's get back to the last program of the previous lesson. We needed Karel to take five balls from each of the three squares in fornt of him.

.. image:: ../../_images/Karel/nested_for_3x5.png
    :width: 300px
    :align: center

The program that solves the task could look like this:

.. activecode:: Karel_nested_for__intro_1
   :passivecode: true

    from karel import *
    move()
    for i in range(5):
        pick_ball()
    move()
    for i in range(5):
        pick_ball()
    move()
    for i in range(5):
        pick_ball()
        
We see that, in this program, the following group of statements repeats three times:

.. activecode:: Karel_nested_for__intro_2
   :passivecode: true

    move()
    for i in range(5):
        pick_ball()

This allows us to shorten the program further. In explaining the *for* statement, we mentioned that other loops can be found in the loop body. Now we have the opportunity to use it.
 
Nested *for* loops
------------------

When there is a second loop in the body of one loop, then the first loop is called an outer loop and the other one is called an inner loop. Together we call them nested or inserted loops. In the following example, we'll see how nested *for* loops are written.

Pick up five balls three times
''''''''''''''''''''''''''''''

.. questionnote::

  There are three squares in front of Karel, and there are 5 balls on each of them. Karel needs to pick up all the balls.

The task is repeated, but now we will solve it in a different way.

.. infonote::
    We mentioned that ``i`` in the previous examples of *for* statements is a name for the repetition counter. Now, for the first time we need to count other things (balls) during the counting of one thing (squares). This means, for example, that we will need to exactly know when we are on the third square, taking the second ball. Therefore, we can not use the same name for both counters, so we have introduced new names for counters instead of the previous ``i``. In the following program, we call the square counter ``i_square``, and the name for the ball counter is ``i_ball``.
   
.. karel:: Karel_for_TakeMxN
   :blockly:

   {
        setup:function() {
           var numAvenues = 4;
           var numBalls = 5;
           var world = new World(numAvenues, 1);
           world.setRobotStartAvenue(1);
           world.setRobotStartStreet(1);
           world.setRobotStartDirection("E");
           
           for (var k = 2; k <= numAvenues; k++)
              world.putBalls(k, 1, numBalls);
           
           var robot = new Robot();

           var code = ["from karel import *",
                       "for i_square in range(3):",
                       "    move()",
                       "    for i_ball in range(5):",
                       "        pick_ball()",
                       ""];
           return {robot:robot, world:world, code:code};
        },
    
        isSuccess: function(robot, world) {
           return robot.getBalls() == 15; // 3 x 5 balls
        },
   }

In the given solution, the statement *pick_ball()* is additionally indented, because it is executed ones for each ``i_ball`` from the range [0, 1, 2, 3, 4]. In addition, the whole statement ``for i_ball in range(5):`` (together with its body and the statement *move()* above it), repeats 3 times, ones for each ``i_square`` from the range [ 0, 1, 2]. This means that the command *pick_ball()* executes a total of 3 x 5 = 15 times (on each of the three squares five times).

.. infonote::
   With nested loops, it is necessary to pay extra attention to the correct indentation of the statements, because it becomes somewhat more complicated. Incorrect indentation of some commands can lead to the wrong result, or to a program that does not work at all.
   
Tasks for exercise
------------------

Skip
''''

.. questionnote::

  In front of Karel, there is one ball on every third square, and Karel should pick them up both.
  
Karl should repeat a group of actions "Move three times, and then take the ball" 2 times.

.. karel:: Karel_for_every_nth_square
    :blockly:

    {
        setup:function() {
            var everyNth = 3;
            var numRepetitions = 2;
            var numBalls = 1;
            var numAvenues = 1 + numRepetitions * everyNth;
            var world = new World(numAvenues, 1);
            world.setRobotStartAvenue(1);
            world.setRobotStartStreet(1);
            world.setRobotStartDirection("E");
           
            for (var k = 1; k <= numRepetitions; k++)
                world.putBalls(1+k*everyNth, 1, numBalls);
            
            var robot = new Robot();
         
            var code = ["from karel import *",
                        "for i_rep in range(2):  # repeat twice everything that follows",
                        "    # use for statement to tell Karel to go 3 squares forward",
                        "    pick_ball()             # take the ball",
                        ""];
    
            return {robot:robot, world:world, code:code};
        },
    
        isSuccess: function(robot, world) {
            return robot.getBalls() == 2; // number of repetitions
        },
    }

.. commented out
   .. reveal:: Karel_for_every_nth_square_reveal
       :showtitle: Решење
       :hidetitle: Сакриј решење
   
       .. activecode:: Karel_for_every_nth_square_solution
           :passivecode: true
         
           from karel import *
           for i_pon in range(2):     # repeat twice everything that follows
               for i_polje in range(3):   # go 3 squares forward
                   move()
               pick_ball()            # take the ball

5 balls on every third square
'''''''''''''''''''''''''''''

.. questionnote::

  There are five balls on every third square in front of Karel, and he should collect them all.
  
The task is similar to the previous, you just need to repeat picking up the ball. Make sure the loop for taking the balls is underneath the loop for moving forward, not in it.


.. karel:: Karel_for_every_nth_square_5
    :blockly:

    {
        setup:function() {
            var everyNth = 3;
            var numRepetitions = 2;
            var numBalls = 5;
            var numAvenues = 1 + numRepetitions * everyNth;
            var world = new World(numAvenues, 1);
            world.setRobotStartAvenue(1);
            world.setRobotStartStreet(1);
            world.setRobotStartDirection("E");
           
            for (var k = 1; k <= numRepetitions; k++)
                world.putBalls(1+k*everyNth, 1, numBalls);
            
            var robot = new Robot();
         
            var code = ["from karel import *",
                        "for i_rep in range(2):      # repeat twice everything that follows",
                        "    # use for statement to tell Karel to go 3 squares forward",
                        "    # use a new for statement to tell Karel to take 5 balls",
                        ""];
    
            return {robot:robot, world:world, code:code};
        },
    
        isSuccess: function(robot, world) {
            return robot.getBalls() == 10; // numRepetitions x numBalls
        },
    }

.. commented out
   .. reveal:: Karel_for_every_nth_square_5_reveal
       :showtitle: Решење
       :hidetitle: Сакриј решење
   
       .. activecode:: Karel_for_every_nth_square_5_solution
           :passivecode: true
         
           from karel import *
           for i_pon in range(2):     # repeat twice everything that follows
               for i_polje in range(3):   # go 3 squares forward
                   move()
               for i_loptica in range(5): # to take 5 balls
                   pick_ball()


Go about
''''''''

.. questionnote::

  Karl once more needs to pick up all the balls.
  
The outer loop should be executed 3 times, and in it Karel should do the following:

- Repeat twice the two actions: "move forward" and "take the ball"
- Turn left

.. karel:: Karel_for_ring
    :blockly:

    {
        setup:function() {
            var w = [
               '███████',
               '█1.1.1█',
               '█.███.█',
               '█0.0█1█',
               '█████.█',
               '█E.1.1█',
               '███████'
            ];

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
                        "... # complete the program",
                        ""];
                     
            return {robot:robot, world:world, code:code};
        },
      
        isSuccess: function(robot, world) {
           return robot.getBalls() == 6;
        }
    }

.. reveal:: Karel_for_ring_reveal_1
    :showtitle: Hint
    :hidetitle: Hide hint

    We've made verbal instructions a little more similar to the program, try converting them into statements. If you still want to see the program itself, click the "Solution" button.
    
    .. activecode:: Karel_for_ring_solution_1
        :passivecode: true
      
        for each of the 3 sides:
            for each of the 2 squares:
                move forward
                pick the ball
            turn left

    .. reveal:: Karel_for_ring_reveal_2
       :showtitle: Solution
       :hidetitle: Hide solution
   
       .. activecode:: Karel_for_ring_solution_2
           :passivecode: true
         
           from karel import *
           for i_side in range(3):     # repeat three times everything that follows
               for i_square in range(2):     # two times do "move" and "pick ball"
                   move()
                   pick_ball()
               turn_left()                   # turn along the next side



Go about and pick 3 balls each time
'''''''''''''''''''''''''''''''''''

.. questionnote::

  Write a program by which Karel will pick up all 18 balls.
  
This task differs from the previous one in just one thing: now picking up the balls should be in an additional loop. This means that we will have three nesting loops: one that counts sides of the maze, one that counts the squares along one side, and the third one that counts the balls on one square.

.. karel:: Karel_for_ring_3
    :blockly:

    {
        setup:function() {
            var w = [
               '███████',
               '█3.3.3█',
               '█.███.█',
               '█0.0█3█',
               '█████.█',
               '█E.3.3█',
               '███████'
            ];

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
                        "... # complete the program",
                        ""];
                     
            return {robot:robot, world:world, code:code};
        },
      
        isSuccess: function(robot, world) {
           return robot.getBalls() == 18;
        }
    }

.. reveal:: Karel_for_ring_3_reveal
    :showtitle: Hint
    :hidetitle: Hide hint

    Again, we give instructions which look like a program (this time without the program itself).
    
    .. activecode:: Karel_for_ring_3_solution
        :passivecode: true
      
        for each of the 3 sides:
            for each of the 2 squares:
                move forward
                for each of the 3 balls:
                    pick the ball
            turn left

.. commented out
   .. reveal:: Karel_for_ring_3_reveal
       :showtitle: Solution
       :hidetitle: Hide solution
   
       .. activecode:: Karel_for_ring_3_solution
           :passivecode: true
         
           from karel import *
           for i_side in range(3):     # three times repeat everything that follows
               for i_square in range(2):   # repeat twice "move forward" and "take 3 balls"
                   move()
                   for i_ball in range(3):
                       pick_ball()
               turn_left()             # turn along the next side
