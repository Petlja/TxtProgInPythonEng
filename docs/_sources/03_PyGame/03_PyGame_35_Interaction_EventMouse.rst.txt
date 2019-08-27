Mouse events
------------

In the "switch" example we have shown how we can react in a program when the user presses a mouse button. Although for the user a click seems like a single action, we have seen that for the computer it is a sequence of events that starts with an event of the type *pg.MOUSEBUTTONDOWN*.

In the following examples and tasks, we will use three types of mouse-generated events:

- Pressing any mouse button (like in the example with the switch), in which case *event.type* has a value of *pg.MOUSEBUTTONDOWN*
- Releasing a mouse button, in which case *event.type* has a value of *pg.MOUSEBUTTONUP*
- Moving the mouse, in which case *event.type* has a value of *pg.MOUSEMOTION*. In fact, when moving the mouse multiple such events are generated (each of them describing a small mouse movement in a very short time interval, so each event of this kind usually describes a movement of only a few pixels).

Event objects whose type is *pg.MOUSEBUTTONDOWN* also contain some additional information, such as:

- *event.pos* - the position of the mouse at the time of registering the event (already used in the switch example)
- *event.button* - a number from 1 to 5 indicating which mouse button is pressed (1 - left, 2 - middle, 3 - right, 4 - scroll up, 5 - scroll down)

Some of the additional event data contained in *pg.MOUSEMOTION* event objects are:

- event.pos - the position of the mouse after the mouse motion event
- event.rel - an ordered pair that describes how much the mouse position has changed since the previous mouse motion event
- event.buttons - a three-element list of logical values, which determine for each of the three mouse buttons (0 - left, 1 - middle, 2 - right) whether it was pressed during mouse movement.

Click processing - exercises
''''''''''''''''''''''''''''

You may not have noticed that in the "switch" program from the previous lesson, the light can be turned on and off by clicking any mouse button. This is because the same type of event is generated for each mouse button, and we did not check which button was pressed when the event occurred.

.. questionnote::

    **Task - left button as a switch:** 
    
    Copy the "switch" program here, then modify it so that the light can be switched on and off only with the left mouse button.

**Hint:** Use *event.button* data.

.. activecode:: PyGame__interact_switch_left_button
    :nocodelens:
    :enablecopy:
    :playtask:
    :modaloutput:
    :includehsrc: src/PyGame/3_Interaction/3d_Mouse_events/Switch_left_button.py




.. questionnote::

    **Task - three switches:** 
    
    Use parts of the "switch" program and create a program that simulates the work of three switches, as shown in the example.

.. image:: ../../_images/Shema3_Off.png
   :width: 50px
.. image:: ../../_images/Shema3_On.png
   :width: 50px
.. image:: ../../_images/SwitchOff.png
   :width: 50px
.. image:: ../../_images/SwitchOn.png
   :width: 50px
.. image:: ../../_images/BulbOff.png
   :width: 50px
.. image:: ../../_images/BulbOn.png
   :width: 50px

.. activecode:: PyGame__interact_switches
    :nocodelens:
    :enablecopy:
    :playtask:
    :modaloutput:
    :includehsrc: src/PyGame/3_Interaction/3d_Mouse_events/Switches.py

    import pygame as pg, pygamebg
    (width, height) = (800, 500)
    canvas = pygamebg.open_window(width, height, "Switches")

    schema_images = (pg.image.load('Shema3_Off.png'), pg.image.load('Shema3_On.png'))
    switch_images = (pg.image.load('SwitchOff.png'), pg.image.load('SwitchOn.png'))
    bulb_images = (pg.image.load('BulbOff.png'), pg.image.load('BulbOn.png'))

    switch_on = [False, False, False]
    switch_pos = [(100, 200), (300, 150), (300, 250)]
    bulb_pos = (500, 100)
    
    # finish the program

Other mouse events
''''''''''''''''''

As it was mentioned at the beginning of this lesson, a program can also respond to mouse button release and mouse motion events. To do that, it is necessary to compare the value of *event.type* with the constants *pg.MOUSEBUTTONUP* and *pg.MOUSEMOTION*. The following are tasks where you can try this out.

.. questionnote::

    **Task - drawing lines:** 
    
    Complete the program so that it can draw straight lines, as in the example.

.. activecode:: PyGame__interact_mouse_lines1
    :nocodelens:
    :enablecopy:
    :playtask:
    :modaloutput:
    :includehsrc: src/PyGame/3_Interaction/3d_Mouse_events/mouse_lines1.py

    import pygame as pg, pygamebg
    (width, height) = (400, 400)
    canvas = pygamebg.open_window(400, 400, "Lines with mouse")

    mosue_pos = (0, 0)
    line_start = mosue_pos
    line_is_being_drawn = False
    previous_lines = []

    def new_frame():
        canvas.fill(pg.Color("white")) # paint canvas
        if line_is_being_drawn:
            pg.draw.line(canvas, pg.Color('black'), line_start, mosue_pos)

        for a, b in previous_lines:
            pg.draw.line(canvas, pg.Color('black'), a, b)


    def handle_event(event):
        global line_is_being_drawn, line_start, mosue_pos

        
        # add statements here that work as follows:
        
        # if the event type is "mouse button down":
        #     the line drawing mode is switched on
        #     we start the line at the current position of the mouse
        # otherwise, if the event type is "mouse button going up":
        #     the line drawing mode is switched off
        #     the new line is from the memorized start of the line to the current position of the mouse
        #     add a new line to the list of previous lines
        # otherwise, if the event type is "moving mouse":
        #     in the mouse_pos variable, remember the current position of the mouse

    pygamebg.frame_loop(30, new_frame, handle_event)






.. questionnote::

    **Task - drawing lines with deletion:**

    Copy the program for drawing lines below, then add an ability to delete all lines with a right-click.

**Hint:** To distinguish between left and right mouse buttons in the program, the *event.button* data must be used again. The code in the *handle_event* function should now look something like this:

.. activecode:: PyGame__interact_mouse_lines2_part
    :passivecode: true

        if the event type is "mouse button going down":
            if button 1 (left button) is pressed
                the line drawing mode is switched on
                the new line is from the memorized start of the line to the current position of the mouse
            if button 3 (right button) is pressed
                empty the list of previous lines
        otherwise, if the event type is "releasing mouse button":
            if button 1 (left button) is pressed
                the line drawing mode is switched off
                the new line is from the memorized start of the line to the current position of the mouse
                add a new line to the list of previous lines
        otherwise, if the event type is "move mouse":
            remember the current position of the mouse in the mouse_pos variable 


.. activecode:: PyGame__interact_mouse_lines2
    :nocodelens:
    :enablecopy:
    :playtask:
    :modaloutput:
    :includehsrc: src/PyGame/3_Interaction/3d_Mouse_events/mouse_lines2.py




.. questionnote::

    **Task - dragging:** 
    
    The following program shows how to allow the user of the program to drag objects.
    
    Try the program out (drag the apples into the basket) and try to understand it, then answer the questions below.

.. image:: ../../_images/apple.png
   :width: 50px
.. image:: ../../_images/basket.png
   :width: 50px
.. image:: ../../_images/drag_scene.png
   :width: 50px

.. activecode:: PyGame__interact_drag
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :includesrc: src/PyGame/3_Interaction/3d_Mouse_events/drag.py

.. mchoice:: pygame__interact_quiz_drag1
   :answer_a: the index of the apple we are drawing
   :answer_b: the index of the apple we are dragging
   :answer_c: total number of apples
   :answer_d: the number of apples remaining on the tree
   :correct: b
   :feedback_a: Try again
   :feedback_b: Correct
   :feedback_c: Try again
   :feedback_d: Try again

   What is the *i_apple* variable in the program? 

.. dragndrop:: pygame__interact_quiz_drag2
    :feedback: Try again!
    :match_1: if mouse_is_on_image(event.pos, basket_pos, basket_image):|||whether the apple should be deleted
    :match_2: if mouse_is_on_image(event.pos, apple_positions[i]|||whether the user "took" the apple
    :match_3: if len(apple_positions) == 0:|||whether the game is over
    :match_4: if i_apple >= 0:|||whether a drag is ongoing

    Pair the checks in the program with their meaning.

.. mchoice:: pygame__interact_quiz_drag3
   :answer_a: we read if a mouse button is down during movement
   :answer_b: dragging is a separate type of event
   :answer_c: when plain moving the mouse, the index of the "apple we are dragging" is -1
   :correct: c
   :feedback_a: This is not a convenient way, since the button can be pressed in an empty space (the user did not "take" the object to be dragged)
   :feedback_b: No, there is no such type of event
   :feedback_c: Correct

   How do we distinguish between dragging and plain mouse movement in a program? 
