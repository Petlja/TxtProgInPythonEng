Drawings movement
-----------------

The animations we have seen so far are based on showing a different image we prepared in advance in each frame. Now we are also going to move the images that are shown, so that the same image appears in different places in the window, that is, it moves.

Let's look at an example first:

.. image:: ../../_images/car.png
   :width: 50px

.. activecode:: PyGame__anim_car_oneway
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :includesrc: src/PyGame/2_Animation/2b_Anim_Motion/car_rightwards_only.py

As before, we have a *new_frame* function that shows an image in each frame. What is new in this example is that the position of that image changes from frame to frame.

The image is shown so that its upper left corner appears at the point (*car_x*, *car_y*). In order for the car to move to the right, in each frame we increase the *x* coordinate of the image. We only keep in mind that when the car goes too far to the right, we return the car so that its right end aligns with the left edge of the window. In this way, the car begins to gradually reappear on the left.

~~~~

Similarly, we can also move drawings we draw ourselves (not just ready-made images). In doing so, we can move the image or drawing in any direction. Here is one example:

.. activecode:: PyGame__anim_billiards
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :includesrc: src/PyGame/2_Animation/2b_Anim_Motion/billiards.py

Notice how we check if the ball touches the edge of the screen. The far right of the ball has an *x* coordinate equal to :math:`cx+r`. If this value were equal to the width of the window, it would mean that the ball touches the right edge of the window, and if :math:`cx + r > width`, it means that the ball has already partially passed the right edge of the window. In this case, with the :math:`dx = -dx` command, starting from the next frame a value opposite to the one so far will be added to the *x* coordinate of the ball, that is, the ball will henceforward be moving 3 pixels to the left. This will look like the ball bounced off the right edge of the window.

Notice another detail: instead of :math:`cx + r > width` we could have also used :math:`cx + r >= width` and the program would work almost the same. However, since the ball **does not move by one pixel**, it would not be valid if we used the condition :math:`cx + r == width`, because then the ball could skip the position we are checking and go through the edge of the window.

We thoroughly analyzed the case of the right edge of the window, and the same reasoning was applied to other edges when the program was being written. The overall effect of the two *if* commands is that the ball bounces off each edge of the window.

Check if you understand this by answering the following questions.

Drawings movement - questions
'''''''''''''''''''''''''''''

.. dragndrop:: pygame__anim_quiz_bounce1
    :feedback: Try again!
    :match_1: for left edge ||| if cx - r < 0
    :match_2: for right edge ||| if cx + r > width
    :match_3: for top edge ||| if cy - r < 0
    :match_4: for bottom edge ||| if cy + r > height

    Match the check that the ball from the previous example has passed a certain edge to the appropriate *if* command.

.. mchoice:: pygame__anim_quiz_bounce2
    :answer_a: right
    :answer_b: up
    :answer_c: left
    :answer_d: down
    :correct: c
    :feedback_a: Try again
    :feedback_b: Try again
    :feedback_c: Correct!
    :feedback_d: Try again

    To what side does an image move by adding a negative value to its *x* coordinate?

.. mchoice:: pygame__anim_quiz_bounce3
    :answer_a: if x + im_width < 0:
    :answer_b: if y + im_height < 0:
    :answer_c: if x < 0:
    :answer_d: if y < 0:
    :correct: b
    :feedback_a: Try again
    :feedback_b: Correct!
    :feedback_c: Try again
    :feedback_d: Try again

    Let the dimensions of a given image be *im_width* and *im_height*, and its upper left corner (*x*, *y*). How do we check if the image has completely gone through the top edge of the window and no part of it is visible?
    
.. dragndrop:: pygame__anim_quiz_bounce4
    :feedback: Try again!
    :match_1: the image came out through the left edge of the window ||| x + im_width < 0
    :match_2: the image began to come out through the left edge of the window ||| x < 0
    :match_3: the image came out through the right edge of the window ||| x > width
    :match_4: the image began to come out through the right edge of the window ||| x + im_width > width

    Let 'width' be the width of the window, 'im_width' the width of the image and (x, y) the upper left corner of the image. Match logical conditions to their meaning.

.. mchoice:: pygame__anim_quiz_bounce5
    :answer_a: x = width; dx = -10
    :answer_b: x = width + im_width; dx = -10
    :answer_c: x = width - im_width; dx = -10
    :answer_d: x = width + im_width; dx = 10
    :correct: a
    :feedback_a: Correct!
    :feedback_b: No, that is too far from the right edge.
    :feedback_c: No, that way the whole image is already in the window.
    :feedback_d: No, the image is too far away and will keep getting farther.

    Let *width* be the width of the window, *im_width* the width of the image, (*x*, *y*) the upper left corner of the image and *dx* the value by which the *x* coordinate of the image will be changed later. What commands will cause the image to begin to appear entering the window through the right edge?

Task - a car going left-right
'''''''''''''''''''''''''''''

Try reworking the first program so that the car moves alternately to one side and to the other, as in the example ("Play Task" button). The program already contains commands to form a tuple of two images. The image of the car facing right is loaded, while the image of the car facing the other side is obtained using the *pg.transform.flip* function, which transforms the given image into one symmetrical to it.

.. activecode:: PyGame__anim_car_right_left
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask:
    :includehsrc: src/PyGame/2_Animation/2b_Anim_Motion/car_right_left.py
    
    import pygame as pg, pygamebg
    (width, height) = (400, 300)
    canvas = pygamebg.open_window(width, height, "Car")
    
    car_rightwards_image = pg.image.load("car.png") 
    # creating flipped image (symmetric with respect to the vertical axis)
    car_leftwards_image = pg.transform.flip(car_rightwards_image, True, False)
    car_images = (car_rightwards_image, car_leftwards_image)
    fps = 50
    
    def new_frame():
        pass
        
    pygamebg.frame_loop(fps, new_frame)

        
