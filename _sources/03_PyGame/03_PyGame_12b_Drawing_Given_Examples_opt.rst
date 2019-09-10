Drawing from reference - additional examples
--------------------------------------------

We assume that you have already acquired some skill in reading coordinates and calling functions for drawing basic shapes. Therefore, in the following tasks there will be some new challenges. 

Many drawings have some regularity, like axial symmetry or a part of the drawing repeating itself. If you want to make such a drawing yourself, in order for it to look good you cannot select all points completely freely. Instead, some points should be chosen and some points should be calculated. 

In order to get closer to creating images that we design ourselves, the way of specifying drawings has been slightly modified. Drawings are still specified with an example program that draws an image (there is a saying that one image is worth 1000 words). What is new is that it will not be possible to read one or both of the coordinates in some parts of the image, but instead you will need to calculate those coordinates based on known coordinates.

In addition to needing a bit of calculation, the drawings in the following tasks also have more details, so it takes a little longer to make them.

Fence
'''''

In this task, reading the :math:`x` coordinate is limited to the first picket of the fence and the first space. All other needed coordinates can be calculated.

.. activecode:: PyGame__drawing_fence
   :nocodelens:
   :enablecopy:
   :modaloutput:
   :playtask:
   :includexsrc: src\PyGame\1_Drawing\4_ByGrid_Additional\fence_assist.py
   
.. reveal:: PyGame__drawing_fence_reveal
   :showtitle: Show solution
   :hidetitle: Hide solution

   The complete program is provided, you can try it here as well.
	       
   .. activecode:: PyGame__drawing_fence_solution
      :nocodelens:
      :enablecopy:
      :modaloutput:
      :includesrc: src\PyGame\1_Drawing\4_ByGrid_Additional\fence.py

Building
''''''''

All windows of the building are the same size, the spaces between the floors are equal, and the left and right sides of the building are symmetrical (except that symmetrical windows are not necessarily the same color). Use this information to calculate the coordinates that you cannot read.

.. activecode:: PyGame__drawing_building
   :nocodelens:
   :enablecopy:
   :modaloutput:
   :playtask:
   :includexsrc: src\PyGame\1_Drawing\4_ByGrid_Additional\building_assist.py
   
.. commented out 

    .. reveal:: PyGame__drawing_building_reveal
       :showtitle: Show solution
       :hidetitle: Hide solution

       The complete program is provided, you can try it here as well.
               
       .. activecode:: PyGame__drawing_building_solution
          :nocodelens:
          :enablecopy:
          :modaloutput:
          :includesrc: src\PyGame\1_Drawing\4_ByGrid_Additional\building.py

Stickman
''''''''

In this example, the coordinates of the points on the right leg cannot be read, but it is symmetrical to the left leg. Since the width of the image is known (see the beginning of the program), the coordinates of the two unknown points on the right can be calculated using the known symmetric points on the left.

**Hint:** Let :math:`A` be a point on the left side of the image, and :math:`B` a point on the right side of the image, symmetrical to the point :math:`A`. The two points then have the same :math:`y` coordinate, and the sum of the :math:`x` coordinates of the points :math:`A` and :math:`B` equals the width of the image.

.. activecode:: PyGame__drawing_stickman
   :nocodelens:
   :enablecopy:
   :modaloutput:
   :playtask:
   :includexsrc: src\PyGame\1_Drawing\4_ByGrid_Additional\stickman_assist.py
   
.. commented out 

    .. reveal:: PyGame__drawing_stickman_reveal
       :showtitle: Show solution
       :hidetitle: Hide solution

       The complete program is provided, you can try it here as well.
               
       .. activecode:: PyGame__drawing_stickman_solution
          :nocodelens:
          :enablecopy:
          :modaloutput:
          :includesrc: src\PyGame\1_Drawing\4_ByGrid_Additional\stickman.py

Cat
'''

The ears of this cat can be depicted as filled triangles. As the ears are attached to the head, two vertices of each triangle can be chosen with more freedom (it is enough to place them somewhere inside the head circle). In addition to the two triangles representing the ears, we also have:

- two circles (head and tip of the snout)
- six ellipses (eyes, pupils and parts of the snout)
- six lines (whiskers)

:math:`x` coordinates on the right side of the image cannot be read, but they can be calculated using symmetry (and the known width of the image - see the beginning of the program). 

**Note:** The procedure for determining ellipse parameters on the right side is slightly different from the one used for circles or line segments. Note that the top **left** vertex of the rectangle circumscribed about the ellipse sought is in fact a mirror image of the top **right** vertex of the rectangle circumscribed about the ellipse known. This means that when we find the parameters *(x, y, w, h)* of the ellipse on the left side, the parameters of its symmetrical ellipse on the right are *(width - x - w, y, w, h)*, where *width* is the width of the window, *x*, *y* are the coordinates of the top left vertex of the rectangle around the ellipse on the left, and *w* and *h* are the width and height of the ellipses.

.. activecode:: PyGame__drawing_cat
   :nocodelens:
   :enablecopy:
   :modaloutput:
   :playtask:
   :includexsrc: src\PyGame\1_Drawing\4_ByGrid_Additional\cat_assist.py

.. reveal:: PyGame__drawing_cat_reveal
   :showtitle: Show solution
   :hidetitle: Hide solution

   The complete program is provided, you can try it here as well.
	       
   .. activecode:: PyGame__drawing_cat_solution
      :nocodelens:
      :enablecopy:
      :modaloutput:
      :includesrc: src\PyGame\1_Drawing\4_ByGrid_Additional\cat.py

