Displaying ready-made images - tasks
------------------------------------

We learned how to display a ready-made image so that its upper left corner is at a given position on the screen. In some situations, the position of the upper left corner of the image will not be known to us, but will need to be calculated. In such cases, it may be necessary to know the width and height of the image. In Python's PyGame library for the image ``im``, the width and height of this image are given as ``im.get_width()`` and ``im.get_height()`` respectively.

Baskets
'''''''

Complete the following program to get the picture as in the example. The positions of the trees are given, and a basket should be drawn next to each tree so that the lower right corners of the basket and tree images overlap.

To complete this task, you need to calculate for each drawn basket the position of its top left corner, which can be done starting from the coordinates of the top left corner of the tree, using the widths and heights of both images.

.. image:: ../../_images/tree.png
   :width: 50px

.. image:: ../../_images/apple_small.png
   :width: 50px

.. image:: ../../_images/basket.png
   :width: 50px

.. activecode:: PyGame__pictures_baskets1
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask:
    :includexsrc: src\PyGame\1_Drawing\9_UsingImages\trees_baskets.py

    tree_image = pg.image.load("tree.png")  # image of a tree
    basket_image = pg.image.load("basket.png")  # image of a basket
    tree_positions = ((200, 70), (120, 150), (240, 290), (550, 170), (400, 200))


Picking apples
''''''''''''''

Complete the following program to get the picture as in the example. The solution to this task is obtained by appending the previous program - copy it and add apples to the trees and to the baskets.

.. activecode:: PyGame__pictures_baskets_apples
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask:
    :includexsrc: src\PyGame\1_Drawing\9_UsingImages\trees_apples_baskets.py

    tree_image = pg.image.load("tree.png")  # image of a tree
    apple_image = pg.image.load("apple_small.png")  # image of an apple
    basket_image = pg.image.load("basket.png")  # image of a basket
    apples_on_tree_positions = ((43,191), (61, 158), (124, 145), (134, 175), (160, 180))
    apples_in_basket_positions = ((15, 38), (60, 41), (22, 43), (49, 45), (34, 48))
    tree_positions = ((200, 70), (120, 150), (240, 290), (550, 170), (400, 200))



Boxes
'''''

.. questionnote:: 

    Write programs that use the image of one box shown below,

    .. image:: ../../_images/PyGame/box.png
        :width: 200px
        :align: center 

    and form images as in examples (use the "Play task" button in each task).
      
    The coordinates of the image, that is, its upper left corner for the leftmost box are (60, 400) and for the highest box are (420, 115).

From the given data and images it is possible to determine the series *x* and *y* of the image coordinates of each box in each example. The order of displaying of the box pictures should also be taken into account here.

To better understand how the same series of numbers (for example, 10, 15, 20, 25, 30) can be obtained in two different orders, and what else to look for, answer the supporting question.

.. dragndrop:: console__pictures_quiz_series_negative_step
    :feedback: Try again.
    :match_1: 10, 15, 20, 25, 30 ||| for x in range(10, 35, 5)
    :match_2: 30, 25, 20, 15, 10 ||| for x in range(30, 5, -5)
    :match_3: empty series ||| for x in range(30, 10, 5)
    :match_4: 5, 15, 25 ||| for x in range(5, 35, 10)

    Match a series of numbers with the statements that generate them.

.. activecode:: PyGame__pictures_boxes1
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask:
    :includexsrc: src\PyGame\1_Drawing\9_UsingImages\boxes1.py

.. activecode:: PyGame__pictures_boxes2
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask:
    :includexsrc: src\PyGame\1_Drawing\9_UsingImages\boxes2.py

.. activecode:: PyGame__pictures_boxes3
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask:
    :includexsrc: src\PyGame\1_Drawing\9_UsingImages\boxes3.py

