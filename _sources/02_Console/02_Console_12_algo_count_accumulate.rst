Counting and summing
====================

It is a very common case that we are only interested in some of the data from a collection. Here we will practice how to count and, if necessary, sum numbers that are of interest to us, or that fulfill some condition.

Counting
--------

The general form of a program (algorithm) by which we count the elements of a collection that meet a given condition looks like this:

.. code::

    num = 0
    for x in collection:
        if (x meets the condition):
            num += 1
    print(num)
    
.. infonote::

    The statement ``x += a`` increases the value of the variable *x* by *a*. This is actually an abbreviated form of the statement :code:`x = x + a`, which assigns the value *x + a* to the variable *x*.

    The statement ``x -= a`` decreases the value of the variable *x* by *a*. This is an abbreviated form of the statement :code:`x = x - a`, which assigns the value *x - a* to the variable *x*.
    
In our example, the statement *num += 1* increases the value of the variable *br* by 1.


Examples and tasks
''''''''''''''''''

.. questionnote::

    **Example - meeting:** 
    
    The team leader has offered two options for the time of the meeting to be held tomorrow. Each team member wrote in a table which term would be more appropriate for him/her (1 for the first term, 2 for the second). This information was transferred to the first line of the following program.
    
    Complete the program - script, so that given the data on voting of team members, it prints how many voted for the first and how many for the second term.
    
.. activecode:: console__counting_meeting

    terms = (1, 2, 2, 1, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 1)
    
For example, we can count the number of team members who voted for the first term, and calculate the rest at the end.

.. activecode:: console__counting_meeting_sol1

    terms = (1, 2, 2, 1, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 1)

    num_first_term = 0
    for t in terms:
        if t == 1:
            num_first_term += 1
            
    num_second_term = len(terms) - num_first_term

    print(num_first_term, 'members voted for the first term and', num_second_term, 'for the second term.')

Another way is to count the votes for both the first term and the second term.

.. activecode:: console__counting_meeting_sol2

    terms = (1, 2, 2, 1, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 1)

    num_first_term = 0
    num_second_term = 0
    for t in terms:
        if t == 1:
            num_first_term += 1
        if t == 2:
            num_second_term += 1
    print(num_first_term, 'members voted for the first term and', num_second_term, 'for the second term.')

or, assuming the data is "clean", that is, there are no values other than 1 and 2:

.. activecode:: console__counting_meeting_sol3

    terms = (1, 2, 2, 1, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 1)

    num_first_term = 0
    num_second_term = 0
    for t in terms:
        if t == 1:
            num_first_term += 1
        else:
            num_second_term += 1
            
    print(num_first_term, 'members voted for the first term and', num_second_term, 'for the second term.')

In case the information is not known in advance but should be entered, we could write a program like this:

.. activecode:: console__counting_meeting_sol4

    n = int(input("How many team members voted: "))
    num_first_term = 0
    for i in range(n):
        t = int(input("Enter one vote: "))
        if t == 1:
            num_first_term += 1
            
    num_second_term = n - num_first_term
    print(num_first_term, 'members voted for the first term and', num_second_term, 'for the second term.')

At the beginning of this program, we load the number of votes *n*, then use the *for* loop to repeat loading and counting one vote *n* times.


.. questionnote::

    **Task - written test:** 
    
    Several people took the traffic proficiency test, which is a prerequisite for taking the practical part of the exam. A test is considered passed if the number of incorrect answers is less than or equal to 3.
    
    At the beginning of the script are given the test results of one group of candidates (number of incorrect answers for each person who took the test). Complete the script by listing how many candidates have passed the test.
    
.. activecode:: console__counting_test

    num_incorrect = (2, 5, 1, 0, 4, 2, 7, 1)
    passed = 0

    # add the missing statements here
    
    print(passed)
    
.. commented out
    
    passed = 0
    for x in num_incorrect:
        if x <= 3:
            passed += 1
    print(passed)



.. questionnote::

    **Task - swimming pool** 
    
    A visit to the pool is being prepared for a group of children. Anyone lower than 160 centimeters can only go into the smaller pool. The organizer is interested in how many children are below 160 centimeters in order to plan the groups.
    
    Children's heights are given at the beginning of the program. Complete the program to print the number of children lower than 160 centimeters.
    
.. activecode:: console__counting_swimmingpool

    heights = (160, 161, 174, 149, 153, 160, 158, 182, 144)
    
    


.. questionnote::

    **Task - humidity** 
    
    In a botanical garden, soil moisture is measured once a day for rare and sensitive species. Humidity is expressed in numbers from 0 to 1, and conditions for the development of plants are considered to be good when the humidity is between 0.3 and 0.7 (including boundaries).
    
    Values of humidity (measured over a period of time) are given at the beginning of the script. Complete the script by printing the number of days when the humidity was not good.

.. activecode:: console__counting_humidity

    humidity = (0.2, 0.5, 0.61, 0.40, 0.72, 0.51, 0.43, 0.35, 0.28)
    


Summing
-------

In one big group of practical problems, we come to the result by gradually building (accumulating) it as we go through the data. For example, if we need the sum of some numbers, we can get to it in this general way:

.. code::

    total = 0
    for num in collection:
        total += num
    print(total)


When we are computing the sum of all the elements of a collection, we get the same result by calling the *sum* function:

.. code::

    print(sum(collection))

We will use gradual formation of results when we need only some elements from the collection, that is, those that fulfill the given condition. In this case, the algorithm for calculating the sum would generally look like this:

.. code::

    total = 0
    for num in collection:
        if (num meets the condition):
            total += num
    print(total)

In order to obtain the mean of the data that fulfills a condition, it is necessary to count and add up such data, and then divide their sum by their number. In the general case it looks like this:

.. code::

    total = 0
    counter = 0
    for num in collection:
        if (num meets the condition):
            total += num
            counter += 1
    print(total / counter)

Note that in Python, the sum and mean of the selected elements of the collection can be obtained in a shorter and more efficient way. We chose the above method because it looks almost the same as in other programming languages.

Examples and tasks
''''''''''''''''''

.. questionnote::

    **Example - Average IQ test result:** 
    
    The results of an IQ test for a group of people are given. A score of -1 means that the person did not take the test. Complete the program by printing the mean obtained on the test.

.. activecode:: console__accumulate_IQ

    iq_results = (-1, 98, 115, -1, 83, 130, 101, 122, -1, 108)

We can write the program like this:

.. activecode:: console__accumulate_IQ_sol

    iq_results = (-1, 98, 115, -1, 83, 130, 101, 122, -1, 108)
    num_tested = 0
    iq_sum = 0
    
    for result in iq_results:
        if result != -1:
            iq_sum += result
            num_tested += 1

    if num_tested > 0:
        mean_iq = iq_sum / num_tested
        print('Mean IQ is', mean_iq)
    else:
        print('No one was tested.')


.. questionnote::

    **Task - on duty:**  
    
    In Company X, all employees occasionally remain on-call. The norm for the previous period is 20 hours on-call. Every extra hour (over 20 hours) on-call is additionally paid. The number of on-call hours for each employee is given, and the director wants to know the total number of on-call hours **over the norm**.
    
    Complete the program by computing and printing the total number of overtime hours on-call.
    
If you solve the task correctly, you should get a score of 25 for the data given, since :math:`(21-20)+(23-20)+(34-20)+(25-20)+(22-20)=25`.


.. activecode:: console__accumulate_overtime

    norm = 20
    hours_on_duty = (21, 23, 19, 34, 25, 22, 17)
    total_overtime = 0
    # complete the program
    
    print('Total overtime on call is', total_overtime)
    
.. commented out
    
    norma = 20
    hours_on_duty = (21, 23, 19, 34, 25, 22, 17)
    total_overtime = 0
    for hours in hours_on_duty:
        if hours > norm:
            total_overtime += (hours - norm)
    print('Total overtime on duty is', total_overtime)






.. questionnote::

    **Task - average yield:**  
    
    In one orchard after the third year, plum yield per tree is monitored. Trees with yields below 3 kilograms are considered damaged or diseased and will be taken out.
    
    The yield of all the trees in the orchard is given. Complete the program by calculating and printing the average yield of healthy trees (with yields of 3 kilograms or more).

    
You should get a result of approximately 14.757 for the given data.

    
.. activecode:: console__accumulate_yield

    yield_per_plant = (11.3, 15.8, 9.5, 2.6, 21.1, 13.4, 17.9, 0.7, 14.3)
    
    # complete the program
