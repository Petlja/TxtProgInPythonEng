Drawing polygons with loops
---------------------------

Recall an example of a program that draws a fence:

.. activecode:: PyGame_loops_fence_fixed
   :nocodelens:
   :enablecopy:
   :modaloutput:
   :includesrc: src\PyGame\1_Drawing\7b_Loops_polygons\fence_fixed.py

As we learned in the meanwhile, drawing each picket with a separate statement is not the best way to draw this drawing. A more flexible program would be obtained by drawing the pickets in a loop. Let's look at how we should draw a polygon (a picket is represented by a hexagon), so that it would be easy to draw the same polygon in other places.

It is certainly useful to introduce a main point (anchor), in relation to which all the polygonal vertices would be expressed. In the case of a fence, the vertices of the first picket are [(20, 80), (30, 70), (40, 80), (40, 270), (20, 270)]. We can select the first specified point (20, 80) for the anchor, and express the other points using the coordinates of the first point. So we get that the vertices of one picket are [(x, y), (x + 10, y-10), (x + 20, y), (x + 20, y + 190), (x, y + 190)] . By setting *x* = 20, *y* = 80, we get the coordinates of the first picket in the fence, and by increasing *x* successively by 40 each, we can get other pickets.

.. code:: 

    y = 80
    for x in range(20, 300, 40):
        pg.draw.polygon(canvas, pg.Color('brown'), [(x, y), (x + 10, y-10), (x + 20, y), (x + 20, y+190), (x, y+190)])

Since all the pickets are at the same height, the *y* coordinate of the anchor does not change, so we don't even have to introduce it (we would need to introduce the *y* coordinates if some of the pickets were above others). This means that in this case, we can write the previous code a little more simply.

.. code:: 

    for x in range(20, 300, 40):
        pg.draw.polygon(canvas, pg.Color('brown'), [(x, 80), (x + 10, 70), (x + 20, 80), (x + 20, 270), (x, 270)])

Various variants of this basic idea are possible. For example, if we initially form a list of polygonal vertices (for the first picket), we can form a list of displaced vertices in several ways.

We can calculate the coordinates of the displaced vertices in an additional loop:

.. code::

    picket = [(0, 0), (10, -10), (20, 0), (20, 190), (0, 190)]
    y0 = 80
    for x0 in range(20, 300, 40):
        displaced_picket = []
        for x, y in picket:
            displaced_picket.append((x+x0, y+y0))
        pg.draw.polygon(canvas, color, displaced_picket)

We can introduce a function to draw a given polygon at a given position, and form the list of displaced vertices in the function:

.. code::

    def draw_polygon(points, color, x0, y0):
        displaced_points = []
        for x, y in points:
            displaced_points.append((x+x0, y+y0))
        pg.draw.polygon(canvas, color, displaced_points)

    picket = [(0, 0), (10, -10), (20, 0), (20, 190), (0, 190)]
    for x0 in range(20, 300, 40):
        draw_polygon(picket, pg.Color('brown'), x0, 80)


Each of these two approaches can replace the seven calls to the *pg.draw.polygon* function in the given initial example, and each is better than drawing attachments with separate commands. Using the function gives slightly longer code, but it has the advantage that the exact same function can be used without any modification to draw any polygon in a new position.

Try one, or both of the suggested changes to the program above, and then use one of these methods to solve the following tasks.


Tasks for exercise
''''''''''''''''''

.. questionnote::

    **Task - octagons**
    
    Write a program that draws octagons as in the example (click the "Play task" button).

The polygon drawing function is similar to the previous one. The only difference is that in it, the *pg.draw.polygon* function is called twice: once for the interior of the polygon, and the other time for the edges.

The coordinates of the octagon are also given, it remains to add a call to the drawing function inside a double loop. Both *x* and *y* start from value 0 and advance in steps of 48 (48 is the octagon's "width" and "height").
    
.. activecode:: PyGame_loops_octagons
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask:
    :includexsrc: src\PyGame\1_Drawing\7b_Loops_polygons\octagons.py
    
    def draw_framed_polygon(vertices, color, frame_color, x0, y0):
        displaced_vertices = []
        for x, y in vertices:
            displaced_vertices.append((x+x0, y+y0))
        pg.draw.polygon(canvas, color, displaced_vertices)
        pg.draw.polygon(canvas, frame_color, displaced_vertices, 2)
    
    octagon = [(14, 0), (34, 0), (48, 14), (48, 34), (34, 48), (14, 48), (0, 34), (0, 14)]
    # finish the program
    
    
.. questionnote::

    **Task - arrows**

    Complete the following program to draw the given image (you can see the image by clicking the "Play task" button).

White arrows are pointing to the left and black arrows are pointing to the right. As the black and white arrows completely cover the image together, notice that it is sufficient to draw only black arrows (on a white background).

.. activecode:: PyGame_loops_arrows
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask:
    :includexsrc: src\PyGame\1_Drawing\7b_Loops_polygons\arrows.py
   
    arrow = [(0, 10), (40, 10), (40, 0), (60, 20), (40, 40), (40, 30), (0, 30)]
    arrow_length, arrow_height = 60, 40
    canvas.fill(pg.Color("white"))
    ??? # finish the program



.. questionnote::

    **Task - a herd of giraffes**

    The coordinates of the vertices of the polygon that represents the giraffe are given. Complete the program by drawing several giraffes (using the *draw_polygon* function). Make a list of giraffe positions as desired.

.. activecode:: PyGame_loops_herd
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :includesrc: src\PyGame\1_Drawing\7b_Loops_polygons\giraffe_herd.py
