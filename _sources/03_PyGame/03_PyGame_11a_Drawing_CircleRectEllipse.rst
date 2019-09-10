Drawing rectangles, ellipses, and circles
-----------------------------------------

All drawing functions in the PyGame library begin with ``pg.draw``. Depending on what shape we want to draw, we call different functions. In the explanations that follow, the meaning of the parameters is:

- The *canvas* parameter is the area in which we draw. In this guide, programs will already have a formed variable (more specifically object) *canvas*, obtained as the result from a call of the ``pygamebg.open_window`` function.
- The *color* parameter is the color we use to draw. As it was said earlier, a color can be specified by its name (for example :code:`pg.Color("black")`), or as a tuple or a list of 3 elements (for example :code:`[255, 0, 0]` for red).
- The *rectangle* parameter is a tuple or a list of four elements :math:`(x, y, w, h)` or :math:`[x, y, w, h]`, that describes a rectangle, as explained earlier (coordinates of the top-left vertex, rectangle width and height).
- The *center* parameter represents a point. As mentioned earlier, a point can be specified as a tuple (or list) of 2 elements, which represent the coordinates of the point in the window in which we draw.
- The *thickness* parameter is thickness of the lines we use to draw. In the functions we explain here, this parameter is optional and can be omitted.

We will now see more detailed descriptions of the functions for drawing rectangles, ellipses, and circles. A brief example of one or two lines of code is given after each function description. You can run each of these examples by copying it to the program below (which doesn't draw anything for now). The pictures that follow the examples are obtained in that same way.


.. activecode:: pygame__drawing_primirives_def
    :nocodelens:
    :modaloutput: 

    import pygame as pg, pygamebg
    canvas = pygamebg.open_window(200, 200, "Pygame")

    canvas.fill(pg.Color("gray"))

    pygamebg.wait_loop()

Drawing a rectangle
'''''''''''''''''''

To draw a rectangle we use the function ``pg.draw.rect``, which has two forms:

.. code::

    pg.draw.rect(canvas, color, rectangle, thickness)
    pg.draw.rect(canvas, color, rectangle)

We use the form without the *thickness* parameter when we want the rectangle's interior to be filled with the indicated color as well.

For example, the first of the following two statements means:

- draw a rectangle (function *rect*)
- paint it black (parameter (0, 0, 0) specifies black color) 
- The top-left vertex of the rectangle has coordinates (40, 80)
- the width of the rectangle is 50 and the height is 30 pixels
- only frame of the rectangle is to be drawn and the lines should be 3 pixels thick

The second statement means:

- draw a rectangle (function *rect*)
- paint it black (parameter pg.Color("black") also specifies black color) 
- The top-left vertex of the rectangle has coordinates (140, 80)
- the rectangle is to be 20 pixels both wide and high, so it will actually be a square
- The square will be filled with color since there is no thickness parameter

.. activecode:: pygame__drawing_rectangles_def
    :passivecode: true
    
    pg.draw.rect(canvas, (0, 0, 0), (40, 80, 50, 30), 3)
    pg.draw.rect(canvas, pg.Color("black"), (140, 80, 20, 20))

.. image:: ../../_images/PyGame/drawing_rectangles.png
   :width: 200px   
   :align: center 

Drawing an ellipse
''''''''''''''''''

To draw an ellipse, we use the function ``pg.draw.ellipse``, with or without the thickness parameter:

.. code::

    pg.draw.ellipse(canvas, color, rectangle, thickness)
    pg.draw.ellipse(canvas, color, rectangle)

The *rectangle* parameter represents the rectangle the ellipse is inscribed in, and the other parameters have the same meaning as before. If we need it, we can calculate the center and major and minor semi-axes of the ellipse using the tuple :math:`(x, y, w, h)` or list :math:`[x, y, w, h]` that defines the rectangle. The coordinates of the center of the rectangle, which is also the center of the ellipse, are :math:`(x + w/2, y + h/2)`, and the major and minor semi-axes of the ellipse are :math:`w/2` and :math:`h/2`. So, for example, statement

.. activecode:: pygame__drawing_ellipse_def
    :passivecode: true

    pg.draw.ellipse(canvas, pg.Color("yellow"), (100, 160, 60, 40))

draws a yellow filled ellipse. The center of the ellipse is the center of the specified rectangle, which is at point (130, 180). The horizontal semi-axis of the ellipse is 30 pixels long, and the vertical 20.

.. image:: ../../_images/PyGame/drawing_ellipse.png
   :width: 200px   
   :align: center 

Drawing a circle
''''''''''''''''

To draw a circle, we use the function ``pg.draw.circle``, with or without the thickness parameter:

.. code::

    pg.draw.circle(canvas, color, center, radius, thickness)
    pg.draw.circle(canvas, color, center, radius)

The *center* parameter is a point representing the center of the circle, and the *radius* parameter is a number representing the radius of the circle in pixels. For example, the following statement draws a red circle, 3 pixels thick, of radius 50 pixels, whose center is at point (100, 100):

.. activecode:: pygame__drawing_circle_def
    :passivecode: true

    pg.draw.circle(canvas, pg.Color("red"), (100, 100), 50, 3)

.. image:: ../../_images/PyGame/drawing_circle.png
   :width: 200px   
   :align: center 

If the last parameter (stroke width 3) had been omitted, the interior of the circle would have been red as well.

Drawing rectangles, ellipses and circles - questions
''''''''''''''''''''''''''''''''''''''''''''''''''''

Check how much you understand and remember about these drawing functions:

.. mchoice:: pygame__drawing_quiz_circle_arglist
   :multiple_answers:
   :answer_a: Top-left vertex coordinates
   :answer_b: Radius
   :answer_c: Center coordinates
   :answer_d: Width and height
   :answer_e: Color
   :correct: b, c, e
   :feedback_a: Top-left vertex coordinates are specified when drawing an ellipse or a rectangle
   :feedback_b: Correct
   :feedback_c: Correct 
   :feedback_d: Width and height are specified when drawing an ellipse or a rectangle
   :feedback_e: Correct

   What needs to be specified when drawing a circle?

.. mchoice:: pygame__drawing_quiz_circle_right_args
   :answer_a: pg.draw.circle(canvas, color, 100, 100, 30, 5)
   :answer_b: pg.draw.circle(canvas, color, (100, 100), 30, 5)
   :answer_c: pg.draw.circle(canvas, color, (100, 100, 30, 5))
   :answer_d: pg.draw.circle(canvas, color, (100, 100), (30, 5))
   :correct: b
   :feedback_a: Try again
   :feedback_b: Correct
   :feedback_c: Try again
   :feedback_d: Try again

   To draw a circle centered at point :math:`(100, 100)`, whose radius is :math:`30` pixels, using line :math:`5` pixel wide, which function call needs to be made?

.. mchoice:: pygame__drawing_quiz_circle_opt_arg
   :answer_a: the latter draws an ellipse whose semi-major and semi-minor axes equal r and 1.
   :answer_b: the latter fills the circle interior with color.
   :answer_c: the former draws a disk (filled circle), and the latter a circular line.
   :answer_d: the former draws a circular line, and the latter a disk (filled circle).
   :correct: c
   :feedback_a: Try again
   :feedback_b: Try again
   :feedback_c: Correct
   :feedback_d: Try again

   The difference between `pg.draw.circle(canvas, color, (cx, cy), r)` and `pg.draw.circle(canvas, color, (cx, cy), r, 1)` is that:

.. mchoice:: pygame__drawing_quiz_rect_args_1
   :answer_a: Top-left vertex coordinates
   :answer_b: Stroke width
   :answer_c: Width
   :answer_d: Height
   :answer_e: Center coordinates
   :correct: e
   :feedback_a: Try again
   :feedback_b: Try again
   :feedback_c: Try again
   :feedback_d: Try again
   :feedback_e: Correct

   What is NOT specified when drawing a rectangle?

.. mchoice:: pygame__drawing_quiz_rect_args_2
   :answer_a: pg.draw.rect(canvas, color, 100, 100, 30, 50)
   :answer_b: pg.draw.rect(canvas, color, (100, 100), (30, 50))
   :answer_c: pg.draw.rect(canvas, color, (100, 100), 30, 50)
   :answer_d: pg.draw.rect(canvas, color, (100, 100, 30, 50))
   :correct: d
   :feedback_a: Try again
   :feedback_b: Try again
   :feedback_c: Try again
   :feedback_d: Correct

   To draw a rectangle whose top-left vertex is at point 
   :math: `(100, 100)`, :math:`30` pixels wide and :math:`50` 
   pixels high, which function call needs to be made?

.. mchoice::  pygame__drawing_quiz_rect_args_3
   :answer_a: pg.draw.rect(canvas, color, (80, 80, 50, 80))
   :answer_b: pg.draw.rect(canvas, color, (80, 80), (130, 160))
   :answer_c: pg.draw.rect(canvas, color, (80, 80, 130, 160))
   :answer_d: pg.draw.rect(canvas, color, (80, 80), (50, 80))
   :correct: a
   :feedback_a: Correct
   :feedback_b: Try again
   :feedback_c: Try again
   :feedback_d: Try again

   To draw a rectangle whose top-left vertex is at point
   :math:`(80, 80)`, and bottom-right vertex at point 
   :math:`(130, 160)`, which function call needs to be made:

Drawing by instructions
'''''''''''''''''''''''

In the following tasks, you can see what your program should draw by clicking the "Play task" button. To provide you necessary information to write the statements you need, detailed instructions with descriptions of the parameters are also given.

Keep in mind that before drawing you should paint the background with the appropriate color, for which you use the statement ``canvas.fill(pg.Color(...))`` (instead of the dots specify a color).

.. questionnote::

    **Task - target:** 
    
    Draw a target on a white background using three filled circles. The centers of all three circles should be at the center of the window and all circles should be filled with color. First, draw a red circle of radius 100, then a blue one of radius 75, and then a green circle of radius 50 pixels.
    
What do you think, could these circles be drawn in a different order? If you are not sure what would happen if the order changed, give it a try.

.. activecode:: PyGame__drawing_target
   :nocodelens:
   :enablecopy:
   :modaloutput:
   :playtask:
   :includexsrc: src/PyGame/1_Drawing/1_BasicExamples/target.py

.. questionnote::

    **Task - duckling:** 
    
    On a green background, draw a duckling as a cartoon character. The drawing consists of the following parts:
    
    - Head: a yellow filled ellipse, inscribed in a 320 x 300 pixel rectangle, with the top left vertex at point (40, 50)
    - Head border: a black ellipse framing the previous ellipse with a line of width 1
    - Left eye: a black filled ellipse, inscribed in a 40 x 40 pixel rectangle with the top left vertex at point (130, 130)
    - Right eye: a black filled ellipse, inscribed in a 40 x 40 pixel rectangle, with the top left vertex at point (280, 120)
    - Mouth (beak): a red filled ellipse, inscribed in a 120 x 140 pixel rectangle, with the top left vertex at point (200, 170)
    - Mouth border: a black ellipse framing the previous ellipse with a line of width 1

Here we have more freedom with the drawing order, but we still need to follow some order. Try to explain which parts of the image need to be drawn exactly in this order, and which need not.

Note that the eyes are inscribed in rectangles that are actually squares. How (thanks to this) can we draw the same eyes in a different way?

.. activecode:: PyGame__drawing_duckling
   :nocodelens:
   :enablecopy:
   :modaloutput:
   :playtask:
   :includexsrc: src/PyGame/1_Drawing/1_BasicExamples/duckling.py

