Reading mouse position
----------------------

In PyGame, there is an easy way to to read the current state of the mouse. The data we are usually most interested in are mouse position and buttons being pressed. In this lesson we will use mouse position reading, and in the next mouse buttons. Aside from the position and the button presses, there is other information about the mouse that we can get, but we won't do that here. Those interested can find more details for example `here <https://www.pygame.org/docs/ref/mouse.html>`__ .

We can get the mouse position by calling the function ``pg.mouse.get_pos()``, which returns an ordered pair of coordinates of the point where the mouse cursor is currently located.

As we will see in the examples and tasks that follow, the use of this function is very simple, and we can further use the read position of the mouse in various ways.

Examples and tasks
''''''''''''''''''

.. questionnote::

    **Example - a butterfly follows the mouse:** 
    
    In this example, we load two butterfly images and display them alternately, as we did in the animations. What is new is that where we show the butterfly is determined by the mouse position we have obtained from the *pg.mouse.get_pos()* function.

.. image:: ../../_images/butterfly1.png
   :width: 50px
.. image:: ../../_images/butterfly2.png
   :width: 50px

.. activecode:: PyGame__interact_butterfly1
    :nocodelens:
    :modaloutput:
    :includesrc: src/PyGame/3_Interaction/3a_Mouse_readpos/butterfly1.py

You have probably noticed that when you move the mouse faster, the butterfly lags a little. This happens because only 5 frames are displayed per second, so the delay can be up to 0.2 seconds.

This delay is easily eliminated by increasing the frame rate (showing more frames per second), but then the images are switched too often and the butterfly flaps its wings too fast. The solution is to increase the frame rate, while displaying each image during multiple frames.

.. questionnote::

    **Task - move fast, flap slowly:** 
    
    Copy the previous program here, then modify it so that the butterfly does not lag behind the mouse while the flapping speed remains the same.

**Hint:** in order for the butterfly not to lag, we certainly need more frames per second, for example *n* times more. This means that the *new_frame* function is called *n* times more often than before. In order to maintain the same flapping speed, each image needs to be displayed *n* times longer, that is, during *n* consecutive frames.
 
.. activecode:: PyGame__interact_butterfly2
    :nocodelens:
    :modaloutput:
    :playtask:
    :includehsrc: src/PyGame/3_Interaction/3a_Mouse_readpos/butterfly2.py

.. questionnote::

    **Task - towards mouse:** Write a program in which a green ball is moving towards the mouse, like in the example ("Play task" button).
    
**Hint:** In this task the key point is how the coordinates :math:`(x, y)` of the center of the ball change. In a situation like the one in the picture, we want to increase *x* by *dx* and *y* by *dy*. Depending on how we want the ball to move, values *dx*, *dy* can be calculated in different ways. One easy way is to choose :math:`dx = {1 \over 10} (xm - x), dy = {1 \over 10} (ym - y)`.

.. image:: ../../_images/PyGame/towards_mouse.png
   :width: 300px   
   :align: center     

.. activecode:: PyGame__interact_towards_mouse
    :nocodelens:
    :modaloutput:
    :playtask:
    :includehsrc: src/PyGame/3_Interaction/3a_Mouse_readpos/towards_mouse.py



.. questionnote::

    **Task - towards mouse with trace:** Copy the previous program and then modify it so that the ball leaves a gray trace, like in the example ("Play task" button). 
    
**Hint:** The motion of the ball is same as in the previous example. To make a trace, we need to store a list of several (we used 20) previous positions of the ball.

When calculating a new state, we add the most recent position to the list, and if the list has become too long, we delete the oldest position.

When drawing a trace, for each circle we use color *(shade, shade, shade)*, where shade equals 255 (white) before the loop, and in the loop it decreases by a certain value, so that in the last pass through the loop it becomes zero (black), or as close to zero as possible.

So, for example, if the list is called *trace*, these or similar statements should appear in your program:

.. code::

    trace = []
    ...
    
    def new_frame():
        
        ...
        trace.append((x, y))
        ...
        if ...
            trace = trace[1:]


.. activecode:: PyGame__interact_towards_mouse_with_trace
    :nocodelens:
    :modaloutput:
    :playtask:
    :includehsrc: src/PyGame/3_Interaction/3a_Mouse_readpos/towards_mouse_with_trace.py

~~~~

Finally, you can try out the following two programs and play around with them.

In order to make programs like these, in addition to the programming techniques shown here, one needs some knowledge of physics (elastic force, Newton's second law) and mathematics (Pythagorean theorem). Take a look at the programs without having to fully understand them. If you like, try modifying some constants a bit, so you can see how this affects the program's behavior.

.. questionnote::

    **Example: Yо-yо**
    
.. activecode:: PyGame__interact_yoyo
    :nocodelens:
    :modaloutput:
    :includesrc: src/PyGame/3_Interaction/3a_Mouse_readpos/yoyo.py

.. questionnote::

    **Example: Eyes** 

This program also requires a little more knowledge of mathematics, so we will not go into detail. If you are interested in how this program works and you аrе good at math, try to understand the details with some help.


.. activecode:: PyGame__interact_eyes
    :nocodelens:
    :modaloutput:
    :includesrc: src/PyGame/3_Interaction/3a_Mouse_readpos/eyes.py
