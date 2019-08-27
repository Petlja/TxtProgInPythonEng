import pygame as pg, pygamebg

(width, height) = (750, 150)
canvas = pygamebg.open_window(width, height, "Story")

font = pg.font.SysFont("Century", 40)  # the font for displaying the text
intro = "This is an old story"
continuation = " about a man, who wanted to tell a story"
num_letters_to_display = 33
visible_text = (intro + continuation)[0 : num_letters_to_display]
next_letter_pos = num_letters_to_display - len(intro)
fps = 5
i_frame = 0

def new_frame():
    global visible_text, next_letter_pos, i_frame
    
    i_frame += 1
    if i_frame > 8:
        visible_text = visible_text[1:] + continuation[next_letter_pos]
        next_letter_pos = (next_letter_pos + 1) % len(continuation)

    canvas.fill(pg.Color("skyblue")) # paint background
    # build an image of the text and display it
    text_image = font.render(visible_text, True, pg.Color("black"))
    canvas.blit(text_image, (50, 50))


pygamebg.frame_loop(fps, new_frame)
