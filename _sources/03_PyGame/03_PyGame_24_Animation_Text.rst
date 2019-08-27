Drawing text
------------

Drawing programs often print various messages along with the pictures (you have probably seen many examples yourself). Here's how to do that in PyGame:

.. activecode:: PyGame__anim_text
    :nocodelens:
    :modaloutput:
    :includesrc: src/PyGame/2_Animation/2d_Anim_Text/text_example.py

As you can see in the example, in order for the text to be displayed **we must first create an object representing a font**. To do this, we use the ``pg.font.SysFont`` function, for which we specify the type and size of the letters. We can also create more such objects in case we intend to use different sizes or types of letters, though often we only need one font.

After creating the font, each time we want to display some text we repeat the following two steps:

- The first step is **to create an image that contains the desired text.** This is accomplished by using the ``font.render`` function, where *font* is the font object created at the beginning. The parameters of the *font.render* function are the text that is to be displayed, the logical value that determines whether to draw nicer lines (i.e. use the so-called anti-aliasing technique) and the color in which the text will be written, in that order.
- The second step is the same as when displaying any ready-made image - **we display the image obtained in the previous step** at the position we choose. In order to calculate the position we can use the image size as needed (like in the example).

Tasks - neon signs
''''''''''''''''''

You must have seen glowing neon tube signs. They attract attention by switching different letter groups on and off in a certain repetitive order. The following are some examples inspired by such flashing signs.


.. questionnote::

    **Flashing text:** Write a program that displays flashing text, similar to the example below ("Play Task" button). 
    
    You can change the text, its color and size, font, on/off switching frequency, or anything else if you like. If you want to mimic our program as closely as possible, it uses letters of type "Arial", size 80 and displays text in every second frame, centered, at 3 frames per second frame rate.
    
**Hint:** For the global variables that describe the scene, one logical variable is sufficient to tell whether the given text should be displayed or not. We will change this variable's value in the *new_frame()* function so that it has a value of *True* in every second frame.

.. activecode:: PyGame__anim_neon1
    :nocodelens:
    :modaloutput:
    :playtask:
    :includehsrc: src/PyGame/2_Animation/2d_Anim_Text/neon_sign1.py

    import pygame as pg, pygamebg
    text = "PYTHON"
    (width, height) = (len(text) * 70, 100)
    canvas = pygamebg.open_window(width, height, "Neon sign")
    
.. reveal:: PyGame__anim_neon1_reveal
   :showtitle: Show solution
   :hidetitle: Hide solution

    .. activecode:: PyGame__anim_neon1_solution
        :nocodelens:
        :modaloutput:
        :includesrc: src/PyGame/2_Animation/2d_Anim_Text/neon_sign1.py

.. questionnote::

    **Adding letters:** Now, try imitating this example. Only the first letter is displayed in the first frame and then one letter more in each following frame until all the letters are displayed. This is followed by one frame showing nothing, then three frames with all the letters being displayed, and then everything is repeated. The frame rate of our program is 2 frames per second.

**Hint:** Here are some comments that may help with solving the problem

- From the description (and observing the example) we can conclude that the full cycle contains four frames more than the number of letters in the text.
- We can determine the size we need our window to be based on the length of the text, as in the previous example.
- The text is always displayed at the same position (the upper left corner of the text is same). Therefore, it is enough to calculate the position once, in the main part of the program.
- We can use a global frame counter variable, and based on its value determine whether and what part of the text should be displayed using *if* commands in the *new_frame()* function.

.. activecode:: PyGame__anim_neon2
    :nocodelens:
    :modaloutput:
    :playtask:
    :includehsrc: src/PyGame/2_Animation/2d_Anim_Text/neon_sign2.py

.. questionnote::

    **Single letters:** In this example first each letter is displayed individually and then all letters are switched on and off 3 times. Can you copy this behavior?

**Hint:** The display positions of the individual letters are (0, 0), (50, 0), (100, 0), (150, 0), etc. The number of frames in a cycle is 6 plus the number of letters in the text. The rest of the ideas are very similar to those in the previous examples.

.. activecode:: PyGame__anim_neon3
    :nocodelens:
    :modaloutput:
    :playtask:
    :includehsrc: src/PyGame/2_Animation/2d_Anim_Text/neon_sign3.py

.. questionnote::

    **Moving letters:** This example is different in that the letters are moving. Try to solve this as well.
    
**Hint:** Once you form an image from the given text, the task becomes very similar to the task with a moving car.

.. activecode:: PyGame__anim_neon4
    :nocodelens:
    :modaloutput:
    :playtask:
    :includehsrc: src/PyGame/2_Animation/2d_Anim_Text/neon_sign4.py


Lastly, if you wish, you can make a neon sign of your own design here.

.. activecode:: PyGame__anim_neon5
    :nocodelens:
    :modaloutput:
