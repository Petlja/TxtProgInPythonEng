*if* statement - practice
===========================

In this section we will only practice using the *if* statement and combining it with loops.

Tasks for exercise
------------------

Go to the end of a path and take only one ball
''''''''''''''''''''''''''''''''''''''''''''''

.. questionnote::

   Karel should arrive at the end of the corridor, and only take the first ball on the way. The starting square never has a ball on it, and Karel initially does not carry any balls.
   
.. karel:: Karel_if__take_first_ball_only
   :blockly:

   {
      setup:function() {
         function random(n) {
            return Math.floor(n * Math.random());
         }
         
         var ww = [
            [
               '█████████████',
               '█E.0.1.0.3.0█',
               '█████████████'
            ],
            [
               '█████████',
               '█E.0.2.2█',
               '█████████'
            ],
            [
               '███████',
               '█E.1.0█',
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
                     "# write the program",
                     ""];
                     
         return {robot:robot, world:world, code:code};
      },
      
      isSuccess: function(robot, world) {
         return robot.getBalls() > 0;
      }
   }

.. reveal:: Karel_if__take_first_ball_only_reveal
    :showtitle: Hint
    :hidetitle: Hide hint
    
    We have started one solution here. You are expected to complete the *if* statements with appropriate conditions.
    
    Karel should take the ball only if two conditions are met:
    
    - the first condition is the one that we check whenever Karel tries to take the ball (without this condition the program could be terminated due to an undoable operation).
    - the second condition is imposed by the requirements of this task, which is that Karel takes the ball only if he has not already taken one before.
    
    The order of checking these two conditions is not important, since both of them should be fulfilled in order to take the ball anyway.
    
    .. activecode:: Karel_if__take_first_ball_only_solution
        :passivecode: true
      
        from karel import *
        while front_is_clear():  # while there are squares in front of Karel
            move()                    
            if ???
                if ???
                    pick_ball()

Take the ball on the neighboring square
'''''''''''''''''''''''''''''''''''''''

.. questionnote::

   There is only one ball on the board. Karel and the ball are located on two adjacent squares with no wall between them (Karel is only one step appart from the ball, if he turns to the ball first). There may or may not be a wall between other squares. Karel should take the ball and he can finish on any square in the end.

   As usual, run the program several times to test it on various examples.

One possible idea is that in each of the four directions, we try to make Karel go one step forward and pick up the ball. Various scenarios can occur in each of the four attempts:

- it is possible that there are no squares in front of Karel in that direction
- it is possible that there is a square in front of Karel, but there are no balls on it
- it is possible that there is a square and that there is a ball on it


When trying the next direction, it is much simpler if we don't have to take into consideration whether Karel has found a square without a ball in the previous direction he tried, or did not find a square at all. To simplify the next attempt, it is convenient for us that Karel finishes the previous attempt when he was on an empty square in the same state as when there was no square. When there is no square in the attempted direction, Karel will remain on the starting square, facing the attempted direction. To facilitate the continuation of the search, we can leave Karel on the same square facing the same direction when he returns from an empty adjacent square. In fact, it won't do any harm if we do it also when Karel takes the ball (it is possible that Karel needlessly continues to search, but that will not cause any errors).
Because we've brought Karel to the same state (position and orientation) after any of the three cases above, we know our new starting state exactly, for each subsequent attempt. After each attempted direction, we just need to turn Karel towards the next direction we will try to find the ball in (either to the left or to the right).

.. karel:: Karel_if__take_neighboring_ball
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
                     "for i in range(4):",
                     "    if front_is_clear():",
                     "        move()",
                     "        # tell Karel to try to take the ball",
                     "        # tell Karel to go back to the starting square...",
                     "        # ... and turn towards the square at which he just tried",
                     "        # (as if he had not gone to that square at all)",
                     "    # tell Karel to prepare for the next attempt",
                     ""];
                     
         return {robot:robot, world:world, code:code};
      },
      
      isSuccess: function(robot, world) {
         return robot.getBalls() > 0;
      }
   }

.. commented out
   .. reveal:: Karel_if__take_neighboring_ball_reveal
       :showtitle: Solution
       :hidetitle: Hide solution
       
       Solution can look like this:
       
       .. activecode:: Karel_if__take_neighboring_ball_solution
           :passivecode: true
         
           from karel import *
           for i in range(4):          # in each of the 4 directions
               if front_is_clear():        # look for a square in that direction
                   move()                    
                   if is_ball_on_square():
                       pick_ball()
                   turn_left()                 # go back to starting square
                   turn_left()
                   move()
                   turn_left()                 # face the square you just tried
                   turn_left()
               turn_left()                 # next direction

Follow the path
'''''''''''''''

.. questionnote::

  There is only one ball on the table, and Karel should take it. The way to the ball is not straight, but there are no intersections (there is always only one way to continue moving, even from the starting square).
  
.. karel:: Karel_if__take_ball_no_branches
   :blockly:

   {
      setup:function() {
         function random(n) {
            return Math.floor(n * Math.random());
         }
         
         var ww = [
            [
               '███████████',
               '█N█0.0.0.0█',
               '█.█.█████.█',
               '█0█0█0.1█0█',
               '█.█.█.███.█',
               '█0.0█0.0.0█',
               '███████████'
            ],
            [
               '█████████',
               '█0.0.0.0█',
               '█.█████.█',
               '█0█0.0.0█',
               '█.█.█████',
               '█0█E█0.0█',
               '█.███.█.█',
               '█0.0.0█1█',
               '█████████'
            ],
            [
               '█████████████',
               '█W.0.0█0.0.0█',
               '█████.█.███.█',
               '█0.0.0█0█0.0█',
               '█.█████.█.███',
               '█0.0.0.0█0.1█',
               '█████████████'
            ],
            [
               '███████████',
               '█0.0█0.0█S█',
               '█.█.█.█.█.█',
               '█0█0.0█0.0█',
               '█.█████████',
               '█0█0.0█0.0█',
               '█.█.█.█.█.█',
               '█0.0█0.0█1█',
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
                     "... # write the program",
                     ""];
                     
         return {robot:robot, world:world, code:code};
      },
      
      isSuccess: function(robot, world) {
         return robot.getBalls() > 0;
      }
   }

.. reveal:: Karel_if__take_ball_no_branches_reveal
    :showtitle: Hint
    :hidetitle: Hide hint
    
    We give a program-like instructions for one possible solution:

    .. activecode:: Karel_if__take_ball_no_branches_solution
        :passivecode: true
      
        # First, turn towards the (only) free square
        
        while you can't move forward: 
            turn left
            
        while you can go forward:
            move forward
            if there is no free square in front of you: # if there is no straight path
                turn left
                if there is no free square in front of you: # if no path to the left either
                    turn right twice
        
        take the ball

.. commented out
   .. reveal:: Karel_if__take_ball_no_branches_reveal
       :showtitle: Solution
       :hidetitle: Hide solution
       
       One possible solution is:
   
       .. activecode:: Karel_if__take_ball_no_branches_solution
           :passivecode: true
         
           from karel import *
           while not front_is_clear(): # turn towards the (only) free square
               turn_left()
               
           while front_is_clear():
               move()
               
               # turn towards the next free square
               if not front_is_clear():   # if there is no straight path,
                   turn_left()                # try left
               if not front_is_clear():   # if there is no path to the left
                   turn_right(); turn_right() # try right
           
           if is_ball_on_square():
               pick_ball()

Sidetrack
'''''''''

.. questionnote::

  There is only one ball on the table and Karel should take it. To get to the ball, Karel should go straight only when he can't turn left or right (there will be no ambiguous crossroads where there is a path to both left and right).
  
.. karel:: Karel_if__p1_left_p2_right_p3_forward
   :blockly:

   {
      setup:function() {
         function random(n) {
            return Math.floor(n * Math.random());
         }
         
         var ww = [
            [
               '███████████',
               '█1.0█0.0.0█',
               '███.█.█████',
               '█0.0.0█0.0█',
               '█████.███.█',
               '█S.0.0.0.0█',
               '███████████'
            ],
            [
               '███████████',
               '█0.0.0█0.0█',
               '█████.█.███',
               '█0.0.0█0.0█',
               '█.█.█.█.█.█',
               '█0█0█E█0█1█',
               '█.█.███.███',
               '█0█0.0.0.0█',
               '███████████'
            ],
            [
               '█████████████',
               '█E.0.0█0.0.0█',
               '███.█.█.█████',
               '█0.0█0█0.0.0█',
               '█.█.███.███.█',
               '█0█0█0.0.0█0█',
               '█.███.█████.█',
               '█0.0.0.0.0█1█',
               '█████████████'
            ],
            [
               '█████████',
               '█0.0.0█S█',
               '█.█████.█',
               '█0.0.0.0█',
               '███.███.█',
               '█0█0.0█0█',
               '█.█.█.███',
               '█0.0█0.1█',
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
                     world.setRobotStartDirection("SWEN".charAt(pos));
                 }
                 let d = w[wy].charCodeAt(wx);
                 if (d >= 48 && d < 58) world.putBalls(x, y, d - 48);
             }
         }
         
         var robot = new Robot();
         
         var code = ["from karel import *",
                     "... # write the program",
                     ""];
                     
         return {robot:robot, world:world, code:code};
      },
      
      isSuccess: function(robot, world) {
         return robot.getBalls() > 0;
      }
   }
   
.. reveal:: Karel_if__p1_left_p2_right_p3_forward_reveal
    :showtitle: Hint
    :hidetitle: Hide hint

    Instructions for one possible solution:
    
    .. activecode:: Karel_if__p1_left_p2_right_p3_forward_solution
        :passivecode: true
      
        # turn towards the only free square
        
        while you can move forward:
            move forward
            # try going left (turn left and try going forward)
            # if you can't go left:
                # try going right
                # if you can't go right either
                    # prepare to try going straight in the next iteration
        
        take the ball

.. commented out
    .. reveal:: Karel_if__p1_left_p2_right_p3_forward_reveal
        :showtitle: Solution
        :hidetitle: Hide solution

        .. activecode:: Karel_if__p1_left_p2_right_p3_forward_solution
            :passivecode: true
          
            from karel import *
            for i in range(3):        # turn towards the only fre square
                if not front_is_clear():
                    turn_left()
            
            while front_is_clear():
                move()
                turn_left()                # try going left
                if not front_is_clear():   # if you can't go left
                    turn_right(); turn_right()     # try going right
                if not front_is_clear():   # if you can't go right either
                    turn_left() # prepare to try going straight in the next iteration
            
            pick_ball()

Go left wherever you can
''''''''''''''''''''''''

.. questionnote::

  There is only one ball on the table and Karel should take it. Karel will always reach the ball by turning left whenever he can, and going straight when he can't go left (when he cannot go either left or straight, that means he has arrived). Karel is initially turned the way he should, and his first step is always straight forward.

.. karel:: Karel_if_p1_left_p2_forward
   :blockly:

   {
      setup:function() {
         function random(n) {
            return Math.floor(n * Math.random());
         }
         
         var ww = [
            [
               '█████████████',
               '█0.0.0.0.0.0█',
               '█.███████.█.█',
               '█0.0.0.1█0█0█',
               '█████.███...█',
               '█0.0.0.0█0.0█',
               '█████████.███',
               '█E.0.0.0.0.0█',
               '█████████████'
            ],
            [
               '█████████████',
               '█0.0.0.0.0█0█',
               '█..██████.█.█',
               '█0.0█0.0.0█0█',
               '█████..██.█.█',
               '█0.0.0.1█0█0█',
               '█████████..██',
               '█E.0.0.0.0.0█',
               '█████████████'
            ],
            [
               '█████████████',
               '█0.0.0.0.0█0█',
               '█.█.........█',
               '█0█0.0.0.0.0█',
               '█.█.███████.█',
               '█0█0.0.1█0█0█',
               '█.█.█████.█.█',
               '█0.0.0.0.0█N█',
               '█████████████'
            ],
            [
               '█████████████',
               '█S█0.0.0.0█0█',
               '█.███.███...█',
               '█0█0.1█0█..0█',
               '█.███████.█.█',
               '█0.0.0.0.0█0█',
               '█.███████████',
               '█0.0.0.0.0.0█',
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
                  world.setRobotStartDirection("SWEN".charAt(pos));
               }
               let d = w[wy].charCodeAt(wx);
               if (d >= 48 && d < 58) world.putBalls(x, y, d - 48);
            }
         }
         
         var robot = new Robot();
         
         var code = ["from karel import *",
                     "... # write the program",
                     ""];
                     
         return {robot:robot, world:world, code:code};
      },
      
      isSuccess: function(robot, world) {
         return robot.getBalls() > 0;
      }
   }

.. reveal:: Karel_if_p1_left_p2_forward_reveal
    :showtitle: Hint
    :hidetitle: Hide hint

    Instructions for one possible solution:
    
    .. activecode:: Karel_if_p1_left_p2_forward_solution
        :passivecode: true
      
        while you can go forward:
            move forward
            # if there is no path to the left
                # stay turned straight

        take the ball

.. commented out
    .. reveal:: Karel_if_p1_left_p2_forward_reveal
        :showtitle: Solution
        :hidetitle: Hide solution

        .. activecode:: Karel_if_p1_left_p2_forward_solution
            :passivecode: true
          
            from karel import *
            while front_is_clear():
                move()
                turn_left()
                if not front_is_clear():
                    turn_right()

            if is_ball_on_square():
                pick_ball()
