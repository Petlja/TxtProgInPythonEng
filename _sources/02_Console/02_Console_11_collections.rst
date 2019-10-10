Data collections
================

In the previous lesson, we used a tuple to perform some commands (computing and printing) over each value from the tuple using the *for* loop.

Tuples are also a type of data in Python, such as numbers, strings, or logical values. The types *int* (integer), *float* (real number), *str* (string) and *bool* (logical value) are **basic types**. The difference between tuples and basic types is that the value of a tuple consists of multiple values of a simpler type.

Each value that consists of multiple values of a simpler type will be called a **collection**. The data the collection consists of are called **collection elements**.

The only collections we have seen so far are tuples, which we will now get to know in more detail. We will see some more types of collections very soon.


Tuple and its elements
----------------------

Packing and unpacking tuples
''''''''''''''''''''''''''''

We can fit the whole tuple into a variable, as we do with values of a simpler type. In the following example, the *temperatures* variable contains the entire tuple as its value.

.. activecode:: console__collections_tuple1
    
    temperatures = (25, 24, 25, 23, 25, 25)
    for t in temperatures:
        print(t)
        
This kind of value assignment (as in the first line of the program) is known as tuple packing. The reverse assignment is also possible: when we know how many elements are there in a tuple, we can assign the tuple elements to the corresponding number of variables:

.. activecode:: console__collections_tuple2
    
    full_name = ("Arthur", "Conan", "Doyle")  
    first_name, middle_name, last_name = full_name
    print(first_name)
    print(middle_name)
    print(last_name)
    
Statements like ``first_name, middle_name, last_name = full name`` are called tuple unpacking.


The same effect is achieved by a related statement

.. code::
    
    first_name, middle_name, last_name = "Arthur", "Conan", "Doyle"
    
Tuples do not appear in this statement, which is called multiple value assignment.

Tuple elements and indices
''''''''''''''''''''''''''

We can also get the elements of a tuple by writing the name of the tuple, and behind it in square brackets the sequence number of the element we want. It should be noted here that counting the elements of any collection starts from zero. For example:

.. activecode:: console__collections_index

    basic_colors = ("Red", "Green", "Blue")
    print(basic_colors[0])
    print(basic_colors[1])
    print(basic_colors[2])

The sequence number of an element is also called the **index** of the element. if the tuple has *n* elements, we can use the numbers 0, 1, 2, ... *n-1* as indices. In the example above, *n* = 3, so indices 0, 1, and 2 are allowed. Trying to use an index outside these bounds causes an error (try it).

Tuple length
''''''''''''

The number of elements of a tuple can be obtained by using the *len* function.

.. activecode:: console__collections_len1
    
    basic_colors = ("Red", "Green", "Blue")
    n = len(basic_colors)
    print(n)
    
or shorter:

.. activecode:: console__collections_len2
    
    print(len(("Red", "Green", "Blue")))
    
Note the double brackets (one for function and the other for tuple).

Through these examples we have seen that tuple elements can be numbers or strings. In fact, the tuple elements can be of any type, basic or complex.

For example, it is possible to create a tuple of tuples:

.. activecode:: console__collections_len3
    
    t = ((11, 12, 13), (21, 22, 23))
    print(len(t))


.. commented out

    t2 = ((1, 2, 3), ) # last comma matters
    print(len(t2))
    
Tuple *t* contains two simpler tuples, therefore the number of its elements is 2.

In Python, the elements of a tuple can be of different types, and we will see such examples latter.


Range
-----

Range is another type of collection. Unlike tuple, the elements of this collection are always integers.

Range can be defined in several ways.


Range with one argument
'''''''''''''''''''''''

The simplest form of specifying a range is *range(n)*, where *n* is a positive integer. The *range(n)* range contains integers from 0 to *n*, not including *n*. For example, *range(5)* contains values 0, 1, 2, 3, 4.

.. activecode:: console__collections_range_n_i
    
    for i in range(5):
        print(i)
        
We see that in the *for* statement, we can use range in the same way as the tuple. In fact, any collection may be in place of the tuple or range.

Since the *range(n)* range contains a total of *n* values, this range is often used when a command only needs to be repeated *n* times in the same way:

.. activecode:: console__collections_range_n
    
    for i in range(5):
        print("Hello!")

The *print* function was executed for each value *i* of sequence 0, 1, 2, 3, 4, but in this example, those values are not used in the loop body. Thus, we achieved that the *print* function was executed 5 times in exactly the same way, that is, it was repeated 5 times.

Another common use of this type of range is to get through all the elements of a tuple. In such case, the loop variable serves as an index. This way of going through the values of the tuple is suitable when besides these tuple values in the loop we also need their sequence numbers (this way of going through the collection is more common in other programming languages than Python).


.. activecode:: console__collections_for_range_len
    
    colors = ["Red", "Green", "Blue", "Yellow", "Magenta"]
    n = len(colors)
    for i in range(n):
        print('Color #', i, 'is', colors[i])
    

Range with two arguments
''''''''''''''''''''''''

When we need a sequence of consecutive integers that does not start at zero, we set the range as *range(a, b)*, where *a* and *b* are integers such that :math:`a<b`. Then the sequence is made up of integers from *a* to *b*, not including *b*. For example, the range *range(1, 6)* gives the sequence of numbers 1, 2, 3, 4, 5:

.. activecode:: console__collections_range_a_b
    
    for i in range(1, 6):
        print(i)

Range with three arguments
''''''''''''''''''''''''''

The third form of specifying a range has three arguments:

.. activecode:: console__collections_range_a_b_c
    
    for i in range(2, 12, 2):
        print(i)

The range values given by *range(a, b, c)* go from *a* to *b* (not including *b*) with the step *c*, i.e. values change by *c*. Step *c* can also be negative:

.. activecode:: console__collections_range_a_b_cneg
    
    for i in range(12, 2, -2):
        print(i)


We can convert a range into a tuple (the opposite is not possible, nor is it ever needed):

.. activecode:: console__collections_range_to_tuple
    
    a = tuple(range(2, 12, 2))
    print(len(a))

String as a collection
----------------------

We have used strings as the basic type so far, but strings can also be used as collections of individual characters. We can traverse string characters using a loop and retrieve individual characters using indices:


.. activecode:: console__collections_str_as_collection
    
    s = 'text'
    print(s[1], s[2])
    for c in s:
        print(c)

Functions on collections
------------------------

There are many functions in Python that accept a collection as an argument. One of them is the *len* function, which we have already met. Some other commonly used functions that apply to collections are:

- *min*, a function that gives the smallest element of a collection
- *max*, a function that gives the largest element of a collection
- *sum*, a function that gives the sum of the elements of a collection

.. activecode:: console__collections_aggregation
    
    print('Tuple:')
    t = (2, 8, 4, 15, 3)
    print('len(t) =', len(t))
    print('min(t) =', min(t))
    print('max(t) =', max(t))
    print('sum(t) =', sum(t))

    print('Range:')
    r = range(1, 10, 2)
    print('len(r) =', len(r))
    print('min(r) =', min(r))
    print('max(r) =', max(r))
    print('sum(r) =', sum(r))

    print('String:')
    s = 'Python'
    print('len(s) =', len(s))
    print('min(s) =', min(s))
    print('max(s) =', max(s))
    # elements of s are not numbers, so uncommenting the next statement would cause an error
    # print('sum(s) =', sum(s)) 

The values of the functions *len*, *sum*, *min*, *max* for the range can also be determined from the parameters of the range. Also, *min* and *max* are not commonly applied to a string (they return character with smallest and biggest code respectively). Here, we are just pointing out that all these functions accept various kinds of collections as their argument (including range and string).

Questions
'''''''''

.. mchoice:: console__collections_quiz_tuple_unpack
   :answer_a: a program error occurs
   :answer_b: 2
   :answer_c: 20
   :answer_d: 3
   :feedback_a: Try again
   :correct: c
   :feedback_b: Try again
   :feedback_c: Correct
   :feedback_d: Try again

   What does the following program print?
   
   .. code::
   
       t = (32, 41, 20, 17)
       a, b, c, d = t
       print(c)

.. mchoice:: console__collections_quiz_tuple_index
   :answer_a: 1
   :answer_b: 2
   :answer_c: a program error occurs
   :answer_d: 3
   :correct: b
   :feedback_a: Try again
   :feedback_b: Correct
   :feedback_c: Try again
   :feedback_d: Try again

   What does the following program print?
   
   .. code::
   
       a = (1, 2, 3)
       print(a[1])


.. mchoice:: console__collections_quiz_range1
   :answer_a: range(4)
   :answer_b: range(1, 4)
   :answer_c: range(3)
   :answer_d: range(1, 3)
   :correct: b
   :feedback_a: Try again
   :feedback_b: Correct
   :feedback_c: Try again
   :feedback_d: Try again

   Which range contains just values 1, 2, 3?

.. mchoice:: console__collections_quiz_range2
   :answer_a: 5
   :answer_b: 6
   :answer_c: 9
   :answer_d: 10
   :correct: a
   :feedback_a: Correct
   :feedback_b: Try again
   :feedback_c: Try again
   :feedback_d: Try again

   How many values does range(1, 10, 2) contain?

.. dragndrop:: console__collections_quiz_range_len
    :feedback: Try again!
    :match_1: 5|||range(5)
    :match_2: 0|||range(3, 3)
    :match_3: 3|||range(1, 4)
    :match_4: 1|||range(3, 6, 3)

    Pair ranges with the number of elements.


.. dragndrop:: console__collections_quiz_range_values
    :feedback: Try again!
    :match_1: 3, 4, 5|||range(3, 6)
    :match_2: 0, 1, 2|||range(3)
    :match_3: 3, 1|||range(3, -1, -2)
    :match_4: 3, 2, 1, 0, -1|||range(3, -2, -1)
    :match_5: 3|||range(3, 6, 3)

    Pair ranges with values.
