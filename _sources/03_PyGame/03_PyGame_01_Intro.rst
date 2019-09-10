The PyGame library
==================

We assume that you are already acquainted with Python as a language, and that you know about expressions (constants, variables, operators), statements (``if``, ``if-else``, ``if-elif-else``, ``for``), functions (those built in, like ``min`` or ``abs``, and those you define yourself using ``def`` keyword), strings (``"Hello"`` or ``'Hello'``), lists (like ``[1, 2, 3]``), tuples (like ``(3, 4)``) and the like.

We will now continue to practice writing Python programs using the PyGame graphics library. We chose this library because it offers the ability to produce interesting results with relatively little programming, which include drawing, animating, and interacting with a user. Therefore, the goal of introducing the PyGame library is for you to continue practicing your programming skills in a fun way. Readers who become more interested in programming will get many opportunities to modify given programs and inspiration for a variety of their own projects.

About the PyGame library
------------------------

The `PyGame <http://pygame.org>`__ library has been developing since the early 2000s. The authors themselves said that this is not the best library for game programming (not even the second, nor the third by quality), but its main advantage is that it is simpler to use than the other libraries and it is suitable for learning programming through the interesting world of computer graphics and computer games.


Online use
----------

To help you get started, we have provided you with an environment where you can write and test simple PyGame programs in the workbook you are reading. We have also prepared a handful of examples and tasks in which, as in the previous chapters, you generally need to complete or modify started programs in order to get them to fully work. You do not need to install anything extra on your computer to use this environment. However, if you want to do some more serious programming (for example, you want to make your own game), we recommend that you install the library on your computer and use it from a Python development environment (such as IDLE), independent from the web browser and this workbook. Among other advantages, programming in an actual development environment is more comfortable and more efficient, easier to test, debug etc.

Installation
------------

In order to run programs written using PyGame in your application development environment, you must first install this library. A prerequisite, of course, is that you have Python installed on your computer (preferably version 3.6 or later). If you have not done so already, visit the site `<https://www.python.org>`__ and download the latest version of Python and its working environment (usually found in the Downloads section, subsection dedicated to the operating system you are using).

When Python is installed on your computer, we can go to the PyGame library installation. It's really very simple. Just type ``pip3 install pygame`` in the command prompt. The easiest way to start command prompt is by holding down the ``windows`` key and pressing the ``r`` key, and then typing ``cmd`` in the window that popped up. If you get the message that the command ``pip3`` does not exist, then try ``py -3 -m pip install pygame``. 

When you complete the installation, it is best to immediately test that everything went well by:

* running IDLE Python development environment, which is installed as a windows application

* opening a new project in the IDLE development environment (option File/New)

* typing the program shown below in the editor (you can just copy it and paste it in the IDLE editor)

* saving the program to a file before running it (option File/Save as...)

* running the program (option Run/Run Module in the menu, or the F5 key)


After running the program, a window should appear in which a square is drawn and displayed for three seconds.

.. activecode:: PyGame__check_install
   :nocodelens:
   :modaloutput: 
   :enablecopy:

   import pygame
   pygame.init()
   prozor = pygame.display.set_mode((200, 200))
   prozor.fill(pygame.Color("white"))
   pygame.draw.rect(prozor, pygame.Color("black"), (20, 20, 160, 160), 5)
   pygame.display.update()
   pygame.time.wait(3000)
   pygame.quit()

You can also run other examples from this guide on your computer, which we recommend you to do at least sometimes.

