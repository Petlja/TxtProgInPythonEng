Defining functions
==================

In the part dedicated to managing Karel, we mentioned that we can separate a group of commands into a separate entity called a function. Let's recall what a function written in Python looks like:

.. activecode:: Console__functions__function_def
    :passivecode: true

    def function_name(argument_list):
        statement_1
        ...
        statement_k
        
The following rules apply to writing functions in Python:

.. infonote::

    **Function writing rules:**

    - The function definition begins with the word ``def``, followed by the function name, then a list of arguments in parentheses, and the ``:`` character (colon) at the end of the line.
    - Any properly written name may appear as a *function_name* (the rules are the same as for variable names).
    - An empty list (nothing) may appear as *argument_list* if the function does not use arguments, or one or more comma-separated arguments.
    - Any Python statements may appear in the function body (*statement_1*, ... *statement_k*). These commands are written indented with respect to the row containing the function name and arguments.

Functions may or may not return some value. So far we have had the opportunity to see both types of functions. For example, the functions by which Karel (the robot) moves forward, turns around, picks up and leaves balls are all functions that do not return any value. On the other hand, mathematical functions like *abs* or *round*, as well as functions to check if Karel has balls with him, whether there are any balls on the square, or whether Karel can go forward are functions that do return a value.

Writing functions that return value
-----------------------------------

In order for a function to return a value, it is necessary to specify the ``return`` statement at least once in the body of the function. The ``return`` statement consists of the word *return*, folowed by an expression whose value the function is to return. 

.. activecode:: console__functions_return_example

    def square(x):
        return x * x
    
    print(square(3))

The *return* statement can appear in multiple places in a function (usually with different values), and must be specified at the end of the function body. The *abs* function, if it had not been embedded, could have been defined as follows:

.. activecode:: console__functions_def_abs
    :passivecode: true

    def abs(x):
        if x > 0:
            return x
        else:
            return -x
    
A function can return more than one value. One such function is the built-in *divmod* function, which returns two numbers - the result of integer division and the reminder. We use the *divmod* function as we do with functions that return a single value, we only place the returned values in multiple variables:

.. activecode:: console__functions_divmod_example

    quotient, reminder = divmod(813, 10)
    print('The quotient is', quotient, 'and the remainder', reminder)
    

When we write functions that return multiple values, it is sufficient to specify comma-separated values after the word *return*. If we were to define the built-in *divmod* function ourselves, we could write it like this:

.. activecode:: console__functions_divmod_def
    :passivecode: true

    def divmod(a, b):
        return a // b, a % b

Example
'''''''

.. questionnote::

    **Example - painting:** 
    
    To paint :math:`1m^{2}` of walls requires about :math:`0.5kg` of paint. Write a function that accepts the following 4 arguments:
    
    - the length of the room
    - the width of the room
    - the height of the room
    - length that is not to be painted (total width of doors, windows, closets, etc.)

    The function should return the amount of paint (in kilograms) required to paint the walls and ceilings.
    
    After the function, write a program that loads the data for 5 different rooms, and then using the written function calculates and prints the total amount of paint needed to paint all five rooms.

.. activecode:: console__functions_paint2


    def paint_needed(a, b, h, not_to_paint):
        coverage = 0.5 # how many kilograms per square meter
        ceiling = a*b
        walls = h * (2*a + 2*b - not_to_paint)
        area_to_paint  = ceiling + walls
        return area_to_paint * coverage
        
    total_paint_needed = 0
    for i in range(5):
        s = input('Enter the length, width and height of the room, and the non-painting length').split()
        total_paint_needed += paint_needed(float(s[0]), float(s[1]), float(s[2]), float(s[3]))

    print("A total of", total_paint_needed, "kilograms of paint is required")  


Tasks for Exercise:
'''''''''''''''''''

.. questionnote::

    **Task - geographic coordinates in GPS format**

    You found an old map of the buried treasure and read the coordinates of the treasure in degrees, minutes and seconds. However, your GPS device only supports geographical coordinates in degrees as real numbers (floats).
    
    Write a program that for a given coordinate in degrees, minutes and seconds, prints a real number of degrees.

The program is almost completely written. An expression needs to be added to calculate the real number of degrees. To convert the (angular) minutes into degrees, we divide them by :math:`60`, and we convert the seconds into degrees by dividing by :math:`60 \cdot 60 = 3600`.

.. activecode:: console__functions_GPS_1

   degrees = int(input())
   minutes = int(input())
   seconds = int(input())
   
   def deg_min_sec_to_degrees(deg, min, sec):
        # complete the function
   
   float_degrees = deg_min_sec_to_degrees(degrees, minutes, seconds)
   print(float_degrees)



.. questionnote::

    **Task - Geographic coordinates in the format for the old map**
    
    After you realized that the old map from the previous assignment was a joke, you decided to make a similar joke to someone. You have selected a nearby location and read coordinates from your GPS device. Now you need to convert the coordinates from the device in real degrees into whole degrees, whole minutes and rounded seconds, to create a proper "old" map.
    
     Complete the started program that performs this conversion.

.. activecode:: console__functions_GPS_2

    def deg_min_sec(real_degrees):
        # complete the function by calculating three values that the function returns
        # (and then remove the comment from the following line of code)
        # return whole_degrees, whole_minutes, whole_seconds

    real_degrees = float(input())
    whole_deg, whole_min, whole_sec = deg_min_sec(real_degrees)
    print(whole_deg, whole_min, whole_sec)



.. questionnote::

    **Task - Plumber:** 
    
    Mike is a plumber and has three interventions planned for today. For each intervention, Mike will record when it began and when it ended. Based on that information it should be calculated how long Mike spent in the interventions.
    
    A partially written program is given that loads the start and end times in hours and minutes for each Mike's intervention, and then determines and prints the total duration of all interventions.
    
    **Complete the program** by writing the *duration(h1, m1, h2, m2)* function, which calculates how many total minutes elapsed from *h1* hours and *m1* minutes to *h2* hours and *m2* minutes.
    
.. activecode:: console__functions_plumber

    # write the duration function

    def process_one_intervention():
        prompt = "Enter the hour and minute of start and hour and minute of completion of the intervention "
        s1, s2, s3, s4 = input(prompt).split()
        h1, m1, h2, m2 = int(s1), int(s2), int(s3), int(s4)
        return duration(h1, m1, h2, m2)
        
    t1 = process_one_intervention()
    t2 = process_one_intervention()
    t3 = process_one_intervention()
    total_minutes = t1 + t2 + t3
    num_hours = total_minutes // 60
    num_minutes = total_minutes % 60
    print("The interventions lasted a total of", num_hours, "hours and", num_minutes, "minutes")


Functions that do not return value
----------------------------------

Functions that do not return value just do some work and we use them as commands. Such were, for example, the *back()* or *take_at_neighboring_square()* functions, which we wrote in a section dedicated to managing Karel. let's look at an example of such function in a program with a text interface.

.. questionnote::

    **Example - transportation:** 
    
    It takes 55, 35, 40 and 20 minutes respectively to members of a family of four to arrive home from where they are, provided that they start going home before 4 p.m. Otherwise they need 15 minutes more.
    
    Write a program that loads the departure time in hours and minutes for each family member and lists the time of arrival home.
    
The *process_family_member* function performs all the necessary actions for one family member: it loads the departure time, than based on departure time it extends the duration of the trip if necessary, then calculates and prints the time of arrival home. In the main program, this function is just called for each family member.

.. activecode:: console__functions_transport

    def process_family_member(which_one, travel_duration):
        prompt = 'Enter the hour and minute of departure of the ' + which_one + ' member'
        s_hour, s_min = input(prompt).split()
        departure_hour, departure_minute = int(s_hour), int(s_min)
        if departure_hour >= 16:
            travel_duration += 15
        arrival_total_minutes = departure_hour * 60 + departure_minute + travel_duration
        arrival_hour = arrival_total_minutes // 60
        arrival_minute = arrival_total_minutes % 60
        print('The', which_one, "member arrived home at", arrival_hour, "hours and", arrival_minute, "minutes.")
        
    process_family_member("first", 55)
    process_family_member("second", 35)
    process_family_member("third", 40)
    process_family_member("fourth", 20)


Tasks for Exercise:
'''''''''''''''''''

.. questionnote::

    **Task - discount:** 
    
    One manufacturer offers goods at a price of 10 euros a piece, and for orders of 50 or more pieces a 10% discount is granted. Several buyers announced that they were coming to buy a certain number of pieces. The customer names and quantities requested are given at the beginning of the program.
    
    Write a function which for the given name of the customer and the quantity of goods prints how much that customer should pay.

The customer name is passed to the function here for print purposes only. The price of goods is calculated on the basis of quantity, which is passed on to the function as a second argument.

.. activecode:: console__functions_discount

    # define the function print_price

    customers = ('Oliver', 'Freddie', 'Sophia', 'Lucas')
    quantities = (70, 28, 150, 6)
    n = len(customers)
    for i in range(n):
        print_price(customers[i], quantities[i])


.. questionnote::

    **Task - text underlining:**

    Write the *underline(text)* function, which shows the given text underlined.
    
**Hint:** The *underline* function should consist of only two *print* statements. The first statement should print the given text, and the second one should print the line. You can get a string containing a line by multiplying the string ``'-'`` by the length of the given string.

.. activecode:: console__functions_underlined_text

    # define the function 'underline'
    
    underline("From Celsius to Fahrenheit:")
    for c in range(15, 46, 5):
        print(c, '°C =', round(c * 9 / 5 + 32, 1), '°F.')
    print()
    
    underline("From Fahrenheit to Celsius:")
    for f in range(50, 111, 10):
        print(f, '°F =', round((f-32) * 5 / 9, 1), '°C.')

.. commented out

    def underline(text):
        print(text)
        print('-' * len(text))

~~~~

Finally, let's mention some of the benefits of writing functions that, because of the shortness of our examples and tasks, could not come to the fore:

- Functions in long programs are often used to decompose the main part of a program and make it shorter and easier to understand. Our programs are not so long that it would be necessary to decompose them, but they show how it could be done with longer programs.
- Functions can help us avoid repeating the same or similar code in programs. Repeating the code should be avoided as such code is harder to maintain - every change should be made in multiple places, which is tedious and subject to errors and omissions.
- When we write functions, we enable others to use parts of our code more easily. The functions we write can be extracted into a separate module, which other people can easily include in their programs.
- For very large programs, forming functions allows the program to be split into multiple files instead of one huge and incomprehensible file.

