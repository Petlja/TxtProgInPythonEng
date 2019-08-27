import pygame as pg, pygamebg

(width, height) = (350, 200)
canvas = pygamebg.open_window(width, height, "Story")
text = (
    "This is an old story",
    "about one man",
    "who wanted",
    "to tell a story")

font = pg.font.SysFont("Arial", 40) # the font for displaying the text
MARGIN_UP_DOWN = 10
TEXT_LINE_HEIGHT = 50
y_text = 80
i_first_visible_text_line = 0
num_visible_lines = 1

def draw():
    canvas.fill(pg.Color("skyblue"))        # paint background
    
    i_text_line = i_first_visible_text_line
    y = y_text
    for _ in range(num_visible_lines):
        # build and display image of a single line of text
        text_image = font.render(text[i_text_line], True, pg.Color("black"))
        canvas.blit(text_image, (20, y)) 
        i_text_line += 1
        if i_text_line == len(text):
            i_text_line = 1
        y += TEXT_LINE_HEIGHT

def new_frame():
    global i_first_visible_text_line, y_text, num_visible_lines
    y_text -= 1
    
    # did the first line of text come out through the top edge
    if y_text < MARGIN_UP_DOWN:
        y_text += TEXT_LINE_HEIGHT
        i_first_visible_text_line += 1
        if i_first_visible_text_line == len(text):
            i_first_visible_text_line = 1
        num_visible_lines -= 1
    
    # is there room for another line of text
    next_line_pos = y_text + TEXT_LINE_HEIGHT * num_visible_lines
    if next_line_pos + TEXT_LINE_HEIGHT + MARGIN_UP_DOWN < height:
        num_visible_lines += 1
        
    draw()

pygamebg.frame_loop(15, new_frame)
