# -*- acsection: general-init -*-
import pygame as pg, pygamebg
(width, height) = (300, 300)
canvas = pygamebg.open_window(width, height, "Relative position")
x = width // 2
y = height // 2
a = 5
# -*- acsection: main -*-


def draw():
    canvas.fill(pg.Color("white"))
    pg.draw.circle(canvas, pg.Color("blue"), (x, y), 12*a)
    pg.draw.circle(canvas, pg.Color("yellow"), (x - 5*a, y - 5*a), 3*a)
    pg.draw.circle(canvas, pg.Color("black"), (x - 4*a, y - 4*a), a)
    pg.draw.circle(canvas, pg.Color("yellow"), (x + 5*a, y - 5*a), 3*a)
    pg.draw.circle(canvas, pg.Color("black"), (x + 4*a, y - 4*a), a)
    pg.draw.ellipse(canvas, pg.Color("red"), (x-5*a, y+2*a, 10*a, 2*a))

   
def handle_event(event):
    global x, y, a
    if event.type == pg.MOUSEMOTION:
            (x, y) = event.pos
            return True
    elif event.type == pg.MOUSEBUTTONDOWN:
        if event.button == 1:
            a += 1
            return True
        elif event.button == 3:
            a -= 1
            return True
    return False

should_redraw = True
kraj = False
while not(kraj):
    if should_redraw:
        draw()
        pg.display.update()  
        should_redraw = False

    event = pg.event.wait()
    if event.type == pg.QUIT:
        kraj = True
    else:
        should_redraw = handle_event(event)

# Completion of the hidden part of the program, that works as an example
pg.quit()
import sys 
sys.exit()

# Completion of user program is in the separate section

# -*- acsection: after-main -*-
pygamebg.wait_loop()
