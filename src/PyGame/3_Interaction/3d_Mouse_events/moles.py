import pygame as pg, pygamebg, random

num_rows, num_cols = 2, 4
moles = []
mole_hit = []
for row in range(num_rows):
    moles.append([0] * num_cols)
    mole_hit.append([False] * num_cols)

# read mole images into the list
mole_images = []   # list that will contain images
for i in range(1, 11): # read images mole1.png, ..., mole10.png
    image_name = "mole" + str(i) + ".png"  # build image name from parts
    mole_images.append(pg.image.load(image_name))
    
a = mole_images[0].get_width() # image size (the pictures are square-shaped)
(width, height) = (num_cols * a, num_rows * a)
canvas = pygamebg.open_window(width, height, "Moles")
BROWN = (60, 42, 3)
num_visible_not_hit = 0
num_not_hit = num_rows * num_cols

def center_text(x, y, text, size):
    font = pg.font.SysFont("Arial", size)
    im = font.render(text, True, pg.Color("black"))
    (x, y) = (x - im.get_width() / 2, y - im.get_height() / 2)
    canvas.blit(im, (x, y))

def draw():
    if num_not_hit == 0:
        canvas.fill(pg.Color('white'))
        center_text(width / 2, height / 2, "Well done!", 100)
    else:
        canvas.fill(BROWN)
        for row in range(num_rows):
            for col in range(num_cols):
                x, y = col * a, row * a
                canvas.blit(mole_images[abs(moles[row][col])], (x, y))

def new_frame():
    global num_visible_not_hit
    if num_visible_not_hit == 0:
        probability = 20
    else:
        probability = 100
    for row in range(num_rows):
        for col in range(num_cols):
            if moles[row][col] == 0:
                if random.randint(1, probability) == 1:
                    moles[row][col] = 1
                    num_visible_not_hit += 1
            elif moles[row][col] == 9 and not mole_hit[row][col]:
                if random.randint(1, 20) == 1:
                    moles[row][col] = -9
            elif moles[row][col] < 9:
                moles[row][col] += 1
            elif moles[row][col] < 0 and not mole_hit[row][col]:
                moles[row][col] += 1
                if moles[row][col] == 0:
                    num_visible_not_hit -= 1
    draw()
    
def handle_event(event):
    global mole_hit, num_not_hit, num_visible_not_hit
    if event.type == pg.MOUSEBUTTONDOWN:
        for row in range(num_rows):
            for col in range(num_cols):
                if abs(moles[row][col]) >= 5:
                    (x, y) = (col * a, row * a)
                    (xm, ym) = event.pos
                    if x <= xm and xm <= x + a and y <= ym and ym <= y + a:
                        mole_hit[row][col] = True
                        num_not_hit -= 1
                        num_visible_not_hit -= 1
    
pygamebg.frame_loop(10, new_frame, handle_event)