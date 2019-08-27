import pygame as pg, pygamebg
(width, height) = (100, 300)
canvas = pygamebg.open_window(width, height, "Traffic lights")

NUM_STAGES = 4  #  RED      RED_YELLOW  GREEN      YELLOW
stage_lights   = ((1, 0, 0), (1, 1, 0), (0, 0, 1), (0, 1, 0) )
stage_duration = ( 2.5,       1,         2.5,       1 ) # in seconds

NUM_LIGHTS = 3
light_colors = (
#    for turned-off  for turned-on
    ((128,   0, 0), (255,   0, 0)), # red
    ((128, 128, 0), (255, 255, 0)), # yellow
    ((  0, 128, 0), (  0, 255, 0))  # green
)
light_position = ((50, 50), (50, 150), (50, 250))
i_stage = 3
num_frames_till_change = 0
fps = 5

def new_frame():
    global i_stage, num_frames_till_change # will be computing these values
    if num_frames_till_change == 0:
        i_stage = (i_stage + 1) % NUM_STAGES
        num_frames_till_change = round(stage_duration[i_stage] * fps)
    
    num_frames_till_change -= 1
    
    canvas.fill(pg.Color("darkgray"))  # paint background
    turned_on = stage_lights[i_stage]
    for i_light in range(NUM_LIGHTS):
        (x, y) = light_position[i_light]
        status = turned_on[i_light] # 0 for turned off, a 1 for turned on
        pg.draw.circle(canvas, light_colors[i_light][status], (x, y), 40)
        
pygamebg.frame_loop(fps, new_frame)
