Complex branching
=================

Successive conditions
---------------------

There are tasks in which, when one condition is not fulfilled, another one should be checked, and if that condition is not valid either then a third one is checked and so on. To avoid writting

.. activecode:: console__more_branching_elif1
    :passivecode: true
    
    if first_condition:
        statement1
    else:
        if second_condition:
            statement2
        else:
            if third_condition:
                statement3
            else:
                if fourth_condition:
                    statement4
                else:
                    statement5

in Python we use the special word ``elif``, which stands for *else:* and the indented *if* in the following line. So we get a more readable code:

.. activecode:: console__more_branching_elif2
    :passivecode: true
    
    if first_condition:
        statement1
    elif second_condition:
        statement2
    elif third_condition:
        statement3
    elif fourth_condition:
        statement4
    else:
        statement5

Note 1: Any number of consecutive *elif* statements can be used this way. 

Note 2: The part

.. activecode:: console__more_branching_elif3
    :passivecode: true

    else:
        statement5

is optional and can be omitted if not needed.


Examples and tasks
''''''''''''''''''

.. questionnote::
    
    **Example - body mass index:** 
    
    Body mass index (abbreviated bmi) is used for quick orientation regarding the degree of obesity or weight loss. The formula for calculating body mass index is :math:`bmi = {m \over {h \times h}}`, where *m* is the mass in kilograms and *h* is the height in meters. The *bmi* values are interpreted as follows:
    
    - up to 18.5: malnourished person
    - from 18.5 to 25: person of normal body weight
    - from 25 to 30: overweight
    - over 30: obese person
    
    Write a program that takes a person's weight and height and then writes to which category that person belongs (limit values belong to a lower category).

One possible solution is given below. Consider why it is not necessary to use complex logical conditions (built with words *and*, *or*, *not*) in this solution.

.. activecode:: console__more_branching_bmi

    m = float(input('Body mass: '))
    h = float(input('Body height: '))
    bmi = m / (h*h)
    if bmi <= 18.5:
        print('Malnourished.')
    elif bmi <= 25:
        print('Normal body weight.')
    elif bmi <= 30:
        print('Overweight.')
    else:
        print('Obese.')



.. questionnote::
    
    **Task - age categories of players:** 
    
    Young basketball players register at the beginning of the basketball season in one of the age categories, according to how many years they turn in the calendar year in which the season begins. The registration rules are as follows:
    
    - 10 and under - no category
    - 11 or 12 years - younger pioneers
    - 13 or 14 years old - pioneers
    - 15 or 16 - Cadets
    - 17 or 18 - juniors
    - 19 years and older - seniors
    
    Write a program that takes the age of a basketball player in the year they register and pritnts their age category.

.. activecode:: console__more_branching_categories

    g = int(input("How old is player: "))
    # finish the program


        
.. questionnote::
    
    **Task - ordinal number:** 
    
    Write a program that loads an integer from 1 to 6 (including borders) and prints the appropriate ordinal number in letters. For example, if number 6 is loaded, the "sixth" (without quotation marks) should be printed.
    
.. activecode:: console__more_branching_ordinal

    n = int(input("Enter a number from 1 to 6: "))
    # finish the program

Nested branching
----------------

Nested branches are *if* statements in the branches of other *if* statements. Nested *if* statements can be found in one or the other, or in both branches of a larger *if* statement. This way of setting *if* statements can go to any depth, but it should be borne in mind that that way programs can become difficult to understand exactly and hard to maintain.

In the first example, we intentionally provide a program with three levels of nesting *if* statements, to help you imagine what a program with even more deeply nested and longer *if* statements might look like. In other examples and tasks, we will limit ourselves to one level of inserting *if* statements.

Examples and tasks
''''''''''''''''''


.. questionnote::
    
    **Example - guess who**
    
    There are eight children in the neighborhood who are often together. Their names are: Alice, Ben, Charlotte, Daniel, Emily, Frankie, Gabriella and Harry. Alice, Ben, Charlotte and Daniel go to the programming section, and Alice, Ben, Emily and Frankie to the sports section. The school cook wanted to praise one of the children for some deed, but did not know the name of that child.
    
    Write a program that asks three questions, accepts the answers to those questions (the letter 'y' for yes, and every other answer for no) and prints out the name of the child in question. The questions the program asks are:

    - Is it a girl?
    - Does he or she go to the sports section?
    - Does he or she go to the programming section?
    
.. activecode:: console__more_branching_guess_who1

    girl = input("Is it a girl? ") == 'y'
    sportsperson = input("Does he or she go to the sports section? ") == 'y'
    programmer = input("Does he or she go to the programming section? ") == 'y'
    if programmer:
        if sportsperson:
            if girl:
                print("Alice")
            else:
                print("Ben")
        else:
            if girl:
                print("Charlotte")
            else:
                print("Daniel")
    else:
        if sportsperson:
            if girl:
                print("Emily")
            else:
                print("Frankie")
        else:
            if girl:
                print("Gabriella")
            else:
                print("Harry")

Note that programs with nested branches can be modified to use only consecutive conditions and form with *elif*, without inserting *if* statements in depth. In doing so, we use complex conditions, which we build using logical operations *and*, *or* and *not*.
   
.. activecode:: console__more_branching_guess_who2

    girl = input("Is it a girl? ") == 'y'
    sportsperson = input("Does he or she go to the sports section? ") == 'y'
    programmer = input("Does he or she go to the programming section? ") == 'y'
    if programmer and sportsperson and girl:
        print("Alice")
    elif programmer and sportsperson and not girl:
        print("Ben")
    elif programmer and not sportsperson and girl:
        print("Charlotte")
    elif programmer and not sportsperson and not girl:
        print("Daniel")
    elif not programmer and sportsperson and girl:
        print("Emily")
    elif not programmer and sportsperson and not girl:
        print("Frankie")
    elif not programmer and not sportsperson and girl:
        print("Gabriella")
    else:
        print("Harry")


.. questionnote::
    
    **Task - crossroads:** 
    
    There is an intersection of A and B streets. The even house numbers in Street A are on the right and odd ones are on the left. On the even (right) side, the numbers up to the intersection are from 2 to 200, and after the intersection are those greater than 200. On the odd (left) side, the numbers up to the intersection are from 1 to 177, and after the intersection they are those from 179 onwards.
    
    Write a program that loads one house number on street A and answers whether that number is before or after the intersection and which side of street A it is on. For example:
    
    - for number 128, print "on the right side, before the intersection"
    - for number 284 print "on the right side, after the intersection"
    - for number 177, enter "on the left side, before the intersection"
    - for number 219 write "on the left side, after the intersection"

**Hint:** After loading, you should first check if *n* is even, that is, if :math:`n \% 2 == 0`.

.. activecode:: console__more_branching_quart

    n = int(input("What is the house number: "))
    # finish the program




.. questionnote::
    
    **Task - studying:** 
    
    John's parents told John that if he received fours or fives in maths and English, he could go to an afternoon football tournament, otherwise he had to learn the subject or subjects from which he received grade(s) less than 4 (grades are from 1 to 5, 1 being the worst, 5 being the best).
    
    Write a program that first loads John's math grade and then English grade and prints a message for John. For example:
    
    - for grades 2, 3 print "learn math and English"
    - for grades 3, 4 print "learn math"
    - for grades 4, 2 print "learn English"
    - for grades 5, 4 print "go to the tournament"
    

.. activecode:: console__more_branching_grades

    math = int(input("What is the grade in math: "))
    english = int(input("What is the grade in English: "))
    # finish the program


.. questionnote::
    
    **Task - dressing up:** 
    
    Ian is writing a program that reads the current temperature (in degrees Celsius) and the chance of rain (from 0 to 100) from the weather website, and based on that information, it writes a recommendation whether to bring a jacket (which has a hood) or an umbrella, or none of these two. Ian chose this rule:

    - when the temperature is below 21, the advice should be: "wear the jacket"
    - when the temperature is 21 or higher and the chance of rain is over 50, the recommendation is: "bring an umbrella"
    - when the temperature is 21 or higher and the chance of rain is up to 50, the advice should be "you can go in a T-shirt"
    
    The task for you is to write a program that loads the temperature first, then the chance of rain, and then prints a recommendation.
    
.. activecode:: console__more_branching_weather

    t = int(input("What is the temperature: "))
    chance_of_rain = int(input("What are the chances of rain: "))
    # finish the program

