Keyboard events
---------------

Of the keyboard-generated events, the most important is the key pressing event, so we will focus on that one the most. When pressing keys on the keyboard, in the *event* object that represents an event in our programs, the value of *event.type* will be ``pg.KEYDOWN``.

When pressing a keyboard key is registered, we almost always want to know which key it is. This we can find out by testing the value of ``event.key``. As we already mentioned in the lesson on reading the keyboard state, that there is a constant for each key corresponding to that key. Let us recall the names of these constants for some frequently tested keys (you can see a complete list of these constants `here <https://www.pygame.org/docs/ref/key.html>`__ ):

============ ==============
constant     key
============ ==============
pg.K_LEFT    left arrow
pg.K_RIGHT   right arrow
pg.K_UP      up arrow
pg.K_DOWN    down arrow
pg.K_SPACE   space bar
pg.K_a       *a* key
pg.K_b       *b* key
pg.K_c       *c* key
============ ==============

The value of the *event.key* field tells us which physical key is pressed, and this value is suitable for keys such as arrow keys, *Ctrl*, *Shift*, *Alt*, *Home*, *End* and the like. When it comes to text, it may be more convenient to use the value of the ``event.unicode`` field, which contains the character that was just typed (as a single character string).

The following example illustrates testing a keystroke, or a *pg.KEYDOWN* event.

.. questionnote::

    **Example - crossword** 
    
    In this example, the user can use the arrow keys on the keyboard to move the frame and enter letters into boxes.
    
Note the *handle_event* function in which the event type check occurs, and then, if it is a key press, additional event information, stored in the *event.key* and *event.unicode* fields, is checked.

Additionally, you can try to put together some interesting crosswords.

.. activecode:: PyGame__interact_crossword
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :includesrc: src/PyGame/3_Interaction/3e_Keyboard_events/crossword.py
    
Let's compare this program to the "Navigation" program from the keyboard status reading lesson:

=========================================================== =============================================================
In the "Navigation" program                                 In the "Crossword" program
=========================================================== =============================================================
the yellow circle was moving by one pixel - it was gliding  the frame moves by one field - it jumps
we had no precise control of where the circle would stop    we can precisely control where the frame will stop
it didn't matter where exactly the circle would stop        it matters where exactly the frame will stop
we were reading the status of the keybard keys (down or up) we are using an event (pressing a key)
=========================================================== =============================================================


.. questionnote::

    **Task - navigation through fields** 
    
    Write a program that works as shown in the example("Play task" button). 
    
    The user can use the arrow keys on the keyboard to guide the character represented with a yellow circle. The character moves around the fields with white dots.
    

.. activecode:: PyGame__interact_pacman1
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask:
    :includehsrc: src/PyGame/3_Interaction/3e_Keyboard_events/pacman1.py
    
    import pygame as pg, pygamebg
    num_rows, num_cols = 10, 10
    a = 50 # square size
    (width, height) = (a* num_cols, a * num_rows)
    canvas = pygamebg.open_window(width, height, "Dot-eater")

    (character_row, character_col) = (num_rows // 2, num_cols // 2)

    def new_frame():
        canvas.fill(pg.Color("black"))   # paint canvas

        # white dots
        for x in range(a // 2, width, a):
            for y in range(a // 2, height, a):
                pg.draw.circle(canvas, pg.Color("white"), (x, y), 3)
       
        # HERE ADD THE STATEMENTS FOR DRAWING THE YELLOW CIRCLE
        # (use character_row, character_col)
        
    def handle_event(event):
        global character_row, character_col
        # ADD THE EVENT PROCESSING STATEMENTS HERE
        
    pygamebg.frame_loop(30, new_frame, handle_event)


.. questionnote::

    **Task - making a maze** 
    
    Write a program that makes a maze. The red frame should be controlled using the arrows, and pressing the space bar should change the color of a square (from black to white and vice versa).
    
When you complete the task, try the following:

- click on the "Play task" button (this time the example program does more than what we asked of you)
- make the maze the way you want
- press *S* for start and watch
- press *P* to turn pause mode on and off, that is to stop or resume searching
    
.. commented out

    Here it would be ideal if the students could not try the search before solving the task

.. activecode:: PyGame__interact_labyrinth
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :includehsrc: src/PyGame/3_Interaction/3e_Keyboard_events/labyrinth_edit_and_search.py
    
    import pygame as pg, pygamebg, random
    a = 50 # square size
    num_rows = 12
    num_cols = 20
    (width, height) = (num_cols * a, num_rows * a)
    canvas = pygamebg.open_window(width, height, "Maze")

    def new_frame():
        canvas.fill(pg.Color('white')) # paint background
        for row in range(num_rows):
            for col in range(num_cols):
                if board[row][col] == 1: # wall
                    pg.draw.rect(canvas, pg.Color('black'), (col * a, row * a, a, a))

        # frame
        pg.draw.rect(canvas, pg.Color('red'), (frame_col * a, frame_row * a, a, a), 3)
        
    def handle_event(event):
        global board, frame_row, frame_col
        
        # ADD STATEMENTS FOR KEYSTROKE PROCESSING HERE
        # (arrow keys and space bar should be covered)

    board = []
    for j in range(num_rows):
        board.append([])
        for i in range(num_cols):
            board[-1].append(random.randint(0, 1))
            
    (frame_row, frame_col) = (0, 0)
    pygamebg.frame_loop(10, new_frame, handle_event)
            

Bonus - a typing practice program
'''''''''''''''''''''''''''''''''

The program below is intended for typing practice. The program is long, but you should be able to understand a big part of it.

You might want (without obligation) to tailor the program to your needs, especially at the beginning. For example:

- to slow down (or later accelerate) the falling of the letters
- not to lose points when you make a mistake
- when you master the letters that fall the first, to remove them from the list of letters to practice
- to change the set of falling characters to numbers and operation signs only (if you want to practice typing only on the numeric keypad on the right side)
- to have pressing the spacebar delete the lowest letter (with somewhat reducing the score) 

or anything else you can think of.
    
When you have time, you are encouraged to also try to get as high a score as you can (without cheating).

.. activecode:: PyGame__interact_typing_tutor
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :includesrc: src/PyGame/3_Interaction/3e_Keyboard_events/typing_tutor.py
