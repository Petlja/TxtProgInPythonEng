Moving the drawing
------------------

In the previous examples, we made several drawings composed of basic shapes. In doing so, it was necessary to determine the correct position for each of these shapes to fit all the pieces together. For some drawings, it was possible (and in some tasks required) that the coordinates of individual points be calculated based on the known coordinates of other points. This computation could have been done outside the program and then the calculated coordinates could just have been entered into the program. However, it is better to perform such calculations in the program itself, for several reasons:

- We may not calculate the coordinates correctly in the first attempt. In such a situation, it is easier to modify the calculation instructions (i.e. the program) than to calculate everything manually from start.
- When we create the drawing ourselves, it may be that after the first version of the program we may want to add something, for example on the left side of the drawing, but that we do not have enough space. In this case, the whole drawing should be moved to the right, so that the *x* coordinates of all points are increased by the same value. If we manually calculated the coordinates of the points, we need to calculate them all again. In a well-organized drawing program, it is sufficient to change one number to move entire drawing to the right. This process may need to be repeated several times until we are happy with the position of the drawn part, so trying it out is a lot easier when the program does the calculation instead of us.
- If we want to draw the same drawing in multiple places in the window, the benefits of computing inside the program come to light again.

We will now systematise the coordinate computation a bit more and use it to move the drawn objects more easily. Before we get started, it would be a good idea to check the background and answer these questions:

.. mchoice:: PyGame__drawing_quiz_point_left
   :answer_a: (50, 60)
   :answer_b: (50, 80)
   :answer_c: (40, 70)
   :answer_d: (60, 70)
   :answer_e: (40, 60)
   :correct: c
   :feedback_a: Try again.
   :feedback_b: Try again.
   :feedback_c: Correct!
   :feedback_d: Try again.
   :feedback_e: Try again.

   What are the coordinates of a point 10 pixels to the left of the point (50, 70)?

.. mchoice:: PyGame__drawing_quiz_point_down
   :answer_a: (50, 60)
   :answer_b: (50, 80)
   :answer_c: (40, 70)
   :answer_d: (60, 70)
   :answer_e: (40, 60)
   :correct: b
   :feedback_a: Try again.
   :feedback_b: Correct!
   :feedback_c: Try again.
   :feedback_d: Try again.
   :feedback_e: Try again.

   What are the coordinates of a point 10 pixels below the point (50, 70)?

.. mchoice:: PyGame__drawing_quiz_rect_up_left
   :answer_a: pg.draw.rect(canvas, color, (70, 120, 50, 60))
   :answer_b: pg.draw.rect(canvas, color, (100, 150, 110, 120))
   :answer_c: pg.draw.rect(canvas, color, (100, 150, 50, 60))
   :answer_d: pg.draw.rect(canvas, color, (70, 120, 80, 90))
   :answer_e: pg.draw.rect(canvas, color, (70, 180, 80, 90))
   :correct: d
   :feedback_a: Try again.
   :feedback_b: Try again.
   :feedback_c: Try again.
   :feedback_d: Correct!
   :feedback_e: Try again.

   The rectangle is drawn using ``pg.draw.rect(canvas, color, (100, 150, 80, 90))``. How can one draw a rectangle of the same size, located 30 pixels to the left and 30 pixels above this rectangle?
   
.. mchoice:: PyGame__drawing_quiz_circle_above
   :answer_a: pg.draw.circle(canvas, color, (100, 120), 40)
   :answer_b: pg.draw.circle(canvas, color, (100, 160), 40)
   :answer_c: pg.draw.circle(canvas, color, (120, 100), 40)
   :answer_d: pg.draw.circle(canvas, color, (160, 100), 40)
   :answer_e: pg.draw.circle(canvas, color, (20, 120), 40)
   :correct: a
   :feedback_a: Correct!
   :feedback_b: Try again.
   :feedback_c: Try again.
   :feedback_d: Try again.
   :feedback_e: Try again.

   The circle is drawn using ``pg.draw.circle(canvas, color, (100, 200), 40)``. How can one draw a circle of the same size above this circle and touching it?


Changes to make a drawing easily movable
''''''''''''''''''''''''''''''''''''''''

Let's see how a cloud is drawn in the following example:

.. activecode:: PyGame__drawing_cloud_fixed
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :includesrc: src\PyGame\1_Drawing\5_Movable\cloud_fixed.py

We presented the cloud with three circles, one larger in the middle and two smaller ones around it:

.. code::

    pg.draw.circle(canvas, pg.Color("white"), (200, 200), 50)
    pg.draw.circle(canvas, pg.Color("white"), (150, 200), 30)
    pg.draw.circle(canvas, pg.Color("white"), (250, 200), 30)

If we wanted to draw that cloud at different heights, we could repeat these three commands, each time with some new value for :math:`y` coordinate of the centers of these three circles instead of 200, as it is in the first drawing. For example:

.. code::

    pg.draw.circle(canvas, pg.Color("white"), (200, 200), 50)
    pg.draw.circle(canvas, pg.Color("white"), (150, 200), 30)
    pg.draw.circle(canvas, pg.Color("white"), (250, 200), 30)

    pg.draw.circle(canvas, pg.Color("white"), (200, 80), 50)
    pg.draw.circle(canvas, pg.Color("white"), (150, 80), 30)
    pg.draw.circle(canvas, pg.Color("white"), (250, 80), 30)
    
    pg.draw.circle(canvas, pg.Color("white"), (200, 320), 50)
    pg.draw.circle(canvas, pg.Color("white"), (150, 320), 30)
    pg.draw.circle(canvas, pg.Color("white"), (250, 320), 30)

.. image:: ../../_images/PyGame/clouds.png
    :width: 400px
    :align: center

In this way, not only does the program grow faster than it has to, we also need to make every change in three places (for example, if we want to try 330 instead of 320, that change should be made in three places). Three changes are not many, but if we adopt this way of doing things, we would have more and more problems in more complex drawings, or in complex programs in general.

Instead, it is better to create a function and pass :math:`y` coordinate of the centers as a parameter:

.. code::

    def cloud(yc):
        pg.draw.circle(canvas, pg.Color("white"), (200, yc), 50)
        pg.draw.circle(canvas, pg.Color("white"), (150, yc), 30)
        pg.draw.circle(canvas, pg.Color("white"), (250, yc), 30)

    cloud(200)
    cloud(80)
    cloud(320)

The new program is easier to read and modify further. For more clouds, or more complex clouds, the advantage of this approach would be even greater.

~~~~

Now let's consider how we should move the cloud to the left or to the right. We should increase or decrease the :math:`x` coordinates of all circles (200, 150, 250) by the same value. For example, if we typed 260, 210, 310 as :math:`x` coordinates, the entire cloud would be moved 60 pixels to the right.

It would be good if we could only use a single number to specify the horizontal position of the cloud. To achieve this, we note that the centers of the smaller circles are 50 pixels away from the center of the middle circle to the left and right. These distances do not change as the cloud moves. This means that if we denote :math:`x` coordinate of the center of the middle circle with :math:`X_c`, then the centers of the smaller circles have :math:`x` coordinates :math:`X_c - 50` and :math:`X_c + 50`. Thanks to this relation (which does not depend on the position of the cloud), we can now also introduce the parameter :math:`x` to the function that draws the cloud:

.. code::

    def cloud(xc, yc):
        pg.draw.circle(canvas, pg.Color("white"), (xc, yc), 50)
        pg.draw.circle(canvas, pg.Color("white"), (xc - 50, yc), 30)
        pg.draw.circle(canvas, pg.Color("white"), (xc + 50, yc), 30)
        
    cloud(200, 200)
    cloud(200, 80)
    cloud(200, 320)

Either of these three clouds could now be easily moved, for example, 60 pixels to the right, by typing 260 as the first parameter instead of 200 in the function calls. It is equally easy to make a drawing with several clouds. Color, or shade of gray, can also be a function parameter. This way, some clouds can be darker and some brighter.

When we use all of the above, we can create a program that draws several clouds of different shades, for example:

.. activecode:: PyGame__drawing_cloud_movable
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :includesrc: src\PyGame\1_Drawing\5_Movable\clouds_movable.py

Let's summarize, with small generalizations, what needs to be done in order to be able to show one drawing in various places:

- We need to select one point whose coordinates are set directly. We call this selected point **the main point**, (sometimes this point is also called **anchor**). In the example of clouds, the main point is the center of the middle circle.
- After selecting the main point, the coordinates of all other significant points are determined in relation to it by adding or subtracting a certain displacement to the coordinates of the main point. In the example with the cloud, to get :math:`x` coordinate of the center of the left circle, from :math:`x` coordinate of the main point (center of the middle circle) we subtract 50 pixels, and for the right circle we add 50 pixels.

In the general case, there may be shapes other than circles in the drawing. The significant points that determine the positions of these shapes are:

- for a line: its ends
- for a polygon: its points
- for a circle: its center
- for a rectangle: its upper left corner
- for an ellipse: the upper left corner of the rectangle in which that ellipse is inscribed

All of these points should be given with respect to the main point, that is, their coordinates should be expressed as coordinates of the main point, increased or decreased by some value.

Check your understanding of the previous explanations and answer the questions.

.. mchoice:: PyGame__drawing_quiz_anchor_introduction1 
   :answer_a: pg.draw.circle(canvas, pg.Color("red"), (x, y), 50, 1)
   :answer_b: pg.draw.circle(canvas, pg.Color("red"), (x+120, y+90), 50, 1)
   :answer_c: pg.draw.circle(canvas, pg.Color("red"), (x+20, y-10), 50, 1)
   :answer_d: pg.draw.circle(canvas, pg.Color("red"), (x-20, y+10), 50, 1)
   :correct: c
   :feedback_a: Try again.
   :feedback_b: Try again.
   :feedback_c: Correct!
   :feedback_d: Try again.

   We want to customize a drawing consisting of several shapes so that everything is drawn relative to the anchor with the coordinates `x = 100`, `y = 100`. One of the statements that form a drawing is
                
   .. activecode:: PyGame__drawing_quiz_anchor_introduction_code1
      :passivecode: true
                    
      pg.draw.circle(canvas, pg.Color("red"), (120, 90), 50, 1)

   What statement should replace the given one?
      
.. mchoice:: PyGame__drawing_quiz_anchor_introduction2
   :answer_a: pg.draw.line(canvas, pg.Color("red"), (x-50, y-50), (150, 150))
   :answer_b: pg.draw.line(canvas, pg.Color("red"), (x-50, y-50), (x+50, y+50))
   :answer_c: pg.draw.line(canvas, pg.Color("red"), (x-50, x+50), (y-50, y+50))
   :answer_d: pg.draw.line(canvas, pg.Color("red"), (x+50, y+50), (x+150, y+150))
   :correct: b
   :feedback_a: Try again.
   :feedback_b: Correct!
   :feedback_c: Try again.
   :feedback_d: Try again.

   We want to customize a drawing consisting of several shapes so that everything is drawn relative to the anchor with the coordinates `x = 100`, `y = 100`. One of the statements that form a drawing is
                
   .. activecode:: PyGame__drawing_quiz_anchor_introduction_code2
      :passivecode: true
                    
      pg.draw.line(canvas, pg.Color("red"), (50, 50), (150, 150))

   What statement should replace the given one?
      
.. mchoice:: PyGame__drawing_quiz_anchor_introduction3
   :answer_a: pg.draw.rect(canvas, pg.Color("red"), (x-50, y-50, x, y))
   :answer_b: pg.draw.rect(canvas, pg.Color("red"), (x, y, 100, 100))
   :answer_c: pg.draw.rect(canvas, pg.Color("red"), (x+50, y+50, 100, 100))
   :answer_d: pg.draw.rect(canvas, pg.Color("red"), (x-50, y-50, 100, 100))
   :correct: d
   :feedback_a: Try again.
   :feedback_b: Try again.
   :feedback_c: Try again.
   :feedback_d: Correct!

   We want to customize a drawing consisting of several shapes so that everything is drawn relative to the anchor with the coordinates `x = 100`, `y = 100`. One of the statements that form a drawing is
                
   .. activecode:: PyGame__drawing_quiz_anchor_introduction_code3
      :passivecode: true
                    
      pg.draw.rect(canvas, pg.Color("red"), (50, 50, 100, 100))

   What statement should replace the given one?
      
.. mchoice:: PyGame__drawing_quiz_move_to_the_right
   :multiple_answers:
   :answer_a: Instead of pg.draw.circle(canvas, color, (x, y), r, d) we call pg.draw.circle(canvas, color, (x+100, y), r, d).
   :answer_b: Instead of pg.draw.circle(canvas, color, (x, y), r, d) we call pg.draw.circle(canvas, color, (x-100, y-100), r, d).
   :answer_c: Instead of pg.draw.rect(canvas, color, (x, y, w, h), d) we call pg.draw.circle(canvas, color, (x+100, y, w+100, h), d).
   :answer_d: Instead of pg.draw.rect(canvas, color, (x, y, w, h), d) we call pg.draw.rect(canvas, color, (x+100, y, w, h), d).
   :answer_e: Instead of pg.draw.rect(canvas, color, (x, y, w, h), d) we call pg.draw.rect(canvas, color, (x-100, y, w, h), d).
   :correct: a, d
   :feedback_a: Correct!
   :feedback_b: Try again.
   :feedback_c: Try again.
   :feedback_d: Correct!
   :feedback_e: Try again.

   We want to move a drawing consisting of several shapes to the right by 100 pixels. Mark the correct claims.

The following are some examples of converting a fixed drawing to a movable one.

Teddy bear - position
'''''''''''''''''''''

The following program, which shows the toy bear's head, is given:

.. activecode:: PyGame__drawing_bear_fixed
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :includesrc: src\PyGame\1_Drawing\5_Movable\teddy-bear_fixed.py





The program calls the *framed_circle* function seven times, which draws the given circle with black border (though it could have been avoided for the three small black circles). To be able to change the position of the drawing, let's select the main point (anchor). Make it the center of a large circle, that is, the heads of the bear. The coordinates of this point are (250, 150). Now we need to express the coordinates of the centers of all other circles relative to the main point. Take the bear's right ear as an example.

:math:`x` coordinate of the center of the right ear is :math:`310 = 250 + 60`, while :math:`y` coordinate is :math:`80 = 150 - 70`. From here we can see that the coordinates of the center of the right ear can be written in the program as `(cx + 60, cy - 70)`, where `(cx, cy)` are the coordinates of the main point. 

Follow the same procedure for the other circles and complete the *draw_teddy* function.

.. activecode:: PyGame__drawing_bear_movable1
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask:
    :includexsrc: src\PyGame\1_Drawing\5_Movable\teddy-bear_movable1b.py

   
    canvas.fill(pg.Color("white")) # paint background
    
    def framed_circle(canvas, color, center, radius):
        pg.draw.circle(canvas, color, center, radius)
        pg.draw.circle(canvas, pg.Color("black"), center, radius, 1)

    def draw_teddy(cx, cy):
        framed_circle(canvas, pg.Color("yellow"), (cx - 60,  cy - 70),  45) # left ear
        # complete the program
        
    draw_teddy(width // 2, height // 2)

    
This program allows us to easily display teddy bears in various places on the screen. For example, the function call

.. code::

    draw_teddy(width // 2, height // 2)
    
which draws a bear with the main point in the center of the window (as it was), can be replaced with the following two:

.. code::

    draw_teddy(width // 2 - 120, height // 2)
    draw_teddy(width // 2 + 120, height // 2)

Try this! It would have been much more difficult to draw another bear if we had not adapted the initial program for this use.

House - position
''''''''''''''''

Let's say you wrote this program, and your goal is to remake the program so that the house can be easily moved:

.. activecode:: PyGame__drawing_house_detailed_fixed
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :includesrc: src\PyGame\1_Drawing\5_Movable\house2D_detailed_fixed.py

Let the main point be: code: `(x, y) = (50, 150)`. Complete the started remodeling of the program in the box below, where the drawing is done in the function :code:`draw_house(x, y, wall_color)`. After making sure that the drawings in the two programs look the same (except that they draw in windows of different sizes), replace the call :code:`draw_house(50, 150, pg.Color (" khaki "))` with the next 4, to get the picture as when clicking the "Play task" button:

.. code::

    draw_house(150,  90, pg.Color(220, 220, 220))
    draw_house(220, 130, pg.Color("white"))
    draw_house(350, 160, (255,255,150))
    draw_house( 50, 150, pg.Color("khaki"))

.. activecode:: PyGame__drawing_house_detailed_movable
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask: 
    :includexsrc: src\PyGame\1_Drawing\5_Movable\house2D_detailed_movable.py
   
    canvas.fill(pg.Color("darkgreen")) # paint background

    def draw_house(x, y, wall_color):
        pg.draw.polygon(canvas, pg.Color("red"), [(x, y), (x+???, y-???), (x+140, y)]) # roof
        pg.draw.rect(canvas, wall_color,       (x,       y,     140, 100)) # walls
        pg.draw.rect(canvas, pg.Color("brown"), (x + ???, y + ???,  30,  30)) # left window
        pg.draw.rect(canvas, pg.Color("brown"), (x + ???, y + ???, ???, ???)) # right window
        pg.draw.rect(canvas, pg.Color("brown"), (x + ???, y + ???, ???, ???)) # door
        
    draw_house( 50, 150, pg.Color("khaki"))




.. commented out

    The task is non-active (commented out) until a related technical issue is resolved.

    Task - a constantly moving drawing
    ''''''''''''''''''''''''''''''''''

    The following function draws some drawing.
       
    .. activecode:: PyGame__drawing_movable_scalable_given
        :passivecode: true

        def draw():
            prozor.fill(pg.Color("white"))
            pg.draw.circle(canvas, pg.Color("blue"), (100, 100), 60)
            pg.draw.circle(canvas, pg.Color("yellow"), (75, 75), 15)
            pg.draw.circle(canvas, pg.Color("black"), (80, 80), 5)
            pg.draw.circle(canvas, pg.Color("yellow"), (125, 75), 15)
            pg.draw.circle(canvas, pg.Color("black"), (120, 80), 5)
            pg.draw.ellipse(canvas, pg.Color("red"), (75, 110, 50, 10))

    In the program that follows, the drawing function is just started. Complete it by drawing the same drawing, but using the anchor :math:`(x, y)`, which is located in the center of the blue circle (initially this is the point :math:`(100, 100)`).

    When you finish the function, make sure it works the same as when you click the "Play task" button.

    .. activecode:: PyGame__drawing_movable
       :nocodelens:
       :enablecopy:
       :modaloutput:
       :playtask:
       :includexsrc: src\PyGame\1_Drawing\5_Movable\movable_scalable.py
       
                     
       def draw():
           canvas.fill(pg.Color("white"))

.. commented out

    .. reveal:: PyGame__drawing_movable_reveal
       :showtitle: Show solution
       :hidetitle: Hide solution

       .. activecode:: PyGame_movable_code
          :passivecode:

          def draw():
              canvas.fill(pg.Color("white"))
              pg.draw.circle(canvas, pg.Color("blue"), (x, y), 60)
              pg.draw.circle(canvas, pg.Color("yellow"), (x-25, y-25), 15)
              pg.draw.circle(canvas, pg.Color("black"), (x-20, y-20), 5)
              pg.draw.circle(canvas, pg.Color("yellow"), (x+25, y-25), 15)
              pg.draw.circle(canvas, pg.Color("black"), (x+20, y-20), 5)
              pg.draw.ellipse(canvas, pg.Color("red"), (x-25, y+10, 50, 10))
           

