Computing with lists
====================

Here we will practice using of lists and combining the techniques we have learned so far.


.. questionnote::

    **Example - the smallest positive number**
    
    A tuple of numbers is given. Print the smallest positive number from that tuple.

This task is a combination of the tasks we have done so far. In the first part of the assignment we copy the positive numbers from the tuple into the list, and in the second part we apply the function *min* to the list of positive numbers.

.. activecode:: console__list_min_positive

    a = (-4, 3, 4, -3, 5, 6, 2, -5)
    positive = []
    for x in a:
        if x > 0:
            positive.append(x)

    print(min(positive))

We mentioned that the functions *min*, *max*, *sum*, *len* can be applied to different collections, and we have shown this with examples of tuple, range and string (except the sum of the elements of a string). We now see that the *min* function also accepts a list as its argument. The same holds for the functions *max*, *sum*, *len*.





.. questionnote::

    **Example - failures**
    
    There are 10 machines in one factory and they are represented by numbers from 0 to 9. For each malfunction that occurred, the number of the malfunctioning machine was recorded. A tuple is given with these numbers describing failures.

    Write a program that lists how many times each of the machines malfunctioned, followed by the numbers of the machines that had never failed.
        
.. activecode:: console__list_malfunctions

    failures = (0, 2, 1, 3, 2, 4, 2, 6, 4, 7, 4, 8)

The first part of the assignment requires that we count the number of times each number appears in the input data. To solve this part of the task, we create the list *num_failures* of 10 elements (that are initially zero), in which each element corresponds to one machine and counts its failures.

.. code::
    
    num_failures = [0] * 10
    for machine in failures:
        num_failures[machine] += 1

After that, we print out for each machine how many failures it had. We use the range here because we want to print machine sequence number and number of failures for each machine:

.. code::

    for i in range(10):
        print('Machine', i, 'failed', num_failures[i], 'times.')

The second part of the assignment asks us to print the machine numbers that had never failed. These are machines whose number of failures is zero. We go through the list *num_failures* again and insert indices of elements equal to zero in the new list, named *not_failed*:

.. code::

    not_failed = []
    for i in range(10):
        if num_failures[i] == 0:
            not_failed.append(i)
            
Finally, we print the items of the list *not_failed*.

.. code::

    print('Machines that did not break down:')
    for machine in not_failed:
        print(machine)

Here's what the whole program looks like:

.. activecode:: console__list_malfunctions_sol

    failures = (0, 2, 1, 3, 2, 4, 2, 6, 4, 7, 4, 8)
    num_failures = [0] * 10
    for machine in failures:
        num_failures[machine] += 1
        
    for i in range(10):
        print('Machine', i, 'failed', num_failures[i], 'times.')

    not_failed = []
    for i in range(10):
        if num_failures[i] == 0:
            not_failed.append(i)
            
    print('Machines that had never failed:')
    for machine in not_failed:
        print(machine)






.. questionnote::

    **Task - football fans**

    Football fans from 8 countries are coming to the tournament in the city *X*. Tournament organizers want to know how many fans come from each country.
    
    
    Each country is represented by a number from 0 to 7. The given numbers for each fan tell what country he or she comes from. Complete the program below that lists for each country how many fans come from it.

The assignment asks for each number 0 to 7 to count how many times that number appears among the given numbers. The missing part in the script is very similar to counting the failures in the given example.

.. activecode:: console__list_counters

    fans = (1, 2, 3, 2, 3, 0, 2, 4, 3, 5, 6, 4, 0, 5, 3, 7, 1, 6, 3)
    num_fans = [0] * 8
    for # complete the statement

    for country in range(8):
        print(num_fans[country], 'fans arrive from country', country)
        

.. commented out

    fans = (1, 2, 3, 2, 3, 0, 2, 4, 3, 5, 6, 4, 0, 5, 3, 7, 1, 6, 3)
    num_fans = [0] * 8
    for country in fans:
        num_fans[country] += 1

    for country in range(8):
        print(num_fans[country], 'fans arrive from country', country)






.. questionnote::

    **Task - most fans**
    
    This is the continuation of the previous task. Organizers now additionally want to know from which country most fans come.

    Copy the previous program and append it so that it eventually prints out the number of the country from which most fans come.

If you complete the task correctly, the program should print number 3, because that number appears most often in the data.

.. questionnote::

.. activecode:: console__list_max_counter

    fans = (1, 2, 3, 2, 3, 0, 2, 4, 3, 5, 6, 4, 0, 5, 3, 7, 1, 6, 3)






.. questionnote::

    **Task - The biggest negative number**

    A tuple of numbers is given. Print the largest negative number from that tuple.

.. activecode:: console__list_max_negative

    a = (-4, 3, 4, -3, 5, 6, 2, -5)







.. questionnote::

    **Task - small sales**

    The tuple is given that contains the amounts of customer accounts in one sales network. All sales of less than 500 are considered small sales. Write a program that calculates the total revenue from all small sales.

There are two ways to solve this task. One is to extract small amounts to a separate list and apply the *sum* function to that list. Another way is to gradually build up the sum, as we did in the lesson on counting and summing.

.. activecode:: console__list_sum_small_sales

    sales = (158, 681, 249, 1250, 335, 5400, 455)


