Moving multiple objects
-----------------------

So far, we have made animations in which various objects were moving (car, billiard ball, plane, text), but in each of these programs there was only one moving object. For the global variables that describe the scene we used the coordinates of that moving object, and sometimes we also used other values, such as displacement, direction of motion, and so on.

The movement of multiple objects is not fundamentally different from the movement of a single object - we will simply need to track values that describe movement for all of the objects. For example, we can represent each object with a tuple of values describing it, and keep all such tuples in a list.

Balls
'''''

In the following example we will see animated motion of several balls. Each ball is represented by a :math:`(x, y, dx, dy, r, color)` tuple, where :math:`x, y` are the coordinates of the center of the ball, :math:`dx, dy` are the displacements of the ball per coordinate, :math:`r` is the radius, and :math:`color` is the color of the ball. All such tuples are placed in the list *balls*.

When unpacking a tuple from a list element (command ``x, y, dx, dy, r, color = balls[i]``), as well as when returning it to the list (command ``balls[i] = (x, y, dx, dy, r, color)``), we should mind the order of the variables.

In the example, we use the ``random`` module to create the balls in order to get random selections (imported using the *import* command). The ``random.randint(a, b)`` function returns a random integer between *a* and *b* (including boundaries), and the ``random.choice(a)`` function returns a random element from the collection *a*.

.. activecode:: PyGame__anim_balls_bouncing
    :nocodelens:
    :modaloutput:
    :includesrc: src/PyGame/2_Animation/2e_Anim_Multiple/balls_bouncing.py

If we compare this program to the animation of motion of a billiard ball, we will notice a great similarity. The *new_frame* function is essentially different only in that now all actions (moving, bouncing, drawing) are done in a loop, since they need to be done for each ball. Setting the initial state is also somewhat more complicated, as there are more objects and we store multiple data for each of them, and we also use random choices.

~~~~

In the previous example, all objects (balls) are present from the beginning to the end of the program. There are situations when we want some objects to cease to exist during program execution, or some new objects to appear (or both). In such cases, we can use an auxiliary list in the *new_frame* function in which we will put values that describe the new state. A typical sequence of activities is as follows:

- create a new blank list at the beggining of the *new_frame* function
- we go through the list of existing tuples, change them, and add the ones that we still need to the new list
- if needed, supplement the list with new tuples
- finally, we update the global list by putting in values from the new, auxiliary list

Let's look at an example.

Stars
''''''

In this example, we simulate moving through space. The stars we encounter are represented with white circles and are determined by their position and radius.

For each frame, we compute a new auxiliary list that describes the next state. We move the stars following some rule, and we copy those that have not completely left the window to the next state list. After processing existing stars, we add new stars to the next state list so that the total number of stars would not decrease. Finally, we move all the stars to the global list so that we can calculate the next frame later.

.. activecode:: PyGame__anim_trough_stars
    :nocodelens:
    :modaloutput:
    :includesrc: src/PyGame/2_Animation/2e_Anim_Multiple/trough_stars.py

This example is given primarily to introduce a different way of working with a list of tuples that describe a scene. Because of that, some interesting details were left in the background. Let us look a bit at those, in this context, side details. To get the effect of approaching, the stars in front of us should move apart and magnify. Therefore, in the program, the values of *x* and *y* change so that the stars move from the center of the window to the edges, moving faster as they go further away from the center.

It's not particularly important that you fully understand the commands that change the values of *x*, *y*, and *r* in order to learn programming, but you can try out how the animation changes when you slightly alter the coefficients in those commands (for example, stars can be moving slower, or growing faster).


Tasks
'''''

.. questionnote::

    **Snowflakes:** Complete the program so that it works as shown in the example ("Play Task" button). 
    
    Each snowflake is described with only two numbers, its coordinates, so the tuples we will use will actually be pairs :math:`(x, y)`. 
    
    Snowflakes fall 1 pixel at a time, and those that go out of the window are replaced with new snowflakes. Forming a new state is similar to that of the "stars" program, only the rules for moving snowflakes are simpler. 
    
    The snowflakes in the initial set are selected anywhere in the window, and the ones that are added later are selected somewhere on the top edge of the window.
    
.. image:: ../../_images/snowflake.png
   :width: 50px
    
.. activecode:: PyGame__anim_snowflakes
    :nocodelens:
    :modaloutput:
    :playtask:
    :includehsrc: src/PyGame/2_Animation/2e_Anim_Multiple/snowflakes.py

    import random, pygame as pg, pygamebg
    (width, height) = (800, 400)
    canvas = pygamebg.open_window(width, height, "Snowflakes")

    snowflake_image = pg.image.load("snowflake.png")  # a snowflake image
    snowflake_height = snowflake_image.get_height()
    num_flakes = 10 # total number of the snowflakes


.. questionnote::

    **Outgoing balls:** Copy the first program (balls) here, and modify it so that the balls do not bounce but continue to move away, and the ones that go off get replaced with new balls. This program is a combination of the two given examples (balls and stars), so try to use parts from both of these programs.

.. activecode:: PyGame__anim_balls_passing
    :nocodelens:
    :modaloutput:
    :playtask:
    :includehsrc: src/PyGame/2_Animation/2e_Anim_Multiple/balls_passing.py


.. questionnote::

    **Gliding text** Try out the program and try to understand how it works. Try altering something in the program (the text being displayed, the color in which the text is being displayed, the speed at which the text moves, or any other detail).
    
    Challenge: Try to modify the program so that the text glides down instead of up.

.. activecode:: PyGame__anim_gliding_text
    :nocodelens:
    :modaloutput:
    :includesrc: src/PyGame/2_Animation/2e_Anim_Multiple/gliding_text.py
