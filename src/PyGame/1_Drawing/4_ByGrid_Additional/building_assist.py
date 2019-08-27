# -*- acsection: general-init -*-
import pygame as pg, pygamebg
canvas = pygamebg.open_window(300, 300, "Building")

# -*- acsection: main -*-
(width, height) = (300, 300)
def draw():
    canvas.blit(user_canvas, (0, 0))  # attach users drawing
    
    # axes
    pg.draw.line(canvas, pg.Color("black"), (mouse_x, 0), (mouse_x, height), 1) # vertical mouse line
    pg.draw.line(canvas, pg.Color("black"), (0, mouse_y), (width, mouse_y), 1) # horizontal mouse line

    # write coordinates
    str_x, str_y = str(mouse_x), str(mouse_y)
    xt_y, yt_y = (5, mouse_y - 25) if 2 * mouse_y > height else (height - 25, mouse_y + 5)
    xt_x, yt_x = (mouse_x - 50, 5) if 2 * mouse_x > width else (mouse_x + 5, width - 50)
    im_x = font.render(str_x, True, pg.Color("black"))
    im_y = font.render(str_y, True, pg.Color("black"))
    if mouse_x <= 150:
        canvas.blit(im_x, (xt_x, xt_y))
    if mouse_y <= 60 or mouse_y >= 135:
        canvas.blit(im_y, (yt_x, yt_y))

def handle_event(event):
    global mouse_x, mouse_y
    if event.type == pg.MOUSEMOTION:    # the mouse is moved
        mouse_x, mouse_y = event.pos
        return True                     # re-plot the scene
    return False                        # no need to re-plot the scene

################# drawing
user_canvas = pg.Surface((width, height)) # the canvas on which user image is drawn
user_canvas.fill(pg.Color("lightgray")) # paint background

pg.draw.rect(user_canvas, pg.Color("darkgray"), (120, 50, 60, 140))   # building
pg.draw.rect(user_canvas, pg.Color("yellow"), (130, 60, 15, 15))      # left window, first row
pg.draw.rect(user_canvas, pg.Color("yellow"), (155, 60, 15, 15))      # right window, first row
pg.draw.rect(user_canvas, pg.Color("yellow"), (130, 80, 15, 15))      # left window, second row
pg.draw.rect(user_canvas, pg.Color("black"),  (155, 80, 15, 15))      # right window, second row
pg.draw.rect(user_canvas, pg.Color("black"),  (130, 100, 15, 15))     # left window, third row
pg.draw.rect(user_canvas, pg.Color("yellow"), (155, 100, 15, 15))     # right window, third row
pg.draw.rect(user_canvas, pg.Color("yellow"), (130, 120, 15, 15))     # left window, fourth row
pg.draw.rect(user_canvas, pg.Color("yellow"), (155, 120, 15, 15))     # right window, fourth row
pg.draw.rect(user_canvas, pg.Color("black"),  (130, 140, 15, 15))     # left window, fifth row
pg.draw.rect(user_canvas, pg.Color("black"),  (155, 140, 15, 15))     # right window, fifth row
pg.draw.rect(user_canvas, pg.Color("black"),  (140, 160, 20, 30))     # door
#################

font = pg.font.SysFont("Arial", 20)
font.set_bold(True)
mouse_x, mouse_y = 0, 0

should_redraw = True
done = False

while not done:
    if should_redraw:
        draw()
        pg.display.update()
        should_redraw = False

    event = pg.event.wait()
    if event.type == pg.QUIT:
        done = True
    else:
        should_redraw = handle_event(event)

# Completion of the hidden part of the program, that works as an example
pg.quit()
import sys 
sys.exit()

# Completion of user program is in the separate section

# -*- acsection: after-main -*-
pygamebg.wait_loop()
