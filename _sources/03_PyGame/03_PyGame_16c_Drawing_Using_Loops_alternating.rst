Making more complex drawings using loops
----------------------------------------

The regularity we want to use in the drawings can be more complex, compred to previous problems. Here are some examples:

.. image:: ../../_images/PyGame/repeat_alternating.png 
   :width: 800px
   :align: center 

In all these cases, regularity still exists and can be used when writing programs. We can also observe that the examples in the picture all have something in common, which is that two rules appear alternately. For example, in a brick drawing, the first row of bricks begins with the whole brick, the second with the half brick, the third again with the whole brick, and so on. Similarly, illuminated and tinted windows appear alternately in the building drawing.

Due to the alternation of the two rules in all the drawings, the programs drawing them will also have some similarities. Let's look at code examples.

Example - zipper
''''''''''''''''

To draw such a zipper, we will certainly draw the lines in a loop. The drawing shows that each subsequent line is the same number of pixels lower than the previous one, so there should be no problem with computing the *y* coordinate. The situation with *x* coordinates is somewhat more difficult because they change according to a slightly more complex rule.

We can solve this problem by using the *if* statement in the loop. After drawing one line, we check which of the two possible values :math:`x` coordinate of the beginning of the line has. If it has the first value - we assign it the second and vice versa. Here's what it looks like in the program:

.. activecode:: PyGame_drawing_loops_zipper1
   :nocodelens:
   :enablecopy:
   :modaloutput:
   :includesrc: src\PyGame\1_Drawing\7c_Loops_alternating\Examples\zipper1.py

Another possibility to solve the problem with *x* coordinates is to draw two lines in one loop, for example:

.. activecode:: PyGame_drawing_loops_zipper2
   :nocodelens:
   :enablecopy:
   :modaloutput:
   :includesrc: src\PyGame\1_Drawing\7c_Loops_alternating\Examples\zipper2.py


Example - Bricks
''''''''''''''''

We have already mentioned that the rows of bricks alternately start with the whole brick and half of the brick. That is why when drawing bricks we can use any of the same two ideas as in the previous example.

Let the length of the brick be denoted by: math:`a` and its height by :math:`h`. We get the whole brick at the beginning of the row by drawing a rectangle at a given height, with :math:`x` coordinate equal to zero. Half of a brick at the beginning of a row can be obtained by drawing an entire brick displaced by :math:`a \over 2` to the left, that is, by drawing a rectangle with :math:`x` coordinate equal to :code:`-a // 2`. Thus, only the right half of the brick is visible. It remains to be solved when we draw a displaced brick and when a regular one.

One solution is to store the beginning of the row of bricks in a variable, call it *x_start*. After each line is drawn, we check that the variable *x_start* has a value of zero or :code:`-a // 2`. As in the previous example, whichever of the two values we have, we will assign the other value to the variable, so that in the next row the drawing of the bricks will start differently.

Complete unfinished statements for setting the x_start variable

.. activecode:: PyGame_drawing_loops_bricks1
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask:
    :includexsrc: src\PyGame\1_Drawing\7c_Loops_alternating\Examples\bricks1.py

    canvas.fill(pg.Color("red"))
    brick_a, brick_h = 80, 40
    x_start = 0
    for y0 in range(0, height, brick_h): # For each row of bricks
        for x0 in range(x_start, width, brick_a): # For each brick in the row
            pg.draw.rect(canvas, pg.Color("black"), (x0, y0, brick_a, brick_h), 1)
            
        if x_start == x_start: # fix the line
            x_start = -brick_a//2
        else:
            x_start = x_start # fix the line

The second idea is to draw two bricks in each pass through the double loop: the one which we drew in the first solution, and the brick below and half-left of it. Notice that in this case the loop by *y0* has twice the step, because the inner loop draws two rows of bricks.

Complete unfinished statements for drawing rectangles

.. activecode:: PyGame_drawing_loops_bricks2
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :includexsrc: src\PyGame\1_Drawing\7c_Loops_alternating\Examples\bricks2.py

    canvas.fill(pg.Color("red"))
    brick_width, brick_height = 80, 40
    for y0 in range(0, height, 2 * brick_height):
        for x0 in range(0, width, brick_width):
            # draw the first brick
            pg.draw.rect(???) # complete the statement as before
            
            # the second brick is in the following row, displaced by half its width
            x1, y1 = x0 - brick_width//2, y0 + brick_height 
            pg.draw.rect(???) # draw the brick below and half-left of the previous one


Tasks for exercise
''''''''''''''''''

.. questionnote:: 

    **Task - chessboard**

    Draw a chessboard across the entire window (the board squares should be 50x50 pixels). The lower left square should be dark.

Most of the program is written, try to finish it.

.. activecode:: PyGame_drawing_loops_chessboard
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask:
    :includexsrc: src\PyGame\1_Drawing\7c_Loops_alternating\Tasks\chessboard1.py
    
    canvas.fill(pg.Color("gray")) # background - light squares
    
    # square size
    num_squares = 8
    square_width = width / num_squares
    square_height = height / num_squares

    # go through all the squares
    for i in range(num_squares):
        for j in range(num_squares):
            # paint black squares only
            if (i + j) % 2 != 0:
                pass # fix the statement


.. questionnote::

    **Task - Building**

    Modify the program below so that the windows are drawn in a double loop.

The part that needs to be changed, after the change, can start like this:

.. code::

    for y in range(5):     # floor
        for x in range(2): # side of the building (0 - left, 1 - right)
            if (x+y) % 2 == 0:
                color = ...


.. activecode:: PyGame_drawing_loops_building_alternating
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask:
    :includexsrc: src\PyGame\1_Drawing\7c_Loops_alternating\Tasks\building_alternating.py
    
    pg.draw.rect(canvas, pg.Color("darkgray"), (120, 50, 60, 140)) # building

    # change this part
    pg.draw.rect(canvas, pg.Color('yellow'), (130,  60, 15, 15))
    pg.draw.rect(canvas, pg.Color('black'), (155,  60, 15, 15))
    pg.draw.rect(canvas, pg.Color('black'), (130,  80, 15, 15))
    pg.draw.rect(canvas, pg.Color('yellow'), (155,  80, 15, 15))
    pg.draw.rect(canvas, pg.Color('yellow'), (130, 100, 15, 15))
    pg.draw.rect(canvas, pg.Color('black'), (155, 100, 15, 15))
    pg.draw.rect(canvas, pg.Color('black'), (130, 120, 15, 15))
    pg.draw.rect(canvas, pg.Color('yellow'), (155, 120, 15, 15))
    pg.draw.rect(canvas, pg.Color('yellow'), (130, 140, 15, 15))
    pg.draw.rect(canvas, pg.Color('black'), (155, 140, 15, 15))

    pg.draw.rect(canvas, pg.Color("black"),  (140, 160, 20, 30))   # door

~~~~

If you haven't had any major problems with all these tasks, try to solve one more difficult task as well.

.. questionnote::

    **Task - challenge: parquet**

    Write a program that shows the parquet (you can see the parquet picture when you click the "Play task" button, and the picture is the same as at the beginning of this page, right). The goal, of course, is to draw the floorboards in a multiple loop. The board dimensions are 10x60 and the colors are goldenrod and brown.

The skeleton of the program roughly looks like this:

.. code::

    for row ...
        for column ...
            if ...
                for floorboard in range(6):
                    pg.draw.rect(...)
            else:
                for floorboard in range(6):
                    pg.draw.rect(...)


.. activecode:: PyGame_drawing_loops_parquet
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask:
    :includexsrc: src\PyGame\1_Drawing\7c_Loops_alternating\Tasks\parquet.py
