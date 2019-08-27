import pygame as pg, pygamebg, random
(width, height) = (600, 400)
canvas = pygamebg.open_window(width, height, "Dragging with mouse")

basket_image  = pg.image.load("basket.png") # read the basket image
apple_image = pg.image.load("apple.png")  # read the apple image
scene_image = pg.image.load("drag_scene.png") # read the scene image
apple_positions = []
for i in range(5):
    apple_positions.append((random.randint(50, 200), random.randint(80, 130)))
basket_pos = (300, 200)
i_apple = -1             # which apple is currently being draged (-1 means none)
done = False

def mouse_is_on_image(mouse_pos, image_pos, image):
    x, y = mouse_pos
    x0, y0 = image_pos # upper left corner
    dx, dy = image.get_width(), image.get_height() # image size
    return x0 <= x and x <= x0 + dx and y0 <= y and y <= y0 + dy

def new_frame():    
    canvas.blit(scene_image, (0, 0)) # display scene
    if not done:
        canvas.blit(basket_image, basket_pos) # display the basket
        for apple_pos in apple_positions: # display apples
            canvas.blit(apple_image, apple_pos)

def handle_event(event):
    global apple_positions, i_apple, done
    if event.type == pg.MOUSEBUTTONDOWN:     # pritisnuto je dugme miša
        for i in range(len(apple_positions)):
            # if mouse is on one of the apples
            if mouse_is_on_image(event.pos, apple_positions[i], apple_image):
                i_apple = i    # start dragging
                
    elif event.type == pg.MOUSEBUTTONUP:     # mouse button released
        if mouse_is_on_image(event.pos, basket_pos, basket_image):
            del apple_positions[i_apple]
            if len(apple_positions) == 0:
                done = True
        i_apple = -1                           # finish dragging
        
    elif event.type == pg.MOUSEMOTION:       # mouse moved
        if i_apple >= 0:                       # if dragging is in progress
            # calculate the position of the apple (upper left corner of the image)
            # so that the center of the apple is at the mouse
            mouse_x, mouse_y = event.pos
            x = mouse_x - apple_image.get_width() // 2
            y = mouse_y - apple_image.get_height() // 2
            apple_positions[i_apple] = (x, y)

pygamebg.frame_loop(30, new_frame, handle_event)
