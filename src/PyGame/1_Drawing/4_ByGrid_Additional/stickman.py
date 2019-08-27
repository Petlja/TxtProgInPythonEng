# -*- acsection: general-init -*-
import pygame as pg, pygamebg
canvas = pygamebg.open_window(300, 300, "Stickman")

# -*- acsection: main -*-
canvas.fill(pg.Color("white")) # paint background

pg.draw.circle(canvas, pg.Color("black"), (150, 70), 20, 2)      # head

pg.draw.line(canvas, pg.Color("blue"), (120, 50), (180,50), 3)   # hat brim
pg.draw.rect(canvas, pg.Color("blue"), (130, 10, 40, 40))        # hat

pg.draw.circle(canvas, pg.Color("black"), (145, 60), 2, 2)       # left eye
pg.draw.circle(canvas, pg.Color("black"), (155, 60), 2, 2)       # right eye

pg.draw.ellipse(canvas, pg.Color("red"), (145, 70, 10, 7))       # mouth

pg.draw.line(canvas, pg.Color("black"), (150, 90), (150,170), 3) # body

pg.draw.line(canvas, pg.Color("black"), (150, 110), (100, 120), 3) # left arm
pg.draw.line(canvas, pg.Color("black"), (100, 120), (80, 100), 3)

pg.draw.line(canvas, pg.Color("black"), (150, 110), (200, 150), 3) # right arm
pg.draw.line(canvas, pg.Color("black"), (200, 150), (210, 170), 3)

pg.draw.line(canvas, pg.Color("black"), (150, 170), (130, 200), 3) # left leg
pg.draw.line(canvas, pg.Color("black"), (130, 200), (140, 250), 3)

pg.draw.line(canvas, pg.Color("black"), (150, 170), (170, 200), 3) # right leg
pg.draw.line(canvas, pg.Color("black"), (170, 200), (160, 250), 3)

# -*- acsection: after-main -*-
pygamebg.wait_loop()
