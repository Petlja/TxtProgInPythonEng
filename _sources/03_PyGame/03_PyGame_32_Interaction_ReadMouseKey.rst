Reading mouse buttons
---------------------

Information about the currently pressed mouse buttons is provided by the ``pg.mouse.get_pressed()`` function. This function returns a tuple of three elements (an ordered triple), which are used as logical values. The tuple elements correspond to the left, middle and right mouse buttons respectively. A value of *True* indicates that a button is currently pressed, and *False* that it is not.

The example below shows how to read which mouse buttons are pressed. This is the part of the program where that happens:

.. activecode:: PyGame__interact_put_ball_into_box_part
    :passivecode: true

    pressed_mouse_button = pg.mouse.get_pressed()

    if pressed_mouse_button[2]: # right button - new game
        (x, y) = (width//2, height//2) # return the ball to the center
        won, lost = False, False # the player has neither won nor lost
        
    if pressed_mouse_button[0]: # left button - move the ball
        (xm, ym) = pg.mouse.get_pos() # mouse position coordinates
        # the ball moves away from the mouse for another half of that distance
        x = x - 0.5 * (xm - x)
        y = y - 0.5 * (ym - y)

The *pressed_mouse_button* tuple gets three values returned by the *pg.mouse.get_pressed()* function. We then typically use these values in *if* statements. For example, *if pressed_mouse_button[2]* means "if right button is pressed" (0 for left, 1 for middle, and 2 for right).

Examples and tasks
''''''''''''''''''

.. questionnote::

    **Example - put the ball into the box:** 
    
    While the left mouse button is held pressed, the ball moves away from the cursor. The goal is to put the ball into the red box by moving the mouse and pressing the left button. Pressing the right button returns the game to the beginning.
    
First, study the *new_frame()* function carefully, and then have a look at the other parts of the code as well. Try the program out and see if it works as you expected after reading the description.
    
.. activecode:: PyGame__interact_put_ball_into_box
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :includesrc: src/PyGame/3_Interaction/3b_Mouse_readkey/put_ball_into_box.py    



.. questionnote::

    **Task - to and from the mouse:** 
    
    Complete the program so that it works as shown in the example ("Play task" button).
    
    - When the left mouse button is pressed, the ball should move away from the mouse, as in the "put the ball into the box" example above, but not by half distance, but only by a tenth of the distance to the mouse.
    - When the left mouse button is not pressed, the ball should move closer by one tenth of the distance to the mouse (as in the "towards mouse" task in the previous lesson).
    
.. activecode:: PyGame__interact_to_and_from_mouse
    :nocodelens:
    :modaloutput:
    :playtask:
    :includehsrc: src/PyGame/3_Interaction/3b_Mouse_readkey/to_and_from_mouse.py
    
    import pygame as pg, pygamebg
    (width, height) = (400, 400)
    canvas = pygamebg.open_window(width, height, "Ball following the mouse")

    (x, y) = (width // 2, height // 2) # ball starts from center of the window

    def new_frame():
        global x, y
        
        # ADD THE MISSING PART
        
        # draw a green ball on a white background
        canvas.fill(pg.Color("white")) 
        pg.draw.circle(canvas, pg.Color("green"), (int(x), int(y)), 10)

    pygamebg.frame_loop(50, new_frame)


.. questionnote::

    **Task - laser:** 
    
    Complete the program so that it works as shown in the example ("Play task" button).
    
    While the left mouse button is held pressed, the "laser" is on, otherwise it is off. While the laser is on, its energy decreases by 1 (but not below 0), and when it's off the energy increases by 2 (but not over 100).
    

.. activecode:: PyGame__interact_laser
    :nocodelens:
    :modaloutput:
    :playtask:
    :includehsrc: src/PyGame/3_Interaction/3b_Mouse_readkey/laser.py

    import pygame as pg, pygamebg
    width, height = 400, 400
    canvas = pygamebg.open_window(width, height, "Laser")

    laser_on = False
    energy = 25 # how full is the laser from 0 to 100

    def draw():
        canvas.fill(pg.Color("black")) # background
        
        # the indicator shows how full the laser is
        pg.draw.rect(canvas, pg.Color("green"), (10, 10, 100, 10), 1)
        pg.draw.rect(canvas, pg.Color("green"), (10, 10, energy, 10))
        
        if laser_on:
            reach = (4 * energy, height - 4 * energy)
            pg.draw.line(canvas, pg.Color("red"), (0, height), reach, 5)
        
    def new_frame():
        global energy, laser_on
        
        # READ THE STATE OF THE LEFT MOUSE BUTTON AND SET THE VALUES
        # OF THE GLOBAL VARIABLES energy, laser_on

        draw()

    pygamebg.frame_loop(15, new_frame)


.. commented out

    .. questionnote::

        **Task - background color:** This simple example only illustrates the reading of the mouse buttons status. While the left button is pressed, the background becomes lighter, and while the right button is pressed, the background becomes darker.
        

    .. activecode:: PyGame__interact_bg_color
        :nocodelens:
        :modaloutput:
        :includesrc: src/PyGame/3_Interaction/3b_Mouse_readkey/bg_color.py

