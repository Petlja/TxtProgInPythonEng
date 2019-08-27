import pygame as pg, pygamebg
(width, height) = (400, 300)
canvas = pygamebg.open_window(width, height, "Car")

car_image = pg.image.load("car.png")
(car_width, car_height) = (car_image.get_width(), car_image.get_height()) # car image size

fps = 50       # number of frames per second
dt = 1 / fps   # duration of one frame in seconds
car_v = 100   # car speed (pixels per second)
(car_x, car_y) = (0, height - car_height) # car position (lower left corner initially)

def new_frame():
    global car_x               # we will only change x coordinate of the car
    car_x += car_v * dt        # move car to the right
    if car_x > width:          # if it went out of the canvas
        car_x = - car_width    # bring it back to the beginning

    canvas.fill(pg.Color("skyblue"))         # paint background to sky-blue
    canvas.blit(car_image, (car_x, car_y))   # displaying car image

pygamebg.frame_loop(fps, new_frame)
