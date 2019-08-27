import pygame as pg, pygamebg

# setting the canvas to be the same size as images
(width, height) = (300, 264)
canvas = pygamebg.open_window(width, height, "Running")

num_images = 8
images = []   # list that will contain images
for i in range(1, num_images+1): # reading images running1.png, ..., running8.png into the list
    image_name = "running" + str(i) + ".png"  # building image name from parts
    images.append(pg.image.load(image_name))

image_index = 0 # index of an image to be displayed

def new_frame():
    global image_index
    image_index = image_index + 1 # switching to the next image
    if image_index == num_images:    # if there is no next image ...
        image_index = 0            # turn back to the first image
    canvas.blit(images[image_index], (0, 0))

pygamebg.frame_loop(15, new_frame)
