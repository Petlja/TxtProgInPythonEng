import pygame as pg, pygamebg
(width, height) = (600, 400)
canvas = pygamebg.open_window(width, height, "Dragging with mouse")

apple_image = pg.image.load("apple.png")  # read the apple image
apple_position = (300, 200)
dragging = False        # whether drag is ongoing

def mouse_is_on_image(mouse_pos):
    x, y = mouse_pos
    x0, y0 = apple_position # upper left corner
    dx, dy = apple_image.get_width(), apple_image.get_height() # image size
    return x0 <= x and x <= x0 + dx and y0 <= y and y <= y0 + dy

def new_frame():
    canvas.fill(pg.Color("darkgreen"))      # paint background
    canvas.blit(apple_image, apple_position)   # display apple

def handle_event(event):
    global apple_position, dragging
    if event.type == pg.MOUSEBUTTONDOWN:     # mouse button pressed
        if mouse_is_on_image(event.pos):     # if mouse is on the apple
            dragging = True                  # start dragging
    elif event.type == pg.MOUSEBUTTONUP:     # mouse button released
        dragging = False                     # finish dragging
    elif event.type == pg.MOUSEMOTION:       # mouse moved
        if dragging:                         # if draggging is in progress
            mouse_x, mouse_y = event.pos
            # compute the upper left corner of the image so that 
            # the center of the apple is at the mouse position
            x = mouse_x - apple_image.get_width() // 2
            y = mouse_y - apple_image.get_height() // 2
            apple_position = (x, y)

pygamebg.frame_loop(30, new_frame, handle_event)
