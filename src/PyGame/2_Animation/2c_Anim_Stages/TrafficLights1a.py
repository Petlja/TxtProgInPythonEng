import pygame as pg, pygamebg
(width, height) = (100, 300)
canvas = pygamebg.open_window(width, height, "Traffic lights")

# stages are: red, red_yellow, green, blinking green, yellow
stage_duration = (25, 10, 25, 6, 10) # 25 frames for red, 10 for red_yellow etc.

stage_end = []
total_frames = 0
for f in stage_duration:
    total_frames += f
    stage_end.append(total_frames)

x = 50             # the x coordinate of all circle centers
y = [50, 150, 250] # y coordinates of the circle centers
r = 40             # circle radius
red_on     = (255,   0, 0)
red_off    = (128,   0, 0)
yellow_on  = (255, 255, 0)
yellow_off = (128, 128, 0)
green_on   = (  0, 255, 0)
green_off  = (  0, 128, 0)

i_frame  = 0
fps = 10

def draw_trafficlights(color_up, color_middle, color_down):
    pg.draw.circle(canvas, color_up,     (x, y[0]), r)
    pg.draw.circle(canvas, color_middle, (x, y[1]), r)
    pg.draw.circle(canvas, color_down,   (x, y[2]), r)
        
def new_frame():
    global i_frame
    i_frame = (i_frame + 1) % total_frames
    
    canvas.fill(pg.Color("darkgray")) # paint background
    if i_frame < stage_end[0]: # if the frame belongs to stage 'red'
        draw_trafficlights(red_on, yellow_off, green_off)
    elif i_frame < stage_end[1]: # if the frame belongs to stage 'red_yellow'
        draw_trafficlights(red_on, yellow_on, green_off)
    elif i_frame < stage_end[2]: # if the frame belongs to stage 'green'
        draw_trafficlights(red_off, yellow_off, green_on)
    elif i_frame < stage_end[3]: # if the frame belongs to stage 'blinking green'
        if i_frame % 2 == 0:
            draw_trafficlights(red_off, yellow_off, green_on)
        else:
            draw_trafficlights(red_off, yellow_off, green_off)
    else: # frame belongs to the last stage ('yellow')
        draw_trafficlights(red_off, yellow_on, green_off)

pygamebg.frame_loop(fps, new_frame)
