Reading data
============

Reading text
------------

The programs we have learned to write so far contain all the information needed and always work the same way. When we need a program to do the same thing with different data, we would have to modify the program itself. This method may be quite appropriate when changes to the data are small and not frequent.

Another way to get our program to handle more diverse tasks is to enable data entry. Iserting data into a program during its execution is done using the *input()* function. This function works by waiting for the program user to type something (and press the *Enter* key) and then returning the typed text as a result.

When you run this program, to see how it works, type something and press *Enter*. Try the same program in the *IDLE* environment or on the *repl.it* site.

.. activecode:: console__text_input_first

    s = input()
    print("You wrote", s)

The program works as described, but this program behavior can be confusing. If someone were to run a program like this in the *IDLE* environment without knowing that the program was expecting data, it might look like their computer was locked because nothing was happening, and in fact the program was just waiting for input from the keyboard.

To help the user understand what is expected of them, we can also use the form of the *input* function with a single text argument, which will be printed as a guide to the user. For example:

.. activecode:: console__text_input_prompt

    s = input("Write something: ")
    print("You wrote", s)

Whether we choose one or the other form of the *input* function, depends on the purpose of the program. When writing a program in which other people will enter data, we use a form with an argument, serving as an instruction. When we write a program only for personal short-term (maybe even one-time) use, then we have no need for instructions and can use a form without arguments.

Also, be aware that for some of the environments in which the program is running, we can arrange that data is being read from another location where we prepared it n advance, instead of reading the data from the keyboard. In such cases there is no waiting for the data to be entered, it is loaded automatically and there is no need to print the instruction. Therefore, in such cases we would also use the *input* function without arguments.

Reading numbers
---------------

We have seen that the *input()* function returns a string (text typed by a user). This means that if we need data of another type, we need to change the type of data returned by the *input()* function from string to the desired type. Changing the data type is also called **conversion**. For example, if we want an integer, then we need to convert the resulting text to an integer. Here's how to do it in Python:

.. activecode:: console__text_input_int1

    s = input("Enter a whole number: ")
    n = int(s)
    print(n+n)

The ``int()`` function converts a text value to an integer value. Thus, with the command ``n = int(s)`` we place an integer value in the variable *n*, which is why the + sign in the program represents the addition of integers. Summation is added to the program as proof that *n* is indeed an integer value (the result shows that the values are added up as numbers).

Since the *input* function returns a string, we can also pass its result directly to the *int* function. That way we avoid using the *s* variable and get a slightly shorter program that does the same thing:

.. activecode:: console__text_input_int2

    n = int(input("Enter a whole number: "))
    print(n+n)

~~~~

For a real number, *int* should just be replaced with *float*, because the ``float()`` function converts a text value to a real number. For example, if we want to load a real number and print twice that number, the program may look like this:

.. activecode:: console__text_input_float1

    s = input("Enter a real number: ")
    a = float(s)
    print(2*a)

or

.. activecode:: console__text_input_float2

    a = float(input("Enter a real number: "))
    print(2*a)


Check out what happens in these two examples when you enter something else rather than a number.

About conversions
-----------------

We have seen that when a string contains an integer or a real number, that string can be converted to an integer or real type using the *int()* or *float()* functions. On the other side, integers and real numbers can always be converted to a string. The *str()* function is used to convert to a string.

.. activecode:: console__text_convert_to_str

    a = 1
    a_str = str(a)
    print(a_str + a_str)

    b = 2.1
    b_str = str(b)
    print(b_str + b_str)

The conversion of an integer value to a real one is done automatically when needed, although we can also do this explicitly by calling the *float* function.

.. activecode:: console__text_convert_int_to_float

    print(float(1))
    
Conversely, when we need to convert a real number to an integer, that conversion does not happen automatically (for a reason) and needs to be set in the program by calling the *int()* function. When converting a real number to an integer, any decimals of the real number are discarded, which means that rounding is always **towards zero**. In other words, when the value of the real number *x* is not integer, * int(x)* is closer to zero than *x*.

.. activecode:: console__text_convert_int_float

    print(float(1))
    
    print(int(1.68))
    print(int(-1.68))
    
Questions
---------

.. mchoice:: console__text_quiz_1
    :answer_a: The program will print 5
    :answer_b: The program will print 23
    :answer_c: An error will occur when trying to add a string and a number
    :correct: c
    :feedback_a: Try again.
    :feedback_b: Try again.
    :feedback_c: Correct!
    
    What happens when we run the next program and enter ``2``?
    
    .. code::
    
        a = input()
        print(a+3)

.. mchoice:: console__text_quiz_2
    :answer_a: The program will print 5
    :answer_b: The program will print 23
    :answer_c: An error will occur when trying to add a string and a number
    :correct: b
    :feedback_a: Try again
    :feedback_b: Correct
    :feedback_c: Try again
    
    What happens when we run the next program and enter ``2``?
    
    .. code::
    
        a = input()
        print(a+'3')

.. dragndrop:: console__text_quiz_4
    :feedback: Try again!
    :match_1: '2.11'|||str(2.1) + '1'
    :match_2: 3.1|||float('2.1') + 1
    :match_3: error in computation|||float('2.1') + '1'
    :match_4: 2.11|||float('2.1') + 1/100
    :match_5: '3.1'|||str(2.1 + int('1'))

    Match the expressions with the calculation results.


.. mchoice:: console__text_quiz_5
   :answer_a: When the first decimal place of a is greater than or equal to 5
   :answer_b: When the number a is negative
   :answer_c: When the number a is positive
   :answer_d: When the number a is single-digit
   :answer_e: When the difference between a and int(a) is greater than 0.5
   :correct: b
   :feedback_a: Try again.
   :feedback_b: Correct!
   :feedback_c: Try again.
   :feedback_d: Try again.
   :feedback_e: Try again.

   When is the integer *int(a)* greater than the real number a?

