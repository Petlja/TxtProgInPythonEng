==================
А very simple game
==================

For this project, let us try to make one very simple game.

    
Images that we are going to use for our simple game.

.. image:: ../../_images/rocket.png
   :alt: Rocket

.. image:: ../../_images/planet.png
   :alt: Planet
         
.. image:: ../../_images/martian.png
   :alt: Martian

.. image:: ../../_images/martian_heart.png
   :alt: Martian with a heart

The final version of the game
-----------------------------

This is what our final mini-game should look like.
         
.. activecode:: rocket_final
   :nocodelens:
   :modaloutput:
   :playtask:
   :includehsrc: src/PyGame/4_Project/rocket_final.py

                
Loading and showing the rocket
------------------------------

As the first step, just load the image of the rocket and show it on
the screen.

.. activecode:: rocket1
   :nocodelens:
   :modaloutput: 
   :playtask:
   :includexsrc: src/PyGame/4_Project/rocket1.py

   # clear screen
   window.fill(pg.Color("black"))
   
   # load image
   ???

   # draw rocket
   ???

Show the rocket on the bottom of the screen
-------------------------------------------

Now adapt the program so that the rocket is shown in the bottom of the screen.

.. activecode:: rocket2
   :nocodelens:
   :modaloutput: 
   :playtask:
   :includexsrc: src/PyGame/4_Project/rocket2.py

   # clear screen
   window.fill(pg.Color("black"))
   
   # load image
   rocket  = pg.image.load("rocket.png")

   # draw rocket
   window.blit(rocket, (0, ???))

   
Draw the planets
----------------

Let us draw a row of planets at the top of the screen. Hint: use a
loop to make the code shorter.

.. activecode:: rocket3
   :nocodelens:
   :modaloutput: 
   :playtask:
   :includexsrc: src/PyGame/4_Project/rocket3.py

   # load images
   rocket  = pg.image.load("rocket.png")
   planet  = pg.image.load("planet.png")

   # clear screen
   window.fill(pg.Color("black"))

   # draw rocket
   window.blit(rocket, (0, height - rocket.get_height()))

   # draw planets
   ???

Animate the martian
-------------------

Let us now animate the martian that moves under the planets, from the
left to the right of the screen and back.

.. activecode:: rocket4
   :nocodelens:
   :modaloutput: 
   :playtask:
   :includexsrc: src/PyGame/4_Project/rocket4.py

   # load images
   rocket  = pg.image.load("rocket.png")
   planet  = pg.image.load("planet.png")
   martian = pg.image.load("martian.png")

   # martian parameters - horizontal position
   martian_x = 0

   # draw game objects
   def draw():
       # these variables are changed during animation
       global martian_x
    
       # clear screen
       window.fill(pg.Color("black"))

       # draw rocket
       window.blit(rocket, (0, height - rocket.get_height()))

       # draw planets
       for i in range(8):
           window.blit(planet, (100*i, 0))

       # draw martian
       ???

       # move martian
       ???
   
React to user commands
----------------------

Now enable moving the rocket to the left or to the right using the two
arrow keys.


.. activecode:: rocket5
   :nocodelens:
   :modaloutput: 
   :playtask:
   :includexsrc: src/PyGame/4_Project/rocket5.py

   # load images
   rocket  = pg.image.load("rocket.png")
   martian = pg.image.load("martian.png")
   planet  = pg.image.load("planet.png")
    
   # martian parameters - position and speed
   martian_x = 0
   martian_y = planet.get_height()
   martian_speed = 3
    
   # rocket position
   ???
    
   # handle events
   def keydown(e):
       # variable that is changed
       global rocket_x
       # right and left arrow moves the rocket by 5 pixels
       if e.key == pg.K_RIGHT:
          ???
    
   # draw game objects
   def draw():
       # variables that are changed in this function
       global martian_x, martian_speed
    
       # clear screen
       window.fill(pg.Color("black"))
    
       # draw planets
       for i in range(8):
           window.blit(planet, (100*i, 0))
    
       # draw martian
       window.blit(martian, (martian_x, martian_y))
           
       # draw rocket
       ???
       
       # move martian
       martian_x += martian_speed
       # change direction if it falls of screen
       if martian_x < 0 or martian_x > width - martian.get_width():
           martian_speed = -martian_speed
           
