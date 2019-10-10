Math functions
==============

We use functions in programming all the time. For example, *print()*, *input()*, *int()*, *float()* and *str()* are functions of the Python language that we have used so far. There are many other functions in Python, and many of them are used in mathematics. We'll see some of the simpler math functions below.

Functions *abs()*, *min()* and *max()*
--------------------------------------

The *abs()*, *min()* and *max()* functions are often used in computational tasks. You probably already used them somewhere, so let's just explain them briefly:

- the *abs()* function returns the absolute value of a numeric expression, which is passed to it as an argument (the absolute value of a number is obtained by ignoring the sign of the number, see example below);
- the *min()* function can have two or more numeric arguments, and returns the value of the smallest of them;
- the *max()* function can have two or more numeric arguments, and returns the value of the greatest of them;

Here's how to use these functions in a program:

.. activecode:: console__numberfunc_absminmax_example

    print("abs(3) =", abs(3))
    print("abs(-7) =", abs(-7))
    print("abs(-5 - -2) =", abs(-5 - -2))
    print("min(5, 2, 7, 3) =", min(5, 2, 7, 3))
    print("max(5, 2, 7, 3) =", max(5, 2, 7, 3))

Functions *abs()*, *min()* and *max()* - questions
--------------------------------------------------

Check your understanding of the above functions:

.. mchoice:: console__numberfunc_min
   :answer_a: 10
   :answer_b: 20
   :answer_c: 30
   :correct: a
   :feedback_a: Correct!
   :feedback_b: The min function returns the smallest of the values passed to it as arguments.
   :feedback_c: The min function returns the smallest of the values passed to it as arguments.
		
   What is the value of the expression ``min(10, 20, 30)``?

.. mchoice:: console__numberfunc_max
   :answer_a: 10
   :answer_b: 20
   :answer_c: 30
   :correct: c
   :feedback_a: The max function returns the largest of the values passed to it as arguments.
   :feedback_b: The max function returns the largest of the values passed to it as arguments.
   :feedback_c: Correct!
		
   What is the value of the expression ``max(10, 20, 30)``?

.. dragndrop:: console__numberfunc_max_0x100
    :feedback: Try again!
    :match_1: the value of the expression is 0 ||| if x is less than zero
    :match_2: the value of the expression is x ||| if x is between 0 and 100
    :match_3: the value of the expression is 100 ||| if x is greater than 100
    
    Match the values of the expression ``min(100, max(0, x))`` with the conditions for x.

.. dragndrop:: console__numberfunc_max_0x
    :feedback: Try again!
    :match_1: abs(x)||| x if x is positive, and the opposite number otherwise
    :match_2: max(0, x)||| x if x is positive and zero otherwise
    :match_3: min(0, x)||| x if x is negative and zero otherwise
    :match_4: min(0, abs(x))||| always zero
		
    Match expressions with their values.

Value Rounding Functions
------------------------

Rounding up real value to an integer is an operation we also often need. We have already seen that by converting a real number to a whole number, we round it towards zero. There are a few more functions that we can use in Python to round up a real number in different ways:

- function *round()* returns the integer closest to the argument (type of the result is int);
- function *floor()* returns the nearest integer less than or equal to the argument value (type of the result is float);
- function *ceil()* returns the closest integer greater than or equal to the argument value (type of the result is float);

Run the following program to see how these functions work and to compare them.

.. activecode:: console__numberfunc_rounding_example

    import math
    
    print("round(56.234) =", round(56.234))
    print("round(56.789) =", round(56.789))

    print("math.floor(56.234) =", math.floor(56.234))
    print("math.floor(56.789) =", math.floor(56.789))

    print("math.ceil(56.234) =", math.ceil(56.234))
    print("math.ceil(56.789) =", math.ceil(56.789))


Note that the *floor* and *ceil* functions are somewhat different from the *round* function and all previous functions - it says `` math.`` in front of their name in the program. This is because these functions are defined in a module called *math*. Modules are programmatic entities that contain various functions, constants, and other pieces of code that we can use in our programs. The *math* module contains many other functions in addition to the *floor* and *ceil* functions. For example, the known constant pi can be used as *math.pi*, and the function square root as *math.sqrt* (we will not use them here).

In order to use the functions of the *math* module, we need to attach this module to our program. We did this by writing ``import math`` at the beginning of the program. This, of course, enables us to use all other mathematical functions and everything else defined in this module as well.

No special module is required for the *round* function and all the previous functions, since these functions are built into Python itself, so they are always directly available to us.

Value Rounding Functions - Questions
------------------------------------

Check your understanding of the functions explained in this lesson:

.. mchoice:: console__numberfunc_abs_round
   :answer_a: -2
   :answer_b: 2
   :answer_c: -3
   :answer_d: 3
   :correct: d
   :feedback_a: Read the explanations about abs and round functions again.
   :feedback_b: The round function returns the closest integer.
   :feedback_c: The abs function returns the absolute value of a number, which is always greater than or equal to zero.
   :feedback_d: Correct!
		
   What is the value of the expression ``abs(round(-2.7))``?
   
.. mchoice:: console__numberfunc_max_abs
   :answer_a: max(x, round(x))
   :answer_b: max(x)
   :answer_c: round(x)
   :answer_d: abs(x)
   :correct: a
   :feedback_a: Correct!
   :feedback_b: The max function should have at least two arguments.
   :feedback_c: In this way, the amount can also be reduced.
   :feedback_d: The amount is already positive, nothing is achieved here with the abs function.
		
   One cashier rounds the bill to the nearest integer only if the amount is increased by rounding, otherwise it reports the amount as it is. What formula does this cashier apply (x is the starting value of the bill)?

.. dragndrop:: console__numberfunc_rounding
    :feedback: Try again!
    :match_1: towards zero|||int()
    :match_2: to a closer whole number|||round()
    :match_3: to a smaller whole number|||floor()
    :match_4: to a greater whole number|||ceil()

    Match rounding functions with the way of rounding.

.. questionnote::

    **The task for the curious** - function *round*
    
    The *round* function can also be called with two arguments (we won't use it that way), where the second argument is usually a small integer. Check for example the values of :math:`round(123.23456, 2)`, :math:`round(123.23456, 3)` and :math:`round(123.23456, -1)`. You can use the space below for trying things out quickly.
    
    Try explaining what the second argument of *round* is for when a function is called with two arguments.
    
.. activecode:: console__givenfunc_round

