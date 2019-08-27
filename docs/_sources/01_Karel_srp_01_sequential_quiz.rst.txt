Управљање Карелом - питалице
::::::::::::::::::::::::::::

.. mchoice:: Karel_quiz_1
   :answer_a: (4, 2)
   :answer_b: (4, 4)
   :answer_c: (2, 4)
   :answer_d: Удариће претходно у зид.
   :correct: a
   :feedback_a: Тачно.
   :feedback_b: Покушај поново. Пази да не помешаш лево и десно.
   :feedback_c: Покушај поново. Пази да не помешаш координате (прво наведи x, а затим y).
   :feedback_d: Покушај поново.

   На ком пољу ће се налазити робот на слици када изврши следеће наредбе?

   .. image:: ../_images/Karel/karel_quiz_1.png
      :width: 300px
      :align: center
   
   .. activecode:: Karel_quiz_1_code
      :passivecode: true
   
      from karel import *
      napred()
      desno()
      napred()
      levo()
      napred()

.. mchoice:: Karel_quiz_2
   :answer_a: napred()
   :answer_b: levo()
   :answer_c: desno()
   :answer_d: Не треба ништа додати.
   :correct: c
   :feedback_a: Тачно.
   :feedback_b: Покушај поново.
   :feedback_c: Покушај поново.
   :feedback_d: Покушај поново.

   Ако робот треба да дође на поље (2, 1), као прву линију кода треба додати:

   .. image:: ../_images/Karel/karel_quiz_1.png
      :width: 300px
      :align: center
   
   .. activecode:: Karel_quiz_2_code
      :passivecode: true
   
      from karel import *
      ???
      napred()
      napred()

