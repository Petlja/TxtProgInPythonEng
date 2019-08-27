import pygame as pg, pygamebg

text = "PYTHON"
num_letters = len(text)
# one frame for each letter, plus 3 times a pair of frames for blinking
# (a blink is one frame with all the letters and one with none)
num_frames = num_letters + 6

(width, height) = (num_letters * 70, 100)
canvas = pygamebg.open_window(width, height, "Neon sign")

x = [0]                   # x coordinate of the first letter
for i in range(1, num_letters):
    x.append(x[-1] + 70)  # each subsequent letter is 70 pixels to the right
y = 0 # the y coordinate of all letters
font = pg.font.SysFont("Arial", 80) # the font for displaying the text

i_frame  = 0

def new_frame():
    global i_frame
    
    canvas.fill(pg.Color("black")) # paint background to black
    if i_frame < num_letters: # if one letter is to be turned on
        text_image = font.render(text[i_frame], True, pg.Color("yellow"))
        canvas.blit(text_image, (x[i_frame], y))
    else:
        # this is one of the blinking frames
        # and in every other of them all letters should be turned on
        if i_frame % 2 == 0: # if all the letters should be turned on
            for i_slovo in range(num_letters):
                text_image = font.render(text[i_slovo], True, pg.Color("yellow"))
                canvas.blit(text_image, (x[i_slovo], y))
                
    # prepare for the next frame
    i_frame = (i_frame + 1) % num_frames

pygamebg.frame_loop(3, new_frame)
