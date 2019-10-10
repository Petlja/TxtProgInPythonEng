Branching statements
====================

In the Karel lessons, every time we wanted Karel to move forward, we needed to check first if Karel could go ahead. These checks were necessary because if we tried to move the robot forward when the square in front of it did not exist, the program would report an error and stop working. For the same reason, we had been checking if there was a ball on a square before taking it, and we had been checking if Karel had a ball with him before dropping the ball.

Similarly, in programs with numbers we often need to compare two values, that is, to determine whether they are equal, whether one is smaller than the other, different from the other, and the like. Depending on the outcome of the comparison, the program may continue to execute in different ways.

Some of the symbols used for comparison are the same as in mathematics (for example ``<`` and ``>``) and some are not. The following table gives the notation of all standard comparisons used in mathematics and in Python (and also in many other programming languages).

====================   ==================== ========================================
Math                   Python               Meaning
====================   ==================== ========================================
:math:`а < b`          a < b                a is less than b
:math:`a \leq b`       a <= b               a is less than or equal to b
:math:`a > b`          a > b                a is greater than b
:math:`a \geq b`       a >= b               a is greater than or equal to b
:math:`a = b`          a == b               a is equal to b
:math:`a \neq b`       a != b               a is not equal to b
====================   ==================== ========================================

Notation :math:`a<b` can be understood as an expression whose value is true or false in each case. These values are written in Python as *True* and *False* and they are **logical constants**, that is, constants of the type ``bool`` which we call the logical type. Expressions whose value is true or false (logical type) are called **logical expressions**. All the expressions in the table above are logical expressions (we will see more logical expressions later).

if statement
------------

The *if* statement was already introduced in the Karel lessons, let's remind ourselves:

The *if* statement is used to decide which of the two groups of statements to execute. In Python it is written as follows:

.. activecode:: console__if_else_syntax
   :passivecode: true

   if condition:
       statement_a1
       ...
       statement_ak
   else:
       statement_b1
       ...
       statement_bm

.. infonote::

    **Meaning (semantics) of the if statement:**
    
    The statement written above means: if the condition is fulfilled, execute *statement_a1*, ... *statement_ak*, otherwise execute *statement_b1*, ... *statement_bm*.
    
    **Writing rules (syntax) of the** if **statement**
    
    - After the word ``if``, a logical expression is written and at the end of the line the character ``:`` (a colon) is required.
    - In the following lines, indented for the same number of spaces (usually 4), the statements that should be executed if the logical expression evaluates to *True* are written. There may be one or more of these statements.
    - After the commands that are executed if the condition is fulfilled, the word ``else`` is written and again the character ``:`` (colon). The word ``else`` is written at the same level of indentation as the word ``if``.
    - In the following lines, indented for the same number of spaces, write the commands that are to be executed if the logical expression evaluates to *False*. There may be one or more of these statements as well.
    
    The ``if`` statement is also called the *branching statement* because the program execution flow for this statement branches: the next statement to execute depends on the value of the logical expression in the condition. Groups of statements after the word *if* or *else* are therefore also called branches of the *if* statement.

In case the program does not need to do anything when the condition of the *if* statement is not fulfilled, that is, when we do not need *else* branch of the *if* statement, we can omit it:

.. activecode:: console__if_syntax
   :passivecode: true

   if condition:
       statement_a1
       ...
       statement_ak

We will use this short form of the *if* statement later.

If statement - examples and tasks
'''''''''''''''''''''''''''''''''

.. questionnote::
    
    **Example - who is younger:** 
    
    Peter and Mark want to play a game of pool. They agreed that the younger player plays first. Write a program that reads the age of Peter and Mark (that are not equal) and prints who will make the first move.
    
.. activecode:: console__branching_younger

    peter = int(input("How old is Peter: "))
    mark = int(input("How old is Mark: "))
    if peter < mark:
        print('Peter plays first.')
    else:
        print('Mark plays first.')





.. questionnote::
    
    **Example - packing:** 
    
    The eggs on the farm are packed in 10-pack boxes and full boxes are sent to the store. Write a program that takes the number of eggs ready for packing and prints whether all the eggs can be packed and shipped to the store, or whether a few eggs will be left unpacked temporarily.
    
Here we need to check that the number of eggs is divisible by 10. For this reason, we use the operator ``%``, which gives the remainder after division. If the remainder after dividing the number of eggs by 10 is equal to zero, all the eggs can be packed and sent.

.. activecode:: console__branching_eggs

    num_eggs = int(input("How many eggs: "))
    if num_eggs % 10 == 0:
        print('All eggs can be sent.')
    else:
        print('Some eggs will remain.')





.. questionnote::
    
    **Task - Street side:** 
    
    Even house numbers are on the right side of the street and odd house numbers on the left. Write a program that takes a house number and prints which side of the street the number is on.


Here it is needed to examine if the given number is divisible by 2. The task is similar to the previous one - if the remainder of dividing the given house number by 2 is equal to zero, the number is on the right side of the street, otherwise it is on the left side.

.. activecode:: console__branching_home_number

    number = int(input("What is the house number: "))
    # finish the program




.. questionnote::
    
    **Task - cinema:** 
    
    You have 10 euros with you. Write a program that takes the movie ticket price and popcorn price, then prints out if you have enough money for both the ticket and popcorn.
    
    

.. activecode:: console__branching_cinema

    ticket_price = int(input("How much for the ticket: "))
    popcorn_price = int(input("How much for the popcorn: "))
    # finish the program


Logical expressions
-------------------

In some tasks we need to express conditions that are more complex than simply comparing two values. The words **and**, **or** and **not** are used to connect the simpler terms, and Python uses exactly the same words for that. Here is how to evaluate such complex contidions. If *a* and *b* are any conditions, then:

- condition ``a and b`` will be fulfilled if both conditions *a* and *b* are fulfilled;
- condition ``a or b`` will be fulfilled if at least one of conditions *a* and *b* is fulfilled;
- condition ``not a`` will be fulfilled if condition *a* is not fulfilled (which we have already mentioned in the lessons on Karel);

These conditions can be further combined into even more complex ones according to the needs of the task. In complex conditions, we can use parentheses to influence the order in which the conditions are calculated (also when we are not sure which is the default order), and to make the program clearer to other people reading it. If there are no parentheses in the complex condition, *not* is applied first, then *and*, and finally *or*.

Logical expressions - examples
''''''''''''''''''''''''''''''

.. questionnote::
    
    **Example - leap year:**

    Write a program that prints whether a given year (between the 1800 and the 2200, including borders) is leaп or simple.
    
    According to the Gregorian calendar, the following rules are used to determine whether a year is simple or leap:
    
    - years that are not divisible by 4 (e.g., 1923, 1070, 2017) are simple;
    - years that are divisible by 100 and not by 400 (e.g. 1700, 1800, 1900, 2100, 2200) are also simple;
    - all other years (eg 1984, 2000, 2012) are leap. These are years that are divisible by 4 and not by 100, or are divisible by 400.

Writing down these rules in the form of logical conditions, we get:
    
.. activecode:: console__branching_leap_year1

    year = int(input())
    if (year % 4 > 0) or (year % 100 == 0 and year % 400 > 0):
        print("Year", year, "is simple.")
    else:
        print("Year", year, "is leap.")

We get an equally good solution if we use the description for leap years given in rule 3 (verify by thinking through it and by trying both programs that we get the same result):
    
.. activecode:: console__branching_leap_year2

    year = int(input())
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("Year", year, "is leap.")
    else:
        print("Year", year, "is simple.")


.. questionnote::

    **Example - office hours:** 
    
    The opening hours of one souvenir shop are from 7 to 11 in the morning and from 17 to 22 in the evening (to be considered that it works at 7:00 and at 17:00 sharp and does not work at 11:00 and at 22:00). Peter came across the store at *H* hours and *M* minutes. Write a program that takes the number *H* (from 0 to 23) and answers whether Peter came across the store during office hours.
    
.. activecode:: console__branching_working_hours1

    h = int(input())
    if (7 <= h and h < 11) or (17 <= h and h < 22):
        print("Peter came across during office hours.")
    else:
        print("Peter came across out of business hours.")
    
We can also come to a solution by gradually computing logical values, using logical variables:

.. activecode:: console__branching_working_hours2

    h = int(input())
    at_morning_office_hours  = 7 <= h and h < 11
    at_evening_office_hours = 17 <= h and h < 22
    at_office_hours = at_morning_office_hours or at_evening_office_hours
    if at_office_hours:
        print("Peter came across during office hours.")
    else:
        print("Peter came across out of business hours.")

In this solution, only *h* is an integer variable, and all others (*at_morning_office_hours*, *at_evening_office_hours*, *at_office_hours*) are logical, which means that they will get values *True* or *False* when executing the program.

Logical expressions - questions
'''''''''''''''''''''''''''''''

.. dragndrop:: console__branching_quiz_compare
    :feedback: Try again!
    :match_1: a <= b ||| a < b or a == b
    :match_2: a >= b ||| b <= a
    :match_3: not (a == b) ||| a < b or a > b
    :match_4: not (a != b) ||| a == b

    Match the equivalent expressions

.. mchoice:: console__branching_quiz_interval
   :multiple_answers:
   :answer_a: h < 7 and 11 <= h
   :answer_b: h < 7 or 11 <= h
   :answer_c: not(7 <= h) or not(h < 11)
   :answer_d: h <= 7 or 11 < h
   :correct: b, c
   :feedback_a: No, this condition is not fulfilled for any h.
   :feedback_b: Correct.
   :feedback_c: Correct.
   :feedback_d: No, the value of the conditions differs if h is exactly 7 or 11.

   What are all conditions equal to **not (7 <= h and h <11)**?


.. dragndrop:: console__branching_quiz_abc_sign
    :feedback: Try again!
    :match_1: At least one of a, b, c is positive ||| a > 0 or b > 0 or c > 0
    :match_2: None of a, b, c is positive ||| a <= 0 and b <= 0 and c <= 0
    :match_3: a, b and c are not all positive ||| a <= 0 or b <= 0 or c <= 0
    :match_4: a, b and c are all positive ||| a > 0 and b > 0 and c > 0

    Match conditions and descriptions

.. mchoice:: console__branching_quiz_sport_center
   :multiple_answers:
   :answer_a: (population <= 10000) or (population > 10000 and income <= 2000)
   :answer_b: population <= 10000 or income <= 2000
   :answer_c: population <= 10000 and income <= 2000
   :answer_d: (income <= 2000) or (income > 2000 and population <= 10000)
   :correct: a, b, d
   :feedback_a: Correct.
   :feedback_b: Correct.
   :feedback_c: Wrong.
   :feedback_d: Correct.

   The state government is offering assistance to build a sports center. Settlements with up to 10,000 residents are eligible to apply, as well as settlements with more than 10,000 residents and an average income of up to 2000. Which of the conditions correctly checks whether a settlement  can apply?

Logical expression - tasks
''''''''''''''''''''''''''

.. questionnote::

    **Task - numbers in order:** 
    
    Write a program that takes integers *a*, *b*, *c* and answers the question whether these numbers are given in order from smallest to largest.

    
.. activecode:: console__branching_increasing3

    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
    # finish the program




.. questionnote::

    **Task - middle number:** 
    
    Write a program that takes integers *a*, *b*, *c* and answers the question whether *b* is medium in size. 

    
.. activecode:: console__branching_middlenum

    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
    # finish the program
    
    
.. questionnote::

    **Task - watching the dog:** 
    
    Anna and Mark live together and have a dog named Bobby. The two are scheduled to travel the same month, Anna from day *a1* to *a2*, and Mark from day *m1* to *m2*. They both leave in the morning and return in the evening. Since they don't want to leave Bobby alone, they wonder if their trips overlap.
    
    Write a program that takes integers *a1*, *a2*, *m1* and *m2*, and answers the question of whether Anna's and Mark's travels overlap.
    
**Hint:** trips overlap if Marko leaves before Ana returns (the day of Mark's departure is less than or equal to the day of Ana's return) or vice versa - if Ana leaves before Marko returns.

.. activecode:: console__branching_intervals

    a1 = int(input("a1 = "))
    a2 = int(input("a2 = "))
    m1 = int(input("m1 = "))
    m2 = int(input("m2 = "))
    # finish the program
    
    
