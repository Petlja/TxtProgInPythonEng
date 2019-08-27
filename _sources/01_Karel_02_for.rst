Shorten your programs
=====================

In the previous chapter there were tasks in which it would be convenient for us to have a shorter way of specifying some repetitive actions. For example, we needed Karel to go three steps forward. In the case of only three steps, it's easy enough to write the ``move()`` statement three times, but when Karel needs to make, say, twelve steps forward, if we write:

.. activecode:: Karel_for_12_steps_manual
   :passivecode: true
   
   move(); move(); move(); move(); move()
   move(); move(); move(); move(); move()
   move(); move()

such way of writing programs is more error prone, and it is also harder to read such programs. If you think that even twelve repetitions are not a problem, have in mind that in the world of programming, it is not uncommon for a statement to be repeated a million times.

*For* statement
---------------

A better way to specify such a maneuver would be to say "twelve times go ahead". To repeat a statement (or a group of statements) certain number of times, we use ``for`` statement. The most commonly used form of this statement in Python looks like this:

.. activecode:: Karel_for_syntax
   :passivecode: true
   
   for i in range(n):
       statement_1
       ...
       statement_k

Later, we will see some other forms of the ``for`` statement as well. 

Using ``for`` statement, our example with twelve repetitions of one step forward can be written this way:
      
.. activecode:: Karel_for_12_steps_loop
   :passivecode: true
   
   for i in range(12):
       move()


Here we give a bit more detailed description of the ``for`` statement. You do not have to fully understand it at this time - the use and rules of writing it will become clearer with the following examples. Should you need more details about the ``for`` statement later, you can return to this explanation (but be aware that it does not describe other forms of *for* statement).

.. infonote::

   According to the rules of writing programs in Python, the words ``for`` and ``in``, as well as the colon character ``:`` at the end of the line, are all mandatory parts of the *for* statement.
   
   - The letter ``i`` here serves as a name for the place where we keep the count of repetitions. Instead of ``i``, another name may be used for that (we will return to this in more detail when we need it). 
   
   - ``range(n)`` represents a range of integers starting with 0, and ``n`` tells how many numbers this range contains. For example, ``range(3)`` is the range containing the numbers :code:`0, 1, 2`, and ``range(7)`` is the range of numbers :code:`0, 1, 2, 3 , 4, 5, 6`.

   - The statements in the following lines make the so-called **body of the for statement**. These can be any statements in Python, including functions for managing Karel, other ``for`` statements, or some statements that we have not mentioned yet. There can be one or more such statements in the body of the for statement.

   The ``for i in range (3)`` is interpreted as: "for value *i* in the range [0, 1, 2]". This means that statements in the body of the for statement will be executed once for i=0, for i=1, and for i=2, so a total of three times. We will not use the value of *i* in the for statement's body for now, so we only need to know how many values are there in the range (that is the number in brackets behind the word ``range``), because statements in the body will be executed that number of times.
   
   In order to make clear what statements are in the body of the *for* statement, these statements are written indented (moved to the right), all for the same number of spaces. We can choose the number of spaces for indentation for each *for* statement. However, it is a good practice to always choose the same number, because that way, we will get accustomed to the certain layout of the program and the code will be more readable. The most common choice for indentation is 4 spaces, so we will also adopt it.
   
*For* statement is also known as a *loop*, because by following the statements we execute, when we come to the *for* statement, we loop a number of times through the statements in its body. The term "loop" is less precise (compared to the "for statement"), because as we will soon see, the *for* statement is not the only loop there is. The word "loop" is usually used when it is clear (or irrelevant) which exact loop statement we are talking about, for it is easier to say, for example, "loop body", rather than "for statement body".

Tasks for exercise
------------------

Move fifteen squares forward and take the ball
''''''''''''''''''''''''''''''''''''''''''''''

.. questionnote::

   Write a program on the basis of which Karel will move to the square (16, 1) and pick up the ball.

A longer (and uglier) program is waiting for you in the solution area. Try replacing it with the *for* statement. In case that your solution with *for* statement does not work (which often happens in the beginning), you can see our solution by clicking on the "Solution" button below.

.. karel:: Karel_for_15_steps_and_take
   :blockly:

   {
      setup:function() {
          var world = new World(16, 1);
          world.setRobotStartAvenue(1);
          world.setRobotStartStreet(1);
          world.setRobotStartDirection("E");
          world.putBall(16, 1);
      
         var robot = new Robot();
      
         var code = ["from karel import *",
                     "move(); move(); move(); move(); move()",
                     "move(); move(); move(); move(); move()",
                     "move(); move(); move(); move(); move()",
                     "pick_ball()"];
                  
         return {robot:robot, world:world, code:code};
      },
      
      isSuccess: function(robot, world) {
         return robot.getBalls() === 1;
      }
   }

.. reveal:: Karel_for_15_steps_and_take_reveal
   :showtitle: Solution
   :hidetitle: Hide solution

   .. activecode:: Karel_for_15_steps_and_take_solution
      :passivecode: true
      
      from karel import *
      for i in range(15):
          move()
      pick_ball()

Go one square forward and collect 10 balls
''''''''''''''''''''''''''''''''''''''''''

.. questionnote::

  There is one square in front of Karel, and there are 14 balls on it. Karel needs to pick up exactly ten balls.
  
.. karel:: Karel_for_one_square_take_10_balls
   :blockly:

   {
        setup:function() {
           var world = new World(2, 1);
           world.setRobotStartAvenue(1);
           world.setRobotStartStreet(1);
           world.setRobotStartDirection("E");
           
           world.putBalls(2, 1, 14);

           var robot = new Robot();

           var code = ["from karel import *",
                       "move()",
                       "# Complete the program",
                       ""];
           return {robot:robot, world:world, code:code};
        },
    
        isSuccess: function(robot, world) {
           return robot.getBalls() == 10;
        },
   }
   
.. reveal:: Karel_for_one_square_take_10_balls_reveal
   :showtitle: Solution
   :hidetitle: Hide solution

   .. activecode:: Karel_for_one_square_take_10_balls_solution
      :passivecode: true
      
      from karel import *
      move()
      for i in range(10):
          pick_ball()


Take one ball on each of the next 8 squares
'''''''''''''''''''''''''''''''''''''''''''

.. questionnote::

  There are eight squares in front of Karel, and on each of them there is one ball. Karel needs to pick up all the balls.
  
Notice that two things need to be done in the loop: steping forward and taking the ball.

.. karel:: Karel_for_EightSquaresOneBallEach_TakeAllBalls
   :blockly:

   {
        setup:function() {
           var numAvenues = 9;
           var world = new World(numAvenues, 1);
           world.setRobotStartAvenue(1);
           world.setRobotStartStreet(1);
           world.setRobotStartDirection("E");
           
         for (var k = 2; k <= numAvenues; k++)
            world.putBall(k, 1);

           var robot = new Robot();

           var code = ["from karel import *",
                       "# Complete the program",
                       ""];
           return {robot:robot, world:world, code:code};
        },
    
        isSuccess: function(robot, world) {
           return robot.getBalls() == world.getAvenues() - 1;
        },
   }
   
.. reveal:: Karel_for_EightSquaresOneBallEach_TakeAllBalls_reveal
   :showtitle: Solution
   :hidetitle: Hide solution

   .. activecode:: Karel_for_EightSquaresOneBallEach_TakeAllBalls_solution
      :passivecode: true
      
      from karel import *
      for i in range(8):
          move()
          pick_ball()


Pick up 5 balls from each of the next three squares
'''''''''''''''''''''''''''''''''''''''''''''''''''

.. questionnote::

  There are three squares in front of Karel, and on each of them there are five balls. Karel needs to pick up all the balls.
  
.. karel:: Karel_for_Take_5_5_5
   :blockly:

   {
        setup:function() {
           var world = new World(4, 1);
           world.setRobotStartAvenue(1);
           world.setRobotStartStreet(1);
           world.setRobotStartDirection("E");
           
           world.putBalls(2, 1, 5);
           world.putBalls(3, 1, 5);
           world.putBalls(4, 1, 5);
           
           var robot = new Robot();

           var code = ["from karel import *",
                       "# Complete the program",
                       ""];
           return {robot:robot, world:world, code:code};
        },
    
        isSuccess: function(robot, world) {
           return robot.getBalls() == 15;
        },
   }
   
.. reveal:: Karel_for_Take_5_5_5_reveal
   :showtitle: Solution
   :hidetitle: Hide solution
   
   .. activecode:: Karel_for_Take_5_5_5_solution
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
