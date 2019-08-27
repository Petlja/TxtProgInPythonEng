import pygame as pg, pygamebg, random
(width, height) = (400, 400)
canvas = pygamebg.open_window(width, height, "Butterfly follows the mouse")

butterfly_images = [pg.image.load("butterfly1.png"), pg.image.load("butterfly2.png")]
i_image = 0

def new_frame():
    global i_image
    i_image = 1 - i_image # the two images are displayed alternately
    canvas.fill(pg.Color("white"))
    (mouse_x, mouse_y) = pg.mouse.get_pos()
    image = butterfly_images[i_image] # image to display
    # show the image centered
    (x, y) = (mouse_x - image.get_width() / 2, mouse_y - image.get_height() / 2)
    canvas.blit(image, (x, y))

pygamebg.frame_loop(5, new_frame)
