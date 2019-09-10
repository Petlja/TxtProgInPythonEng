Changing the drawing size
-------------------------

When we talked about moving a drawing, we mentioned that it is better to do all the calculations in the program, because it is easier that way to move the drawing, or to draw it in several places when needed. The situation is similar when we want to draw the same drawing in different size, possibly in several places (each could be in different size). Instead of calculating all the coordinates from scratch, it may be enough to change one single number in our program to get a drawing of another size.

To learn how to make drawings that can be resized easily, let's first see what needs to be changed in a drawing program so that the drawing gets a different size. For example, if we drew a cloud using these statements:

.. code::

    def cloud(x, y, shade):
        # draw a cloud of three circles
        gray = (shade, shade, shade)
        pg.draw.circle(canvas, gray, (x,      y), 50)
        pg.draw.circle(canvas, gray, (x - 50, y), 30)
        pg.draw.circle(canvas, gray, (x + 50, y), 30)

    cloud(200, 200, 180)

and now we want the cloud to be twice as small and its midpoint to be still at point (200, 200), then we would change the function given above to:

.. code::

    def cloud(x, y, shade):
        # draw a cloud of three circles
        gray = (shade, shade, shade)
        pg.draw.circle(canvas, gray, (x,      y), 25)
        pg.draw.circle(canvas, gray, (x - 25, y), 15)
        pg.draw.circle(canvas, gray, (x + 25, y), 15)
    
The radii of all three circles should be cut to half the previous size (25 pixels instead of 50 and 15 instead of 30), but that is not enough. If the centers of the small circles remained where they were, we would get three separate circles (try it). In order for the drawing to still look like a cloud, we also need to bring the circles closer together. More specifically, the distances of the centers of the smaller circles from the center of the large circle should also be twice less than before, that is, 25 instead of 50 pixels.

In general, we do not always want a cloud that is twice as small, but that the clouds can be of different sizes. In addition, we do not want to create a separate function for each cloud size, but to have one function that can draw a cloud of a given size. IUt would be the most comfortable if we could set the size of the cloud with only one number and change the size of the cloud by changing that one number. To do this, we need to express all the sizes that change with the change of cloud size (which is the distances between the centers of the circles and the radii of those circles) using one selected size. For example, for that selected size we can take the radius of the middle circle, which we will denote by :math:`r`. The distances of the centers of the smaller circles to the center of the larger circle are exactly :math:`r`, and the radius of the smaller circles is equal :math:`{3 \over 5} r` regardless of the size of the cloud. When we use all these relations we have noticed, the function looks like this:

.. code::

    def cloud(x, y, r, shade):
        # draw a cloud of three circles
        gray = (shade, shade, shade)
        r_small = round(3 * r / 5)
        pg.draw.circle(canvas, gray, (x,     y), r)
        pg.draw.circle(canvas, gray, (x - r, y), r_small)
        pg.draw.circle(canvas, gray, (x + r, y), r_small)

The function has one parameter more - besides the position and the shade of gray, we also set the size of the cloud to this function. Now we can make drawings like this:

.. activecode:: PyGame__drawing_clouds_scalable
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :includesrc: src\PyGame\1_Drawing\6_Scalable\clouds_scalable.py

Now, let's list the steps for a general procedure to remake any movable drawing so that it can be resized as well:

- We need to determine one length in the drawing, which will be set directly. We can call this selected length **basic length** or **unit of measure**. In the example of clouds, the basic length is the radius of the middle circle.
- All radii of the circles of which the drawing consists are expressed in proportion to the basic length. This means that if our base length is denoted by :math:`a`, all other lengths in the program will be multiples of :math:`a`, for example :math:`2a` or :math:`5a`. We determine the number :math:`a` from the ratio of the required length and the selected basic length in the initial drawing (this ratio remains the same when the size of the drawing changes). In the example with the cloud, the radius of the small circle is always :math:`{3 \over 5}` of the selected basic length :math:`r`. If rectangles or ellipses appear in the drawing, the heights and widths of those rectangles and ellipses should also be expressed in proportion to the basic length, in the same way as the radii of the circles.
- We determine the coordinates of all points with respect to the main point, by adding or subtracting a certain number of basic lengths to coordinates of the main point. The required number of basic lengths is determined again from the relation in the initial drawing. In the example with the cloud, to obtain :math:`x` coordinate of the center of the left circle, we subtract **one** basic length from :math:`x` coordinate of the main point (center of the middle circle). We do so because the ratio of the difference of :math:`x` coordinates and basic length equals to one. The same procedure applies in principle to :math:`y` coordinates, though in this case it is particularly simple. Since :math:`y` coordinates of the centers of the circles are the same, the ratio of the difference of the :math:`y` coordinates and the basic length is zero, so zero basic lengths should be added to :math:`y` coordinate of the anchor to get :math:`y` coordinate of the center of a smaller circle.

To better understand the process of resizing a drawing, we will also apply it to the example of a teddy bear.

Teddy - size
''''''''''''

The following program is presented, which shows the teddy bear's head so that it can be easily moved:

.. activecode:: PyGame__drawing_bear_movable
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :includesrc: src\PyGame\1_Drawing\5_Movable\teddy-bear_movable1a.py

In order to resize the drawing, we introduce a basic length, for example :math:`a = 5`. Now we can express all radii using :math:`a` like this:

.. code::

    framed_circle(canvas, pg.Color("yellow"), (cx - 60,  cy - 70),  9*a) # left ear
    framed_circle(canvas, pg.Color("yellow"), (cx + 60,  cy - 70),  9*a) # right ear
    framed_circle(canvas, pg.Color("yellow"), (cx,       cy)     , 20*a) # head
    framed_circle(canvas, pg.Color("yellow"), (cx,       cy + 50), 10*a) # snout
    framed_circle(canvas, pg.Color("black"),  (cx - 50,  cy - 30),  3*a) # left eye
    framed_circle(canvas, pg.Color("black"),  (cx + 50,  cy - 30),  3*a) # right eye
    framed_circle(canvas, pg.Color("black"),  (cx,       cy + 20),  3*a) # snout top
    
Any number can be chosen as the base length, and by choosing a base length of 5 pixels, we have no need to use real numbers - all radii are integer multiples of :math:`a` and we can easily calculate them by heart. For example, we express the radius of 45 pixels as :math:`45 = 9 \cdot 5 = 9 \cdot a`, and so on.

Now we need to express the coordinates of the centers of all other circles starting from the main point :math:`(cx, cy)` and moving by the required number of lengths :math:`a` in the :math:`x` and :math:`y` axis direction. Take the bear's right ear as an example.

:math:`x` coordinate of the center of the right ear is :math:`cx + 60 = cx + 12 a`, while :math:`y` coordinate is :math:`cy - 70 = cy - 14 a`. When we do this for all the centers of the circles, we come to the following form of the program:

.. activecode:: PyGame__drawing_bear_tmp2
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :includesrc: src\PyGame\1_Drawing\6_Scalable\teddy-bear_scalable1a.py
    
Now we can not only move or copy a teddy bear across the screen, but also display it in various sizes. To confirm that resizing really works, the function call

.. code::

    draw_teddy(width // 2, height // 2, 6)
    
which draws a bear with the center point in the center of the window, can be replaced with the following five:

.. code::

    draw_teddy(85, 100, 4)
    draw_teddy(235, 100, 3)
    draw_teddy(50, 250, 2)
    draw_teddy(150, 250, 2)
    draw_teddy(250, 250, 2)

Copy or retype these five lines of code into the program and try it out! Consider how much work it would be to have these five bears displayed without computing in the program.

Now try to complete one started example.

Task - house size
'''''''''''''''''

We will start with a program that draws four houses in the given positions on the screen:

.. activecode:: PyGame__drawing_house_detailed1
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :includesrc: src\PyGame\1_Drawing\5_Movable\house2D_detailed_movable.py

Complete the program remodel in the box below so that the houses can be easily resized. For example, you can take 10 pixels for the basic size, because in that case, expressing all lengths using basic length is very easy. When you confirm that the program after the remake displays the same image as the starting program above, replace the given *house* function calls with the following 4 and confirm that the resizing of the house is working properly (you should get the image as if you clicked on the button "Play task"):

.. code::

    house(150,  90,  8, pg.Color(220, 220, 220))
    house(250, 130,  9, pg.Color("white"))
    house(350, 160, 10, (255,255,150))
    house( 50, 150, 10, pg.Color("khaki"))

.. activecode:: PyGame__drawing_house_scalable1
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask: 
    :includexsrc: src\PyGame\1_Drawing\6_Scalable\house2D_detailed_scalable1.py
   
    canvas.fill(pg.Color("darkgreen")) # paint background

    def house(x, y, a, wall_color):
        pg.draw.polygon(canvas, pg.Color("red"), [(x, y), (x + ???*a, y - ???*a), (x+14*a, y)]) # roof
        pg.draw.rect(canvas, wall_color,       (x,       y,      14*a, 10*a)) # walls
        pg.draw.rect(canvas, pg.Color("brown"), (x + ???, y + ???, 3*a,  3*a)) # left window
        pg.draw.rect(canvas, pg.Color("brown"), (x + ???, y + ???, ???,  ???)) # right window
        pg.draw.rect(canvas, pg.Color("brown"), (x + ???, y + ???, ???,  ???)) # door
        
    house(150,  90, 10, (220, 220, 220))
    house(220, 130, 10, pg.Color("white"))
    house(350, 160, 10, (255, 255, 150))
    house( 50, 150, 10, pg.Color("khaki"))

After successfully changing the *house* function, try different layouts, colors and sizes of houses, such as the one below, or some other you choose yourself:

.. code::

    house(278, 110, 1, (211, 207, 169))
    house(231, 119, 2, (217, 211, 164))
    house(174, 130, 3, (228, 221, 152))
    house(112, 142, 4, (231, 222, 150))
    house( 18, 160, 6, (240, 230, 140))
