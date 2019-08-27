import pygame as pg, pygamebg

text = "PYTHON"
num_letters = len(text)
(width, height) = (num_letters * 70, 100)
canvas = pygamebg.open_window(width, height, "Neon sign")

# one frame for each letter, plus 
# one frame to turn-off and three frames to turn-on all the letters
num_frames = num_letters + 4

font = pg.font.SysFont("Arial", 80) # the font for displaying the text

# Each text is displayed in the same position, which is calculated here
text_image = font.render(text, True, pg.Color("yellow"))
x = (width - text_image.get_width()) // 2
y = (height - text_image.get_height()) // 2
i_frame  = 0

def new_frame():
    global i_frame
    
    canvas.fill(pg.Color("black")) 
    if i_frame < num_letters: # if some prefix of the text is to be turned-on
        text_image = font.render(text[:i_frame+1], True, pg.Color("yellow"))
        canvas.blit(text_image, (x, y))
    elif i_frame == num_letters:
        pass #  this is the frame where no letters are displayed
    else:
        # this is one of the last three frames, the whole text is displayed
        text_image = font.render(text, True, pg.Color("yellow"))
        canvas.blit(text_image, (x, y))
                
    # preparing for the next frame
    i_frame = (i_frame + 1) % num_frames

pygamebg.frame_loop(2, new_frame)
