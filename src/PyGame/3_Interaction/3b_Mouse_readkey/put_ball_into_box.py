# -*- acsection: general-init -*-
import pygame as pg, pygamebg
width, height = 400, 400
canvas = pygamebg.open_window(width, height, "Put the ball in")
font = pg.font.SysFont("Arial", 30) # the font to display the text

r = 10 # ball size
(target_x, target_y) = (width//4, height//4) # target point
target_box = (target_x - 2*r, target_y - 2*r, 4*r, 4*r) # box around target point

(x, y) = (width//2, height//2) # ball starts from the center of the window
won, lost = False, False

def draw():
    canvas.fill(pg.Color("black")) # black background
    if won or lost:
        # the game is over, display a message
        poruka = "Well done!" if won else "ran away..."
        text_image = font.render(poruka, True, pg.Color("green"))
        tx = (width - text_image.get_width()) // 2
        ty = (height - text_image.get_height()) // 2
        canvas.blit(text_image, (tx, ty))
    else:
        # the game is still running, draw the box and the ball
        pg.draw.rect(canvas, pg.Color("red"), target_box, 3)
        pg.draw.circle(canvas, pg.Color("green"), (int(x), int(y)), 10)

# -*- acsection: main -*-
def new_frame():
    global x, y, won, lost
    
    pressed_mouse_button = pg.mouse.get_pressed()
    if pressed_mouse_button[2]: # right button - new game
        (x, y) = (width//2, height//2) # return the ball to the center
        won, lost = False, False # the player has neither won nor lost
        
    if pressed_mouse_button[0]: # left button - move the ball
        (xm, ym) = pg.mouse.get_pos() # mouse position coordinates
        # the ball moves away from the mouse for another half of that distance
        x = x - 0.5 * (xm - x)
        y = y - 0.5 * (ym - y)

    # if the center of the ball is near the center of the target - the player wins
    if abs(x - target_x) < r and abs(y - target_y) < r:
        won = True
    # if the center of the ball is out the window - the player has lost
    if x < 0 or x > width or y < 0 or y > height:
        lost = True
    draw()
# -*- acsection: after-main -*-

pygamebg.frame_loop(50, new_frame)
