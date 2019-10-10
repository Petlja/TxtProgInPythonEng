Programs with Computation - Exercise
====================================

So far, we have learned how to load numbers in programs, how to perform computational operations on them, and how to print results. We can now practice these things with a few simple math tasks. 

Tasks without loading data
--------------------------

Example
'''''''

.. questionnote::

    **Example - Celebration**

    Jessica and Oscar are organizing a celebration. The rented space accommodates 100 people, Jessica has so far invited 43, and Oscar 28.
    
    Write a program that calculates and prints how much more space is available.

The problem can be solved as follows:

.. activecode:: console__computing_party1
    
    print(100-43-28)

or like this:

.. activecode:: console__computing_party2

    total_places = 100
    called_by_jessica = 43
    called_by_oscar = 28
    places_left = total_places - called_by_jessica - called_by_oscar
    print(places_left)


.. infonote::

    While this may seem unnecessary here, the solution with variables is worth practicing. Programs that use variables can do much more than those without variables. For example, if we load values into a program, variables are necessary. Also, more complex calculations would be very incomprehensible if they could not be broken down into simpler steps, and for intermediate values we again need variables.
    
    We mentioned earlier that we should try to give meaningful names to the variables. It doesn't matter to the computer (it works equally well with any names), but when we calculate something that matters to us, using variables with meaningful names will help us understand that program after a long time. Also, such a program will be easier to understand by other people who read it.
    

Tasks for exercise 
''''''''''''''''''

.. questionnote::

    **Task - buying for all the money**
    
    How many items for 76 euros can be bought for 500 euros? How much money will remain if the largest possible number of items is bought?

The shorter (and less clear) version of the solution is

    .. activecode:: console__computing_divmod_sol1
        :passivecode: true
        
        print(500 // 76, 500 % 76)

Write a clearer solution using variables.

.. activecode:: console__computing_divmod





.. questionnote::

    **Task - datum**

    If today is the 15th of the month and the month is 31 days, how many days are there until the 11th of the next month (at the same time)?

Your job is to write a solution in which the starting and calculated values are assigned to variables. By clicking on the "short solution" button you can see a short solution as a hint.

.. reveal:: console__computing_divmod_reveal
    :showtitle: Short solution
    :hidetitle: Hide short solution

    .. activecode:: console__computing_buying3_simple_sol1
        :passivecode: true
        
        print(11+31-15)

.. activecode:: console__computing_date



.. questionnote::

    **Task - purchase of 3 pieces**

    Ben has 20 euros and wants to buy 3 bicycle lamps for 1.58 euros each. How much money will he have left?
    
Write a program that uses variables for the starting and calculated values.

.. activecode:: console__computing_buying3_simple


            
Tasks with loading data
-----------------------

Example
'''''''

.. questionnote::

    **Example - paintwork** 
    
    Philip prepares to paint the ceiling in one room. In order to know how much paint to buy, he needs to know the dimensions of the room and how many square meters covers one kilogram of paint. Write a program that loads the length of the room, the width of the room, an area that covers one kilogram of paint, and prints the required number of kilograms of paint.
    
Solution:

.. activecode:: console__computing_painting

    length = float(input("Enter the length of the room: "))
    width = float(input("Enter the width of the room: "))
    area_per_kg = float(input("Enter the area covered by 1 kg of paint: "))
    needed_kg = length * width / area_per_kg
    print(needed_kg, "kg of paint is required.")


Tasks for exercise
''''''''''''''''''

.. questionnote::

    **Task - rabits** 
    
    The rabbit population on one island is doubling every year. Write a program that loads the current number of rabbits on the island and the number of years, and prints how many rabbits would be on the island in a given number of years if they continue to reproduce at the same pace.

.. activecode:: console__computing_rabbits



.. questionnote::

    **Task - Buying a car**

    John buys the car in installments. Write a program that sequentially loads the contract price, the amount of one installment and the number of installments, and prints how much more John will pay in total over the price stated in contract.
        
.. activecode:: console__computing_buying_car
