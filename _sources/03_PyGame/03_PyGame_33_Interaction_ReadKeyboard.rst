Reading keyboard
----------------

Acquiring information about keystrokes on a keyboard is very similar to reading the mouse buttons. Function ``pg.key.get_pressed()`` returns a tuple whose elements are used as logical values, showing for each key on the keyboard whether it is currently being pressed or not.

Because the keyboard has many more keys than the mouse, using indices 0, 1, 2, etc. for certain keys would be impractical. In order not to have to know which index in the tuple corresponds to which key, the PyGame library contains named constants that we use as indices. For example, constants ``pg.K_LEFT``, ``pg.K_RIGHT``, ``pg.K_UP``, ``pg.K_DOWN`` correspond to the frequently used arrow keys. For the space key the corresponding constant is ``pg.K_SPACE``, while for the letter keys, for example *a*, *b*, *c* the corresponding constants would be ``pg.K_a``, ``pg.K_b``, ``pg .K_c`` etc. The complete list of these constants can be seen `here <https://www.pygame.org/docs/ref/key.html>`__ .
 
Examples and tasks
''''''''''''''''''

.. questionnote::

    **Example - Spaceship:** In this example, we have an image of a spaceship, which we move left and right in accordance with the pressed arrow keys. In addition, we can fire from the ship by pressing the space bar key.
    
First, pay attention to the highlighted part of the code with a lighter background (lines 23-37). That part is new here, and it is also commented in more detail in the code itself.

The rest of the program is just animating multiple objects, a technique known from before.

.. image:: ../../_images/spaceship.png
   :width: 50px

.. activecode:: PyGame__interact_spaceship_arrow_keys
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :includesrc: src/PyGame/3_Interaction/3c_Keyboard_read/spaceship_arrow_keys.py

So, after reading the status of all the keys and placing it in the tuple *pressed*, we can simply check the status of the keys we are interested in using *if* statement.


.. questionnote::

    **Task - navigation:** 
    
    Complete the following program so that the 4 arrow keys control the yellow circle, like in the example. The circle should not move if no arrows are pressed and move one pixel in the direction of the arrows that are pressed (opposite arrows cancel each other out).
    

.. activecode:: PyGame__interact_navigtate1
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask:
    :includexsrc: src/PyGame/3_Interaction/3c_Keyboard_read/navigtate1.py

        pressed = pg.key.get_pressed()
        if pressed[pg.K_LEFT] and (x > 0):
            x -= 1
            
        # COMPLETE THE PROGRAM



.. questionnote::

    **Task - snake:** 
    
    Complete the following program so that the arrows can control a 'snake' consisting of several squares, like in the example.
    
    Variables *d_row* and *d_col* indicate the direction of movement of the snake. While no arrows are pressed, the value of these variables does not change and the snake continues to move in the same direction. Your task is to add commands for reading the status of the keyboard and calculating new values for *(d_row, d_col)* based on the arrows pressed, so that the movement continues in the chosen direction.

**Hint:** if the snake's head was in the square *(row, col)*, in the new frame it will be in the square *(row + d_row, col + d_col)*. Check if you understood how you should assign values to the variables *d_red*, *d_kol* for each direction:

.. mchoice:: pygame__interact_quiz_direction
   :answer_a: Up
   :answer_b: Down
   :answer_c: Left
   :answer_d: Right
   :correct: c
   :feedback_a: No, values for up are (d_row, d_col) = (-1, 0)
   :feedback_b: No, values for down are (d_row, d_col) = (1, 0)
   :feedback_c: Correct
   :feedback_d: No, values for right are (d_row, d_col) = (0, 1)

   If variables (d_row, d_col) are assigned values (0, -1), in which direction does the movement continue?

.. activecode:: PyGame__interact_snake
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask:
    :includexsrc: src/PyGame/3_Interaction/3c_Keyboard_read/snake.py
    
        # HERE CALCULATE THE DISPLACEMENT (d_row, d_col)
        # BASED ON THE KEYS PRESSED


Questions
'''''''''

As you answer the questions, go back to the "snake" program as needed and look up the parts you need to answer.

.. fillintheblank:: pygame__interact_quiz_snake_tablesize

    How many rows does the board have?

    - :40: Correct!
      :[0-9]+: Look at the beginning of the program more carefully.
      :.*: The answer should be written in digits.

.. mchoice:: pygame__interact_quiz_snake_rowcol_to_xy
   :answer_a: x = row*a + a, y = col*a + a
   :answer_b: x = col*a + a, y = row*a + a
   :answer_c: x = row*a, y = col*a
   :answer_d: x = col*a, y = row*a
   :correct: d
   :feedback_a: Try again
   :feedback_b: Try again
   :feedback_c: Try again
   :feedback_d: Correct

   What are the coordinates of the top left corner of the square *(row, col)*?

.. mchoice:: pygame__interact_quiz_snake_head
   :multiple_answers:
   :answer_a: In each frame list 'snake' is extended by a new element representing the new position of the snake's head.
   :answer_b: List 'snake' has the same number of elements throughout the program.
   :answer_c: One element which represents the end of the snake's tail is removed from list 'snake' in each frame.
   :correct: b
   :feedback_a: There is no such command in the program
   :feedback_b: Correct
   :feedback_c: There is no such command in the program

   Which sentences are true?
    

.. commented out

    chase_and_avoid.py
