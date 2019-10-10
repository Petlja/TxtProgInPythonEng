Python programs
===============

As we saw in the chapter on Karel, programs consist of stetments. Let's look at some of the basic Python stetments we will use to write the first programs.

Assigning a value to a variable
-------------------------------

Variable is a named space in the memory of a computer, in which we can store values of any kind (number, text, logical value, or something else). Intermediate results are often placed in variables when calculating. When we run a Python shell, we can assign a value to a variable with one command, and then use the value of that variable in the following commands. For example:

.. code::

    >>> base = 6*8
    >>> base
    48
    >>> base * 1.5
    72.0
    >>> base * 1.6
    76.80000000000001

.. infonote::

    **Value assignment statement**

    The value assignment statement is written by writing the name of a variable, followed by the equals sign ``=``, and then the expression whose value we assign to the variable. We also consider integers and real numbers to be expressions (these are the simplest possible expressions).
    
.. infonote::

    **Names of variables**
    
    Variable names (as well as other names in programs we write) can consist of uppercase and lowercase letters, digits and underscore, but they cannot begin with a digit.
    
    Python distinguishes between uppercase and lowercase letters. *N* and *n* are different names and if we use them both, they would represent two different variables.
    
    The variable name can be as long as we need it.
    
    When writing programs (or individual statements), we try to give the variables meaningful names so that the commands and programs are as clear as possible.

In Python, it is a common style that capital letters are not used (though allowed), and when a name is made up of more than one word, those words are separated by an uderscore, for example, *price_of_one_piece*. Numbers are used in names when it makes sense (which is not often).

**Variable names - check your understanding:**

.. dragndrop:: console__basics_quiz_variable_names
    :feedback: Try again!
    :match_1: 2_date ||| incorrect, starts with an illegal character
    :match_2: pet_no_2 ||| correct name
    :match_3: state_at_23:59 ||| incorrect, contains an illegal character

    Match the proposed variable names with the answers.


.. mchoice:: console__basics_quiz_name
   :multiple_answers:
   :answer_a: vArIaBlE
   :answer_b: а1
   :answer_c: 2D_graphics
   :answer_d: _3D_graphics
   :answer_e: pet-no-2
   :correct: a, b, d

   Which of these can be the name of a variable?


Print values from a program
---------------------------

In interactive work, it is enough to enter an expression to see its value, but we cannot use that in programs. To print something from a program, we use the *print()* function. For now, we will use only the simplest form of this function.

The expression whose value we want to print is put between brackets, for example:

.. code::

    >>> print(2 + 2)
    4
    >>> 

With a single call of function *print()* we can print multiple values. Expressions whose values we want to print are listed between brackets and separated by commas, for example:

.. code::

    >>> a = 10
    >>> b = 20
    >>> circumference  = 2*a + 2*b
    >>> area = a*b
    >>> print(circumference, area)
    60 200
    >>> 


.. infonote::

    We have already encountered the functions in the chapters on Karel, we recognize them by the parentheses behind the name. Recall, we call the data that we specify between parentheses **parameters** or **arguments**. We'll talk more about functions soon.
    

Starting a program
------------------

**Running programs in browser**

To help you get started, we used the **ActiveCode** component of the `Runestone Interactive <http://runestoneinteractive.org/>`__ project and enabled you to run Python programs in the web pages of this course. For example, below are the statements we previously entered interactively, but this time written as a program. You can start the program by clicking the "Run" button.

.. activecode:: console__program_first

    a = 10
    b = 20
    circumference  = 2*a + 2*b
    area = a*b
    print(circumference, area)
    
**Running programs from the IDLE environment**

It is recommended that you, in addition to writing programs on these web pages, run programs at least occasionally in the *IDLE* environment. Getting used to the *IDLE* environment is important for you to become more independent in programming.

When you run *IDLE* on your computer, open the integrated text editor (File / New File menu) and type in the previous (or any other) program.

When you finish the program, save it (menu File / Save) and then run it (menu Run / Run Module).

.. image:: ../../_images/Console/console_run_from_idle.png
  :width: 350px
  :align: center

You will see the result in the interactive shell window.


**Running programs from an online environment**

Another way to run your Python program is to use one of the online programming environments. One such environment is https://repl.it/.

.. image:: ../../_images/Console/console_repl.it_start.png
  :width: 500px
  :align: center

Click on the ``+ new repl`` button, select the Python language and click ``Create repl``. Your web browser will open a page where you can type a program and run it.

.. image:: ../../_images/Console/console_repl.it_run.png
  :width: 500px
  :align: center


Program errors
--------------

Sometimes, you may not type a statement in the program exactly as required by the Python rules. In such case, the Python interpreter cannot understand the statement and you receive an error message. Each runtime environment reports an error in a slightly different way, but each of them tells in which line of the program the error occurred and what type of error it is.

The occurrence of errors (also known as bugs) should not worry you as it is a common thing and happens to experienced developers as well. Look at the message carefully, make sure you understand what is wrong, then correct it and run the program again. Understanding error messages is an integral part of programming and can be practiced like many other skills.

To help you understand the error messages you will be getting (and to become less anxious about errors), we recommend that you now try to deliberately make some small mistakes that might anyway happen to you when writing a program.

When you make a few intentional errors, you will gain some experience how error messages look like and it will be easier for you to understand the same messages latter, when they occur unintentionally. 

You can try some errors here:

.. activecode:: console__program_make_err

    # add statement(s)
    

We have also prepared a few programs with intentionally made mistakes, which we then explain. Programs are short to make errors more noticeable, but in longer programs, debugging is almost the same. Since the error message contains the program line number in which the error occured, in longer programs you just need to first find the program line mentioned and look at that (and possibly the previous) line.

Run each of the following programs, then see the error message and explanation.

.. activecode:: console__program_err1

    prit(2+2)
    
The message says that it is an error of type *NameError*. This means that some of the names in the specified line are unknown to the Python interpreter (name is not defined). Note that the name of the *print* function is not spelled correctly (and the function *prit* does not exist). By inserting the letter *n* the error is corrected and the program works.

.. activecode:: console__program_err2

    result = 2 + 2
    print(resultt)
    
The error is of the same type, only this time it refers to the name *resultt*. By removing the superfluous letter *t*, the program becomes correct.

.. activecode:: console__program_err3

    a = 3
    b = 2
    print(a b)
    
The error is of type *SyntaxError*, which means that Python statement construction rules are not followed. In this case, a comma between *a* and *b* is missing.

.. activecode:: console__program_err4

    a = 3
    b = 2
    print a, b

Another syntax error. Again, the rules of statement construction were not followed, and this time the brackets are missing.

.. activecode:: console__program_err5

    a = 3
    b = 0
    print(a / b)

The error is of type *ZeroDivisionError*. This error is different from the previous ones, because the statement was written correctly and was successfully interpreted. However, the execution of this command resulted in zero division, which is not a permitted operation. The program should be written in such a way that it does not attempt a zero division. The correction in this case depends on what we want our program to do in this situation. One possibility is to check that the divisor is not zero before dividing.

~~~~

Make sure you understand these three types of error by answering the question.

.. dragndrop:: console__program_quiz_errors
    :feedback: Try again!
    :match_1: SyntaxError|||print(3*(2+2)
    :match_2: NameError|||а=3</br>print(a / b)
    :match_3: ZeroDivisionError|||b=3//6</br>print(3 // b)

    Match the error type with the program.
