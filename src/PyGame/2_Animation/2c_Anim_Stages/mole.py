import pygame as pg, pygamebg
(width, height) = (150, 150)
canvas = pygamebg.open_window(width, height, "Mole")

images = []   # list that will contain the images
for i in range(1, 11): # reading images mole1.png, ..., mole10.png into the list
    image_name = "mole" + str(i) + ".png"  # building the image name from parts
    images.append(pg.image.load(image_name))

brown = (60, 42, 3)
Y_HORIZON = 125
GROUND = (0, Y_HORIZON, width, height - Y_HORIZON) # part of the image under the horizon
i_frame = 0 # frame counter

def new_frame():
    global i_frame, i_image
    i_frame = (i_frame + 1) % 28 # total number of frames is 28
    if i_frame < 10:
        i_image = i_frame        # stage one - coming out
    elif i_frame < 15:
        i_image = 9              # stage two - mole is up
    elif i_frame < 25:
        i_image = 24 - i_frame   # stage three - going down
    else:
        i_image = 0              # stage four - mole is down

    canvas.fill(pg.Color("skyblue"))     # paint background
    pg.draw.rect(canvas, brown, GROUND)  # paint rectangle GROUND to brown
    canvas.blit(images[i_image], (0, 0)) # display the image

pygamebg.frame_loop(10, new_frame)
