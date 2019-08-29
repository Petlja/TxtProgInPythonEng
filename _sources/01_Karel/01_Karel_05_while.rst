Solve multiple tasks at once
============================

Judging by the programs we have seen so far, one might think that a special program should be written for each, even a slightly different task. If that were the case, programming would be a very, very tedious job.

In order to apply one program to a group of similar tasks, we need that program to behave differently in different situations. This means that we need a way for the program to figure out the current situation and then choose which commands will be executed, depending on the situation. By the situation, we mean the number of balls on a square or with Karel, the position of the walls around Karel and so on. A program that could get answers to the questions concerning Karel and its surroundings could also solve several similar tasks, or (in other words) a general task.

Questions about Karel
---------------------

At the beginning of the introductory chapter, we saw commands for Karel, by which we instruct him to perform some actions (going forward, turning left and right, taking and dropping balls). We mentioned then that there are five other functions related to Karel. These five functions are different from the previous ones, since, by using these functions, we ask some questions and get the answers about Karel or the square he is located on. Here are these functions:

- ``front_is_clear()`` - we ask if Karel can go forward (are there walls in front of him). We get the answer "yes" or "no".
- ``num_balls_on_square()`` - we ask how many balls are there on the square Karel is on. We get the number of balls on the square.
- ``is_ball_on_square()`` - we ask if there is at least one ball on the Karel's square. We get the answer "yes" or "no".
- ``num_balls_with_karel()`` - we ask how many balls Karel currently has with him. We get the number of balls that Karel holds.
- ``any_balls_with_karel()`` - we ask if Karel has at least one ball with him. We get the answer "yes" or "no".

We cannot write these answer-giving functions as separate statements, as we have done so far. Instead, we write these functions as a part of some Python statements. Let's take a look at the examples.

As long as needed (*while* statement)
-------------------------------------

One way to use the functions that give the answer is to write them in ``while`` statement. The *while* statement exists in almost all programming languages and it is written very similarly in different languages. In Python it looks like this:

.. activecode:: while_syntax
   :passivecode: true

   while condition:
       statement_1
       ...
       statement_k

.. infonote::

    The meaning of ``while`` statement is: as long as the ``condition`` is fulfilled, execute the statement or statements that are written indented below. Word ``condition`` above stands for anything that is correctly written in Python, and comes down to **yes** or **no** (technical term for that "anything" is a **logical expression**).

    The rules of writing *while* statement require writting colon character ``:`` after the condition. After the condition (and colon), we write statements that we want to repeat as long as the condition is met, that is, while the answer to the question inside the condition is **yes** (or **True**). These repeating statements make the body of the while statement, and are written indented in the following lines (the same number of spaces are added before each of the repeated statements).

The condition is examined before each execution of the statements in the body of the *while* statement. The first time the condition is not met, *while* statement's execution (together with the statements in its body) is completed, and next statement to be executed is the one listed below the body of *while* statement. For example, if we execute:

.. activecode:: while_example
   :passivecode: true

   while front_is_clear():
       move()
   pick_ball()

Karel will move forward as far as he can, that is, until we get the answer "no" to the question front_is_clear(), which means that Karel has encountered a wall. When he finishes moving, Karel will take the ball. In case that Karel is already in front of the wall, the command move() will not be executed at all and Karel will immediately take the ball.

~~~~

Each of the following examples and tasks is a general one. This means that, for each task, at different program launches, the task will look similar, but slightly different. The program should be written to solve the task in each of these similar cases.

Go forward as far as you can and pick up the ball
'''''''''''''''''''''''''''''''''''''''''''''''''

.. questionnote::

   There is one or more squares in front of Karel, and on the last square there is one ball. Write a program that will make Karel pick up the ball from the last square.
    
   **The program should run multiple times**, because at different launches, Karel's world will have different number of squares. Here are some examples of how the task may look:
     
   .. image:: ../../_images/Karel/While_01.jpg
      :width: 600px   
      :align: center

We'll use while statement to move Karel, and after that, tell him to pick up the ball.

.. karel:: Karel_while__many_squares_and_ball_at_the_end
   :blockly:

   {
      setup:function() {
         function random(n) {
            return Math.floor(n * Math.random());
         }

         var N = 2 + random(14);
         var world = new World(N, 1);
         world.setRobotStartAvenue(1);
         world.setRobotStartStreet(1);
         world.setRobotStartDirection("E");
         world.putBall(N, 1);
      
         var robot = new Robot();
      
         var code = ["from karel import *",
                     "while front_is_clear():",
                     "    move()",
                     "pick_ball()"];
         return {robot:robot, world:world, code:code};
      },
      
      isSuccess: function(robot, world) {
         return robot.getBalls() === 1;
      }
   }

.. infonote::
    
    It may happen that a program often produces a good result, occasionally giving a bad result or being interrupted due to an error. **Such a program should be considered buggy (defective)**. The correct program should always give the correct result.

Tasks for exercise
------------------

Go one square forward and pick up all the balls
'''''''''''''''''''''''''''''''''''''''''''''''

.. questionnote::

  There is exactly one square In front of Karel, and on it there are any number of balls. Karl needs to pick them up.
  
Following the instructions in the program below, Karel will try to repeat the command ``pick_ball()`` infinitely. However, when Karel takes all the balls from that square, we will receive an error message because we told Karel to take a ball from the empty square (feel free to try this and see what the error message looks like). Try to fix the program so that Karel takes the balls only while there are some on the square.

.. karel:: Karel_while__one_square_many_balls
   :blockly:

   {
        setup:function() {
           function random(n) {
              return Math.floor(n * Math.random());
           }
           
           var world = new World(2, 1);
           world.setRobotStartAvenue(1);
           world.setRobotStartStreet(1);
           world.setRobotStartDirection("E");
           
           var N = random(14);
           world.putBalls(2, 1, N);

           var robot = new Robot();

           var code = ["from karel import *",
                       "move()",
                       "while True: # instead of True use the function is_ball_on_square()",
                       "    pick_ball()",
                       ""];
           return {robot:robot, world:world, code:code};
        },
    
        isSuccess: function(robot, world) {
           var N = world.getAvenues();
           for (var k = 1; k <= N; k++)
              if (world.getBalls(k, 1) > 0)
                 return false;
               
           return true;
        },
   }

.. commented out
   .. reveal:: Karel_while__one_square_many_balls_reveal
      :showtitle: Solution
      :hidetitle: Hide solution
   
      .. activecode:: Karel_while__one_square_many_balls_solution
         :passivecode: true
         
         from karel import *
         move()
         while is_ball_on_square():
             pick_ball()

Go as long as you can, taking one ball at each square
'''''''''''''''''''''''''''''''''''''''''''''''''''''

.. questionnote::

   There are one or more squares in front of Karel, and on each square there is one ball. Write a program that makes Karel collect the balls from all squares.
   
   **Run this program multiple times as well** to make sure that it solves the task regardless of the length of the Karel's path.
   
One *while* statement should be used for both moving Karel and taking the balls.

.. karel:: Karel_while__many_squares_and_ball_at_each
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
             world.putBall(k, 1);

         var robot = new Robot();
      
         var code = ["from karel import *",
                     "# complete the program",
                     ];
         return {robot:robot, world:world, code:code};
      },
      
      isSuccess: function(robot, world) {
         return (robot.getBalls() == world.getAvenues() - 1);
      }
   }

Move all the balls from the last to the first square
''''''''''''''''''''''''''''''''''''''''''''''''''''

.. questionnote::

   There are one or more squares in front of Karel, and there are several balls on the last square. Karel should take all the balls from the last square and leave them on the first square.
   
   (Run the program multiple times.)
   
In this task, four loops are needed one after another (not one inside another):

- In the first loop, Karel arrives to the last square
- In the second loop, Karel takes the balls
- In the third loop, Karel returns to the starting square
- In the last loop, Karl leaves all the balls he has with him

Of course, after the first or the second loop, Karel should turn towards the starting square (twice to the left or twice to the right).

.. karel:: Karel_while__bring_balls_to_front_square
    :blockly:

    {
        setup:function() {
            function random(n) {
                return Math.floor(n * Math.random());
            }

            var N = 2 + random(5);
            var world = new World(N, 1);
            world.setRobotStartAvenue(1);
            world.setRobotStartStreet(1);
            world.setRobotStartDirection("E");
            world.putBalls(N, 1, 2 + random(4));

            var robot = new Robot();
      
            var code = ["from karel import *",
                        "# go forward while you can",
                        "# take all the balls",
                        "turn_right()",
                        "turn_right()",
                        "# go forward while  you can",
                        "# drop all the balls",
                       ];
            return {robot:robot, world:world, code:code};
        },
      
        isSuccess: function(robot, world) {
            var N = world.getAvenues();
            for (var k = 2; k <= N; k++) {
                if (world.getBalls(k, 1) > 0)
                    return false;
            }
            if (robot.getBalls() > 0)
                return false;

            return true;
        }
    }
    
.. commented out
   .. reveal:: Karel_while__bring_balls_to_front_square_reveal
       :showtitle: Solution
       :hidetitle: Hide solution
   
       .. activecode:: Karel_while__bring_balls_to_front_square_solution
           :passivecode: true
         
           from karel import *
           while front_is_clear():
               move()
           while is_ball_on_square():
               pick_ball()
           turn_right()
           turn_right()
           while front_is_clear():
               move()
           while any_balls_with_karel():
               drop_ball()

Put the balls in the top row
''''''''''''''''''''''''''''

.. questionnote::

  Karel's world this time consists of two rows of the same, but unknown length. Karel is in the lower left corner, facing east. All squares of the upper row are empty, and each square of the first row contains one ball, **including the square where Karel is**. Karel's task is to put a single ball onto the each square of the top row.
  
  (Run the program multiple times.)
  
.. karel:: Karel_while__put_balls_in_upper_row
   :blockly:

   {
      setup:function() {
         function random(n) {
            return Math.floor(n * Math.random());
         }

         var N = 2 + random(4);
         var world = new World(N, 2);
         world.setRobotStartAvenue(1);
         world.setRobotStartStreet(1);
         world.setRobotStartDirection("E");
         for (var k = 1; k <= N; k++)
             world.putBall(k, 1);

         var robot = new Robot();
      
         var code = ["from karel import *",
                     "# complete the program",
                     ];
         return {robot:robot, world:world, code:code};
      },
      
      isSuccess: function(robot, world) {
          var N = world.getAvenues();
          for (var k = 1; k <= N; k++) {
              if (world.getBalls(k, 1) > 0)
                  return false;
              if (world.getBalls(k, 2) != 1)
                  return false;
          }
          if (robot.getBalls() > 0)
              return false;

          return true;
      }
   }

.. reveal:: Karel_while__put_balls_in_upper_row_reveal
    :showtitle: Hint
    :hidetitle: Hide hint
    
    We give instructions that resemble the program:

    .. activecode:: Karel_while__put_balls_in_upper_row_solution
        :passivecode: true
        
        pick up the ball
        while you can go forward:
            go forward
            pick up the ball
        turn towards the top row
        get in the top row
        turn towards the beginning of the row
        drop the ball
        while you can go forward:
            go forward
            drop the ball

.. commented out
    .. reveal:: Karel_while__put_balls_in_upper_row_reveal
        :showtitle: Solution
        :hidetitle: Hide solution

        .. activecode:: Karel_while__put_balls_in_upper_row_solution
            :passivecode: true
          
            from karel import *
            pick_ball()
            while front_is_clear():
                move()
                pick_ball()
            turn_left()
            move()
            turn_left()
            drop_ball()
            while front_is_clear():
                move()
                drop_ball()
