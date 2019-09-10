Drawing with the help of loops
------------------------------

Consider the following task: let's draw 6 circles, as in this picture:

.. image:: ../../_images/PyGame/target.png
   :width: 300px
   :align: center 

Looking at the picture, we can assume (or it could have been said in the problem setting) that the circles are equally spaced. This means that the radius difference of each two adjacent circles is the same.

We choose the size of the circles to be as large as possible, but to fit in a given drawing space of 300x300 pixels. Since the width of the window is 300 pixels, the radius of the largest circle is 150. For the difference of radii of the two adjacent circles we can take :math:`{150 \over 6} = 25`. This gives radii of 25, 50, 75, 100, 125, 150.

Based on the calculated values, we could write a program like this:

.. activecode:: PyGame_loop__target_fixed
   :nocodelens:
   :enablecopy:
   :modaloutput:
   :includesrc: src\PyGame\1_Drawing\7a_UsingLoops\Examples\circles_target_fixed.py

Let's imagine that after this we were given the new task of making the same drawing, but with 5 circles. This is a very small change, isn't it? We should be able to reuse the previously solved task.

When we start working on a 5-circle drawing, we see that very little of the previous program can be used. In fact, we can only use the idea, and the size of the circles should be calculated from scratch.

If we had written the program differently, customizing it would have been much easier. We could, for example, write the number of circles in a variable and then use that variable in all the necessary calculations. This program would look like this:

.. activecode:: PyGame_loop__target_flexible
   :nocodelens:
   :enablecopy:
   :modaloutput:
   :includesrc: src\PyGame\1_Drawing\7a_UsingLoops\Examples\circles_target_flexible.py

In this program it is enough to change only one number so that it draws any given number of circles.

As we said earlier, many drawings have some regularity, such as symmetry or some repeating part (and many other, more complex patterns). If we understand the regularity in such drawings and express it mathematically, we will be able to use it when writing a program to draw such drawings, as we did in the previous example. That way we get a program that is much easier to modify to get another, similar drawing. For drawings with a large number of repetitions of a part (identical or slightly modified), the program that uses regularity will also be much shorter.

.. infonote::

    Many programs used by millions of people are constantly being improved and refined and new versions of such programs are being published. Therefore, program changes are something completely normal that happens all the time. The situation is similar with the programs we write ourselves. When we write a program, it can easily happen that we later think of something new and want to modify a part of the program that has already been written.
    
    Therefore, when writing programs, we should keep in mind that someone (possibly ourselves) will want to create a similar program and may want to use our program as an initial version.

Let's look at another example of how we can use the regularities in a drawing to write a more flexible program (a program that is easier to adapt to a slightly different purpose).

Example - antenna
'''''''''''''''''

We have already seen a program drawing this antenna. Now the program is written so that it is not too difficult to change the number of transverse segments, the spacing between them, the difference of lengths of successive segments and the like.

.. activecode:: PyGame_loop__antenna
   :nocodelens:
   :enablecopy:
   :modaloutput:
   :includesrc: src\PyGame\1_Drawing\7a_UsingLoops\Examples\antenna1.py

Part of the program that draws the transverse segments of the antenna could be written as follows:

.. code::

    for i in range(6):
        pg.draw.line(canvas, pg.Color('darkgray'), (120 - 10 * i,  75 + 25 * i), (180 +  10 * i,  75 + 25 * i), 1 + i//2)

The program written in this way would be slightly shorter, but the first one is clearer, so each has its advantages. Let's just point out that both of these programs are better than drawing 6 lines one by one for transverse segments (we used to do). If this part of the program consisted of six calls to the line drawing function, it would be more difficult to modify and adjust the program to draw a different antenna.

Equidistant numbers
'''''''''''''''''''

In both previous examples, it was necessary to enumerate one or more series of equidistant numbers. In the task with circles, these were numbers 25, 50, 75, 100, 125, 150 (radii of circles), and in the task with the antenna, we needed as many as four series of numbers - *x* and *y* coordinates of the ends of the transverse antenna segments. In particular, these numbers are:

- *x* coordinates of left ends: 120, 110, 100, 90, 80, 70
- *y* coordinates of left ends: 75, 100, 125, 150, 175, 200
- *x* coordinates of right ends: 180, 190, 200, 210, 220, 230
- *y* coordinates of right ends: 75, 100, 125, 150, 175, 200

We have seen that there are different ways to get the values we need. For example, in a task with concentric circles, values 25, 50, 75, 100, 125, 150 we could obtain in any of the following (equally good) ways:

..  code::

    for r in range(25, 151, 25):
        pg.draw.circle(canvas, pg.Color("red"), center, r, 2)

..  code::

    for i in range(br_krugova):
        pg.draw.circle(canvas, pg.Color("red"), center, round(25 + i * 25), 2)

..  code::

    r = 25
    for _ in range(br_krugova):
        pg.draw.circle(canvas, pg.Color("red"), center, r, 2)
        r += 25

In the general case, if we need to get a series of values of *a*, *a+d*, *a+2d*, ... *a+(n-1)d*, the previous three methods can be used as follows:

..  code::

    for x in range(a, a + n*d, d):
        print(x)

..  code::

    for i in range(n):
        print(a+i*d)

..  code::

    x = a
    for _ in range(n):
        print(x)
        x += d


We will see that many tasks with drawing equidistant shapes can be solved by applying loops like this.

Note that the ``range`` function with a step (with three arguments) must receive integer arguments, so in situations where the step is not an integer its use is not possible.

When we need (as in an antenna assignment) to make several series in one loop, the first mode is less convenient, so we have to choose one of the other two ways.

The following questions will help you consolidate your knowledge of forming a series of equidistant numbers.

.. dragndrop:: pygame__loop_quiz_match_series
    :feedback: try again!
    :match_1: 100, 200, 300, 400, 500|||for i in range(100, 600, 100)
    :match_2: 100, 300, 500|||for i in range(100, 601, 200)
    :match_3: 100, 200, 300, 400, 500, 600|||for i in range(100, 601, 100)
    :match_4: 200, 300, 400, 500, 600|||for i in range(200, 601, 100)

    Match a series of numbers with a loop that generates it.
     
.. dragndrop:: pygame__loop_quiz_match_series2
    :feedback: try again!
    :match_1: 100, 150, 200, 250, 300|||x = 100 + i*50
    :match_2: 50, 150, 250, 350, 450|||x = 50 + i*100
    :match_3: 0, 100, 200, 300, 400|||x = i*100
    :match_4: 100, 200, 300, 400, 500|||x = 100+i*100

    Match the numbers obtained with the expression in the "for i in range (5):" loop that generates them.
    

.. mchoice:: pygame__loop_quiz_range01
    :answer_a: x = 25 * i + 50
    :answer_b: x = (25 + i) * 50
    :answer_c: x = 25 * 2*i+1
    :answer_d: x = 25 + 50 * i
    :correct: d
    :feedback_a: No.
    :feedback_b: No.
    :feedback_c: No.
    :feedback_d: Correct!
    
    Which expression should be used in the loop
    
    .. code::
    
        for i in range(19):
            x = ???
            ...
            
    for *x* to have the same values as in a loop

    .. code::
    
        for x in range(25, 500, 50):
            ...
            
The following are the tasks for the exercise.

Ladder
''''''

Modify the program so that the ladder steps are drawn in a loop.

.. activecode:: PyGame_loop__ladder
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask:
    :includexsrc: src\PyGame\1_Drawing\7a_UsingLoops\Tasks\ladder.py

    canvas.fill(pg.Color("green")) # paint background

    pg.draw.line(canvas, pg.Color("brown"), (100, 10), (100, height - 10), 10)    # left side
    pg.draw.line(canvas, pg.Color("brown"), (200, 10), (200, height - 10), 10)    # right side

    # change (rewrite) this part
    pg.draw.line(canvas, pg.Color("brown"), (100,  50), (200, 50), 10) # step
    pg.draw.line(canvas, pg.Color("brown"), (100, 100), (200, 100), 10) # step
    pg.draw.line(canvas, pg.Color("brown"), (100, 150), (200, 150), 10) # step
    pg.draw.line(canvas, pg.Color("brown"), (100, 200), (200, 200), 10) # step
    pg.draw.line(canvas, pg.Color("brown"), (100, 250), (200, 250), 10) # step

   
.. reveal:: PyGame_loop__ladder_reveal
    :showtitle: Hint
    :hidetitle: Hide hint

    Instead of 5 line drawing statements, you can use a loop of the following form:
    
    .. code::
    
        for y in ???:
            pg.draw.line(canvas, pg.Color("brown"), (100, y), (200, y), 10)
            
    To complete the loop correctly, you need to answer the following question:
    
    .. mchoice:: pygame__loop_quiz_range1
        :answer_a: range(0, 50, 250)
        :answer_b: range(250, 50)
        :answer_c: range(50, 251, 50)
        :answer_d: range(50, 250, 50)
        :correct: c
        :feedback_a: No, the first number is not appropriate for that range.
        :feedback_b: No, try again.
        :feedback_c: Correct!
        :feedback_d: No, the last number is not appropriate for that range.
        
        Which of the ranges offered gives values 50, 100, 150, 200, 250?

          
Trees
'''''

Modify the program so that one tree is drawn in each or the three passes through the loop.

.. activecode:: PyGame_loop__trees
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask:
    :includexsrc: src\PyGame\1_Drawing\7a_UsingLoops\Tasks\trees.py
   
    canvas.fill(pg.Color("green")) # paint background

    pg.draw.rect(canvas, pg.Color("brown"), (40, 180, 20, 100))        # first tree
    pg.draw.ellipse(canvas, pg.Color("darkgreen"), (10, 50, 80, 150))  # first treetop
    pg.draw.rect(canvas, pg.Color("brown"), (140, 180, 20, 100))       # second tree
    pg.draw.ellipse(canvas, pg.Color("darkgreen"), (110, 50, 80, 150)) # second treetop
    pg.draw.rect(canvas, pg.Color("brown"), (240, 180, 20, 100))       # third tree
    pg.draw.ellipse(canvas, pg.Color("darkgreen"), (210, 50, 80, 150)) # third treetop

.. reveal:: PyGame_loop__trees_reveal
    :showtitle: Hint
    :hidetitle: Hide hint

    The program can look like this:
    
    .. activecode:: PyGame_loop__trees_solution
        :nocodelens:
        :enablecopy:
        :modaloutput:
        :includexsrc: src\PyGame\1_Drawing\7a_UsingLoops\Tasks\trees.py

        canvas.fill(pg.Color("green")) # paint background

        for i in range(3):
            pg.draw.rect(canvas, pg.Color("brown"), (???, 180, 20, 100))        # tree
            pg.draw.ellipse(canvas, pg.Color("darkgreen"), (???, 50, 80, 150))  # treetop

    
    whereby appropriate expressions for the *x* coordinate should be placed instead of the question marks. When *i* takes the values 0, 1, 2 in order, the expression in the first statement should take the values 40, 140, 240 and the expression in the second statement should take the values 10, 110, 210.

Grid
''''

Modify the program so that vertical lines are drawn in one loop and horizontal lines in the second loop.

.. activecode:: PyGame_loop__grid
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask:
    :includexsrc: src\PyGame\1_Drawing\7a_UsingLoops\Tasks\grid.py
    
    pg.draw.line(canvas, pg.Color("black"), (10, 10), (10, height - 10), 1)
    pg.draw.line(canvas, pg.Color("black"), (30, 10), (30, height - 10), 1)
    pg.draw.line(canvas, pg.Color("black"), (50, 10), (50, height - 10), 1)
    pg.draw.line(canvas, pg.Color("black"), (70, 10), (70, height - 10), 1)
    pg.draw.line(canvas, pg.Color("black"), (90, 10), (90, height - 10), 1)
    pg.draw.line(canvas, pg.Color("black"), (110, 10), (110, height - 10), 1)
    pg.draw.line(canvas, pg.Color("black"), (130, 10), (130, height - 10), 1)
    pg.draw.line(canvas, pg.Color("black"), (150, 10), (150, height - 10), 1)
    pg.draw.line(canvas, pg.Color("black"), (170, 10), (170, height - 10), 1)
    pg.draw.line(canvas, pg.Color("black"), (190, 10), (190, height - 10), 1)
    pg.draw.line(canvas, pg.Color("black"), (210, 10), (210, height - 10), 1)
    pg.draw.line(canvas, pg.Color("black"), (230, 10), (230, height - 10), 1)
    pg.draw.line(canvas, pg.Color("black"), (250, 10), (250, height - 10), 1)
    pg.draw.line(canvas, pg.Color("black"), (270, 10), (270, height - 10), 1)
    pg.draw.line(canvas, pg.Color("black"), (290, 10), (290, height - 10), 1)
    pg.draw.line(canvas, pg.Color("black"), (310, 10), (310, height - 10), 1)
    pg.draw.line(canvas, pg.Color("black"), (330, 10), (330, height - 10), 1)
    pg.draw.line(canvas, pg.Color("black"), (350, 10), (350, height - 10), 1)
    pg.draw.line(canvas, pg.Color("black"), (370, 10), (370, height - 10), 1)
    pg.draw.line(canvas, pg.Color("black"), (390, 10), (390, height - 10), 1)
    pg.draw.line(canvas, pg.Color("black"), (410, 10), (410, height - 10), 1)
    pg.draw.line(canvas, pg.Color("black"), (430, 10), (430, height - 10), 1)
    pg.draw.line(canvas, pg.Color("black"), (450, 10), (450, height - 10), 1)
    pg.draw.line(canvas, pg.Color("black"), (470, 10), (470, height - 10), 1)
    pg.draw.line(canvas, pg.Color("black"), (490, 10), (490, height - 10), 1)
    
    pg.draw.line(canvas, pg.Color("black"), (10, 10), (width - 10, 10), 1)
    pg.draw.line(canvas, pg.Color("black"), (10, 30), (width - 10, 30), 1)
    pg.draw.line(canvas, pg.Color("black"), (10, 50), (width - 10, 50), 1)
    pg.draw.line(canvas, pg.Color("black"), (10, 70), (width - 10, 70), 1)
    pg.draw.line(canvas, pg.Color("black"), (10, 90), (width - 10, 90), 1)
    pg.draw.line(canvas, pg.Color("black"), (10, 110), (width - 10, 110), 1)
    pg.draw.line(canvas, pg.Color("black"), (10, 130), (width - 10, 130), 1)
    pg.draw.line(canvas, pg.Color("black"), (10, 150), (width - 10, 150), 1)
    pg.draw.line(canvas, pg.Color("black"), (10, 170), (width - 10, 170), 1)
    pg.draw.line(canvas, pg.Color("black"), (10, 190), (width - 10, 190), 1)
    pg.draw.line(canvas, pg.Color("black"), (10, 210), (width - 10, 210), 1)
    pg.draw.line(canvas, pg.Color("black"), (10, 230), (width - 10, 230), 1)
    pg.draw.line(canvas, pg.Color("black"), (10, 250), (width - 10, 250), 1)
    pg.draw.line(canvas, pg.Color("black"), (10, 270), (width - 10, 270), 1)
    pg.draw.line(canvas, pg.Color("black"), (10, 290), (width - 10, 290), 1)

