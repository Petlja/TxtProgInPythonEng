import pygame as pg, pygamebg
(width, height) = (400, 100)
canvas = pygamebg.open_window(width, height, "LED")

NUM_DIODES_LIT = 10  # the number of LEDs that light up (also the number of frames during which each LED lights up)
TOTAL_NUM_DIODES = 20                # total number of diodeS on the display
r = width // (2 * TOTAL_NUM_DIODES)  # diode radius
color = []
for i in range(NUM_DIODES_LIT + 1):
    shade = 255 * (1 - i/NUM_DIODES_LIT)
    color.append((shade, shade, shade)) # gray shades from white to black
    
x = []              # x coordinates of the centers of the diodes
for i in range(TOTAL_NUM_DIODES):
    x.append(r + i * 2 * r)
y = height // 2     # y coordinate of the centers of all diodes
i_leading_diode = 0  # index of the last diode turned on

def new_frame():
    global i_leading_diode
    i_leading_diode = (i_leading_diode + 1) % TOTAL_NUM_DIODES   # switch to the next diode

    canvas.fill(pg.Color("black"))               # paint background
    for delay in range(NUM_DIODES_LIT + 1):   # gor each diode currently lit
        # determine index of the diode that is turned on before 'delay' frames
        i_diode = (i_leading_diode + TOTAL_NUM_DIODES - delay) % TOTAL_NUM_DIODES  
        pg.draw.circle(canvas, color[delay], (x[i_diode], y), r)  # draw the diode

pygamebg.frame_loop(25, new_frame)
