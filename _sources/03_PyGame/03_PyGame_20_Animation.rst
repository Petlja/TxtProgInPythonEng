Animation
=========

It is known that videos consist of a large number of images, which are displayed fast enough one after the other, with successive images differing only slightly. Creating videos in this way is essentially possible because a person (human being), at a sufficiently high speed of rendering images, is not able to see individual images, but rather they blend together and create an impression of movement.

Creating a motion impression with still images is called animation. For example, from the following eight pictures of a character in different positions:

.. image:: ../../_images/PyGame/pganim_running1.png
   :width: 120px
.. image:: ../../_images/PyGame/pganim_running2.png
   :width: 120px
.. image:: ../../_images/PyGame/pganim_running3.png
   :width: 120px
.. image:: ../../_images/PyGame/pganim_running4.png
   :width: 120px
.. image:: ../../_images/PyGame/pganim_running5.png
   :width: 120px
.. image:: ../../_images/PyGame/pganim_running6.png
   :width: 120px
.. image:: ../../_images/PyGame/pganim_running7.png
   :width: 120px
.. image:: ../../_images/PyGame/pganim_running8.png
   :width: 120px


the following animation of running is created:
           
.. image:: ../../_images/PyGame/pganim_running.gif
   :width: 120px
           
Each of the images that appear in an animation is called a *frame*. The programs we have been working on so far were drawing only one drawing (frame) and the image was not changed after that. In programs that use animation one image must be drawn for each frame. In the following lessons we will see how we can do that.

   .. toctree::
      :maxdepth: 1

      ./03_PyGame_21_Animation_Basics.rst
      ./03_PyGame_22_Animation_Motion.rst
      ./03_PyGame_23_Animation_Stages.rst
      ./03_PyGame_24_Animation_Text.rst
      ./03_PyGame_25_Animation_Multiple.rst
