Text values
===========

In addition to integers and real numbers, one of the basic types of data in programming is text. The text data is called a **string**. In addition to letters, they can contain all other characters used in the text: punctuation, parentheses, numbers, mathematical operators, various special characters such as ``%``, ``$``, ``^``. ``&`` etc.

Text values are written between quotation marks. We call the text under quotation marks a **text constant** or a **literal**. Single ``'...'`` and double ``"..."`` quotes can equally be used in Python (it is only important that quotes are of the same type at the beginning and end of the string). For example:

.. code::

    s1 = 'One text'
    s2 = "Another text"

We will use the word string for the textual data type, as well as for any expression whose value is that type. The most important examples of string expressions are text constants (literals) and variables that contain text.

Printing text
-------------

The strings are printed in the same way as the numeric data. The string we want to print is simply specified as a *print()* function argument.

.. activecode:: console__text_hello

    print("Hello world!")

When the *print()* function has multiple arguments, these arguments can be of different types:

.. activecode:: console__text_compute

    print('2+2 =', 2+2)

When we use multiple arguments, we write them separated by commas (as with any function). The values of all the arguments specified will be printed in the same order, and will be separated by one space.

More about printing numbers
---------------------------

Sometimes the printed result looks illegible:

.. activecode:: console__text_format1a

    print(5/3)

Most often we don't need all these digits. Real numbers can look more readable if we use the *format* function. With this function (among other things) we can specify how many digits after the decimal point we want to display:

.. activecode:: console__text_format1b

    x = 5/3
    s = format(x, '.2f')
    print(s)
    
To specify the number of decimal places to display, we called the *format* function like this: the first argument of the function is the value we print, and the second argument is the description of the printing format. In this description, the part '.2' means that we want two decimal places, and the part 'f', abbreviated from *float*, means that we give a description for a real number (the type of real numbers is called *float*). The function returns a string in which the number *x* is written as specified.

Note that this formatted printing does not change the value of the variable *x*.

We've broken the example down into steps to make it clearer, though it could also be written in one line of code. For example, to print with 4 decimal places:

.. activecode:: console__text_format1c

    print(format(5/3, '.4f'))
    
~~~~

When displaying multiple real numbers one below the other, we can make them more readable by aligning the decimal points. For example, this way of printing is not easily comprehensible:

.. activecode:: console__text_format2a

    print(-1.23)
    print(7251.7)
    print(84.15)

To get a more readable look, we can use the *format* function like this:

.. activecode:: console__text_format2b

    print(format(-1.23, '8.2f'))
    print(format(7251.7, '8.2f'))
    print(format(84.15, '8.2f'))

In the description '8.2f' the number 8 means that the textual version of the given number should be left-padded with spaces (if needed) to take up total of 8 places. These 8 places include the digits, the decimal point, possible sign of the number and spaces in front of the number. 

Other parts of the description ('.2f') have the same meaning as before.


The *format* function has many other features, but we will not use them here.


String operations
-----------------

Joining strings
'''''''''''''''

Strings can be joined together with a **string concatenation** operation. This operation is denoted by the sign ``+``, just like the operation of summation, so in programming concatenation is often informally called string addition.

.. activecode:: console__text_concat1

    s = 'continu' + 'ation'
    print(s)

Sometimes, we may have an integer or a real number wiitten in a string, so it is important to understand when the sign ``+`` refers to the addition of numbers, and when concatenation of strings. For example, in the following program, the first *a + b* is the addition of numbers, and the second is the addition of strings. Accordingly, the printed results also differ (try it out).

.. activecode:: console__text_concat2

    a = 14.2
    b = 1
    print(a + b)
    
    a = '14.2'
    b = '1'
    print(a + b)

It is likely that occasionally you may be confused by the result when executing a program. The result may be different than expected for many reasons, and one possibility is that you unintentionally added up strings instead of numbers.

The ``+`` character can stand between two numeric expressions or between two strings, but not between a string and a number (in any order). Such combinations result in a *TypeError* (try it).

.. activecode:: console__text_concat3

    print('2' + 2)

String multiplication
'''''''''''''''''''''

Strings can also be multiplied. This means that it is allowed to multiply a string by an integer (either from left or right), and the result is a new string, which is obtained by repeating a given string a given number of times.

In the following example we underline the numbers with a line, and that line is obtained as a result of multiplying the string '-' by 12.

.. activecode:: console__text_str_mult

    a = 1.23958
    b = 5467251.707256
    c = 384.150576
    total = a + b + c
    print(format(a, '12.2f'))
    print(format(b, '12.2f'))
    print(format(c, '12.2f'))
    print(12 * '-')
    print(format(total, '12.2f'))

    
Questions and Tasks
-------------------

.. dragndrop:: console__text_quiz_format
    :feedback: Try again!
    :match_1: '12.34'|||format(12.34, '.2f')
    :match_2: '__12.34'|||format(12.34, '7.2f')
    :match_3: '_12.34'|||format(12.34, '6.2f')
    :match_4: '__12.3'|||format(12.34, '6.1f')
    :match_5: '12.3'|||format(12.34, '.1f')

    Match the *format* function calls with the results. The spaces are represented by '_' as they would not otherwise be visible.

.. mchoice:: console__text_quiz_quotes
    :answer_a: s = 'a' + "b"
    :answer_b: s = 'ab"
    :answer_c: s = 'ab'
    :correct: b
    :feedback_a: Try again
    :feedback_b: Correct!
    :feedback_c: Try again
    
    Which of the statements is faulty?

.. mchoice:: console__text_quiz_tralala
   :multiple_answers:
   :answer_a: print('tra' + 2 * '-la')
   :answer_b: print('tra-' + 2 * 'la-')
   :answer_c: print('tra-' + 'la-' + 'la')
   :answer_d: print('tra-' + 'la-la')
   :answer_e: print('tra-la-' + '-la')
   :correct: a, c, d

   Which statement prints `` tra-la-la ''? (Mark all correct answers)
       
.. dragndrop:: console__text_quiz_nanana
    :feedback: Try again!
    :match_1: 'NA' * 3 ||| 'NANANA'
    :match_2: 'N' + 3 * 'A' ||| 'NAAA'
    :match_3: 'N' * 3 + 'A' ||| 'NNNA'
    :match_4: 'N' * 3 + 3 * 'A' |||'NNNAAA'

    Match expressions with their values.

.. fillintheblank:: console__text_quiz_N_A

    What the statement **print(('N' + 'A') * 2)** prints?
    
    - :NANA: Correct!
      :NNAA: First, calculate the part in brackets (as with numbers)
      :.*: Try again.

.. questionnote::

    **Task - Profit Sharing**

    The three friends agreed to divide the profits from the joint venture so that the first would get 2/7 of the earnings, the second 1/3, and the third the remaining sum. The total profit was 40000. Complete the program, which will print, in two decimal places, the earnings of each of the three friends.
    
.. activecode:: console__computing_earnings

    total_earnings = 40000
    first = total_earnings * 2 / 7
    second = 0 # fix the staement
    third = total_earnings - first - second
    # add statement(s) for printing

