Dictionaries
============

Now we are going to introduce a new type of structured data, i.e. collection, which is quite different from the ones we have met so far.

Suppose we need to write a program that answers questions about an individual's age. The names and ages of the persons are known to us, for example Mary is 14 years old, Michael 15, Daniel also 15, and Matilda 16 (actual data would be more extensive, but this is just an illustration).

We can solve this problem by placing the names in one tuple and the ages in the other. Having these two tuples, we can use a loop to search for a given name in the name's tuple, and when we find it, we use the same index to access and print the appropriate age.

.. activecode:: dict__two_tuples

    name = ('Mary', 'Michael', 'Daniel', 'Matilda')
    age = (14, 15, 15, 16)
    asked_name = input('Please enter a name: ')
    name_has_been_found = False
    for i in range(len(name)):
        if asked_name == name[i]:
            print(asked_name, 'is', age[i], 'years old.')
            name_has_been_found = True
            break
    
    if not name_has_been_found:
        print('Name', asked_name, 'has not been found.')

As we can see, the collections we already know can serve us in this case as well. However, for this type of task, there is a collection in which data is recorded in a more coherent way, and the necessary data is found easier and more efficiently. Let's look at another solution:

.. activecode:: dict__1st_example

    age = {'Mary':14, 'Michael':15, 'Daniel':15, 'Matilda':16}
    asked_name = input('Please enter a name: ')
    if asked_name in age:
        print(asked_name, 'is', age[asked_name], 'years old.')
    else:
        print('Name', asked_name, 'has not been found.')

A collection of the form {'Mary':14, 'Michael':15, 'Daniel':15, 'Matilda':16} is called a **dictionary**. We can see that a dictionary can be set up similarly to a tuple and a list - by listing comma-separated elements. Dictionary elements are written between the curly brackets ``{}``. Each element consists of two parts, between which there is a colon ``:``. The first part of the element is called the **key** and the second is the **value**. For example, for the key 'Mary' the corresponding value is 14, etc.

We use dictionaries to quickly and easily obtain value for a given key. In our example, we found the age for a given name in the dictionary. In tuples and lists, we similarly retrieve the element's value by the sequence number (index) of that element. We can say that the key in the dictionary plays the role that the index plays in the tuples and lists. The essential difference between dictionaries on the one hand, and tuples and lists on the other, is that in the dictionary the key can be of any immutable type (integer, real number, string, tuple ...) while in the tuple or list the indices have to be integers starting from 0.

Building a dictionary
---------------------

We can also build a dictionary by computing. We do this by inserting new key-value pairs into the dictionary and then changing the value for a given key as needed.

In the following example, the starting tuple contains the names of the football clubs that won the European Champions Cup (or the UEFA Champions League) from 1956-2019. Based on this information we will form a dictionary in which we will keep the number of championships won for each club. Here's how we can do it.

.. activecode:: dict__counting

    champions = (
        'Real Madrid',       'Real Madrid',       'Real Madrid',       'Real Madrid',
        'Real Madrid',       'Benfica',           'Benfica',           'Milan',
        'Internazionale',    'Internazionale',    'Real Madrid',       'Celtic',
        'Manchester United', 'Milan',             'Feyenoord',         'Ajax',
        'Ajax',              'Ajax',              'Bayern Munich',     'Bayern Munich',
        'Bayern Munich',     'Liverpool',         'Liverpool',         'Nottingham Forest',
        'Nottingham Forest', 'Liverpool',         'Aston Villa',       'Hamburg',
        'Liverpool',         'Juventus',          'Steaua București',  'Porto',
        'PSV Eindhoven',     'Milan',             'Milan',             'Red Star Belgrade',
        'Barcelona',         'Marseille',         'Milan',             'Ajax',
        'Juventus',          'Borussia Dortmund', 'Real Madrid',       'Manchester United',
        'Real Madrid',       'Bayern Munich',     'Real Madrid',       'Milan',
        'Porto',             'Liverpool',         'Barcelona',         'Milan',
        'Manchester United', 'Barcelona',         'Internazionale',    'Barcelona',
        'Chelsea',           'Bayern Munich',     'Real Madrid',       'Barcelona',
        'Real Madrid',       'Real Madrid',       'Real Madrid',       'Liverpool'
    )
    num_titles = {} # empty dictionary
    for club in champions:
        if club in num_titles:
            num_titles[club] += 1
        else:
            num_titles[club] = 1
    
    print('club     number of titles')
    print('-' * 25)    
    for club in num_titles:
        s_num_titles = str(num_titles[club])
        space = ' ' * (25 - len(club) - len(s_num_titles))
        print(club + space + s_num_titles)

At the beginning we form an empty dictionary *num_titles*. For each club in the list of champions, we first check if the club already exists in the *num_titles* dictionary. If so, we add one to the club's title count, and if it doesn't, add the club to the dictionary with one title won.

At the end of the count, we go through the dictionary using a loop and print the keys and values from that dictionary.


One way to shorten this program is to use the function (method) ``get``, which is part of each dictionary and is called with *dictionary_name.get(key, default_value)*. As we can see, this function has two arguments. First argument is the key for which we need the value. In case that key exists in the dictionary, the *get* function returns the value corresponding to that key, and if the key is not in the dictionary, the function returns the value of its second argument. So for example, instead

.. code::

    if club in num_titles:
        num_titles[club] += 1
    else:
        num_titles[club] = 1

we can write

.. code::

    num_titles[club] = num_titles.get(club, 0) + 1
    
and the effect is the same. In this example, *num_titles.get(club, 0)* returns the number of titles of a given club if that club is already in the dictionary, or 0 if it is not yet in the dictionary. In either case, 1 should be added to that value and stored in the dictionary as the new number of titles for that club.

Tasks for exercise
''''''''''''''''''

.. questionnote::

    **Task - grocery prices**
    
    Prices in one store are:
    
    - Bread: 1 (per loaf - half kilogram)
    - Milk: 0.8 (per liter)
    - Egg: 0.08 (per piece)
    - Chicken breast: 7.3 (per kilogram)
    - Apples: 2.2 (per kilogram)
    - Tomatoes: 1 (per kilogram)

    Put this information in a dictionary and then complete the program by loading the name of a food and displaying the price of that food, or information that it is not available.
    
.. activecode:: console__dict__prices
    

.. questionnote::

    **Task - absence**
    
    The names of the students who were absent from the class were given in a tuple. Each appearance of one name represents absence from one class. Complete the program so that it calculates and prints out how many classes each student has missed.
    
    To help you check your program, here is the expected result: for the data given in the tuple *absent*, you should get that James has 4 absences, Maya 3, Alexander 2, and Violet, Mark, Frankie, Peter, Ronnie and Oliver one absence each (not necessarily in that order).
    
.. activecode:: console__dict__absence
    
    absent = (
        'Maya', 'James', 'Violet', 'Alexander', 'James', 
        'Mark', 'Maya', 'Frankie', 'James', 'Peter',
        'Ronnie', 'Oliver', 'Maya', 'Alexander', 'James')
        
.. commented out

    absences = {}
    for name in absent:
        absences[name] = absences.get(name, 0) + 1
    for name in absences:
        print(name, absences[name])        

.. questionnote::

    **Task - stock status**
    
    Purchases and sales of goods in the form of tuple of pairs are given. In each pair, the first element is the name of the goods, and the second is the change in stock status. For example, a pair *('cheese', -1.5)* means that the available quantity of cheese has decreased by 1.5 (so much cheese has been sold).
     
    Complete the program that calculates and prints the state after these changes, based on the given state changes. Assume that there are no stocks at the beginning.
    
    Check the result: for the data given, you should get (in any order)
    
    - cheese 18.5
    - milk 297
    - flour 985
    - eggs 1988
    - fish 47
     
In this task, the most important part of the program is traversing through all the pairs. For clarity, we immediately unpack each pair from the tuple *changes* to variables *good*, *change*.

.. activecode:: console__dict__stock_status
    
        changes = (
            ('cheese', 20), ('milk', 300), ('cheese', -1.5), ('flour', 1000),
            ('eggs', 2000), ('milk', -2), ('flour', -5), ('fish', 50),
            ('eggs', -12), ('milk', -1), ('flour', -10), ('fish', -3)
        )
        
        status = {}
        for good, change in changes:
            # complete
            
        for good in status:
            print(good, status[good])
