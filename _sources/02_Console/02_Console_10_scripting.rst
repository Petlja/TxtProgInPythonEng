Scripts and *for* loop
======================

Scripts
-------

People often write short programs In Python and use them by themselves to calculate or automate something. Such programs are also known as **scripts.** It is not unusual for scripts to have some or all of the input data contained within the script itself instead of being loaded. For example, the following script calculates a 20 percent discount:

.. activecode:: console__scripting_fixed

    discount = 20
    regular_price = 250
    discounted_price = regular_price * (1 - discount / 100)
    print(regular_price, discounted_price)

Instructions for using this script could be: "In the first two lines of the script, set the values you want and then run the script."

You won't see a similar instruction for programs you install on your computer or mobile phone. We call such programs **applications**, and they are written so that users do not need to know (and most often they cannot know) what the statemets of that program look like.

With scripts, there is no strict division between users and developers as with applications. Scripts are often written for personal use or for a user who uses or understands programming. All the programs in this guide are actually more scripts than applications.

We have already emphasized that this manual is not intended only for future professionals in programming. If you do not program applications, you can still benefit from programming. You may write a script or customize an existing one, as expected in the presumed instruction of the previous example.

Repeating computation for multiple data
---------------------------------------

Let's make the previous example more general. Suppose that in one store we are entitled to a 20 percent discount over the regular prices. We are interested in discounted prices of various products, whose regular prices we know.

**Restarting program that loads data**

The solution we already know how to write is to load the regular price of the product and then calculate and print the reduced price. This program can look like this:

.. activecode:: console__scripting_input

    discount = 20
    regular_price = int(input())
    discounted_price = regular_price * (1 - discount / 100)
    print(regular_price, discounted_price)

We can run the program multiple times, setting each time a regular price for one of the products we are interested in.


**Multiple inputs in the program itself**

In the case where we know in advance all the regular prices of products that interest us, multiple program launches and entering one price at a time is not the most comfortable way to get all the discounted prices. Instead, it would be more convenient to enter all regular prices directly into the program and to repeat calculation and printing the results for each of these data.

*for* statement
---------------

In order to be able to repeat some part of the program for each piece of multiple data, we need the **for** statement, which allows other statements to be repeated. Now we are going to see one way to use *for* statement, and we will see some other forms of *for* statement in the following lessons.

Let's return to the discounted price example. Let's say that the regular prices of the products we are interested in are 250, 120, and 310 and we want to calculate the discounted prices for those products with a single execution. Here is how we can do it:

.. activecode:: console__scripting_for

    discount = 20
    for regular_price in (250, 120, 310):
        discounted_price = regular_price * (1 - discount / 100)
        print(regular_price, discounted_price)

Note: notation (250, 120, 310) is called a **tuple**.

Running the program we see that it prints:

.. code::

    250 200.0
    120 96.0
    310 248.0

We notice that the last two lines of the program were executed three times, with the variable *regular_price* receiving the values 250, 120, 310 in that order. We achieved this with the ``for`` statement. The parts of the program that are repeated are called loops, so we can say that in the previous example we used a **for loop**.

The following figure shows the main elements of the *for* loop:

.. image:: ../../_images/Console/console_loop_tuple.png
  :width: 400px
  :align: center

- Required elements are written in red (the words ``for``, ``in`` and the colon character ``:`` in the first line). These elements are written in the same way in each *for* statement.
- The **loop variable** is written in blue. At that place we write the name of the variable that will take the values specified in the tuple. In our example, the loop variable is *regular_price*.
- A tuple of values is written in green. At that place we write comma-separated values in parentheses. These are the values that loop variable will take in turn. In our example, the tuple is (250, 120, 310).
- **The body of the loop** is written in black. These are commands that are executed once for each value of the loop variable. Loop variables may or may not be used in statements of the loop body.

Statements of the loop body are written indented with respect to the first line of the *for* statement. It is common to use 4 indentation spaces and we will stick to that recommendation.


Examples and tasks
''''''''''''''''''

.. questionnote::
    
    **Example - when to depart**
    
    Ronnie should arrive at destination no later than 5:00 pm. Depending on the way of travel he chooses, Ronnie may need 55, 70, 85, or 95 minutes. Write a program that prints for each way of travel when Ronnie needs to leave at the latest to arrive on time.
    
    
A program that solves this task could look like this:

.. activecode:: console__scripting_start_travel
    
    arrival = 17*60
    for travel_duration in (55, 70, 85, 95):
        leaving = arrival - travel_duration
        leaving_hours = leaving // 60
        leaving_minutes = leaving % 60
        print("If the travel lasts", travel_duration, "minutes, Ronnie should leave at", leaving_hours, "hours and", leaving_minutes, "minutes.")




.. questionnote::

    **Task - trip duration**

    George intends to start a 600-kilometer car trip at 9 a.m. and is interested in arriving time if he was traveling at an average speed of 90, 100, 120 or 130 kilometers per hour. Finish the program to list the time of arrival at the destination for each of the aforementioned average speeds.
    
.. activecode:: console__scripting_speed

    path_length = 600 # Km
    leaving = 9       # h
    for a in ():  # fix
        trip_duration = path_length / speed # h
        arrival = leaving + trip_duration    # h
        arrival_hours = int(arrival)
        arrival_minutes = round((arrival - arrival_hours) * 60)
        print("At", speed, "km / h the arrival time is at", arrival_hours, "hours and", arrival_minutes, "minutes.")
        
.. commented out

    path_length = 600
    leaving = 9
    for speed in (90, 100, 120, 130):
        trip_duration = path_length / speed
        arrival = leaving + trip_duration
        arrival_hours = int(arrival)
        arrival_minutes = round((arrival - arrival_hours) * 60)
        print("At", speed, "km / h the arrival time is at", arrival_hours, "hours and", arrival_minutes, "minutes.")




.. questionnote::

    **Task - final grade**

    The sum of 5 Katie's grades so far is 23. Katie expects another grade from the final control task. Finish the program below so that for each possible final grade (1, 2, 3, 4, or 5) it prints what the average grade would be in that case.
    
.. activecode:: console__scripting_final_mark

    sum_grades_so_far = 23
    num_grades_so_far = 5
    for # complete the statement
        average_grade = 0 # fix
        print("With the final grade", final_grade, "average grade would be", average_grade)



.. questionnote::

    **Task - allowance**

    Theo makes a plan for spending his pocket money over a 14-day vacation. Write a program that, for an average daily spend of 5, 10, or 20 euro, lists how much money in total Theo would need in each case.
   

.. activecode:: console__scripting_allowance

    num_days = 14
    # finish the program

