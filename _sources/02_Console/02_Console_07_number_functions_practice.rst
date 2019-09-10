Math Functions - Exercise
=========================

Let's practice using the mathematical functions we have learned.

.. questionnote::
    
    **Task - advertising:** 
    
    Thomas distributes advertising packages containing one calendar, a keychain and a pen. Write a program that loads how many calendars, keychains, and pens Thomas has and then prints how many advertising packages he can make.

To finish the program insert one of the mathematical functions you have learned.

.. activecode:: console__mathfunc_promo_material

    num_calendars = int(input("How many calendars are there?"))
    num_keychains = int(input("How many keychains are there?"))
    num_pens = int(input("How many pens are there?"))
    num_packages = 0 # complete the statement
    print(num_packages, "packages can be made.")


.. questionnote::

    **Task - lemonade:** 
    
    A group of people set out on a journey and Zoe made lemonade for everyone. Write a program that loads how many liters of lemonade Zoe has made (as a real number), then writes how many half-liter bottles can be filled with that lemonade and how many bottles it takes for all the lemonade (the two numbers can vary by one at most).
    
  
.. activecode:: console__mathfunc_lemonade

.. reveal:: console__mathfunc_lemonade_reveal
   :showtitle: Help
   :hidetitle: Hide help
   
   To complete the following program, use some of the rounding functions.
   
   .. activecode:: console__mathfunc_lemonade_solution
   
        liters = float(input())
        num_full_bottles = 0 # complete the statement
        total_bottles = 0 # complete the statement
        print(num_full_bottles, "bottles can be filled.")
        print("A total of", total_bottles, "bottles are required.") 

    
.. questionnote::

    **Task - the game:**
    
    The six friends agreed to get on the playground at a certain time and play a game. Write a program that loads the delay time of each player in minutes (as whole numbers) and prints with how many minutes of delay the match could have started.
    
.. activecode:: console__mathfunc_late_game

.. reveal:: console__mathfunc_late_game_reveal
   :showtitle: Help
   :hidetitle: Hide help
   
   One possible solution is partially written below. Try to complete it.
   
   .. activecode:: console__mathfunc_late_game_help

        t1 = int(input("How many minutes late was the first: "))
        # load the remaining data the same way
        game_delay = 0 # fix this statement
        print("The match could have started with a", game_delay, "minute delay.")

.. commented out

   .. activecode:: console__mathfunc_late_game_solution

        t1 = int(input("How many minutes late was the first: "))
        t2 = int(input("How many minutes late was the second: "))
        t3 = int(input("How many minutes late was the third: "))
        t4 = int(input("How many minutes late was the fourth: "))
        t5 = int(input("How many minutes late was the fifth: "))
        t6 = int(input("How many minutes late was the sixth: "))
        game_delay = 0 # complete this statement
        print("The match could have started with a", game_delay, "minute delay.")



.. questionnote::

    **Task - two buses:** 
    
    Maya and Lola travel on the same highway in two different buses and talk on the phone. One of them has just noticed the milestone *x* and the other *y*. Write a program that loads integers: *x* and *y* and prints how many miles Maya and Lola are away from each other.
    
.. activecode:: console__mathfunc_buses

.. commented out
    
    .. reveal:: console__mathfunc_buses_reveal
       :showtitle: Help
       :hidetitle: Hide help
       
       To complete the following program, use one of the math functions you have learned.
       
       .. activecode:: console__mathfunc_buses_solution

            x = int(input("Enter x: "))
            y = int(input("Enter y: "))
            distance = 0 # complete thes statement
            print("Distance is", distance)



.. questionnote::

    **Task - Video lessons**

    The course consists of several video lessons that all last equally. You have decided to devote 90 minutes to this course every day and you want to know how many days it will take for the whole course. Write a program that loads the number of lessons and the duration of one lesson in minutes, and prints the required number of days, rounded to the nearest integer.
    
.. activecode:: console__mathfunc_videolessons
