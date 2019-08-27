import pygame as pg, pygamebg

(width, height) = (700, 250)
canvas = pygamebg.open_window(width, height, "Story")
text = (
    "Young children learn to walk",
    "by starting to walk.",
    "At first, they often fall,",
    "but they get up and keep going",
    "and with time",
    "they're getting better.",
    "Why not learn",
    "all the other skills",
    " that way?",
    " "
)

font = pg.font.SysFont("Arial", 40) # font for displaying the text
MARGIN_UP_DOWN = 30
TEXT_HEIGHT = 50
y_text_start = 200
i_first_visible_text_line = 0
num_visible_text_lines = 1

def draw():
    canvas.fill(pg.Color("skyblue")) # paint the background
    
    i_line = i_first_visible_text_line
    y = y_text_start
    for _ in range(num_visible_text_lines):
        # build an image of a text line and display it
        gray = min(230 - y, 192)
        color = (gray, gray, gray)
        text_image = font.render(text[i_line], True, color)
        canvas.blit(text_image, (20, y)) 
        i_line = (i_line + 1) % len(text)
        y += TEXT_HEIGHT

def new_frame():
    global i_first_visible_text_line, y_text_start, num_visible_text_lines
    y_text_start -= 1 # entire text glides 1 pixel up
    
    # check if the first line of text came out through the top
    if y_text_start < MARGIN_UP_DOWN:
        i_first_visible_text_line = (i_first_visible_text_line + 1) % len(text)
        y_text_start += TEXT_HEIGHT
    
    # is there room for another row
    next_line_pos = y_text_start + TEXT_HEIGHT * num_visible_text_lines
    if next_line_pos + TEXT_HEIGHT + MARGIN_UP_DOWN < height:
        num_visible_text_lines += 1
        
    draw()

pygamebg.frame_loop(30, new_frame)
