import pygame as pg, pygamebg
canvas = pygamebg.open_window(200, 181, "Heart")

# images of the smaller and the bigger heart
heart_images = [
    pg.image.load("heart_smaller.png"), 
    pg.image.load("heart_bigger.png")
]

image_index = 0 # index of an image to be displayed

def new_frame():
    global image_index
    image_index = 1 - image_index       # chosing the other image

    canvas.fill(pg.Color("blue"))         # paint background
    canvas.blit(heart_images[image_index], (0, 0))

pygamebg.frame_loop(2, new_frame)
