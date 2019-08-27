Interaction
===========

In the PyGame programs we have seen so far, the user could not affect their execution, aside from ending the program. We can compare this kind of programs to watching movies - the user is essentially a viewer.

In the next section, we will deal with programs in which the user has an active role and can influence the running of the program using a mouse and a keyboard. There are two basic ways for our program to "know" when the user has made an action.

- One way is to **read the status** of the mouse and keyboard. From the code we can ask what is the current position of the mouse, whether any key is being pressed and the like.
- Another way is to use system **events.** Any user action (pressing a mouse button or a keyboard key, releasing a key, moving the mouse, etc.) is an event, and in the programs we can obtain information about such events and respond to them.

In this chapter, we will familiarize with both of these ways that enable our programs to respond to user actions.

   .. toctree::
      :maxdepth: 1

      ./03_PyGame_31_Interaction_ReadMousePos.rst
      ./03_PyGame_32_Interaction_ReadMouseKey.rst
      ./03_PyGame_33_Interaction_ReadKeyboard.rst
      ./03_PyGame_34_Interaction_Events.rst
      ./03_PyGame_35_Interaction_EventMouse.rst
      ./03_PyGame_36_Interaction_EventKeyboard.rst
