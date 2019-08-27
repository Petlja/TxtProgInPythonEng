import pygame as pg, pygamebg
(width, height) = (400, 400)
canvas = pygamebg.open_window(width, height, "Image as mouse cursor")

mouse_image = (pg.image.load("HammerUp.png"), pg.image.load("HammerDown.png"))
i_image = 0
(mouse_x, mouse_y) = (width // 2, height // 2)
pg.mouse.set_pos((mouse_x, mouse_y))
pg.mouse.set_visible(False)
marks = []

def new_frame():
    canvas.fill(pg.Color("skyblue")) # paint canvas
    # draw the image so that the mouse is in the middle of the image
    image_width = mouse_image[i_image].get_width()
    image_height = mouse_image[i_image].get_height()
    image_pos = (mouse_x - image_width // 2, mouse_y - image_height // 2)
    canvas.blit(mouse_image[i_image], image_pos)
    for x, y in marks:
        pg.draw.circle(canvas, pg.Color("black"), (x+25, y+15), 5)

def handle_event(event):
    global mouse_x, mouse_y, i_image
    if event.type == pg.MOUSEBUTTONDOWN:
        i_image = 1
        marks.append(event.pos)
    elif event.type == pg.MOUSEBUTTONUP:
        i_image = 0
    elif event.type == pg.MOUSEMOTION:
        mouse_x, mouse_y = event.pos

pygamebg.frame_loop(30, new_frame, handle_event)
