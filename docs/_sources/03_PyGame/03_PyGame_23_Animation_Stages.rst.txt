Animation by stages
-------------------

Traffic light
'''''''''''''

One of the best known examples of a device that works by stages is a traffic light. In the example of the traffic light we will explain working by stages and how we can animate events that take place in stages on a computer.

There are several states in which a traffic light can be. For example, it can display red light, flashing yellow light, be turned off, etc. We shall call a period during which the traffic light does not change its state a stage. In normal operation of the traffic light, the stages alternate cyclically and each stage has its own duration. For example, take a traffic light for which the following four stages alternate: 1 - red light, 2 - red and yellow light, 3 - green light, and 4 - yellow light.

To make the animation simpler, we will express the duration of each stage in the number of frames (instead of seconds). Let the durations of the said stages be :math:`n_1`, :math:`n_2`, :math:`n_3` and :math:`n_4` frames respectively. Then the whole cycle lasts :math:`N = n_1 + n_2 + n_3 + n_4` frames. Of these :math:`N` frames, the first :math:`n_1` belong to the first stage, the next :math:`n_2` to the second stage etc.

To know which stage the current frame belongs to, we can introduce a global variable that will count the frames. Since the whole cycle lasts :math:`N` frames, it is enough to count by modulus :math:`N`. This means that when the frame counter reaches the value :math:`N-1`, the next value is zero (we only count within one cycle). In this case, for values from 0 to :math:`n_1 - 1`, the frame belongs to the first stage, for values from :math:`n_1` to :math:`n_1 + n_2 - 1` to the second stage, for values from :math:`n_1 + n_2` to :math:`n_1 + n_2 + n_3 - 1` to the third stage, and for values from :math:`n_1 + n_2 + n_3` to :math:`N-1` to the fourth stage.

Here's what a program based on this logic might look like:

.. activecode:: PyGame__anim_stages_traffic_lights1
    :nocodelens:
    :modaloutput:
    :includesrc: src/PyGame/2_Animation/2c_Anim_Stages/TrafficLights1.py

Tasks
'''''

.. questionnote::

    **Stage Five:** Copy the previous program, then insert a stage for flashing green light, after the green light and before the yellow light (as shown in the example - "Play Task" button).
    
**Hint:** In the fifth phase, we will not have a single call to the *draw_trafficlights* function, but rather a piece of code that looks something like this:

.. code::

        if i_frame % 2 == 0:
            draw_trafficlights(...)
        else:
            draw_trafficlights(...)


.. activecode:: PyGame__anim_stages_traffic_lights1a
    :nocodelens:
    :modaloutput:
    :playtask:
    :includehsrc: src/PyGame/2_Animation/2c_Anim_Stages/TrafficLights1a.py

.. questionnote::

    **Plane:** Write a program that works as shown in the example ("Play Task" button). 
    
    Movement description: the plane starts from the center of the left edge of the window. First it moves for 20 frames 2 pixels right and up, then 20 frames 2 pixels right and down. When it comes out through the right edge of the window, it appears at the same height on the left edge. Frame rate is 50 frames per second.

.. image:: ../../_images/airplane.png
   :width: 50px
.. image:: ../../_images/sun.png
   :width: 50px

.. activecode:: PyGame__anim_stages_plane
    :nocodelens:
    :modaloutput:
    :playtask:
    :includehsrc: src/PyGame/2_Animation/2c_Anim_Stages/airplane.py
    
    import pygame as pg, pygamebg
    (width, height) = (800, 350)
    canvas = pygamebg.open_window(width, height, "Plane")
    
    def new_frame():
        pass
    
    pygamebg.frame_loop(50, new_frame)


    sun_image = pg.image.load("sun.png")        # image of the sun
    plane_image = pg.image.load("airplane.png") # image of the plane
    plane_width = plane_image.get_width()       # plane image width
    plane_height = plane_image.get_height()     # plane image height

    # finish the program


.. questionnote::

    **Mole:** Write a program that works as shown in the example ("Play Task" button).  
    
    10 images are loaded with the mole coming out of the hole a bit more in each image. The cycle has four stages lasting 28 frames in total.
    
    - Stage one lasts 10 frames and during this stage the mole is coming out of the hole (the images are shown in order, from first to tenth).
    - Stage two lasts 5 frames during which the mole is in the highest position (the tenth image is shown).
    - Stage three lasts 10 frames and during this stage the mole is coming into the hole (the images are shown from tenth to first).
    - Stage four lasts 3 frames and during it the mole is in the hole (the first image is shown).

.. image:: ../../_images/mole1.png
   :width: 50px
.. image:: ../../_images/mole2.png
   :width: 50px
.. image:: ../../_images/mole3.png
   :width: 50px
.. image:: ../../_images/mole4.png
   :width: 50px
.. image:: ../../_images/mole5.png
   :width: 50px
.. image:: ../../_images/mole6.png
   :width: 50px
.. image:: ../../_images/mole7.png
   :width: 50px
.. image:: ../../_images/mole8.png
   :width: 50px
.. image:: ../../_images/mole9.png
   :width: 50px
.. image:: ../../_images/mole10.png
   :width: 50px

.. activecode:: PyGame__anim_stages_mole
    :nocodelens:
    :modaloutput:
    :playtask:
    :includehsrc: src/PyGame/2_Animation/2c_Anim_Stages/mole.py

    import pygame as pg, pygamebg
    (width, height) = (150, 150)
    canvas = pygamebg.open_window(width, height, "Mole")

    images = []   # list that will contain the images
    for i in range(1, 11): # reading images mole1.png, ..., mole10.png into the list
        image_name = "mole" + str(i) + ".png"  # building the image name from parts
        images.append(pg.image.load(image_name))

    brown = (60, 42, 3)
    Y_HORIZON = 125
    GROUND = (0, Y_HORIZON, width, height - Y_HORIZON) # part of the image under the horizon
    i_frame = 0 # frame counter
    i_image = 0

    def new_frame():
        # complete the function - calculate which image is displayed in this frame

        canvas.fill(pg.Color("skyblue"))     # paint background
        pg.draw.rect(canvas, brown, GROUND)  # paint rectangle GROUND to brown
        canvas.blit(images[i_image], (0, 0)) # display the image

    pygamebg.frame_loop(10, new_frame)
