import pygame as pg, pygamebg
(width, height) = (800, 350)
canvas = pygamebg.open_window(width, height, "Plane")

sun_image = pg.image.load("sun.png")        # image of the sun
plane_image = pg.image.load("airplane.png") # image of the plane
plane_width = plane_image.get_width()       # plane image width
plane_height = plane_image.get_height()     # plane image height

# plane position - initially the middle of the left edge
(plane_x, plane_y) = (0, (height - plane_height)  // 2)
i_frame = 0 # frame counter
END_STAGE_ONE = 20
TOTAL_NUM_FRAMES = 40
def new_frame():
    global plane_x, plane_y, i_frame    # will be changing plane position and frame counter
    i_frame = (i_frame + 1) % TOTAL_NUM_FRAMES
    if i_frame < END_STAGE_ONE:
        plane_y -= 2  # in stage one we move the plane 1 pixel up
    else:
        plane_y += 2  # in stage two we move the plane 1 pixel up

    plane_x += 2      # move the plane 1 pixel to the right
    if plane_x > width:
        plane_x = -plane_width

    canvas.fill(pg.Color("skyblue"))             # paint background
    canvas.blit(sun_image, (0, 0))               # display the sun
    canvas.blit(plane_image, (plane_x, plane_y)) # display the plane

pygamebg.frame_loop(50, new_frame)
