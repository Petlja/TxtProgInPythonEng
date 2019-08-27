import pygame as pg, pygamebg, math
(width, height) = (400, 400)
canvas = pygamebg.open_window(width, height, "Eyes")

# Function draws an eye whose center is at (cx, cy), radius is r, 
# and its pupil is positioned to look at the position of the mouse (mx, my)
def draw_eye(cx, cy, r, mx, my):
    pg.draw.circle(canvas, pg.Color("black"), (cx, cy), 2*r, 1)        # draw an eye
    D = math.sqrt((mx-cx)**2 + (my-cy)**2)          # mouse to eye center distance 
    # k is the part of the vector CM for which we move from the center of the eye
    k = r/D if D > r else 1 
    pupil_center = (cx + round(k*(mx-cx)), cy + round(k*(my-cy))) 
    pg.draw.circle(canvas, pg.Color("black"), pupil_center, r)     # draw pupil

def new_frame():
    global mouse_x, mouse_y
    (mouse_x, mouse_y) = pg.mouse.get_pos()     # mouse position coordinates

    canvas.fill(pg.Color("white"))   # paint background to white
    # draw both eyes using the auxiliary function
    draw_eye(left_eye_xc, left_eye_yc, pupil_r, mouse_x, mouse_y)
    draw_eye(right_eye_xc, right_eye_yc, pupil_r, mouse_x, mouse_y)
    
(canvas_xc, canvas_yc) = (width // 2, height // 2) # center of the window
eye_r = width // 8                                 # eye radius
pupil_r = eye_r // 2                               # pupil radius
left_eye_xc = canvas_xc - 3 * pupil_r              # x coordinate of center of left eye
right_eye_xc = canvas_xc + 3 * pupil_r             # x coordinate of center of right eye
left_eye_yc = right_eye_yc = canvas_yc             # y coordinate of centers of both eyes
(mouse_x, mouse_y) = pg.mouse.get_pos()
    
pygamebg.frame_loop(50, new_frame)

